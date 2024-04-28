from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import PostBlogForm,RegistrationForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth.decorators import login_required





# Create your views here.
def blog_list(request):
   all_data = BlogPost.objects.all().order_by('-Publish_Date')
   return render(request,"blog_app/post-list.html",{'post_info':all_data})

   # return HttpResponse(all_data)
@login_required(login_url='login')
def post_detail(request,pk):
   post_data=get_object_or_404(BlogPost,pk=pk)
   return render(request,'blog_app/post_detail.html',{'post':post_data})
def post_new(request):
   if request.method=='POST':
      form_data=PostBlogForm(request.POST)
      if form_data.is_valid():
         post_data=form_data.save(commit=False)
         post_data.Author=request.user
         post_data.Create_Date=timezone.now()
         post_data.save()
         messages.success(request,"YOUR DATA INSERTED SUCCESSFULLY")
         return redirect('blog_list')
   else:
      messages.error(request,'YOUR DATA IS NOT INSERTED SUCCESSFULLY')
      form_data=PostBlogForm()
   return render(request,'blog_app/post_new_edit.html',{'form_data':form_data})

def post_edit(request,pk):
   post_data = get_object_or_404(BlogPost,pk=pk)
   if request.method=='POST':
      form_data=PostBlogForm(request.POST,instance=post_data)
      if form_data.is_valid():
         post_data=form_data.save(commit=False)
         post_data.Author=request.user
         post_data.Create_Date=timezone.now()
         post_data.delete()
         messages.success(request,'data updated successfully')
         return redirect('blog_list')
   else:
      form_data=PostBlogForm(instance=post_data)
   return render(request,'blog_app/post_new_edit.html',{'form_data':form_data})


def post_delete(request,pk):
   post = get_object_or_404(BlogPost,pk=pk)
   post.delete()
   messages.info(request,'Data deleted successfully')
   return redirect('blog_list')


def register(request):
   if request.method == "GET":
      form = RegistrationForm()
      context = {'form': form}
      return render(request, 'register.html', context)
   if request.method == "POST":
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request, 'Account was created for ' + user)
         return redirect('blog_list')
      else:
         print('Form is not valid')
         messages.error(request, 'Error Processing Your Request')
         context = {'form': form}
         return render(request, 'register.html', context)
   form = RegistrationForm()
   return render(request, 'register.html', {'form': form})









