from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Question,Answer
#import decorator from django.contrib.auth.decorators
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers
import random
# Create your views here.
def loginpage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=email ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/')
        
        return render(request,'home.html')
    # return render(request,'home.html')
    return redirect('/home/')
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST.get('username')
        name=request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        department = request.POST.get('department')
        state = request.POST.get('state')
        if password1!=password2:
            messages.info(request,'Password not matching')
            return redirect('/register/')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists')
            return redirect('/register/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('/register/')
        else:
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=name)
            user.save()
            return redirect('/')
    # return render(request,'register.html')
@login_required
def home(request):
    if request.method == 'POST':
        q=request.POST.get('q')
        posts=Question.objects.filter(question=q)
        if posts:
            return render(request,'search.html',{'posts':posts})
        else:
            posts=Question.objects.all()
            return render(request,'search.html',{'posts':posts}) 

    else:
        answ=Answer.objects.all()
        answers=[]
        for i in answ:
            answers.append(i)
        random.shuffle(answers)
        ans=[]
        posts=[]
        user=[]
        uk=request.user.first_name
        for answer in answers:
            ans.append(answer)
            q_id=answer.forquestion_id
            q_obj=Question.objects.get(id=q_id)
            u_id=answer.author_id
            u_obj=User.objects.get(id=u_id)
            posts.append(q_obj)
            user.append(u_obj.username)
        zipp=zip(ans,posts,user)
        return render(request,'home.html',{'zipp':zipp,'uk':uk})
    
@login_required
def ask(request):
    return render(request,'ask.html')
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required
def posted(request):
    
    question = request.POST.get('question')
    #get user id
    user_id = request.user
    insta = Question(question=question)
    insta.author=user_id
    insta.save()
    return redirect('/home/')


# def questions(request):
#     u_id=request.user.id
#     u_name=uesr.username
#     # implement
#     user=User.objects.get(id=Answer.objects.filter(forquestion_id=q_id))
#     q_id=request.POST['id']
#     q_obj = Question.objects.get(id=q_id)
#     ans_obj=Answer.objects.filter(forquestion_id=q_id)
#     return render(request,'questions.html',{'q_obj':q_obj,'q_id':q_id,'ans_obj':ans_obj,'u_name':u_name,'u_id':u_id})

def questions(request):
    # implement
    # an=Answer.objects.filter(forquestion_id=q_id)
    # user_id=an.id
    # user=User.objects.get(id=user_id)
    # q_id=request.POST['id']
    # q_obj = Question.objects.get(id=q_id)
    # ans_obj=Answer.objects.filter(forquestion_id=q_id)


    user_name=[]
    answers=[]
    q_id=request.POST['id']
    q_obj = Question.objects.get(id=q_id)
    ans_obj=Answer.objects.filter(forquestion_id=q_id)
    for ans in ans_obj:
        answers.append(ans.answer)
        user_id=ans.author_id
        use=User.objects.get(id=user_id)
        user_name.append(use.username)
    zipp=zip(answers,user_name)
    return render(request,'questions.html',{'zipp':zipp,'q_obj':q_obj})


def postanswer(request):
    u_id=request.user.id
    q_id=request.POST.get('id')
    answer=request.POST.get('answer')
    insta = Answer(answer=answer)
    insta.author_id=u_id
    insta.forquestion_id=q_id
    insta.like=0
    insta.dislike=0
    insta.save()
    return redirect('/home/')
def answering(request):
    # q_id=request.POST.get('id')
    # q_obj=Question.objects.get(id=q_id)
    # return render(request,'questions.html',{'q_obj':q_obj,'q_id':q_id})
    user_name=[]
    answers=[]
    q_id=request.POST['id']
    q_obj = Question.objects.get(id=q_id)
    ans_obj=Answer.objects.filter(forquestion_id=q_id)
    for ans in ans_obj:
        answers.append(ans.answer)
        user_id=ans.author_id
        use=User.objects.get(id=user_id)
        user_name.append(use.username)
    zipp=zip(answers,user_name)
    return render(request,'questions.html',{'zipp':zipp,'q_obj':q_obj})