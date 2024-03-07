from django.db import models
from django.contrib.auth.models import AbstractUser

class AdminUser(AbstractUser):
    def __str__(self):
        return self.username

# Foydalanuvchilar
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    telegram_id = models.BigIntegerField(unique=True)
    start_time = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField(default=0)
    entry = models.IntegerField(default=0)
    middle = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    puzzle = models.IntegerField(default=0)
    entry_count = models.IntegerField(default=1)
    middle_count = models.IntegerField(default=1)
    high_count = models.IntegerField(default=1)
    puzzle_count = models.IntegerField(default=1)


    def __str__(self):
        return f'{self.full_name}, {self.telegram_id}'

# Puzzle
class puzzle_question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return f"{self.id}"

class puzzle_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(puzzle_question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField()
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question_id}"

# Entry
class entry_questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}'

class entry_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(entry_questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField(default=True)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question_id}'

# Middle
class middle_questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)

    def __str__(self):
        return self.question

class middle_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(middle_questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField(default=True)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question_id}"

# High
class high_questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)

    def __str__(self):
        return self.question

class high_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(high_questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField()
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question_id}"
