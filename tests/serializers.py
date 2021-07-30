from rest_framework import serializers
from .models import Answer, Test

class AnswerSerializer(serializers.ModelSerializer):

    question= serializers.ReadOnlyField(source='question.content')
    student= serializers.ReadOnlyField(source='student.name')

    class Meta:
        model= Answer
        fields=[
            'student', 
            'question', 
            'chosen_answer',
            'correct_answer', 
            'correct',
            'test'
            ]

class TestSerializer(serializers.ModelSerializer):

    student= serializers.ReadOnlyField(source='student.name')
    subject= serializers.ReadOnlyField(source='subject.name')

    class Meta:
        model= Test
        fields=['student','subject', 'grade']