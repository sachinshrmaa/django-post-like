from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import BlogPost



def post_view(request):
    post_list = BlogPost.objects.all()

    context = {
        'post': post_list,
    }

    return render(request, "post.html", context)



# Simple Post like without api
def post_like(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect("all-post")




# Post like Using Jsax and API
class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        post = get_object_or_404(BlogPost, id=pk)
        user = self.request.user

        liked = False
        updated = False

        if user.is_authenticated:
            if post.likes.filter(id=request.user.id).exists():
                liked = False
                post.likes.remove(request.user)
            else:
                liked = True
                post.likes.add(request.user)
            updated = True
        
        data = {
            "updated": updated,
            "liked": liked
        }
        
        return Response(data)
