from django.shortcuts import render
from .models import Post, Category, Comment
from taggit.models import Tag
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.

def potst_list (request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)

    page_number = request.GET.get('page')
    post_list = paginator.get_page(page_number)

    context = {
        'post_list' : post_list

    }

    return render(request, 'Post/post_list.html', context)

def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    tag = Tag.objects.all()
    comment_list = Comment.objects.filter(post=post_detail)
    comment_total = comment_list.count()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()
    else:
        comment_form = CommentForm()


    context = {
        'post_detail' : post_detail,
        'categories' : categories,
        'tags' : tag,
        'comment_list' : comment_list,
        'comment_total' : comment_total,
        'comment_form' : comment_form
    }

    return render(request, 'Post/post_detail.html', context)

def post_by_tag(request, tag):
    potst_list = Post.objects.filter(tags__name__in=tag)

    context = {
        'potst_list' : potst_list
    }

    return render(request, 'Post/post_list.html', context)

def post_by_category(request, category):
    potst_list = Post.objects.filter(category__name=category)

    context = {
        'potst_list' : potst_list
    }

    return render(request, 'Post/post_list.html', context)
