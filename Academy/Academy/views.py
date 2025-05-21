from django.http import HttpResponse,HttpRequest
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from Admission_Form.models import Admission




#home page
def index(requst):
    return render(requst,'index.html')

# admission
def admission(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        father_name = request.POST.get('fatherName')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        whatsapp = request.POST.get('whatsapp')
        cnic = request.POST.get('cnic')
        domicile = request.POST.get('domicile')
        student_class = request.POST.get('class')
        fees = request.POST.get('fees')
        photo = request.FILES.get('photo')  # Handling file upload

        Admission.objects.create(
            full_name=full_name,
            father_name=father_name,
            dob=dob,
            gender=gender,
            email=email,
            phone=phone,
            whatsapp=whatsapp,
            cnic=cnic,
            domicile=domicile,
            student_class=student_class,
            photo=photo,
            fees = fees,
        )    
    return render(request, 'Admission_page.html')

# # fees page
def search(request):
    return render(request, 'search.html')

def search_admission(request):
    cnic = request.GET.get('cnic')
    student = get_object_or_404(Admission, cnic=cnic)
    return render(request, 'search_result.html', {'student': student})




# contact
def contact(request):
    return render(request, 'Contact_page.html')

# login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,'Login Successful!')
            return redirect('/')
        else:
            messages.error(request,'Invalid email or Password!')

    return render(request, 'login.html')

#signup
def signup_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email2')
        password = request.POST.get('password2')
        if User.objects.filter(username = email).exists():
            messages.error(request, 'Email already registered!')
        
        else:
            user = User.objects.create_user(
                username= email,
                email=email,
                first_name = fname,
                last_name = lname,
                password= password
            )
            user.save()
            messages.success(request, "Signup successful! Please login!")
            return redirect('login')


    return render(request, 'signup.html')