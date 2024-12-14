# quiz/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Max
import random
import time
import crispy_forms

from .models import Question, QuizResult
from .forms import UserRegistrationForm, QuizAnswerForm



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('quiz:start_quiz')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def start_quiz(request):
    # Reset or create new quiz session
    request.session['quiz_started'] = True
    request.session['start_time'] = int(time.time())
    question_ids=list(Question.objects.values_list('id',flat=True))
    random.shuffle(question_ids)
    request.session['quiz_questions'] = question_ids
    request.session['answered_questions'] = []
    return render(request, 'start_quiz.html', {'timer_duration': 900})  # 15 minutes



@login_required
def get_quiz_question(request):
    if not request.session.get('quiz_started', False):
        return redirect('quiz:start_quiz')

    # Get remaining questions
    question_ids = request.session.get('quiz_questions', [])
    answered_questions = request.session.get('answered_questions', [])

    # Remove already answered questions
    remaining_questions = [
        qid for qid in question_ids if qid not in answered_questions
    ]

    if not remaining_questions:
        return redirect('quiz:quiz_result')

    # Get a random question
    question_id = random.choice(remaining_questions)
    question = Question.objects.get(id=question_id)

    if request.method == 'POST':
        form = QuizAnswerForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['answer']
            is_correct = user_answer == question.correct_answer

            # Update session data
            answered_questions.append(question_id)
            request.session['answered_questions'] = answered_questions

            # Track results
            if 'quiz_results' not in request.session:
                request.session['quiz_results'] = {
                    'total_questions': 0,
                    'correct_answers': 0,
                    'incorrect_answers': 0
                }

            quiz_results = request.session['quiz_results']
            quiz_results['total_questions'] += 1
            if is_correct:
                quiz_results['correct_answers'] += 1
            else:
                quiz_results['incorrect_answers'] += 1

            request.session['quiz_results'] = quiz_results

            return redirect('quiz:get_question')
    else:
        form = QuizAnswerForm()

    return render(request, 'quiz.html', {
        'question': question,
        'form': form,
        'timer_duration': 900,
        'questions_remaining': len(remaining_questions) - 1
    })



@login_required
def quiz_result(request):
    # Calculate quiz results
    start_time = request.session.get('start_time', int(time.time()))
    time_taken = int(time.time()) - start_time

    quiz_results = request.session.get('quiz_results', {
        'total_questions': 0,
        'correct_answers': 0,
        'incorrect_answers': 0
    })

    total_questions = quiz_results['total_questions']
    correct_answers = quiz_results['correct_answers']
    incorrect_answers = quiz_results['incorrect_answers']

    percentage_score = (correct_answers / total_questions * 100) if total_questions > 0 else 0

    # Save result to database
    QuizResult.objects.create(
        user=request.user,
        total_questions=total_questions,
        correct_answers=correct_answers,
        incorrect_answers=incorrect_answers,
        percentage_score=percentage_score,
        time_taken=time_taken
    )

    # Clear session
    request.session['quiz_started'] = False
    request.session['quiz_questions'] = []
    request.session['answered_questions'] = []
    request.session['quiz_results'] = {}

    return render(request, 'results.html', {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'percentage_score': round(percentage_score, 2),
        'time_taken': time_taken
    })