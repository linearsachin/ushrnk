from django.shortcuts import render,redirect
from django.views.generic import View ,ListView
import random, string
from django.db.models import F
from django.utils import timezone
from django.http import JsonResponse
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
        print(request.META)

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
                    xcode=self.generate_xcode(),
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
        we_dont_have_it = True
        while we_dont_have_it:
            try:
                letters = string.ascii_letters + '1234567890'
                ui = ''.join(random.choice(letters) for i in range(7))
                sr = ''.join(random.sample(ui, len(ui)))
                return sr
            except:
                we_dont_have_it=True
        return None
    def generate_xcode(self):
        we_dont_have_it = True
        while we_dont_have_it:
            try:
                letters = string.ascii_letters + '0123456789'
                ui = str(random.randint(10,99)) + ''.join(random.choice(letters) for i in range(3))
                sr = ''.join(random.sample(ui, len(ui)))
                return sr
            except:
                we_dont_have_it=True
        return None


class ShrnkView(View):
    def get(self, request,slug, *args, **kwargs):
        shrnk_url = ShrnkUrl.objects.filter(
            shrnk_url_slug=slug
        )
        shrnk_url.update(total_clicks=F('total_clicks')+1)
        if Click.objects.filter(
            shrnk_url = shrnk_url[0], 
            date = timezone.now().date(),
        ).exists():
            click = Click.objects.filter(shrnk_url = shrnk_url[0],date = timezone.now().date(),)
            click.update(clicks = F('clicks')+1)
        else:
            Click.objects.create(
                shrnk_url = shrnk_url[0],
                date = timezone.now().date(),
                clicks=1,
            )
        return redirect(shrnk_url[0].og_url)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'core/metrics.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

def chart(request, xcode):
    labels = []
    data = []
    shrnk = ShrnkUrl.objects.get(xcode=xcode)
    queryset = Click.objects.filter(shrnk_url =shrnk ).order_by('-date')
    for entry in queryset:
        labels.append(entry.date)
        data.append(entry.clicks)
    print(labels, data)
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


