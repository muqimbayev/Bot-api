from rest_framework import serializers
from .models import *

class puzzle_questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = puzzle_question
        fields = '__all__'


class puzzle_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = puzzle_answers
        fields = '__all__'


class entry_questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = entry_questions
        fields = '__all__'


class entry_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = entry_answers
        fields = '__all__'


class middle_questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = middle_questions
        fields = '__all__'


class middle_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = middle_answers
        fields = '__all__'


class high_questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = high_questions
        fields = '__all__'

class high_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = high_answers
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


