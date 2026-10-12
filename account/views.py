from .models import User, UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
import re
import requests


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_strong_password(pw):
    if len(pw) < 8:
        return False
    if not any(c.isdigit() for c in pw):
        return False
    if not any(c.islower() for c in pw):
        return False
    return True

# register
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        p_1 = request.POST.get("password1")
        p_2 = request.POST.get("password2")
        email = request.POST.get("email")
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        national_id = request.POST.get("national_id")
        birthday = request.POST.get("birthday")

        form = [
            name.strip() if name else "",
            last_name.strip() if last_name else "",
            p_1.strip() if p_1 else "",
            p_2.strip() if p_2 else "",
            email.strip() if email else "",
            username.strip() if username else "",
            phone.strip() if phone else "",
            national_id.strip() if national_id else "",
            birthday.strip() if birthday else ""
        ]

        if all(f == "" for f in form):
            return render(request, "register.html", {"error": "لطفاً ابتدا فرم را پر کنید."})

        if form[0] == "":
            return render(request, "register.html", {"error": "نام را وارد نکرده‌اید."})
        if form[1] == "":
            return render(request, "register.html", {"error": "نام خانوادگی را وارد نکرده‌اید."})
        if form[2] == "":
            return render(request, "register.html", {"error": "رمز عبور را وارد نکرده‌اید."})
        if form[3] == "":
            return render(request, "register.html", {"error": "تکرار رمز عبور را وارد نکرده‌اید."})
        if form[4] == "":
            return render(request, "register.html", {"error": "ایمیل را وارد نکرده‌اید."})
        if form[5] == "":
            return render(request, "register.html", {"error": "نام کاربری را وارد نکرده‌اید."})
        if form[6] == "":
            return render(request, "register.html", {"error": "شماره موبایل را وارد نکرده‌اید."})
        if form[7] == "":
            return render(request, "register.html", {"error": "کد ملی را وارد نکرده‌اید."})
        if form[8] == "":
            return render(request, "register.html", {"error": "تاریخ تولد را وارد نکرده‌اید."})

        if p_1 != p_2:
            return render(request, "register.html", {"error": "دو رمز عبور یکسان نیستند."})

        if not is_valid_email(email):
            return render(request, "register.html", {"error": "ایمیل معتبر نیست."})

        if not is_strong_password(p_1):
            return render(request, "register.html", {
                "error": "رمز عبور باید حداقل ۸ کاراکتر، یک عدد و یک حرف کوچک داشته باشد."
            })

        try:
            User.objects.get(email=email)
            return render(request, "register.html", {"error": "این ایمیل قبلاً ثبت شده است."})
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(phone=phone)
            return render(request, "register.html", {"error": "این شماره موبایل قبلاً ثبت شده است."})
        except User.DoesNotExist:
            pass

        new_user = User.objects.create_user(
            first_name=name,
            last_name=last_name,
            email=email,
            username=username,
            password=p_1,
            national_id=national_id,
            phone=phone,
            birthday=birthday
        )

        cus_group = Group.objects.get(name='customer')
        new_user.groups.add(cus_group)

        return redirect(login)

    else:
        return render(request, "register.html")

# login
def login_view(request):
    if request.method == 'POST':
        the_user = authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if the_user is not None:
            login(request, the_user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'ایمیل یا رمز عبور اشتباه است.'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, "login.html")

# get user profile
def _get_user_profile(user):
    profile = UserProfile.objects.filter(user=user).first()
    if profile is not None:
        return profile
    for attr in ('profile', 'userprofile', 'user_profile'):
        try:
            obj = getattr(user, attr)
            if obj is not None:
                return obj
        except Exception:
            continue
    return None

# profile
def profile_view(request):
    profile = _get_user_profile(request.user)
    has_address = bool(profile and str(profile.address or '').strip())
    has_image = bool(profile and profile.image and getattr(profile.image, 'name', None))
    profile_complete = has_address or has_image
    return render(request, 'profile.html', {
        'profile': profile,
        'profile_complete': profile_complete,
        'has_address': has_address,
        'has_image': has_image,
    })

# add profile 
def add_profile_view(request):
    profile = _get_user_profile(request.user)
    if profile is None:
        profile = UserProfile.objects.create(user=request.user)

    profile_exists = bool(
        str(profile.address or '').strip()
        or (profile.image and getattr(profile.image, 'name', None))
    )

    if request.method == 'POST':
        address = request.POST.get('address', '').strip()
        image = request.FILES.get('image')
        profile.address = address
        if image:
            profile.image = image
        profile.save()
        if profile_exists:
            messages.success(request, 'پروفایل با موفقیت به‌روزرسانی شد.')
        else:
            messages.success(request, 'اطلاعات پروفایل با موفقیت اضافه شد.')
        return redirect('profile')

    return render(request, 'add_user_profile.html', {
        'profile': profile,
        'profile_exists': profile_exists,
    })