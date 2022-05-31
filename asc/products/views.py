
from django.shortcuts import render, redirect

from .models import Product, Order, Deliver, complete
from math import ceil

6

from .decorators import unauthenticated_user

from datetime import datetime, timedelta
import  pytz
from django.contrib.auth.decorators import login_required

def home(request):
    allProds = []
    catprods = Product.objects.values('type', 'id')
    cats = {item['type'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(type=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        hv = n
    params = {'allProds': allProds,'hv':hv}
    return render(request, 'home.html', params)

def productview(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    pv = Product.objects.filter(id=myid)

    return render(request, 'productview.html', {'product': product[0],'pv':pv})

def order(request):
    if request.method == "POST":
        pname = request.POST.get('pname', '')
        fullname = request.POST.get('fullname', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        cnic = request.POST.get('cnic', '')
        city = request.POST.get('city', '')
        qty = request.POST.get('qty', '')
        amount = request.POST.get('amount', '')

        # ////////////Converting Qty int Total Amount ///////////
        qty = int(qty)
        amount = int(amount)
        tot = qty * amount
        order = Order(pname=pname, fullname=fullname, address=address, phone=phone,
                      cnic=cnic, city=city, qty=qty,amount=tot)
        order.save()
        s = pname
        id = order.order_id
    return render(request, "productview.html", {'s': s,'id':id})

def status(request):
    status = 'y'
    return render(request, 'status.html',{'status':status})

def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', '')
        cnic = request.POST.get('cnic', '')
        no = 'cnic'
        ye = 'cnic'
        status = 'y'
        order = Order.objects.filter(order_id=order_id, cnic=cnic)
        if len(order) > 0:
            order_count = Order.objects.filter(cnic=cnic)
            count = order_count.count()
            products = Order.objects.filter(cnic=cnic)
            order = Order.objects.filter(order_id=order_id, cnic=cnic)
            return render(request, "status.html",{'count':count,'products':products,'order':order,'ye':ye})
        else:
            return render(request, "status.html", {'no': no,'status':status})

def deletOrder(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', '')
        print(order_id)
        dele = order_id
        dels = Order.objects.get(order_id=order_id)
        dels.delete()
    return render(request, 'status.html',{'dele':dele})

def forgottrackingid(request):
    return render(request, 'forgottrackingid.html')

def checkingcnicids(request):
    if request.method == "POST":
        cnic = request.POST.get('cnic', '')
        order = Order.objects.filter(cnic=cnic)
        nots = []
        if len(order) > 0:
            return render(request, "forgotid_secondpage.html", { 'order': order,'nots':nots})
        else:
            return render(request, "forgotid_secondpage.html", {'cnic':cnic})
    else:
        return render(request, "forgotid_secondpage.html")

def delivers(request):
    if request.method == "POST":
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')
        deilver = Deliver.objects.filter(user=user, password=password)
        if len(deilver) > 0:

            if user == 'Admin':
                lable = []
                data = []
                pan = complete.objects.order_by('-order_id')[:5]
                for i in pan:
                    lable.append(i.order_id)
                    data.append(i.received_money)


                return render(request, 'admin.html',{'lable':lable,'data':data})
            else:

                fa = Deliver.objects.get(user=user)
                faa = request.session['city'] = fa.city

                cn = request.session['city'] = fa.cnic

                # datetime object containing current date and time
                now = datetime.today()
                threedays = datetime.today() - timedelta(days=2)

                # changing Type of datetime
                threedays = pytz.utc.localize(now)
                now = pytz.utc.localize(now)

                # Counting Orders
                dcity = Order.objects.filter(city=faa).count()
                pan = Order.objects.filter(city=faa, STATUS='Pending').count()
                comp = complete.objects.filter(branch_name=cn).count()

                # Calculating Total Amount Received
                total_amount = complete.objects.filter(branch_name=cn)
                am =0
                am = int(am)
                for i in total_amount:
                    am = am + i.received_money

                # Getting Customer Details
                cus = Order.objects.filter(city=faa, STATUS='Pending')

                #Getting Information of Dilver
                de = Deliver.objects.filter(user=user)
                noti = 0
                count_pend = 0
                noti = int(noti)
                for i in cus:
                    if threedays >= i.order_time:
                        noti = noti + 1

                # Sending data to the template
                return render(request, 'deshboard.html',
                              {'dcity': dcity, 'pan': pan, 'comp': comp, 'cus': cus, 'user':user,
                               'now':now,'threedays':threedays,'am':am,'de':de,'noti':noti})
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'login.html')

@unauthenticated_user
def deshboard(request):
    return render(request, 'deshboard.html')

def home(request):
    allProds = []
    catprods = Product.objects.values('type', 'id')
    cats = {item['type'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(type=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        hv = n
    params = {'allProds': allProds,'hv':hv}
    return render(request, 'home.html', params)


def productview(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    pv = Product.objects.filter(id=myid)

    return render(request, 'productview.html', {'product': product[0],'pv':pv})

def order(request):
    if request.method == "POST":
        pname = request.POST.get('pname', '')
        fullname = request.POST.get('fullname', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        cnic = request.POST.get('cnic', '')
        city = request.POST.get('city', '')
        qty = request.POST.get('qty', '')
        amount = request.POST.get('amount', '')

        # ////////////Converting Qty int Total Amount ///////////
        qty = int(qty)
        amount = int(amount)
        tot = qty * amount
        order = Order(pname=pname, fullname=fullname, address=address, phone=phone,
                      cnic=cnic, city=city, qty=qty,amount=tot)
        order.save()
        s = pname
        id = order.order_id
    return render(request, "productview.html", {'s': s,'id':id})


def status(request):
    status = 'y'
    return render(request, 'status.html',{'status':status})

def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', '')
        cnic = request.POST.get('cnic', '')
        no = 'cnic'
        ye = 'cnic'
        status = 'y'
        order = Order.objects.filter(order_id=order_id, cnic=cnic)
        if len(order) > 0:
            order_count = Order.objects.filter(cnic=cnic)
            count = order_count.count()
            products = Order.objects.filter(cnic=cnic)
            order = Order.objects.filter(order_id=order_id, cnic=cnic)
            return render(request, "status.html",{'count':count,'products':products,'order':order,'ye':ye})
        else:
            return render(request, "status.html", {'no': no,'status':status})


def deletOrder(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', '')
        print(order_id)
        dele = order_id
        dels = Order.objects.get(order_id=order_id)
        dels.delete()
    return render(request, 'status.html',{'dele':dele})

def forgottrackingid(request):
    return render(request, 'forgottrackingid.html')

def checkingcnicids(request):
    if request.method == "POST":
        cnic = request.POST.get('cnic', '')
        order = Order.objects.filter(cnic=cnic)
        nots = []
        if len(order) > 0:
            return render(request, "forgotid_secondpage.html", { 'order': order,'nots':nots})
        else:
            return render(request, "forgotid_secondpage.html", {'cnic':cnic})
    else:
        return render(request, "forgotid_secondpage.html")

def delivers(request):
    if request.method == "POST":
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')
        deilver = Deliver.objects.filter(user=user, password=password)
        if len(deilver) > 0:
            if user == 'Admin':
                pan = Order.objects.filter(STATUS='Pending').count()
                cm = Order.objects.filter(STATUS='Recived').count()
                total_amount = complete.objects.all()

                total_rider = Deliver.objects.all().count()
                total_riderk = Deliver.objects.filter(city='Karachi').count()
                total_riderl = Deliver.objects.filter(city='Lahore').count()
                total_riderc = Deliver.objects.filter(city='Chakwal').count()

                am = 0
                am = int(am)
                for i in total_amount:
                    am = am + i.received_money

                return render(request, 'admin.html',{'pan':pan,'cm':cm,'total_amount':total_amount,
                                                     'total_rider':total_rider,'total_riderk':total_riderk,
                                                     'total_riderl':total_riderl,'total_riderc':total_riderc,
                                                     'am':am
                                                     })
            else:
                fa = Deliver.objects.get(user=user)
                faa = request.session['city'] = fa.city

                cn = request.session['cnic'] = fa.cnic

                # datetime object containing current date and time
                now = datetime.today()
                threedays = datetime.today() - timedelta(days=2)

                # changing Type of datetime
                threedays = pytz.utc.localize(now)
                now = pytz.utc.localize(now)

                # Counting Orders
                dcity = Order.objects.filter(city=faa).count()
                pan = Order.objects.filter(city=faa, STATUS='Pending').count()
                comp = complete.objects.filter(deliver_cnic=cn).count()

                # Calculating Total Amount Received
                total_amount = complete.objects.filter(deliver_cnic=cn)
                am =0
                am = int(am)
                for i in total_amount:
                    am = am + i.received_money

                # Getting Customer Details
                cus = Order.objects.filter(city=faa, STATUS='Pending')

                #Getting Information of Dilver
                de = Deliver.objects.filter(user=user)
                noti = 0
                count_pend = 0
                noti = int(noti)
                for i in cus:
                    if threedays >= i.order_time:
                        noti = noti + 1
                print(noti)

                # Sending data to the template
                return render(request, 'deshboard.html',
                              {'dcity': dcity, 'pan': pan, 'comp': comp, 'cus': cus, 'user':user,
                               'now':now,'threedays':threedays,'am':am,'de':de,'noti':noti})
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'login.html')

@unauthenticated_user
def deshboard(request):
    return render(request, 'deshboard.html')

def updtecash(request, order_id):
    sa = Order.objects.get(order_id=order_id)
    saa = sa.amount
    city = sa.city
    sa.STATUS = 'Recived'
    sa.save()

    de_cn = request.session.get('cnic')
    ins = complete(
        deliver_cnic=de_cn,
        order_id=order_id,
        received_money=saa,
        city=city,
    )
    ins.save()
    return render(request, 'deshboard.html',{'city':city,'order_id':order_id,'saa':saa})

def logout(request):
    return redirect('/index')

def search(request):
    if request.method == "POST":
        sname = request.POST.get('sname', '')
        print(sname)
        v = Product.objects.filter(product_name=sname)
        se = sname
        if len(v)>0:
            product = Product.objects.filter(product_name=sname)
            return render(request, 'home.html', {'product': product[0],'se':se,})
        else:
            nots = sname
            return render(request, 'home.html', {'nots':nots})
    else:
        return render(request, 'home.html')

def logout(request):
    return redirect('/index')

def search(request):
    if request.method == "POST":
        sname = request.POST.get('sname', '')
        print(sname)
        v = Product.objects.filter(product_name=sname)
        se = sname
        if len(v)>0:
            product = Product.objects.filter(product_name=sname)
            return render(request, 'home.html', {'product': product[0],'se':se,})
        else:
            nots = sname
            return render(request, 'home.html', {'nots':nots})
    else:
        return render(request, 'home.html')


