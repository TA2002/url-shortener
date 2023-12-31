from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import LinkyURL

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()

        bg_image = 'https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?cs=srgb&dl=pexels-pixabay-36717.jpg&fm=jpg'
        context = {
            "title": "Linky.co",
            "form": the_form,
            "bg_image": bg_image
        }

        return render(request, "shortener/home.html", context)
    
    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.POST["url"])
        # print(request.POST.get("url"))
        form = SubmitUrlForm(request.POST)
        bg_image = 'https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?cs=srgb&dl=pexels-pixabay-36717.jpg&fm=jpg'
        context = {
            "title": "Linky.co",
            "form": form,
            "bg_image": bg_image
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = LinkyURL.objects.get_or_create(url = new_url)
            context = {
                "object": obj,
                "created": created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/link_exists.html"

            return render(request, template, context)
            # print(form.cleaned_data.get("url"))

        return render(request, template, context)


class URLRedirectView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LinkyURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)