from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
# Create your views here.
def Validator_Forms(request):
    form=NameForm()
    d={'form':form}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'Validator_Forms.html',d)