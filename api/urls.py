from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    #function based view
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    # #class based view
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),

    path('',include(router.urls)),

    #class based views
    path('blogs/', views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),

    path('blogs/<int>:pk',views.BlogDetailView.as_view()),
    path('comments/<int>:pk',views.CommentDetailView.as_view()),


]