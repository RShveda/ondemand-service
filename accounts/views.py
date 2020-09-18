from django.shortcuts import render
from django.contrib.auth.models import Group
from accounts.models import User
from rest_framework import viewsets
from rest_framework import permissions
from accounts.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def home(request):
    return render(request, "home.html")

