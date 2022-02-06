from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from . models import Centers, District


def allDistCen(request, c_slug=None):
    c_page = None
    districts = None
    if c_slug!=None:
        c_page = get_object_or_404(Centers, slug=c_slug)
        districts = District.objects.all().filter(center=c_page)
    else:
        districts = District.objects.all().filter()
    return render(request, "center.html", {'center': c_page, 'districts': districts})


def distDetail(request, c_slug, district_slug):
    try:
        district = District.objects.get(center__slug=c_slug, slug=district_slug)
    except Exception as e:
        raise e
    return render(request, "district.html", {'district': district})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/form')
        else:
            messages.info(request, "Invalid Entry")
            return redirect('/login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnf_password = request.POST['password']

        if password == cnf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print("successfully created account")
            return redirect('/')

        else:
            messages.info(request, "Password Not matching ")

        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        age = request.POST['age']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        if patient_name == form:
            if User.objects.filter(patient_name=patient_name).exists():
                messages.info(request, "user filled form already")
                return redirect('/form')
            else:
                user = User.objects.create_user(patient_name=patient_name, age=age, address=address, blood_group=blood_group)
                user.save()
            return render(request, "message.html")

    return render(request, "form.html")
