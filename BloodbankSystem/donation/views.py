from django.shortcuts import render
from django.http import HttpResponse
from .models import donor
from .models import BloodStock
from .models import HospitalRequest
from django.core.mail import send_mail
from django.db.models import Case, When
# from geopy.geocoders import Nominatim
# from geopy import distance 


# geolocator = Nominatim(user_agent="DistanceCalculator")


# def get_lat_long(city):
#     country = "Egypt"
#     loc = geolocator.geocode(city + ", " + country)

#     return [loc.latitude, loc.longitude]

# def calculateDistance(lat1, lon1, lat2, lon2):
#     coord1 = (lat1, lon1)
#     coord2 = (lat2, lon2)

#     return geopy.distance.geodesic(coord1, coord2).miles

# Create your views here.
# Define the order based on priority

# def Home(request):
#     return HttpResponse("Hello Donation App is ready!!")
def Home(request):
    
    return render(request,'index.html')

def Donor_info(request):
    if request.method=='POST':
        national_id=request.POST.get('national_id','unkown nationa')
        Name=request.POST.get('donor_name','unkown name')
        City=request.POST.get('city', 'unkown city')
        Email = request.POST.get('email', 'unkownemail@gmail.com')
        virus_test=request.POST.get('virus_test','negative')
        Time_achived=request.POST.get('Time_achived','yes')
        
        #save the donor info to the donor table in the database            
        Donor_info=donor.objects.create(
            National_ID=national_id,
            Name=Name,
            City=City,
            Email=Email
        )
         
        if Time_achived == 'no' and virus_test == 'positive':
            # Send rejection email for positive virus test
            send_mail(
                'Donation request status',
                f'Dear {Name},\n\nUnfortunately, your request has been rejected as it is mandatory to have a 3-month gap between each 2 donation processes and to pass the blood virus test.\n\nBest regards,\nBlood Bank',
                '',  # Sender's email
                [Email],  # Recipient's email
                fail_silently=False,
            )
            donation_status = 'rejected'
        elif Time_achived == 'no':
            # Send rejection email for not meeting time requirement
            send_mail(
                'Donation request status',
                f'Dear {Name},\n\nUnfortunately, your request has been rejected as it is mandatory to have a 3-month gap between each 2 donation processes.\n\nBest regards,\nBlood Bank',
                '',  # Sender's email
                [Email],  # Recipient's email
                fail_silently=False,
            )
            donation_status = 'rejected'
        elif virus_test == 'positive':
            # Send rejection email for positive virus test
            send_mail(
                'Donation request status',
                f'Dear {Name},\n\nUnfortunately, your request has been rejected as It is mandatory to pass the blood virus test.\n\nBest regards,\nBlood Bank',
                '',  # Sender's email
                [Email],  # Recipient's email
                fail_silently=False,
            )
            donation_status = 'rejected'
        else:
            # Donation is accepted
            print("It is accepted")
            donation_status = 'accepted' 
            
   
        return render(request, 'process_donation.html', {'donation_status': donation_status}) 
        
    return render(request,'donor.html') 

def process_donation(request):
    if request.method=='POST':
        blood_group = request.POST.get('Blood_group', 'Unknown Blood Group')
        blood_bank_city = request.POST.get('Bloodbankcity', 'Unknown City')
        blood_expiration_date = request.POST.get('Blood_expiration_date', None)

        blood_info = BloodStock.objects.create(
            Blood_group=blood_group,
            Bloodbankcity=blood_bank_city,
            Blood_expiration_date=blood_expiration_date,
        )

    


    return render(request, 'index.html')

def blood_request(request):
    
    #Save the request in the database in the hospital request table
    if request.method=='POST':
        hospital_name = request.POST.get('hospitalName', 'Unknown hospital')
        city = request.POST.get('city', 'Unknown city')
        blood_group = request.POST.get('bloodGroup', 'Unknown group')
        patient_status = request.POST.get('patientStatus', 'Unknown status')

        blood_info = HospitalRequest.objects.create(
            hospital_name=hospital_name,
            blood_group=blood_group,
            city=city,
            patient_status=patient_status
        )
        
        #count the number of requests
        request_count = HospitalRequest.objects.count()
        
        #take action only if the requests reach >=10
        if request_count >= 3:

            #sort the requests based on the patient status
            # Define the order based on priority
            order_priority = Case(
                When(patient_status='Immediate', then=0),
                When(patient_status='Urgent', then=1),
                When(patient_status='Normal', then=2),
                default=3  # Set a default value for any other status
            )
            # Fetch all requests and order them based on priority
            all_requests = HospitalRequest.objects.all().order_by(order_priority)
            #fetch the table of Bloodstock
            all_blood_quantities = BloodStock.objects.all()

            for request_obj in all_requests:
                # Access attributes of each HospitalBloodRequest object
                Request_blood_group = request_obj.blood_group
                Request_city = request_obj.city
                matching_quantities = [] 

                if Request_blood_group == 'O':
                    # Filter blood quantities for blood group O
                    matching_quantities = all_blood_quantities.filter(Blood_group='O')
                elif Request_blood_group == 'A':
                # Filter blood quantities for blood group A or blood group O
                    matching_quantities = all_blood_quantities.filter(Blood_group__in=['O', 'A'])
                elif Request_blood_group == 'B':
                # Filter blood quantities for blood group B or blood group O
                    matching_quantities = all_blood_quantities.filter(Blood_group__in=['O', 'B'])
                else:
                    matching_quantities=all_blood_quantities
                    
                first_element = matching_quantities.first()    
                if first_element is not None:
                    id=first_element.pk
                    
                        
                print(matching_quantities)                           
                    
                

        
        return render(request, 'index.html')
    return render(request, 'blood_request.html')

def about(request):
    
    return render(request,'about.html')

def FAQ(request):
    
    return render(request,'FAQ.html')

