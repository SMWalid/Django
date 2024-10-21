from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer


def index(request):
    return HttpResponse("Hello you Lazy fucker, this is your first Django app!")


@api_view(['GET'])
def user_list(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, username):
    user = CustomUser.objects.get(username=username)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)



#def user_list(request):
#   users = CustomUser.objects.all().values('username', 'email', 'bio', 'location')
#   return JsonResponse(list(users), safe=False)

#def user_detail(request, username):
#    user = get_object_or_404(CustomUser, username=username)
#    user_data = {
#        'username': user.username,
#        'email': user.email,
#        'bio': user.bio,
#        'location': user.location,
#    }
#    return JsonResponse(user_data)

# Create your views here.
