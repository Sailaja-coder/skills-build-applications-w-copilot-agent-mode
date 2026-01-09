from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='swim', duration=60, date=date.today())
        Activity.objects.create(user=users[3], type='yoga', duration=20, date=date.today())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
