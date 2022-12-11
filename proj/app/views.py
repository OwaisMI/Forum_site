from django.shortcuts import render,redirect
from django.views.generic import (TemplateView, CreateView, DetailView,
                                DeleteView, ListView, UpdateView)
from app.models import *
from app.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#imports for comment functions
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

class index(TemplateView):
    template_name = 'app/index.html'

class About(TemplateView):
    template_name = 'app/about.html'

class createPost(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    # redirect_field_name = 'app/post_form.html' #Might need to change the tempalte

    form_class = PostForm

    model = Post
    
class deletePost(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('list')

class listPosts(ListView):
    model = Post
    
    # def get_queryset(self):
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# class updatePost(LoginRequiredMixin, UpdateView):
#     login_url = '/login/'
#     redirect_field_name = 'app/postPost.html' #Might need to change the tempalte

#     model = Post
#     fields = ('text',)

class DraftPost(LoginRequiredMixin, ListView):
    
    login_url = '/login/'
    #Might need to change the tempalte

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

class PostDetail(DetailView):
    model = Post


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish
    return redirect('post_detail',pk=pk)

#Lets handle comments now

@login_required
def add_comments(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            save_c_form = c_form.save(commit=False)
            save_c_form.post=post
            save_c_form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        c_form = CommentForm()
    return render(request,'app/comment_form.html',{'form':c_form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('post_detail')

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)