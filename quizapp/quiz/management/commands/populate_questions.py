# quiz/management/commands/populate_questions.py
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Populate database with initial quiz questions'

    def handle(self, *args, **kwargs):
        # Sample questions - you can expand or replace these
        questions = [
            {
                'text': 'What is a Django?',
                'option_a': 'A programming language',
                'option_b': 'A web framework written in Python',
                'option_c': 'A database management system',
                'option_d': 'A python library for data analysis',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the extension of Django template file?',
                'option_a': '.txt',
                'option_b': '.html',
                'option_c': '.tpl',
                'option_d': '.py',
                'correct_answer': 'B'
            },
            {
                'text': 'In Django, which of these is used to filter query results in views?',
                'option_a': 'filter()',
                'option_b': 'find()',
                'option_c': 'serach()',
                'option_d': 'lookup()',
                'correct_answer': 'A'
            },
            {
                'text': 'Which function is used to render a template in Django?',
                'option_a': 'render_template()',
                'option_b': 'render()',
                'option_c': 'template()',
                'option_d': 'render_page()',
                'correct_answer': 'B'
            },
            {
                'text': 'Which template is used to loop through a list in Django?',
                'option_a': '{% for %}',
                'option_b': '{% loop %}',
                'option_c': '{% each %}',
                'option_d': '{% iterate %}',
                'correct_answer': 'A'
            },
            {
                'text': 'What is the default Django database?',
                'option_a': 'MySQL',
                'option_b': 'PostgreSQL',
                'option_c': 'SQLite',
                'option_d': 'Oracle',
                'correct_answer': 'C'
            },
            {
                'text': 'What command is used to create superuser in Django?',
                'option_a': 'Django-admin createsuperuser',
                'option_b': 'python manage.py createsuperuser',
                'option_c': 'python manage.py createsuperuser',
                'option_d': 'python manage.py superuser',
                'correct_answer': 'C'
            },
            {
                'text': 'Which method is used to save a model instance in Django?',
                'option_a': 'insert()',
                'option_b': 'save()',
                'option_c': 'commit()',
                'option_d': 'update()',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the purpose of Django csrf_token?',
                'option_a': 'To prevent SQL injection',
                'option_b': 'To encrypt user data',
                'option_c': 'To prevent Cross-Site Request Forgery attacks',
                'option_d': 'To handle session management',
                'correct_answer': 'C'
            },
            {
                'text': 'In Django settings, what is variable used to set the template pack for Crispy Forms?',
                'option_a': 'CRISPY_PACK',
                'option_b': 'CRISPY_TEMPLATE_PACK',
                'option_c': 'TEMPLATE_PCK',
                'option_d': 'BOOTSTRAP_TEMPLATE_PACK',
                'correct_answer': 'B'
            },
            {
                'text': 'In Crispy Forms, what is the default template pack that can be set in settings.py for Bootstrap?',
                'option_a': 'bootstrap4',
                'option_b': 'bootstrap3',
                'option_c': 'bootstrap5',
                'option_d': 'bootstrapp2',
                'correct_answer': 'A'
            },
            {
                'text': 'Which Django method allows you to generate a form with Crispy Forms that includes fields with Bootstrap styling?',
                'option_a': '{{ form | render}}',
                'option_b': '{{ form | crispy}}',
                'option_c': '{{ form | style}}',
                'option_d': '{{ form | formcontrol}}',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the command used to strat the Django development server?',
                'option_a': 'Python startserver',
                'option_b': 'Python runserver',
                'option_c': 'python manage.py runserver',
                'option_d': 'Python runserver',
                'correct_answer': 'C'
            },
            {
                'text': 'How do you apply migrations in Django?',
                'option_a': 'Python manage.py migrate',
                'option_b': 'python manage.py apply',
                'option_c': 'Django-admin migrate',
                'option_d': 'python apply.py',
                'correct_answer': 'A'
            },
            {
                'text': 'Which command is used to create a new Django app?',
                'option_a': 'Python manage.py startapp',
                'option_b': 'Django-admin newapp',
                'option_c': 'Python createapp',
                'option_d': 'Python manage.py createapp',
                'correct_answer': 'B'
            },
            
            
            # Add more questions here
        ]

        for q in questions:
            Question.objects.get_or_create(
                text=q['text'],
                defaults={
                    'option_a': q['option_a'],
                    'option_b': q['option_b'],
                    'option_c': q['option_c'],
                    'option_d': q['option_d'],
                    'correct_answer': q['correct_answer']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated questions'))