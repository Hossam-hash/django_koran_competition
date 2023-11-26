from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .models import UserProfile
import regex
import re
# Create your views here.
def signin(request):
    if request.method== 'POST' and 'btnsignin' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if "rememberme"  not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            #messages.success(request, 'تم تسجيل الدخول بنجاح')
        else:
            messages.error(request,'إسم مستخدم أو كلمة مرور غير صحيحة')
        return redirect('signin')
    else:
        return render(request,'accounts/signin.html')



def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')
def signup(request):
    if request.method== 'POST' and 'btnsignup' in request.POST:
        fname=None
        secname=None
        thirdname=None
        address=None
        email=None
        username=None
        password=None
        terms=None
        is_added=None
        if 'fname' in request.POST: fname=request.POST['fname']
        else:messages.error(request, 'خطأ فى الإسم الأول')
        if 'secname' in request.POST: secname=request.POST['secname']
        else:messages.error(request, 'خطأ فى إسم الاب')
        if 'thirdname' in request.POST: thirdname=request.POST['thirdname']
        else: messages.error(request, 'خطأ فى اللقب')
        if 'address' in request.POST: address=request.POST['address']
        else: messages.error(request, 'خطأ فى العنوان')
        if 'email' in request.POST: email=request.POST['email']
        else: messages.error(request, 'خطأ فى الايميل')
        if 'username' in request.POST: username=request.POST['username']
        else:messages.error(request, 'خطأ فى إسم المستخدم')
        if 'password' in request.POST: password=request.POST['password']
        else: messages.error(request, 'خطأ فى الرقم السرى')
        if 'terms' in request.POST: terms=request.POST['terms']

        if fname and secname and thirdname and address and email and username and password:
            if terms == 'on':
                if User.objects.filter(username=username).exists() == True:
                    messages.error(request, 'تم استخدام إسم المستخدم من قبل')
                else:
                    if User.objects.filter(email=email).exists() == True:
                        messages.error(request, 'تم إستخدام هذا الايميل من قبل')
                    else:
                        pattern = r'^[a-zA-Z0-9._%+-\u0600-\u06FF]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                        print('llllllll',email)
                        if re.match(pattern, email):
                            # add user
                            user = User.objects.create_user(first_name=fname, last_name=secname, email=email,username=username, password=password)
                            user.save()
                            # add profile
                            userprofile = UserProfile(user=user, third_name=thirdname,address=address)
                            userprofile.save()
                            #clear fields
                            fname=''
                            secname=''
                            thirdname=''
                            address=''
                            email=''
                            username=''
                            password=''
                            is_added=True

                            # success message
                            messages.success(request, 'تم إنشاء ملف المستخدم بنجاح')
                        else:
                            messages.error(request, 'ايميل خطا ')
            else:
                messages.error(request, 'يجب الموافقة على الشروط')
        else:
            messages.error(request,'تحقق من القيم المدخلة')

        return render(request,'accounts/signup.html',{'fname':fname,'secname':secname,'thirdname':thirdname,
                                                      'address':address,'email':email,'username':username,'password':password,'is_added':is_added})
    else:
        return render(request,'accounts/signup.html')
def profile(request):
    if request.method== 'POST' and 'btnprofsave' in request.POST:
        fname=request.POST['fname']
        secname=request.POST['secname']
        thirdname=request.POST['thirdname']
        address=request.POST['address']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        if fname and secname and thirdname and address and email and username and password:
            userprofile = UserProfile.objects.get(user=request.user)

            request.user.first_name=fname
            request.user.last_name=secname
            userprofile.third_name = thirdname
            userprofile.address = address
            #request.user.email=email
            #request.user.username=username
            #request.user.password=password
            if not request.POST['password'].startswith('pbkdf2_sha256$6'):
                request.user.set_password(request.POST['password'])
            request.user.save()
            userprofile.save()
            auth.login(request,request.user)

        else:
            messages.error(request,'تحقق من المدخلات')
        redirect(request,'profile')
    else:
        #render the basic informations
        context = None
        if not request.user.is_anonymous:
            if request.user is not None:
                userprofile=UserProfile.objects.get(user=request.user)
                context={
                    'fname': request.user.first_name,
                    'secname': request.user.last_name,
                    'email': request.user.email,
                    'username': request.user.username,
                    'password': request.user.password,
                    'thirdname':userprofile.third_name,
                    'address':userprofile.address,
                }
                return render(request,'accounts/profile.html',context)
        else:
            return redirect('profile')