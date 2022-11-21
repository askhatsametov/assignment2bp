from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Country, Diseasetype, Disease, Discover, Users, Doctor, Publicservant, Record, Specialize
from django.contrib import messages
from django.db import IntegrityError
from django.forms.models import model_to_dict
# Create your views here.
def home(request):
    return render(request, 'crud/home.html')

def country(request):
    country = Country.objects.all().order_by('cname')
    return render(request, 'crud/country.html', {"country": country})

def create_country(request):
    if request.method == 'POST':
        country = Country()
        cname = request.POST.get('cname')
        if Country.objects.filter(cname=cname).exists() == False:
            country.cname = cname
            country.population = request.POST.get('population')
            country.save()
        else:
            messages.error(request, 'This country already in database')
            return HttpResponseRedirect('/country/')

    return HttpResponseRedirect('/country/')

def upd_country(request, cname):
    try:
        country = Country.objects.get(cname=cname)

        if request.method == 'POST':
            #country.cname = request.POST.get('cname')
            country.population = request.POST.get('population')
            country.save()

            return HttpResponseRedirect('/country/')
        else:
            return render(request, 'crud/upd_country.html', {'country': country})

    except Country.DoesNotExist:
        return HttpResponseNotFound('No such country in the database')

def delete_country(request, cname):
    try:
        country = Country.objects.get(cname=cname)
        country.delete()
        return HttpResponseRedirect('/country/')
    except Country.DoesNotExist:
        return HttpResponseNotFound('No such country')

def dType(request):
    diseaseType = Diseasetype.objects.all().order_by('diseasetype_id')
    return render(request, 'crud/dType.html', {"diseaseType": diseaseType})

def create_dType(request):
    if request.method == 'POST':
        dType = Diseasetype()
        disid = request.POST.get('diseasetype_id')
        if Diseasetype.objects.filter(diseasetype_id=disid).exists() == False:
            dType.diseasetype_id = disid
            dType.description = request.POST.get('description')
            dType.save()
        else:
            messages.error(request, 'This disease type already in database')
            return HttpResponseRedirect('/diseaseType/')

    return HttpResponseRedirect('/diseaseType/')

def upd_dType(request, diseasetype_id):
    try:
        dType = Diseasetype.objects.get(diseasetype_id=diseasetype_id)

        if request.method == 'POST':
            dType.description = request.POST.get('description')
            dType.save()

            return HttpResponseRedirect('/diseaseType/')
        else:
            return render(request, 'crud/upd_dType.html', {'dType': dType})

    except Diseasetype.DoesNotExist:
        return HttpResponseNotFound('No such disease type in the database')

def delete_dType(request, diseasetype_id):
    try:
        dType = Diseasetype.objects.get(diseasetype_id=diseasetype_id)
        dType.delete()
        return HttpResponseRedirect('/diseaseType/')
    except Diseasetype.DoesNotExist:
        return HttpResponseNotFound('No such disease type')

def disease(request):
    dis = Disease.objects.all().order_by('disease_code')
    return render(request, 'crud/disease.html', {"dis": dis})

def create_disease(request):
    if request.method == 'POST':
        disease = Disease()
        disease_code = request.POST.get('disease_code')
        if Disease.objects.filter(disease_code=disease_code).exists() == False:
            disease.disease_code = disease_code
            disease.pathogen = request.POST.get('pathogen')
            disease.description = request.POST.get('description')
            dType = request.POST.get('diseasetype_id')
            if Diseasetype.objects.filter(diseasetype_id=dType).exists():
                disease.diseasetype = Diseasetype.objects.get(diseasetype_id=dType)
                disease.save()
            else:
                messages.error(request, 'No such disease type in database')
                return HttpResponseRedirect('/disease/')
        else:
            messages.error(request, 'This disease already in database')
            return HttpResponseRedirect('/disease/')

    return HttpResponseRedirect('/disease/')

def upd_disease(request, disease_code):
    try:
        disease = Disease.objects.get(disease_code=disease_code)

        if request.method == 'POST':
            #country.cname = request.POST.get('cname')
            disease.pathogen = request.POST.get('pathogen')
            disease.description = request.POST.get('description')
            dType = request.POST.get('diseasetype_id')
            if Diseasetype.objects.filter(diseasetype_id=dType).exists():
                disease.diseasetype = Diseasetype.objects.get(diseasetype_id=dType)
                disease.save()
            else:
                messages.error(request, 'No such disease type in database')
                return HttpResponseRedirect('/disease/')

            return HttpResponseRedirect('/disease/')
        else:
            return render(request, 'crud/upd_disease.html', {'disease': disease})

    except Disease.DoesNotExist:
        return HttpResponseNotFound('No such disease in the database')

def delete_disease(request, disease_code):
    try:
        disease = Disease.objects.get(disease_code=disease_code)
        disease.delete()
        return HttpResponseRedirect('/disease/')
    except Disease.DoesNotExist:
        return HttpResponseNotFound('No such disease')

def discover(request):
    discover = Discover.objects.all().order_by('cname')
    return render(request, 'crud/discover.html', {"discover": discover})

def create_discover(request):
    if request.method == 'POST':
        discover = Discover()
        cname = request.POST.get('cname')
        if Country.objects.filter(cname=cname).exists() == False:
            messages.error(request, 'No such country in database')
            return HttpResponseRedirect('/discover/')

        disease_code = request.POST.get('disease_code')
        if Disease.objects.filter(disease_code=disease_code).exists() == False:
            messages.error(request, 'No such disease in database')
            return HttpResponseRedirect('/discover/')

        if Discover.objects.filter(cname=cname, disease_code=disease_code).exists() == False:
            discover.cname = Country.objects.get(cname=cname)
            discover.disease_code = Disease.objects.get(disease_code=disease_code)
            discover.first_enc_date = request.POST.get('first_enc_date')
            discover.save()
        else:
            messages.error(request, 'This discovery already in database')
            return HttpResponseRedirect('/discover/')

    return HttpResponseRedirect('/discover/')

def upd_discover(request, cname, disease_code):
    try:
        discover = Discover.objects.get(cname=cname, disease_code=disease_code)

        if request.method == 'POST':
            # country.cname = request.POST.get('cname')
            discover.first_enc_date = request.POST.get('first_enc_date')
            discover.save()

            return HttpResponseRedirect('/discover/')
        else:
            return render(request, 'crud/upd_discover.html', {'discover': discover})

    except Discover.DoesNotExist:
        return HttpResponseNotFound('No such discovery in the database')

def delete_discover(request, cname, disease_code):
    try:
        discover = Discover.objects.get(cname=cname, disease_code=disease_code)
        discover.delete()
        return HttpResponseRedirect('/discover/')
    except Discover.DoesNotExist:
        return HttpResponseNotFound('No such discovery')

def users(request):
    users = Users.objects.all().order_by('surname')
    return render(request, 'crud/users.html', {"users": users})

def create_users(request):
    if request.method == 'POST':
        user = Users()
        email = request.POST.get('email')
        user.firstname = request.POST.get('firstname')
        user.surname = request.POST.get('surname')
        user.salary = request.POST.get('salary')
        user.phone = request.POST.get('phone')
        cname = request.POST.get('cname')

        if Country.objects.filter(cname=cname).exists() == False:
            messages.error(request, 'No such country in database')
            return HttpResponseRedirect('/users/')

        if Users.objects.filter(email=email).exists() == False:
            user.email = email
            user.cname = Country.objects.get(cname=cname)
            user.save()
        else:
            messages.error(request, 'User with this email already exists')
            return HttpResponseRedirect('/users/')

    return HttpResponseRedirect('/users/')

def upd_users(request, email):
    try:
        user = Users.objects.get(email=email)

        if request.method == 'POST':
            # country.cname = request.POST.get('cname')
            user.firstname = request.POST.get('firstname')
            user.surname = request.POST.get('surname')
            user.salary = request.POST.get('salary')
            user.phone = request.POST.get('phone')
            cname = request.POST.get('cname')
            if Country.objects.filter(cname=cname).exists():
                user.cname = Country.objects.get(cname=cname)
                user.save()
            else:
                messages.error(request, 'No such country in database')
                return HttpResponseRedirect('/users/')

            return HttpResponseRedirect('/users/')
        else:
            return render(request, 'crud/upd_users.html', {'user': user})

    except Users.DoesNotExist:
        return HttpResponseNotFound('No such user in the database')

def delete_users(request, email):
    try:
        user = Users.objects.get(email=email)
        user.delete()
        return HttpResponseRedirect('/users/')
    except Users.DoesNotExist:
        return HttpResponseNotFound('No such user')

def publicservant(request):
    pubS = Publicservant.objects.all().order_by('email')
    return render(request, 'crud/publicservant.html', {"pubS": pubS})

def create_publicservant(request):
    if request.method == 'POST':
        publicservant = Publicservant()
        email = request.POST.get('email')
        publicservant.department = request.POST.get('department')

        if Users.objects.filter(email=email).exists() == False:
            messages.error(request, 'No such user in database')
            return HttpResponseRedirect('/publicservant/')

        if Publicservant.objects.filter(email=email).exists() == False:
            publicservant.email = Users.objects.get(email=email)
            publicservant.save()
        else:
            messages.error(request, 'This public servant already in database')
            return HttpResponseRedirect('/public servant/')

    return HttpResponseRedirect('/publicservant/')

def upd_publicservant(request, email):
    try:
        publicservant = Publicservant.objects.get(email=email)

        if request.method == 'POST':
            # country.cname = request.POST.get('cname')
            publicservant.department = request.POST.get('department')
            publicservant.save()

            return HttpResponseRedirect('/publicservant/')
        else:
            return render(request, 'crud/upd_publicservant.html', {'publicservant': publicservant})

    except Publicservant.DoesNotExist:
        return HttpResponseNotFound('No such public servant in the database')

def delete_publicservant(request, email):
    try:
        publicservant = Publicservant.objects.get(email=email)
        publicservant.delete()
        return HttpResponseRedirect('/publicservant/')
    except Publicservant.DoesNotExist:
        return HttpResponseNotFound('No such public servant')

def doctor(request):
    doc = Doctor.objects.all().order_by('email')
    return render(request, 'crud/doctor.html', {"doc": doc})

def create_doctor(request):
    if request.method == 'POST':
        doctor = Doctor()
        email = request.POST.get('email')
        doctor.doctor_degree = request.POST.get('doctor_degree')

        if Users.objects.filter(email=email).exists() == False:
            messages.error(request, 'No such user in database')
            return HttpResponseRedirect('/doctor/')

        if Doctor.objects.filter(email=email).exists() == False:
            doctor.email = Users.objects.get(email=email)
            doctor.save()
        else:
            messages.error(request, 'This doctor already in database')
            return HttpResponseRedirect('/doctor/')

    return HttpResponseRedirect('/doctor/')

def upd_doctor(request, email):
    try:
        doctor = Doctor.objects.get(email=email)

        if request.method == 'POST':
            # country.cname = request.POST.get('cname')
            doctor.doctor_degree = request.POST.get('doctor_degree')
            doctor.save()

            return HttpResponseRedirect('/doctor/')
        else:
            return render(request, 'crud/upd_doctor.html', {'doctor': doctor})

    except Doctor.DoesNotExist:
        return HttpResponseNotFound('No such doctor in the database')

def delete_doctor(request, email):
    try:
        doctor = Doctor.objects.get(email=email)
        doctor.delete()
        return HttpResponseRedirect('/doctor/')
    except Doctor.DoesNotExist:
        return HttpResponseNotFound('No such doctor')

def specialize(request):
    specialize = Specialize.objects.all().order_by('email')
    return render(request, 'crud/specialize.html', {"specialize": specialize})

def create_specialize(request):
    if request.method == 'POST':
        specialize = Specialize()
        disid = request.POST.get('diseasetype_id')
        if Diseasetype.objects.filter(diseasetype_id=disid).exists() == False:
            messages.error(request, 'No such disease type in database')
            return HttpResponseRedirect('/specialize/')

        email = request.POST.get('email')
        if Doctor.objects.filter(email=email).exists() == False:
            messages.error(request, 'No such doctor in database')
            return HttpResponseRedirect('/specialize/')

        try:
            specialize.diseasetype = Diseasetype.objects.get(diseasetype_id=disid)
            specialize.email = Doctor.objects.get(email=email)
            specialize.save()
        except IntegrityError:
            messages.error(request, 'This specialization already in database')
            return HttpResponseRedirect('/specialize/')
    return HttpResponseRedirect('/specialize/')

def upd_specialize(request, id):
    try:
        specialize = Specialize.objects.get(id=id)
        email = specialize.email
        specialize.delete()
        specialize.email = email

        if request.method == 'POST':
            disid = request.POST.get('diseasetype')
            if Diseasetype.objects.filter(diseasetype_id=disid).exists():
                specialize.diseasetype = Diseasetype.objects.get(diseasetype=disid)
            else:
                messages.error(request, 'No such disease type in database')
                return HttpResponseRedirect('/specialize/')

            specialize.save()

            return HttpResponseRedirect('/specialize/')
        else:
            return render(request, 'crud/upd_specialize.html', {'specialize': specialize})

    except Specialize.DoesNotExist:
        return HttpResponseNotFound('No such specialization in the database')

def delete_specialize(request, id):
    try:
        specialize = Specialize.objects.get(id=id)
        specialize.delete()
        return HttpResponseRedirect('/specialize/')
    except Specialize.DoesNotExist:
        return HttpResponseNotFound('No such specialization')

def record(request):
    record = Record.objects.all().order_by('email')
    return render(request, 'crud/record.html', {"record": record})

def create_record(request):
    if request.method == 'POST':
        record = Record()
        email = request.POST.get('email')
        if Publicservant.objects.filter(email=email).exists() == False:
            messages.error(request, 'No such public servant in database')
            return HttpResponseRedirect('/record/')

        cname = request.POST.get('cname')
        if Country.objects.filter(cname=cname).exists() == False:
            messages.error(request, 'No such country in database')
            return HttpResponseRedirect('/record/')

        disease_code = request.POST.get('disease_code')
        if Disease.objects.filter(disease_code=disease_code).exists() == False:
            messages.error(request, 'No such disease in database')
            return HttpResponseRedirect('/record/')

        try:
            record.email = Publicservant.objects.get(email=email)
            record.cname = Country.objects.get(cname=cname)
            record.disease_code = Disease.objects.get(disease_code=disease_code)
            record.total_deaths = request.POST.get('total_deaths')
            record.total_patients = request.POST.get('total_patients')
            record.save()
        except IntegrityError:
            messages.error(request, 'This record already in database')
            return HttpResponseRedirect('/record/')

    return HttpResponseRedirect('/record/')

def upd_record(request, id):
    try:
        record = Record.objects.get(id=id)
        if request.method == 'POST':
            record.total_deaths = request.POST.get('total_deaths')
            record.total_patients = request.POST.get('total_patients')
            record.save()

            return HttpResponseRedirect('/record/')
        else:
            return render(request, 'crud/upd_record.html', {'record': record})

    except Record.DoesNotExist:
        return HttpResponseNotFound('No such record in the database')

def delete_record(request, id):
    try:
        record = Record.objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/record/')
    except Record.DoesNotExist:
        return HttpResponseNotFound('No such record')
