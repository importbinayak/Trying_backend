from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post

# Create your views here.

def post_list(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return JsonResponse({'data':serializer.data})