from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PostForm


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list()) # Many To Many를 사용하려면 Post가 저장되어 pk값이 있어야 한다.
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect("/")
    else:
        form = PostForm()
    return render(request, 'instagram/post_form.html', {
        'form': form,
    })
