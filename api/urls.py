from django.urls import path,include
from . import views

urlpatterns = [
    #function based view
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    #class based view
    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),


]