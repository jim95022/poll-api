from rest_framework import serializers
from .models import *


class PollSerializer(serializers.ModelSerializer):
    qstns = serializers.PrimaryKeyRelatedField(many=True, queryset=Questions.objects.all())
    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields =  ('start_date',)


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'
