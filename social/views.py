from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy

from .forms import PostModelForm, CommentModelForm
from .models import PostModel, CommentModel
from django.views.generic.edit import UpdateView, DeleteView


class PostModelListView(View):

    def get(self, request, *args, **kwargs):
        posts = PostModel.objects.all().order_by('-created_at')
        form = PostModelForm()
        context = {
            'post_list': posts,
            'form': form,

        }
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = PostModel.objects.all().order_by('-created_at')
        form = PostModelForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,

        }
        return render(request, 'social/post_list.html', context)


class PostModelDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=pk)
        form = CommentModelForm()
        comments = CommentModel.objects.filter(post=post).order_by('-created_at')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=pk)
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = CommentModel.objects.filter(post=post).order_by('-created_at')

        context = {
            'post': post,
            'form': form,
            'comments': comments,

        }

        return render(request, 'social/post_detail.html', context)


class PostModelUpdateView(UpdateView):
    model = PostModel
    fields = ['body']
    template_name = 'social/post_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})


class PostModelDeleteView(DeleteView):
    model = PostModel
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('social:post-list')


class CommentModelDeleteView(DeleteView):
    model = CommentModel
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})









