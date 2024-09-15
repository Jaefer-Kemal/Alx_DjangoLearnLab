from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm

def register(request):
    if request.method == "POST":
        form =  RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Username: {username}, your account is created")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,"blog/register.html",{"form":form})


def index(request):
    return render(request,"blog/index.html")


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'blog/profile.html', {'user': user})

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = "post"
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
# def post_detail_view(request, primary_key):
#     try:
#         post = post.objects.get(pk=primary_key)
#     except Post.DoesNotExist:
#         raise Http404('Post does not exist')

#     return render(request, 'blog/post_detail.html', context={'post': post})

class PostCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    template_name = 'blog/post_form.html'  
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  
    form_class = PostForm 

    def test_func(self):
        post = self.get_object()  
       
        return self.request.user == post.author  # Check if the logged-in user is the author
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,generic.edit.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'  
    success_url = reverse_lazy('post-list') 
    
    
    
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author