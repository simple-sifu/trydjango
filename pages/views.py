from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print("user is ++++>", request.user)
    # return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})   # string of HTML code


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [15,20,40],
    }
    return render(request, "about.html", my_context)   # string of HTML code
