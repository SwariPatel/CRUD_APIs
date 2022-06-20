from django.urls import re_path
from schoolApp import views


urlpatterns = [
    # end points of create and read API
    re_path(r'^studentRecord/',views.studentRecordApi),
    # end point of delete API
    re_path(r'^delete/([0-9]+)$',views.studentRecordApi),

]



