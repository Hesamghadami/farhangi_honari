from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
    
class PostListView(ListView):
    
    template_name = 'blogs/Goods.html'
    paginate_by = 2
    context_object_name = 'posts'

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Post.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('username'):
            return Post.objects.filter(client__username = self.kwargs.get('username'))
        elif self.request.GET.get('search'):
            return Post.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Post.objects.filter(status=True) 



    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/GoodsDetails.html'
    context_object_name = 'post'

    





