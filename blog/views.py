from ssl import VerifyMode
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

#aca creamos la vista del indice del blog, enlistamos todos los post que existen.
#eso tambien lo podriamos hacer en la vista home


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts=Post.objects.all()
        context = {
            "posts":posts
        }
        return render(request, "blog_list.html", context)

# que raro, hicimos una funcion duplicada pero usando post... nueva habilidad poderosa? mas que get?

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            "form":form
        }
        return render(request, "blog_create.html", context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get("title")
                contento = form.cleaned_data.get("contento")

                p, created=Post.objects.get_or_create(title=title, contento=contento)
                p.save()
                return redirect("blog:home")

        context={
        }
        return render(request, "blog_create.html", context)

class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post=get_object_or_404(Post, pk=pk)
        context = {
            "post":post  
        }
        return render(request, "blog_detail.html", context)

class BlogUpdateView(UpdateView):
        model=Post
        fields=["title","contento"]
        template_name="blog_update.html"

        def get_success_url(self):
            pk=self.kwargs["pk"]
            return reverse_lazy("blog:detail", kwargs={"pk":pk})

class BlogDeleteView(DeleteView):
        model=Post
        template_name="blog_delete.html"
        success_url=reverse_lazy("blog:home")
           