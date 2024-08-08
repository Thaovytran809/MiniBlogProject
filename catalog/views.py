from django.shortcuts import render
from .models import Blog, Blogger, Comment
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    context = {
        'num_blogs' : num_blogs,
        'num_bloggers': num_bloggers
    }
    
    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5
class BlogDetailView(generic.DetailView):
    model = Blog
class BloggerListView(generic.ListView):
    model = Blogger
class BloggerDetailView(generic.DetailView):
    model = Blogger


# @permission_required("catalog.can_mark_returned")
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.blog.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context


class BloggerCreate(PermissionRequiredMixin, CreateView):
    model = Blogger
    fields = '__all__'
    permission_required = 'catalog.add_blogger'

class BloggerUpdate(PermissionRequiredMixin, UpdateView):
    model = Blogger
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    permission_required = 'catalog.change_blogger'

class BloggerDelete(PermissionRequiredMixin, DeleteView):
    model = Blogger
    success_url = reverse_lazy('blogger_list')
    permission_required = 'catalog.delete_blogger'
        
class BlogCreate(PermissionRequiredMixin, CreateView):
    model = Blog
    fields = '__all__'
    permission_required = 'catalog.add_blog'

class BlogUpdate(PermissionRequiredMixin, UpdateView):
    model = Blog
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    permission_required = 'catalog.change_blog'

class BlogDelete(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
    permission_required = 'catalog.delete_blog'

    


