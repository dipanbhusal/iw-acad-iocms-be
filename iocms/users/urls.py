from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

from .views import CreateStudentView, CreateTeacherView


app_name = "users"

router = DefaultRouter()
router.register('api/student-register', CreateStudentView, basename='StudentModel')
router.register('api/teacher-register', CreateTeacherView, basename='TeacherModel')


urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', auth_views.obtain_auth_token, name='login')
]
