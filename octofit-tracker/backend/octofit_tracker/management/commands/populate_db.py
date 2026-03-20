from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='medium')
        squats = Workout.objects.create(name='Squats', description='Legs', difficulty='easy')

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='pushup', duration=15, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='squat', duration=20, date=timezone.now().date())
        Activity.objects.create(user=clark, type='run', duration=25, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=bruce, score=100, rank=3)
        Leaderboard.objects.create(user=clark, score=90, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
