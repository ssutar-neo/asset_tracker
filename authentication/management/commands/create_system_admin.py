from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a default System Admin user'

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = 'admin'  # Change this to a more secure password
        email = 'admin@example.com'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists.'))
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser "{username}".'))
