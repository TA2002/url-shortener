
from django.core.management.base import BaseCommand, CommandError

from shortener.models import LinkyURL


class Command(BaseCommand):
    help = 'Refrehes all LinkyURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return LinkyURL.objects.refresh_shortcodes(items=options['items'])