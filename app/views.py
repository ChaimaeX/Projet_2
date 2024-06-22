from django.shortcuts import redirect, render
from django.views import View
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
class LoginView(View):
    templates_names="log.html"
    def get(self,request,*arg,**kwargs):
        return render(request,self.templates_names)
    def post(self, request, *args, **kwargs):
        form = LoginForm()
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(request, username=username, password=password)

          if user is not None:
                if  user.is_authenticated and user.is_superuser:
                   auth.login(request, user)
                   return redirect('Home')
                else:
                    auth.login(request, user)
                    # messages.success(request, 'Connexion réussie.')
                    return redirect('Home')
          else:
                messages.error(request, 'Informations de connexion incorrectes.')
        else:
          messages.error(request, 'Formulaire invalide. Veuillez réessayer.')
        return render(request,self.templates_names)  
     
class HomeView(View):
    templates_names="PageAdmin.html"
    def get(self,request,*arg,**kwargs):
        name = request.user.username
        print(name)
        context = {'name':name}
        return render(request,self.templates_names,context)

class custumerView(View):
    templates_names="PageCostumer.html"
    users = User.objects.all()
    context = {'users': users}

    def get(self,request,*args,**kwargs):
        
        return render(request, self.templates_names,self.context)

class MessagesView(View):
    templates_names="PageCostumer.html"
    def get(self,request,*arg,**kwargs):
        return render(request,self.templates_names)
    
class addDoctorView(View):
    templates_names="AddDoctor.html"
    def get(self,request,*arg,**kwargs):
        return render(request,self.templates_names)
    def post(self,request,*args,**kwargs):
        cutumer = request.user.id
        nom = request.POST.getlist('nom')
        prenom = request.POST.getlist('prenom')
        specialite = request.POST.getlist('specialite')
        Exercice = request.POST.get('Exercice')
        ug = request.POST.get('ug')
        Ville = request.POST.get('Ville')
        adresse = request.POST.get('adresse')
        potentiel = request.POST.get('potentiel')
        coeur = request.POST.get('coeur')
        titre = request.POST.get('titre')
        frequence = request.POST.get('frequence')
        return render(request,self.templates_names)


class addCostumerView(View):
    templates_names="AddCustumer.html"
    context={}
    def get(self,request,*arg,**kwargs):
        return render(request,self.templates_names)
    def post(self,request,*arg,**kwargs):

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            
    
            messages.success(request,'data saved seccessfully..')
                
              
            self.context = {'registerform':form}
        else:
            print('hello')
            messages.error(request,'data not saved ..')


             
        return render(request,self.templates_names,self.context)
    
def user_logout(request):

    auth.logout(request)

    return redirect("Login")
