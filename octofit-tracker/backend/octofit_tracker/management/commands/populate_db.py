from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data from collections
        # (Models will be created in the next steps)
        self.stdout.write(self.style.SUCCESS('Populating octofit_db with test data...'))
        # TODO: Implement data deletion and insertion for users, teams, activities, leaderboard, workouts
        self.stdout.write(self.style.SUCCESS('Database population complete.'))
