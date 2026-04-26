from django.shortcuts import get_object_or_404, render
from Q1.forms import StudentForm
from Q1.models import Course, Student

# Create your views here.
def add_Course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')

        course = Course(name=name, description=description, duration=duration)
        course.save()

    return render(request, 'add_course.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def enroll_student(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        student.courses.add(course)

        return render(request, 'course_detail.html', {
            'student': student,
            'course': course
        })

    return render(request, 'enroll.html', {
        'form': form,
        'course': course
    })

def student_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'student_course.html', {
        'course': course,
        'students': students
    })
