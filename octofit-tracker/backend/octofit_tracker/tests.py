from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'Clark Kent')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, date='2026-03-31')
        self.assertIn('Running', str(activity))

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertIn('Marvel', str(leaderboard))
