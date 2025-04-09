from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create additional test users
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_brown', email='bob@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create additional test teams
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3, user4)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))

        # Create additional test activities
        Activity.objects.create(user=user3, activity_type='Swimming', duration=timedelta(minutes=45))
        Activity.objects.create(user=user4, activity_type='Hiking', duration=timedelta(hours=2))

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=150)
        Leaderboard.objects.create(user=user2, score=200)

        # Create additional test leaderboard entries
        Leaderboard.objects.create(user=user3, score=180)
        Leaderboard.objects.create(user=user4, score=220)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing morning yoga session')
        Workout.objects.create(name='HIIT', description='High-intensity interval training')

        # Create additional test workouts
        Workout.objects.create(name='Evening Pilates', description='A calming evening pilates session')
        Workout.objects.create(name='Strength Training', description='Weightlifting and resistance exercises')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
