from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Resume
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .decorators import admin_only

@login_required(login_url='login')
@admin_only
def index(request):
    latest_resume_list = Resume.objects.order_by('-resume_date')[:10]
    return render(request, 'resume/main.html', {'latest_resume_list':latest_resume_list})


@login_required(login_url='login')
@admin_only
def detail_resume(request, resume_id):
    pass
    try:
        a = Resume.objects.get( id = resume_id)
    except:
        raise Http404("Резюме не знайдено")
        
    latest_comments_list = a.comment_set.order_by('-id')[:3]
    
        
    return render(request, 'resume/detail_resume.html', {'resume': a, 'latest_comments_list':latest_comments_list })


@login_required(login_url='login')
@admin_only
def leave_comment(request, resume_id):
    
    try:
        a = Resume.objects.get( id = resume_id)
    except:
        raise Http404("Резюме не знайдено")
    
    a.comment_set.create(author_name =request.POST['name'], comment_text=request.POST['text'], comment_type=request.POST['type'])
    
    #a.comment.create(resume_id=resume_id, author_name =request.POST['name'], comment_text=request.POST['text'])
    #com.save()
    
    return HttpResponseRedirect(reverse('resume:detail_resume', args =(a.id,)))
    #return redirect('/')
