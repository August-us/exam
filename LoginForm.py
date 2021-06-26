from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.c

class LoginForm(forms.Form):
    username=forms.CharField(max_length=32,min_length=6,required=True,error_messages={"required":'用户名不能为空',"invalid":"格式错误"},widget=forms.TextInput(attrs={'class':'c'}))
    passwd=forms.CharField(max_length=32,min_length=6,widget=forms.PasswordInput)


# views.py

def login(request):
    if request.method=='POST':
        cur_form=LoginForm(request.POST)
        if cur_form.is_valid():
            name=cur_form.cleaned_data["username"]
            pswd=cur_form.cleaned_data["passwd"]
            # return HttpResponse('my name is login')
            return redirect()
        else:
            return render(request, 'login.html', {'title': 'login'})
    else:
        f=LoginForm()
        return render(request,'login.html',{'title':'login','form':f,"error":f.errors})
