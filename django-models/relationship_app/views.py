#1st task
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# 2nd task

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


#3rd 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import UserProfile






#1st
# Function-based 
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based 
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

#2nd

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    
    
    
# 3rd
def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')    