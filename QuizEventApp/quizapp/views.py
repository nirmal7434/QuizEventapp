from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Quiz, UserSubmission, Answer, UserAnswer, Event
from .serializers import QuizSerializer, QuizDetailSerializer, UserAnswerSerializer, EventSerializer


def home(request):
    return render(request, 'home.html')


def quiz_list(request):
    quizess = Quiz.objects.all()
    return render(request,'quiz_list.html',{'quizzes':quizess})

def take_quiz(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(request,'take_quiz.html',{'quiz':quiz, 'questions':questions})


def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()


    submission = UserSubmission.objects.create(
        quiz=quiz,
        user_name=request.POST.get("user_name", "Guest")
    )

    score = 0

    for q in questions:
        user_answer_id = request.POST.get(f"q{q.id}")

        if user_answer_id:
            try:
                selected_answer = Answer.objects.get(id=user_answer_id)
            except:
                selected_answer = None
        else:
            selected_answer = None

        is_correct = False
        if selected_answer and selected_answer.is_correct:
            score += 1
            is_correct = True


        UserAnswer.objects.create(
            submission=submission,
            question=q,
            answer=selected_answer,
            is_correct=is_correct
        )


    submission.score = score
    submission.save()


    total_questions = questions.count()
    percentage = round((score / total_questions) * 100) if total_questions > 0 else 0

    return render(request, "result.html", {
        "quiz": quiz,
        "score": score,
        "total": total_questions,
        "submission": submission,
        "percentage": percentage
    })


def events_list(request):

    events = Event.objects.all().order_by('date')


    today = date.today()


    upcoming_count = Event.objects.filter(date__gte=today).count()


    cities_count = Event.objects.values('location').distinct().count()


    for event in events:
        event.is_upcoming = event.date >= today

    context = {
        'events': events,
        'upcoming_count': upcoming_count,
        'cities_count': cities_count,
    }

    return render(request, 'events.html', context)

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")


        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("home")


        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("home")


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect("home")

    return redirect("home")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("home")

    return redirect("home")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")



# ------------------- DRF APIs --------------------------------------------------

class QuizListApi(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailApiview(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer

class SubmitQuizAPIView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer

    def create(self, request, quiz_id, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_name = serializer.validated_data.get("user_name", "Guest")
        answers_dict = serializer.validated_data.get("answers", {})

        quiz = Quiz.objects.get(id=quiz_id)
        questions = quiz.questions.all()

        submission = UserSubmission.objects.create(
            quiz=quiz,
            user_name=user_name
        )

        score = 0


        for q in questions:
            key = f"q{q.id}"
            user_answer_id = answers_dict.get(key)

            if user_answer_id:
                try:
                    selected_answer = Answer.objects.get(id=user_answer_id)
                except Answer.DoesNotExist:
                    selected_answer = None
            else:
                selected_answer = None

            is_correct = False
            if selected_answer and selected_answer.is_correct:
                score += 1
                is_correct = True


            UserAnswer.objects.create(
                submission=submission,
                question=q,
                answer=selected_answer,
                is_correct=is_correct
            )

        submission.score = score
        submission.save()

        total_questions = questions.count()
        percentage = round((score / total_questions) * 100) if total_questions > 0 else 0

        return Response({
            "quiz": quiz.title,
            "user_name": submission.user_name,
            "score": score,
            "total_questions": total_questions,
            "percentage": percentage,
            "submission_id": submission.id
        }, status=status.HTTP_201_CREATED)

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer

    def get_queryset(self):
        today = date.today()
        if self.request.GET.get('upcoming') == 'true':
            return Event.objects.filter(date__gte=today).order_by('date')
        return Event.objects.all().order_by('date')