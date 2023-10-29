from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Article

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def create_superuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create_superuser(username=username, password=password)
        return redirect('admin-login')  # Redirect to the admin login page or any other page as needed
    return render(request, 'admin_login.html')  # Display the admin login page



class HomePageView(TemplateView):
    template_name = 'home.html'

class AdminLoginView(TemplateView):
    template_name = 'admin_login.html'

class ArticlesView(TemplateView):
    template_name = 'articles.html'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()  # Retrieve all articles
        return context

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'author', 'doi_link', 'pdf_file']
    success_url = '/articles/'
