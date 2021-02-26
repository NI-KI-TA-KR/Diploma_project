from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from resume.models import Resume, Comment
from django.utils import timezone
from sklearn import tree
import pandas as pd
import sqlite3 

@login_required(login_url='login')
def main_gl(request):
    
    users=User.objects.all()
    count_users=users.count()
    
    resumes=Resume.objects.all()
    count_resume=resumes.count()
    
    comments=Comment.objects.all()
    count_comment=comments.count()
    
    context={'count_users':count_users, 'count_resume':count_resume,'count_comment':count_comment}
    return render(request, 'main_gl.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                group = Group.objects.get(name='user')
                user.groups.add(group)
                
                messages.add_message(request, messages.SUCCESS, 'Account was created for ' + username)
                return redirect('login')

        context={'form' :form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return  redirect('/')
            else: 
                messages.info(request,'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_resume(request):
    messages.add_message(request, messages.SUCCESS, 'Resume was created')
    return render(request, 'resume/add_resume.html')

@login_required(login_url='login')
def create_resume(request):

    
    
    res = Resume(user_id=request.user.id, resume_PIB = request.POST['PIB'], resume_email=request.POST['email'], resume_adress=request.POST['adress'], resume_phone=request.POST['phone'], resume_github=request.POST['github'], resume_years=request.POST['years'], resume_position=request.POST['position'], resume_experience=request.POST['experience'], resume_education=request.POST['education'], resume_lng_c_plus=request.POST['lng_c_plus'], resume_lng_c_sharp=request.POST['lng_c_sharp'], resume_lng_pascal=request.POST['lng_pascal'],
    resume_lng_java=request.POST['lng_java'], resume_lng_html_css=request.POST['lng_html_css'], resume_lng_JS=request.POST['lng_JS'], resume_lng_Bootstrap=request.POST['lng_Bootstrap'], resume_lng_php=request.POST['lng_php'], resume_lng_python=request.POST['lng_python'], resume_lng_django=request.POST['lng_django'], resume_lng_NET=request.POST['lng_NET'], resume_lng_nodejs=request.POST['lng_nodejs'], resume_cms_wordpress=request.POST['cms_wordpress'], resume_cms_joomla=request.POST['cms_joomla'], resume_cms_drupal=request.POST['cms_drupal'], resume_os_windows=request.POST['os_windows'], resume_os_linux=request.POST['os_linux'], resume_os_macos=request.POST['os_macos'], resume_english=request.POST['english'], resume_date=timezone.now())
    
    res.save()
    
    data = pd.DataFrame({'exprexience': [ 0,0, 0,0, 2, 0,2,2,2,2,2,4,4,4,6,6,6,0,0,0,0], 'education': [0,0, 2, 2, 4, 2,4,4,4,4,4,4,4,4,6,6,6,0,0,0,0], 'english': [0, 0,0 ,2,2,0,2,2,4,4,4,4,4,4,6,6,6,2,2,4,2], 'lang_prog': [0,1,2,1,6,1,2,2,8,4,4,10,4,4,12,6,6,6,6,4,6], 'web_prog': [0,0,1,2,2,1,6,2,4,8,4,4,10,4,6,12,6,5,6,6,12], 'cms':
                     [0,0,0,0,2,2,6,2,4,4,8,4,4,10,6,6,12,12,6,0,8], 'os': [0,0,1,1,2,1,4,4,6,6,6,8,8,8,10,10,10,8,8,8,8], 'Position': [0,0,1,1,2,1,2,2,3,3,3,4,4,4,5,5,5,1,1,1,3], 'Area':[0,0,1,2,1,3,2,3,1,2,3,1,2,3,1,2,3,3,2,1,3]})


    clf=tree.DecisionTreeClassifier()

    X=data[['exprexience', 'education', 'english','lang_prog', 'web_prog','cms', 'os']]
    Y=data[['Position','Area']]
    
    clf.fit(X,Y)
    
    con = sqlite3.connect("db.sqlite3")
    data_site = pd.read_sql("SELECT * from resume_resume", con)

    data_site_new=pd.DataFrame()
    data_site_new['exprexience'] = data_site['resume_experience'].map({"I have not": 0, "0.5-3 years": 2, "3-5 years": 4, "More than 5 years": 6})
    data_site_new['education'] = data_site['resume_education'].map({"Secondary education": 0, "Junior Specialist": 2, "Bachelor": 4, "Mas4ter": 6})
    data_site_new['english'] = data_site['resume_english'].map({"don't now": 0, "first level": 2, "middle level": 4, "expert": 6})
#data_site_new['lang_prog'] = 0

    data_site_new['lng_c_plus']= data_site['resume_lng_c_plus'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_c_sharp']= data_site['resume_lng_c_sharp'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_pascal']= data_site['resume_lng_pascal'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_java']= data_site['resume_lng_java'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_python']= data_site['resume_lng_python'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_net']= data_site['resume_lng_NET'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lang_prog']= data_site_new['lng_c_plus'] + data_site_new['lng_c_sharp'] + data_site_new['lng_pascal'] + data_site_new['lng_java'] +data_site_new['lng_python'] + data_site_new['lng_net'] 
    data_site_new=data_site_new.drop(['lng_c_plus', 'lng_c_sharp', 'lng_pascal', 'lng_java', 'lng_python', 'lng_net'], axis=1 )

    data_site_new['lng_html_css']= data_site['resume_lng_html_css'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_JS']= data_site['resume_lng_JS'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_Bootstrap']= data_site['resume_lng_Bootstrap'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_php']= data_site['resume_lng_php'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_nodejs']= data_site['resume_lng_nodejs'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['lng_django']= data_site['resume_lng_django'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['web_prog']= data_site_new['lng_html_css'] + data_site_new['lng_JS'] + data_site_new['lng_Bootstrap'] + data_site_new['lng_php'] +data_site_new['lng_nodejs'] + data_site_new['lng_django'] 
    data_site_new=data_site_new.drop(['lng_html_css', 'lng_JS', 'lng_Bootstrap', 'lng_php', 'lng_nodejs', 'lng_django'], axis=1 )

    data_site_new['cms_drupal']= data_site['resume_cms_drupal'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['cms_wordpress']= data_site['resume_cms_wordpress'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['cms_joomla']= data_site['resume_cms_joomla'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['cms']= data_site_new['cms_drupal'] + data_site_new['cms_wordpress'] + data_site_new['cms_joomla'] 
    data_site_new=data_site_new.drop(['cms_drupal', 'cms_wordpress', 'cms_joomla'], axis=1 )
    data_site_new['cms']*=2

    data_site_new['os_windows']= data_site['resume_os_windows'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['os_linux']= data_site['resume_os_linux'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['os_macos']= data_site['resume_os_macos'].map({"don't now": 0, "basic knowledge": 1,"experienced":2})
    data_site_new['os']= data_site_new['os_windows'] + data_site_new['os_linux'] + data_site_new['os_macos'] 
    data_site_new=data_site_new.drop(['os_windows', 'os_linux', 'os_macos'], axis=1 )
    data_site_new['os']*=2
    
    data_progn = clf.predict(data_site_new)
    
    data_add=pd.DataFrame(data_progn)
    data_add['system_position']=data_add[0].map({0:"no suit", 1:"intern",2:"junior developer", 3:"middle developer", 4:"senior developer",5:"Team Lead"})
    data_add['system_area']=data_add[1].map({0:" ", 1:"programming", 2:"web-programming",3:"system administration"})
    data_add=data_add.drop([0,1], axis=1)
    data_add['user_id']=data_site['user_id']
    data_add['id']=data_site['id']
    
    #con.execute("DROP TABLE IF EXISTS resume_position_area")
    data_add.to_sql("resume_position_area", con, if_exists='replace', index = False)
    
    return redirect('/my_resume') 

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def my_resume(request):
    a=Resume.objects.get(id=request.user.resume.id)
    latest_comments_list = a.comment_set.order_by('-id')[:3]
    return render(request, 'my_resume.html', {'latest_comments_list':latest_comments_list})
        
    
    

