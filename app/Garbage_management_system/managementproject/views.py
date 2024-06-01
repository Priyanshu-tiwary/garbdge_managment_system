from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Complaint
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        user = User(
            username=username,
            email=email,
            mobile_number=mobile_number,
            password=password,
       
      )
        print(user)
        user.save()

        return HttpResponse('success')  # Redirect to a success page
    else:
        return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_for_driver(request):
    return render(request, 'dashboardfordriver.html')

def complaint_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        complaint_text = request.POST.get('complaint')
        address = request.POST.get('address')
        location = request.POST.get('location')
        picture = request.FILES.get('picture')

        # Create a new Complaint object with the form data
        complaint = Complaint(
            name=name,
            email=email,
            mobile_number=mobile_number,
            complaint=complaint_text,
            address=address,
            location=location,
            picture=picture
        )

        # Save the Complaint object to the database
        complaint.save()

        # You can perform additional actions here, such as sending notifications or redirecting to a thank you page
        return HttpResponse('Complaint submitted successfully!')

    return render(request, 'complaintform.html')

def honor(request):
    return render(request, 'Honor.html')