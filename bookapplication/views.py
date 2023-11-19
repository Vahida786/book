from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.views.generic import View 
# Create your views here.
from bookapplication.forms import BookModelForms,RegistrationForm,LoginForm
from bookapplication.models import Books
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


@method_decorator(signin_required,name="dispatch")
class BooksView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForms()
        return render(request, "book_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookModelForms(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"added successfully")

            # Employees.objects.create(**form.cleaned_data)
            print("created")
            return render(request, "book_add.html",{"form":form})
        else:
            messages.error(request,"error to add")

            return render(request, "book_add.html",{"form":form})

@method_decorator(signin_required,name="dispatch")
class BookListView(View):
    
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        authors=Books.objects.all().values_list("author",flat=True).distinct()
        print(authors)

        if "author" in request.GET:
            dept=request.GET.get("author")
            qs=qs.filter(author__iexact=dept)
        return render(request,"book_list.html",{"data":qs,"authors":authors})

    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Books.objects.filter(bname__icontains=name)
        return render(request,"book_list.html",{"data":qs})

@method_decorator(signin_required,name="dispatch")
class BookDetailVeiw(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})
    

@method_decorator(signin_required,name="dispatch")   
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        messages.success(request,"added successfully")
        return redirect("book-all")
    
@method_decorator(signin_required,name="dispatch")
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForms(instance=obj)

        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            obj=Books.objects.get(id=id)
            form=BookModelForms(request.POST,instance=obj,files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"added successfully")

                return redirect("book-detail",pk=id)
            else:
                messages.error(request,"updation")

                return render(request, "book_edit.html",{"form":form})

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print("saved")
            messages.success(request,"account has created")
            return render(request,"register.html",{"form":form})
        else:
            print("failed")
            messages.error(request,"account has failed to create")
            return render(request,"register.html",{"form":form})
    
 

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                print("valid credential")
                login(request,user_obj)
                return redirect("book-all")
            
        messages.error(request,"invalid credential")
        return render(request,"login.html",{"form":form})

@method_decorator(signin_required,name="dispatch")
class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")