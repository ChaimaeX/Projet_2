from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    templates_names="PageAdmin.html"
    def get(self,request,*arg,**kwargs):
        return render(request,self.templates_names)
