from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data in correct order, deleting each object individually
        for obj in Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.pk:
                obj.delete()
        for obj in User.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Team.objects.all():
            if obj.pk:
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Banner', email='bruce@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc)
        barry = User.objects.create(name='Barry Allen', email='barry@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Swimming', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=diana, activity_type='Yoga', duration_minutes=40, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        workout2 = Workout.objects.create(name='Sprints', description='Speed training')
        workout1.suggested_for.set([tony, steve, clark])
        workout2.suggested_for.set([diana, barry])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=200)
        Leaderboard.objects.create(team=dc, total_points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
