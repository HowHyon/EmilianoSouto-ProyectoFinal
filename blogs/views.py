from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from blogs.models import Post, Categorias
from blogs.models import timezone
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from blogs.forms import *
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, CreateView
from django.contrib import messages

# Create your views here.

def home_page(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now()
    )
    categorias = Categorias.objects.all()
    destacado = Post.objects.filter(destacado=True).filter(
        pub_date__lte=timezone.now()
    )[:3]
    
    context = {
        'post_listas': posts,
        'destacado': destacado
    }
    
    
    return render(request, 'blogs/home_page.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(
        pub_date__lte=timezone.now()
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCommentForm()
        return context
    
    
    
class FeaturedListView(generic.ListView):
        model = Post
        template_name = 'blogs/results.html'
        paginate_by = 2
        
        def get_queryset(self):
            query = Post.objects.filter(destacado=True).filter(
            pub_date__lte=timezone.now()
            )
            return query
             
        
      
class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'
    paginate_by = 2
    
    def get_queryset(self):
        query = self.request.path.replace('/categoria/', '')
        post_list = Post.objects.filter(categorias__slug=query).filter(
            pub_date__lte=timezone.now()
            )
        return post_list
             
    
    
class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'
    paginate_by = 2
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        post_list = Post.objects.filter(
            Q(titulo__icontains=query) | Q(categorias__titulo__icontains=query)
        ).filter(
            pub_date__lte=timezone.now()
        ).distinct()
        return post_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')
        return context
    
    
class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'blogs/post_detail.html'
    form_class = PostCommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor = self.request.user
        f.post = self.object
        f.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('blogs:post', kwargs={'slug': self.object.slug}) + '#comments-section'


class PostView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)

    
@login_required
def agregar_post(request):
    """View to add new posts."""

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = NuevoPost()
    
    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = NuevoPost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, '¡Nuevo post agregado con éxito!')
            return redirect('blogs:NewPost')

    context = {
        'form': form, 
        'title': 'Nuevo Post',
    }
    return render(request, 'new_post.html', context)

######

def eliminar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.autor:
        if request.method == 'POST':
        # Confirmar la eliminación del post
            post.delete()
            return redirect('/')  # Redirigir a la página principal o a donde desees después de eliminar
        return render(request, 'blogs/eliminar_post.html', {'post': post})
    

def editar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Verifica si el usuario actual es el autor del post
    if request.user == post.autor:
        if request.method == 'POST':
            form = NuevoPost(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = NuevoPost(instance=post)
        return render(request, 'blogs/editar_post.html', {'form': form, 'post': post})
    
    
def aboutMe(request):
    return render(request, 'about_me.html')