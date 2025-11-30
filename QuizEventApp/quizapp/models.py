from django.db import models

class Quiz(models.Model): # CRUD
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    Question_types = (
        ('mcq','multiple Choice'),
        ('text','Text Answer')
    )
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=20,choices=Question_types,default='mcq')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}({'Correct' if self.is_correct else 'Wrong'})"

class UserSubmission(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}-{self.quiz.title}-{self.score}"

class UserAnswer(models.Model):
    submission = models.ForeignKey(UserSubmission,on_delete=models.CASCADE,related_name='user_answers')
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.SET_NULL,null=True,blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} - {self.answer}"

class Event(models.Model): # CRUD
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=50)


    def __str__(self):
        return self.title