
from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data using pymongo.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Users
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
        ]
        db.users.delete_many({})
        db.users.insert_many(users)

        # Teams
        teams = [
            {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team Beta", "members": ["carol@example.com"]}
        ]
        db.teams.delete_many({})
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {"user": "alice@example.com", "type": "run", "duration": 30, "date": "2025-08-01"},
            {"user": "bob@example.com", "type": "walk", "duration": 45, "date": "2025-08-02"},
            {"user": "carol@example.com", "type": "cycle", "duration": 60, "date": "2025-08-03"}
        ]
        db.activity.delete_many({})
        db.activity.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"user": "alice@example.com", "score": 120},
            {"user": "bob@example.com", "score": 100},
            {"user": "carol@example.com", "score": 150}
        ]
        db.leaderboard.delete_many({})
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"name": "Push Ups", "description": "Do 20 push ups"},
            {"name": "Sit Ups", "description": "Do 30 sit ups"},
            {"name": "Jumping Jacks", "description": "Do 50 jumping jacks"}
        ]
        db.workouts.delete_many({})
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully in MongoDB.'))
