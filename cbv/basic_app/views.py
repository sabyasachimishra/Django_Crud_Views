from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                        CreateView,UpdateView,DeleteView)
from . import models

# # Create your views here.
# def index(request):
#     return render(request,'index.html')

# We will create a basic class based view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("This is a class based View !")

# Now we will create a template view with CBV
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectkey']='This text is injected'
        return context


# Now we will create a List View

class SchoolListView(ListView):
    # if you donot want the default name which is model_list then you can rename it by following
    # context_object_name = 'schools'  --> This will return a variable named as schools
    model=models.School
    #this returns a list named as school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model=models.School
    # This returns a default variable name as lower case school(model name lower case)
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
