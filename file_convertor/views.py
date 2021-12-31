from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponse


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        return HttpResponse(content='Invalid Credentials', status=401)


def sign_up(request):
    # print(request)
    username = request.POST['username']
    print(username)
    password = request.POST['password']

    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
    except:
        return HttpResponse(content='Invalid input data', status=400)
