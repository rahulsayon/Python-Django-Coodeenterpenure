
from django.urls import path
from .views import CourseView,CourseDetailsView,CourseListView

urlpatterns = [
    # path('contact/' , contact_view),
    path('' , CourseListView.as_view()),
    path('about/' , CourseView.as_view(template_name="courses/about.html"),name="about"),
    path('<int:id>/' , CourseDetailsView.as_view()),
    # path('articles/' , include('blogs.urls')),
    
        


]
