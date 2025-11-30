from datetime import date

from rest_framework import serializers

from .models import Quiz, Question,Answer,UserSubmission,UserAnswer,Event

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = '__all__'


class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = '__all__'

class UserAnswerSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=False, default="Guest")
    answers = serializers.DictField()


class EventSerializer(serializers.ModelSerializer):
    is_upcoming = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = '__all__'

    def get_is_upcoming(self, obj):
        return obj.date >= date.today()
