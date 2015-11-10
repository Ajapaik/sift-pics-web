from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Do all the usual stuff'

    def handle(self, *args, **options):
        call_command('migrate', interactive=False)
        call_command('collectstatic', interactive=False)
        call_command('compress', force=True, interactive=False)
