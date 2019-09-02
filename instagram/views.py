from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Image,Profile,Like,Followers,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,PostImage,CommentForm,UpdateImage
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all().order_by('-post_date')
    users = User.objects.all()  
    current = request.user
    likes = Like.objects.all().count()
    
    return render(request, 'index.html',{"images":images,'users':users,'current':current,"likes":likes})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    if current_user.id == user.id:
        images = Image.objects.filter(owner_id=id)
        current_user = request.user
        user = User.objects.get(id=id)
        try:
            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:
            return redirect(update_profile,current_user.id)
    else: 
        try:
            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:
            
            return redirect(no_profile,id)      
            
    return render(request,'profile/profile.html',{'user':user,'profile':profile,'images':images,'current_user':current_user})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=id
            profile.save()
            return redirect(home)
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':user,'form':form})

def no_profile(request,id):
    
    user = User.objects.get(id=id)
    return render(request,'profile/no_profile.html',{"user":user})

def search_results(request):
    profile = Profile.objects.all
    
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        
        searched_users = User.objects.filter(username__icontains=search_term)
        
        message = f"{search_term}"
        
        return render(request, 'searched.html',{"message":message,"users": searched_users,"profile":profile})

    else:
        message = "Please input a name in the search form"
        return render(request, 'searched.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_image(request,id):
    current_user = request.user
    try:
        current_profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile,current_user.id)
        
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.profile = current_profile
            image.save()
        return redirect(home)
    else:
        form = PostImage()
        
    return render(request, 'new_image.html', {'user':current_user,"form": form})

@login_required(login_url='/accounts/login/')   
def comment(request,c_id):
    comments = Comment.objects.filter(image_id=c_id)
    current_user = request.user
    current_image = Image.objects.get(id=c_id)
    try:
        likes = Like.objects.filter(post_id=c_id).count()
    except ObjectDoesNotExist:
        likes =0
    try:
        like = Like.objects.filter(post_id=c_id).get(user_id=request.user)
    except ObjectDoesNotExist:
        like =0
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = current_image
            comment.user = current_user   
            comment.save()
            return redirect(home)
    else:
        form = CommentForm()
        
    return render(request,'comments.html',{"form":form,'comments':comments,"image":current_image,"user":current_user,'like':like,"likes":likes})   

def like_pic(request, pic_id):
    current_user = request.user
    
    image = Image.objects.get(id=pic_id)
    new_like = Like(post=image,user=current_user)
    new_like.save()
    return redirect(comment,image.id)

def follow(request,user_id):
    current_user = request.user
    to_follow = Profile.objects.get(user_id=user_id)
    new_profile = Profile(user_id=to_follow,followers=current_user.id,following=to_follow)
    new_profile.save()
    return redirect(home)  

@login_required(login_url='/accounts/login/')
def update_image(request,id):
    current_user = request.user
    image = Image.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateImage(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.update_image(current,new)
            return redirect(home)
    else:
        form = UpdateImage()

    return render(request,'update_image.html',{'user':current_user,'form':form,"image":image})



