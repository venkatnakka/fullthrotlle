from django.core.management.base import BaseCommand
from usermanagement.models import ActivityPeriod, User

class Command(BaseCommand):
    help = 'Displays all user activites'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stdout.write('processing...')

    def handle(self, *args, **kwargs):
        activity_periods = ActivityPeriod.objects.all().values()
        self.stdout.write('success')
        self.stdout.write('{}'.format(activity_periods))