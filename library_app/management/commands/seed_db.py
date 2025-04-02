from django.core.management.base import BaseCommand
from library_app.models import Author, Book

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Author.objects.all().delete()
        Book.objects.all().delete()

        # Add your own data
        author1 = Author.objects.create(name='Dr A P J Abdul Kalam')
        author2 = Author.objects.create(name='J.K. Rowling')

        Book.objects.create(title='Wings of Fire', isbn='9788173711466', author=author1)
        Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', isbn='9780747532743', author=author2)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
