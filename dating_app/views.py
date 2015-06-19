from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'dating_app/index.html')


def user_list(request):
    users = User.objects.filter(is_staff=False)  # <-- To exclude the administrators
    return render(request, 'dating_app/user/list.html', {'users': users})
