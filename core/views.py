from django.shortcuts import render
from django.views.generic import View ,ListView

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'core/index.html')
 
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')