from django.urls import re_path
from schoolApp import views


urlpatterns = [
    re_path(r'^studentRecord$',views.studentRecordApi),
    re_path(r'^studentRecord/([0-9]+)$',views.studentRecordApi),
]