from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = PollSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = QuestionsSerializer

class ResultsUserViewSet(viewsets.ModelViewSet, models.Manager):


    def get_queryset(self, user):
        return Results.objects.all().filter(poll_name=self.kwargs['user'])
    
    permission_classes = [
                permissions.AllowAny 
            ]
    serializer_class = ResultsSerializer


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()

    permission_classes = [
            permissions.AllowAny 
        ]
    serializer_class = ResultsSerializer