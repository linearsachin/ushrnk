from django.shortcuts import render,redirect
from django.views.generic import View ,ListView
import random, string
from .models  import (
    ShrnkUrl,
    Click,
)
from .forms import (
    ShrnkForm
)
# Create your views here.
class HomeView(View):
    def get(self, request,slug=False, *args, **kwargs):
        form = ShrnkForm()
        context = {
            'form':form,
            'slug':slug
        }
        return render(request,'core/index.html',context)
 
    def post(self, request, *args, **kwargs):
        form = ShrnkForm(request.POST or None)
        if form.is_valid():
            og_url = form.cleaned_data.get('og_url')
            if not ShrnkUrl.objects.filter(og_url=og_url).exists():
                shrnk_url_slug = self.unique_id()
                ShrnkUrl.objects.create(
                    og_url = og_url,
                    shrnk_url_slug = shrnk_url_slug,
                )
            slug = ShrnkUrl.objects.get(
                og_url = og_url,
            )
            context = {
                'form':ShrnkForm(data={
                    'og_url':og_url
                }),
                'slug':slug,
            }
            return render(request,'core/index.html',context)

    def unique_id(self):
        letters = string.ascii_letters
        ui = str(random.randint(100,999)) + ''.join(random.choice(letters) for i in range(4))
        sr = ''.join(random.sample(ui, len(ui)))
        return sr

class ShrnkView(View):
    def get(self, request,slug, *args, **kwargs):
        shrnk_url = ShrnkUrl.objects.get(
            shrnk_url_slug=slug
        )
        return redirect(shrnk_url.og_url)
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')