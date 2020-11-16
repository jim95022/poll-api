from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PollSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = QuestionsSerializer

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = ResultsSerializer