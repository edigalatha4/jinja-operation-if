from django.shortcuts import render

# Create your views here.
def operation(request):
    d={'a':20}
    return render(request,'operation.html',d)
