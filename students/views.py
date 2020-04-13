from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm
from django.views.generic.list import ListView
from courses.models import Course
from django.views.generic.detail import DetailView
from .forms import UserForm, SignUpForm
from django.core.mail import send_mail
from instinct_hub.settings import EMAIL_HOST_USER


#To Noah: Pull in data from the form (cd) to populate variables

class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = SignUpForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        subject = 'I am a subject'
        message = 'I am a message'
        email = ['mustyumr@gmail.com',]

        result = super(StudentRegistrationView,
                       self).form_valid(form)
        cd = form.cleaned_data

        send_mail(subject, message, EMAIL_HOST_USER, email, fail_silently=False)

        user = authenticate(username=cd['username'],
                           password=cd['password1'])
        
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView,
                     self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail',
                            args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView,
                        self).get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(
                                    id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()[0]
        return context
