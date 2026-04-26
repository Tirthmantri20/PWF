from django.contrib import admin
from django.urls import path

from Q1.views import add_Course, course_list, enroll_student, student_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_course/', add_Course, name='add_course'),
    path('courses/', course_list, name='course_list'),
    path('enroll/<int:course_id>/', enroll_student, name='add_enrollment'),
    path('courses/<int:course_id>/', student_course, name='student_course'),
    
]
