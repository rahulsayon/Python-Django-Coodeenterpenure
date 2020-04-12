from django.shortcuts import render , get_object_or_404
from django.views import View
from . models import Course

# Create your views here.
class CourseView(View):
    template_name = "courses/about.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{})


class CourseDetailsView(View):
    template_name = "courses/details.html"
    
    def get(self,request,id=None,*args,**kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course,id=id)
            context["object"] = obj
        return render(request,self.template_name,context)

class CourseListView(View):
    template_name = "courses/list.html"
    obj = Course.objects.all()


    def get_queryset(self):
        return self.obj

    def get(self,request,*args,**kwargs):
        context = {}
        context["object_list"] = self.get_queryset()
        return render(request,self.template_name,context)