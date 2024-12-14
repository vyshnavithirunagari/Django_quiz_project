# quiz/admin.py
from django.contrib import admin
from .models import Question, QuizResult

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer')
    search_fields = ('text',)

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_questions', 'correct_answers', 'percentage_score', 'completed_at')
    list_filter = ('completed_at',)