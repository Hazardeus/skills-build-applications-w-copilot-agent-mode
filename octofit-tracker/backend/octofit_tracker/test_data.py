# Fichier de données de test pour l'application OctoFit

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
    {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
]

test_activities = [
    {"user": "thundergod", "activity_type": "Cycling", "duration": "1:00:00"},
    {"user": "metalgeek", "activity_type": "Crossfit", "duration": "2:00:00"},
    {"user": "zerocool", "activity_type": "Running", "duration": "1:30:00"},
    {"user": "crashoverride", "activity_type": "Strength", "duration": "0:30:00"},
    {"user": "sleeptoken", "activity_type": "Swimming", "duration": "1:15:00"},
]

test_leaderboard = [
    {"user": "thundergod", "score": 100},
    {"user": "metalgeek", "score": 90},
    {"user": "zerocool", "score": 95},
    {"user": "crashoverride", "score": 85},
    {"user": "sleeptoken", "score": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
