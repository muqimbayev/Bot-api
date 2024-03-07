from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.
class PuzzleQuestionView(ModelViewSet):
    queryset = puzzle_question.objects.all()
    serializer_class = puzzle_questionSerializer
    permission_class = [IsAuthenticated]

class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_class = [IsAuthenticated]

class PuzzleAnswerView(ModelViewSet):
    queryset = puzzle_answers.objects.all()
    serializer_class = puzzle_answerSerializer
    permission_class = [IsAuthenticated]


class EntryQuestionView(ModelViewSet):
        queryset = entry_questions.objects.all()
        serializer_class = entry_questionSerializer
        permission_class = [IsAuthenticated]


class EntryAnswerView(ModelViewSet):
    queryset = entry_answers.objects.all()
    serializer_class = entry_answerSerializer
    permission_class = [IsAuthenticated]


class MiddleQuestionView(ModelViewSet):
    queryset = middle_questions.objects.all()
    serializer_class = middle_questionSerializer
    permission_class = [IsAuthenticated]


class MiddleAnswerView(ModelViewSet):
    queryset = middle_answers.objects.all()
    serializer_class = middle_answerSerializer
    permission_class = [IsAuthenticated]


class HighQuestionView(ModelViewSet):
    queryset = high_questions.objects.all()
    serializer_class = high_questionSerializer
    permission_class = [IsAuthenticated]


class HighAnswerView(ModelViewSet):
    queryset = high_answers.objects.all()
    serializer_class = high_answerSerializer
    permission_class = [IsAuthenticated]

class UserCountViewSet(ViewSet):
    def list(self, request):
        count_user = Users.objects.count()
        data = {'foydalanuvchi_son': count_user}
        return Response(data)

class CountQuestions(ViewSet):
    def list(self, request):
        count_entry_question = entry_questions.objects.count()
        count_puzzle_question = puzzle_question.objects.count()
        count_middle_question = middle_questions.objects.count()
        count_high_question = high_questions.objects.count()
        puzzle_count_question = puzzle_question.objects.count()
        data = {'entry_count': count_entry_question,
                'middle_count': count_middle_question,
                'high_count': count_high_question,
                'puzzle_count': puzzle_count_question}
        return Response(data)

@api_view(['GET'])
def point_get(request, telegram_id):
    user = Users.objects.get(telegram_id=telegram_id)
    point = user.point
    entry = user.entry
    middle = user.middle
    high = user.high
    puzzle = user.puzzle
    user_position = Users.objects.filter(point__gt=Users.objects.filter(telegram_id=telegram_id).values('point')).count()
    return Response({'point': point,
                     'entry': entry,
                     'middle': middle,
                     'high':high,
                     'puzzle': puzzle,
                     'user_position': user_position})

@api_view(['GET'])
def top_users(request):
    top_users_data = Users.objects.all().order_by('-point')[:10]
    user_data = []

    for user in top_users_data:
        user_data.append({
            'full_name': user.full_name,
            'point': user.point,
        })
    return Response(user_data)


@api_view(['GET'])
def is_answers_entry(request, telegram_id, question_id):
        is_answer_entry = entry_answers.objects.filter(user_id=telegram_id, question_id=question_id).values('is_answer')
        return Response({'is_answer_entry': is_answer_entry})

@api_view(['GET'])
def is_answers_middle(request, telegram_id, question_id):
        is_answer_entry = middle_answers.objects.filter(user_id=telegram_id, question_id=question_id).values('is_answer')
        return Response({'is_answer_middle': is_answer_entry})

@api_view(['GET'])
def is_answers_high(request, telegram_id, question_id):
        is_answer_entry = high_answers.objects.filter(user_id=telegram_id, question_id=question_id).values('is_answer')
        return Response({'is_answer_high': is_answer_entry})

@api_view(['GET'])
def is_answers_puzzle(request, telegram_id, question_id):
        is_answer_entry = puzzle_answers.objects.filter(user_id=telegram_id, question_id=question_id).values('is_answer')
        return Response({'is_answer_puzzle': is_answer_entry})


@api_view(['PUT'])
def UpdatePoint(request, telegram_id, point, level):
    user = Users.objects.get(telegram_id=telegram_id)
    user.point += point
    setattr(user, level, getattr(user, level) + 1)
    user.save()
    return Response({'message': 'Ma\'lumot muvaffaqiyatli yangilandi.'})


@api_view(['GET'])
def FindUserId(request, telegram_id):
    user = Users.objects.get(telegram_id=telegram_id)
    user_id = user.id
    return Response({'user_id': user_id})

@api_view(['PUT'])
def add_number(request, userId, level):
    user = Users.objects.get(telegram_id=userId)
    if level == 'entry':
        user.entry_count += 1
    elif level == 'middle':
        user.middle_count += 1
    elif level == 'high':
        user.high_count += 1
    elif level == 'puzzle':
        user.puzzle_count += 1
    user.save()
    return Response({'message': 'Ma\'lumot muvaffaqiyatli yangilandi.'})

@api_view(['PUT'])
def sub_number(request, userId, level):
    user = Users.objects.get(telegram_id=userId)
    if level == 'entry':
        user.entry_count -= 1
    elif level == 'middle':
        user.middle_count -= 1
    elif level == 'high':
        user.high_count -= 1
    elif level == 'puzzle':
        user.puzzle_count -= 1
    user.save()
    return Response({'message': 'Ma\'lumot muvaffaqiyatli yangilandi.'})


@api_view(['GET'])
def ViewCount(request, userId):
    user = Users.objects.get(telegram_id=userId)
    entry_count = user.entry_count
    middle_count = user.middle_count
    high_count = user.high_count
    puzzle_count = user.puzzle_count
    return Response({'entry_count': entry_count,
    'middle_count': middle_count,
    'high_count': high_count,
    'puzzle_count': puzzle_count})


@api_view(['PUT'])
def add_number(request, userId, level):
    user = Users.objects.get(telegram_id=userId)
    if level=='entry':
        user.entry_count += 1
    elif level == 'middle':
        user.middle_count += 1
    elif level == 'high':
        user.high_count += 1
    elif level == 'puzzle':
        user.puzzle_count+=1
    user.save()
    return Response({'message': 'Ma\'lumot muvaffaqiyatli yangilandi.'})

@api_view(['PUT'])
def sub_number(request, userId, level):
    user = Users.objects.get(telegram_id=userId)
    if level=='entry':
        user.entry_count -= 1
    elif level == 'middle':
        user.middle_count -= 1
    elif level == 'high':
        user.high_count -= 1
    elif level == 'puzzle':
        user.puzzle_count-=1
    user.save()
    return Response({'message': 'Ma\'lumot muvaffaqiyatli yangilandi.'})