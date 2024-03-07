from django.urls import include, path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import *

router = routers.DefaultRouter()
router.register(r'puzzle_question', PuzzleQuestionView)
router.register(r'puzzle_answer', PuzzleAnswerView)
router.register(r'entry_question', EntryQuestionView)
router.register(r'entry_answer', EntryAnswerView)
router.register(r'middle_question', MiddleQuestionView)
router.register(r'middle_answer', MiddleAnswerView)
router.register(r'high_question', HighQuestionView)
router.register(r'high_answer', HighAnswerView)
router.register(r'count_user', UserCountViewSet, basename='count_user')
router.register(r'count_questions', CountQuestions, basename='count_question')
router.register(r'users', UsersView, basename='users')

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('point/<int:telegram_id>/', point_get, name='point'),
   path('top_users/', top_users, name='top_users'),

   path('is_answers_entry/<int:telegram_id>/<int:question_id>/', is_answers_entry, name='is_answers'),
   path('is_answers_middle/<int:telegram_id>/<int:question_id>/', is_answers_middle, name='is_answers'),
   path('is_answers_high/<int:telegram_id>/<int:question_id>/', is_answers_high, name='is_answers'),
   path('is_answers_puzzle/<int:telegram_id>/<int:question_id>/', is_answers_puzzle, name='is_answers'),

   path('update_point/<str:telegram_id>/<int:point>/<str:level>/', UpdatePoint, name='update_point_entry'),
   path('find_user_id/<int:telegram_id>/', FindUserId, name='finduser_id'),
   path('get_count/<int:userId>/', ViewCount, name='view_count'),
   path('add_number/<int:userId>/<str:level>/', add_number, name='add_count'),
   path('sub_number/<int:userId>/<str:level>/', sub_number, name='sub_count'),
   path('', include(router.urls)),
]



urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

