from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    codespace_url = "https://automatic-funicular-4p4x4rw9r63jv4p-8000.app.github.dev"  # Updated codespace URL
    return Response({
        'users': f'{codespace_url}/api/users/',
        'teams': f'{codespace_url}/api/teams/',
        'activities': f'{codespace_url}/api/activities/',
        'leaderboard': f'{codespace_url}/api/leaderboard/',
        'workouts': f'{codespace_url}/api/workouts/'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
