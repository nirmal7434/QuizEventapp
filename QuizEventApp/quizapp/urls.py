from django.urls import path

from .views import QuizListApi, QuizDetailApiview, SubmitQuizAPIView, EventListAPIView

urlpatterns = [
    path('quizess/',QuizListApi.as_view(), name='quiz-list'),
    path('apiquiz/<int:pk>/',QuizDetailApiview.as_view(),name='quiz-detail'),
    path('apiquiz/<int:quiz_id>/submit/',SubmitQuizAPIView.as_view(), name='submit-quiz'),
    path('apievents/', EventListAPIView.as_view(), name='apievents-list'),

]