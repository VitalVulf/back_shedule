from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Create a backup of the database.'

    def handle(self, *args, **kwargs):
        # Вызываем стандартную команду dumpdata для создания бэкапа
        with open('backup.json', 'w') as f:
            call_command('dumpdata', stdout=f)
        self.stdout.write(self.style.SUCCESS('Successfully created backup'))