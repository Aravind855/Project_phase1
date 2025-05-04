from django.db import models
from django.contrib.auth.models import User
import pymongo
import os

# MongoDB Atlas Connection (for reference, actual connection is in views.py)
myClient = pymongo.MongoClient(os.getenv('MONGODB_URI', 'mongodb+srv://sutgJxLaXWo7gKMR:sutgJxLaXWo7gKMR@cluster0.2ytii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))

class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    interview_type = models.CharField(max_length=50)
    resume_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'interviews'

class InterviewResponse(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)

    class Meta:
        db_table = 'interview_responses'

class InterviewAnalysis(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    rating = models.IntegerField()
    explanation = models.TextField()

    class Meta:
        db_table = 'interview_analyses'