from django.shortcuts import render,HttpResponseRedirect ,reverse
#from django.contrib.auth.models import User
from .forms import AvtorizeForm, userRegistration
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    context = {}
    context['app_title']='Стартовая страница'
    return render(request,'ServiceExpenses/base.html',context)


def avtorization(request):
    if request.method == 'POST':
        form = AvtorizeForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Правильный пароль и пользователь "активен"
                auth.login(request, user)
                # Перенаправление на "правильную" страницу
                return HttpResponseRedirect(reverse('office'))
            else:
                context={
                'error_avt': 'Неправильный пароль или пользователь заблокирован',
                'form': form,
            }
            return render(request,'ServiceExpenses/avtorization.html',context)
        else:
            context={
                'error_avt': 'Некоректные данные при заполнении',
                'form': form,
            }
            return render(request,'ServiceExpenses/avtorization.html',context)

    else:
        context = {'form': AvtorizeForm()}
        return render(request,'ServiceExpenses/avtorization.html',context)


@login_required(login_url='/avtorization')
def office(request):
    return render(request,'ServiceExpenses/office.html')


def logout(request):
     auth.logout(request)
     return  render(request,'ServiceExpenses/base.html')

def registration(request):
    if request.method == 'POST':
        form = userRegistration(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            password2 = request.POST['password2']
            context={'form': form}
            if len(password)<8:
                context['error_avt']='Пароль должен быть больше 8 символов'
                return render(request,'ServiceExpenses/registration.html',context)                    
            elif password !=password2:
                context['error_avt']='Оба пароля должны совпадать'  
                return render(request,'ServiceExpenses/registration.html',context)
            else:                
                user = User.objects.create_user(username=username,
                                    password=password)
                user.save()
                return HttpResponseRedirect(reverse('avtorization'))
    else:
        context = {'form': userRegistration()}
        return render(request,'ServiceExpenses/registration.html',context)