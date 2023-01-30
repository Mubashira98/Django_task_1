from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from home.forms import studentform, userregister, adminform, marksform
from home.models import Student, Marks


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_view_students')
            elif user is not None and user.is_student:
                login(request,user)
                return redirect('student_viewprofile')
    return render(request,'loginpage.html')

def admin_profile(request):
    return render(request,'admin_viewstudents.html')

def student_profile(request):
    return render(request,'student_dashboard.html')

def student_viewprofile(request):
    student = Student.objects.get(user=request.user)
    return render(request,'student_profile.html',{'student':student})

def student_updateprofile(request):
    student1 = Student.objects.get(user=request.user)
    form = studentform(instance=student1)
    if request.method == 'POST':
        form = studentform(request.POST,request.FILES, instance=student1)
        if form.is_valid():
            form.save()
        return redirect('student_viewprofile')
    return render(request, 'student_update_profile.html', {'form': form})

def delete_profile_student(request):
    user = request.user
    if request.method == "POST":
        user.delete()
        messages.info(request, 'Your account deleted successfully')
        return redirect('index')
    return render(request,'delete_account.html')



def student_registration(request):
    u_form = userregister()
    s_form = studentform()
    if request.method == "POST":
        u_form = userregister(request.POST)
        s_form = studentform(request.POST, request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, "student registration completed")

            return redirect('login_user')
    return render(request, 'register_student.html', {'u_form': u_form, 's_form': s_form})


def admin_registration(request):
    u_form = userregister()
    a_form = adminform()
    if request.method == "POST":
        u_form = userregister(request.POST)
        a_form = adminform(request.POST,request.FILES)
        if u_form.is_valid() and a_form.is_valid():
            user = u_form.save(commit=False)
            user.is_staff = True
            user.save()
            admin = a_form.save(commit=False)
            admin.user = user
            admin.save()
            messages.info(request, "admin registered successfully")

            return redirect('login_user')
    return render(request, 'register_admin.html',{'u_form':u_form,'a_form':a_form})

def admin_view_students(request):
    data = Student.objects.all()
    return render(request,'admin_viewstudents.html',{'data':data})

def admin_add_marks(request):
    form = marksform()
    if request.method == "POST":
        form = marksform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_marks')
    return render(request,'add_marks.html',{'form':form})

def admin_view_marks(request):
    data = Marks.objects.all()
    return render(request,'view_marks.html',{'data':data})

def admin_edit_marks(request,id):
    mark1 = Marks.objects.get(id=id)
    form = marksform(instance=mark1)
    if request.method == 'POST':
        form = marksform(request.POST,instance=mark1)
    if form.is_valid():
        form.save()
        return redirect('admin_view_marks')
    return render(request,'admin_update_marks.html',{'form':form})

def student_view_marks(request):
    u = Student.objects.get(user=request.user)
    data = Marks.objects.filter(name=u)
    return render(request, 'student_view_marks.html', {'data': data})



def logout_view(request):
    logout(request)
    return redirect('index')