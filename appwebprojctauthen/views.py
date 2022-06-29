from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from appwebprojctauthen.models import course,student 

#create views here //Authenitcation method//
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')    
def addcourse(request):
    return render(request,'addcourse.html')  
def addstudent(request):
    return render(request,'addstudent.html',{'courses':course})
def showstudent(request):
    return render(request,'showstudent.html',{'courses':course})    
    
#enter student details
def add_student_details(request):
    if request.method=='POST':
       sname=request.POST['student_name']
       print(sname)
       Addres=request.POST['Address']
       course= request.POST['sel']
       print(course)
       course1=course.object.get(id='sel')
       print(course1)
       student=student(student_name=sname,
                       address=Addres,
                                               )
       student.save()
        

       print("hii")
   # return redirect('show_student')     

def about(request):
    # if 'uid' in request.session:
    if request.user.is_authenticated:
        return render(request,'about.html')    
    return render(request,'login.html')
#......students  and course details add
def add_course(request):
    if request.method=='POST':
       cors=request.POST['course']
       cfee=request.POST['fee']
       print(cors)  
       crs=course(course_name=cors,course_fee=cfee)
        
       crs.course_name=cors
       crs.course_fee=cfee
       crs.save()
       print("course added")
       return render(request,'home.html')

#..values added to insert table..........
#......Msg Passing and Check Username and Password....
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('user_login')
    else:
        return render(request,'signup.html')
def show_student(request):
    std=student.objects.all()
    return render(request,'admin/show_stud.html',{'student':std})

#User login functionality view
def user_login(request):
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                # request.session["uid"] = user.id
                if user is not None:
                    login(request,user)
                    auth.login(request, user)
                    messages.info(request, f'Welcome {username}')
                    return redirect('about')
                else:
                    messages.info(request, 'Invalid username or password')
                    return redirect('loginpage')
            except:
                messages.info(request, 'Invalid username or password')
                return render(request, 'login.html')
        else:
            # messages.info(request, 'Invalid username or password')
            return render(request, 'login.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')


# logout function call
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')

