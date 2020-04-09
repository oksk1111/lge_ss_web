from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import Post

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })


# def post_detail(request: HttpRequest, pk: int) -> HttpRequest:
#     # response = HttpRequest()
#     # response.write("Hello world")
#     # response.write("Hello world")
#     # return response
#
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

post_detail = DetailView.as_view(model=Post)


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")