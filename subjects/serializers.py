from rest_framework import serializers
from .models import Question, Subject

class QuestionSerializer(serializers.ModelSerializer):

    subject= serializers.ReadOnlyField(source='subject.name')
    question_id= serializers.ReadOnlyField(source='id')

    class Meta:
        model= Question
        fields= [
            'subject', 'question_id',
            'content',
            'ans1','ans2',
            'ans3','ans4',
            'correct_answer'
        ]

class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Question
        fields= [
            'subject',
            'content',
            'ans1','ans2',
            'ans3','ans4',
            'correct_answer'
        ]

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model= Subject
        fields=['name', 'academic_year']