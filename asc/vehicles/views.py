from django.shortcuts import render
from .models import vehicle,tool,drone,Booking,branche,complaint
from math import ceil
# Create your views here.

def homev(request):
    return render(request,'homev.html')

def vehicles(request):
    allProds = []
    catprods = vehicle.objects.values('TYPE', 'id')
    cats = {item['TYPE'] for item in catprods}
    for cat in cats:
        prod = vehicle.objects.filter(TYPE=cat)
        n = len(prod)
        n= int(n)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds,'n':n}

    return render(request, 'vehicles.html', params,)

def tools(request):
    allProds = []
    catprods = tool.objects.values('TYPE', 'id')
    cats = {item['TYPE'] for item in catprods}
    for cat in cats:
        prod = tool.objects.filter(TYPE=cat)
        n = len(prod)
        v =len(prod)
        n= int(n)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds,'v':v}

    return render(request, 'vehicles.html', params,)

def drones(request):
    allProds = []
    catprods = drone.objects.values('TYPE', 'id')
    cats = {item['TYPE'] for item in catprods}
    for cat in cats:
        prod = drone.objects.filter(TYPE=cat)
        n = len(prod)
        d =len(prod)
        n= int(n)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds,'d':d}

    return render(request, 'vehicles.html', params)

def productviewV(request, myid):
    # Fetch the product using the id
    product = vehicle.objects.filter(id=myid)
    v = vehicle.objects.filter(id=myid)

    return render(request, 'prodectviewVe.html', {'product': product[0],'v':v})

def productviewT(request, myid):
    # Fetch the product using the id
    product = tool.objects.filter(id=myid)
    t = tool.objects.filter(id=myid)
    return render(request, 'prodectviewVe.html', {'product': product[0],'t':t})

def productviewD(request, myid):
    # Fetch the product using the id
    product = drone.objects.filter(id=myid)
    d = drone.objects.filter(id=myid)
    return render(request, 'prodectviewVe.html', {'product': product[0],'d':d})



def bookingV(request, myid):
    # Fetch the product using the id
    product = vehicle.objects.filter(id=myid)
    f = vehicle.objects.filter(id=myid)
    v = vehicle.objects.filter(id=myid)
    return render(request, 'bookingPage.html', {'product': product[0],'f':f,'v':v})

def bookingT(request, myid):
    # Fetch the product using the id
    product = tool.objects.filter(id=myid)
    f = tool.objects.filter(id=myid)
    t = tool.objects.filter(id=myid)
    return render(request, 'bookingPage.html', {'product': product[0],'f':f,'t':t})

def bookingD(request, myid):
    # Fetch the product using the id
    product = drone.objects.filter(id=myid)
    f = drone.objects.filter(id=myid)
    d = drone.objects.filter(id=myid)
    return render(request, 'bookingPage.html', {'product': product[0],'f':f,'d':d})

def bookingOrder(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        vname = request.POST.get('vname', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        cnic = request.POST.get('cnic', '')
        amount = request.POST.get('amount', '')
        branch = request.POST.get('branch', '')
        bookings = Booking(name=name,vname=vname,address=address, phone=phone,
                  cnic=cnic,amount=amount,branch=branch, )
        s = 'new'
        bookings.save()
        id = bookings.booking_id
        print(id)
        return render(request, 'bookingPage.html', {'s':s,'id':id})
    else:
        return render(request, 'homev.html')

def search(request):
    if request.method == "POST":
        sname = request.POST.get('sname', '')
        sv = vehicle.objects.filter(vehicle_name=sname)
        st = tool.objects.filter(tool_name=sname)
        sd = drone.objects.filter(drone_name=sname)

        if len(sv)>0:
            product = vehicle.objects.filter(vehicle_name=sname)
            return render(request, 'vehicles.html', {'product': product[0],'sv':sv,})
        elif len(st)>0:
            product = tool.objects.filter(tool_name=sname)
            return render(request, 'vehicles.html', {'product': product[0],'st':st,})
        elif len(sd)>0:
            product = drone.objects.filter(drone_name=sname)
            return render(request, 'vehicles.html', {'product': product[0],'sd':sd,})
        else:
            nots = sname
            return render(request, 'vehicles.html', {'nots':nots})
    else:
        return render(request, 'homev.html')

def branches(request):
    brnmain = 'g'
    return render(request, 'OurBranches.html',{'brnmain':brnmain})

def branchesK(request):
    b = 'Karachi'
    branch = branche.objects.filter(branch_name=b)
    return render(request, 'OurBranches.html',{'branch': branch[0],'b':b})
def branchesR(request):
    b = 'Rawalpindi'
    branch = branche.objects.filter(branch_name=b)
    return render(request, 'OurBranches.html', {'branch': branch[0], 'b': b})
def branchesL(request):
    b = 'Lahore'
    branch = branche.objects.filter(branch_name=b)
    return render(request, 'OurBranches.html', {'branch': branch[0], 'b': b})
def branchesC(request):
    b = 'Chakwal'
    branch = branche.objects.filter(branch_name=b)
    return render(request, 'OurBranches.html', {'branch': branch[0], 'b': b})


def complaints(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        comtype = request.POST.get('comtype', '')
        details = request.POST.get('details', '')

        conpl = complaint(name=name,phone=phone, complaint_type=comtype, complaint_details=details, )
        conpl.save()
        c = name
    return render(request, 'bookingPage.html',{'c':c})

def bookingStatus(request):
    status = 'y'
    return render(request, 'bookingStatus.html',{'status':status})

def checkingbookingStatus(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id', '')
        cnic = request.POST.get('cnic', '')
        no = 'cnic'
        ye = 'cnic'
        status = 'y'
        order = Booking.objects.filter(booking_id=booking_id, cnic=cnic)
        if len(order) > 0:
            order_count = Booking.objects.filter(cnic=cnic)
            count = order_count.count()
            products = Booking.objects.filter(cnic=cnic)
            order = Booking.objects.filter(booking_id=booking_id, cnic=cnic)
            return render(request, "bookingStatus.html",{'count':count,'products':products,'order':order,'ye':ye})
        else:
            return render(request, "bookingStatus.html", {'no': no,'status':status})

def cancelbooking(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id', '')
        dele = booking_id
        dels = Booking.objects.get(booking_id=booking_id)
        dels.delete()
    return render(request, 'bookingStatus.html',{'dele':dele})
