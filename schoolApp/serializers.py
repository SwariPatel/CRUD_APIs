from rest_framework import serializers
from schoolApp.models import studentRecord

class studentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentRecord
        fields = ('rollnumber','name','age','marks')