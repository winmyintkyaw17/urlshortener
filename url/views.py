from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Url
from hashlib import md5
from django.contrib import messages
# Create your views here.
def url_list(request):
    urls = Url.objects.all()
    print(urls)
    return render(request, "url_list.html", {
        "urls": urls
    })
def delete_url(request, id):
    if request.method == "POST":
        url = get_object_or_404(Url, pk=id)
        return HttpResponse("delete")
def update_url(request, id):
    url = get_object_or_404(Url, pk=id)
    if request.method == "POST":
        #init status
        status =False
        req_url = request.POST.get("url")

        check_url = URLValidator()

        try:
            check_url(req_url)
        except ValidationError as e:
            return render(request, "sg_url.html",{
                "error": e.message,
                "old_value": url
            })
        status= True
        #hash the code using md5
        hash_code= md5(req_url.encode()).hexdigest()[:10]

        #create host
        host = request.get_host()
        #build hash url
        hash_url = "http://" +host + "/"+ hash_code

        #update data
        url.hash_url= hash_url
        url.actual_url= req_url
        url.save()
        messages.success(request, "Hey you just updated successfully")

        return redirect("sg_url", id= url.id)
    return render(request, "sg_url.html", {
        "url": url
    })

def index(request):
    if request.method == "POST":
        #init status
        
        url = request.POST.get("url")

        check_url = URLValidator()

        try:
            check_url(url)
        except ValidationError as e:
            return render(request, "home.html",{
                "error": e.message,
                "old_value": url
            })
        
        #hash the code using md5
        hash_code= md5(url.encode()).hexdigest()[:10]

        #create host
        host = request.get_host()
        #build hash url
        hash_url = "http://" +host + "/"+ hash_code
        create_url = Url(hash_url = hash_url, actual_url = url)
        create_url.save()
        messages.success(request,"Hey You just inserted successfully")
        return redirect("home")

        print(hash_code)
        return render(request, "home.html", {
                "message": f"Shortened URL: {hash_url}"
            })
    # else:
    #     return render(request, "home.html", {
    #             "error": "URL field is empty."
    #         })
    return render(request,"home.html")