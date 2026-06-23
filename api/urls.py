from django.urls import path,include
from . import views

urlpatterns = [
    path('students/',views.studentsView),
    #function based view
    path('students/<int:pk>/',views.studentDetailView),

]