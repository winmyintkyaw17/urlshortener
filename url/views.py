from django.shortcuts import render
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Url
from hashlib import md5
# Create your views here.
def url_list(request):
    urls = Url.objects.all()
    print(urls)
    return render(request, "url_list.html", {
        "urls": urls
    })
def sg_url(request, id):
    return render(request, "sg_url.html")

def index(request):
    if request.method == "POST":
        #init status
        status =False
        url = request.POST.get("url")

        check_url = URLValidator()

        try:
            check_url(url)
        except ValidationError as e:
            return render(request, "home.html",{
                "error": e.message,
                "old_value": url
            })
        status= True
        #hash the code using md5
        hash_code= md5(url.encode()).hexdigest()[:10]

        #create host
        host = request.get_host()
        #build hash url
        hash_url = "http://" +host + "/"+ hash_code
        create_url = Url(hash_url = hash_url, actual_url = url)
        create_url.save()

        return render(request, "home.html", {
            "status": status
        })

        print(hash_code)
        return render(request, "home.html", {
                "message": f"Shortened URL: {hash_url}"
            })
    # else:
    #     return render(request, "home.html", {
    #             "error": "URL field is empty."
    #         })
    return render(request,"home.html")