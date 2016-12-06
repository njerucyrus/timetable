from django.shortcuts import render, get_object_or_404
from django.http.response import (
    HttpResponse,
    HttpResponseRedirect,
)
from availability.forms import(
    AvailabilityForm,
    UserRegistrationForm,
    LecturerForm,
    MessageBroadCastForm,
    LoginForm,
)
from django.contrib.auth.models import User
from random import randint
from availability.models import LecturerAvailability, Lecturer
from availability.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):
    user = request.user
    next_url = request.GET.get('next', '')
    if user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next_url == '':
                        return HttpResponseRedirect('/')
                    elif next_url:
                        return HttpResponseRedirect(next_url)
            else:

                message = 'Wrong username or password'
                form = LoginForm()
                return render(request, 'login.html', {'form': form, 'message': message, })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, })


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return render(request, 'logout_then_login.html', {})


def register_lecturer(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        lecturer_form = LecturerForm(request.POST)
        if user_form.is_valid() and lecturer_form.is_valid():
            user = user_form.save()
            cd = lecturer_form.cleaned_data
            phone_number = cd['phone_number']
            range_start = 10 ** (6 - 1)
            range_end = (10 ** 6) - 1
            code = randint(range_start, range_end)
            lecturer_code = str(code)
            lecturer = Lecturer.objects.create(
                user=user,
                phone_number=phone_number,
                lecturer_code=lecturer_code
            )
            lecturer.save()
            message = "Lecturer saved successfully"
            return render(request, 'registration_success.html', {'message': message})
    else:
        lecturer_form = LecturerForm()
        user_form = UserRegistrationForm()

    return render(request, 'registration.html', {'user_form': user_form, 'lecturer_form': lecturer_form, })


def set_availability(request):
    if request.method == 'POST':
        day_monday = request.POST.get('monday', '')
        monday_from = request.POST.get('monday_from', '')
        monday_to = request.POST.get('monday_to', '')

        day_tuesday = request.POST.get('tuesday', '')
        tuesday_from = request.POST.get('tuesday_from', '')
        tuesday_to = request.POST.get('tuesday_to', '')

        day_wednesday = request.POST.get('wednesday', '')
        wednesday_from = request.POST.get('wednesday_from', '')
        wednesday_to = request.POST.get('wednesday_to', '')

        day_thursday = request.POST.get('thursday', '')
        thursday_from = request.POST.get('thursday_from', '')
        thursday_to = request.POST.get('thursday_to', '')

        day_friday = request.POST.get('friday', '')
        friday_from = request.POST.get('friday_from', '')
        friday_to = request.POST.get('friday_to', '')

        user = get_object_or_404(User, username=str(request.user))
        lec = get_object_or_404(Lecturer, user=user)

        monday = LecturerAvailability.objects.create(
            lecturer=lec,
            day=day_monday,
            from_hr=monday_from,
            to_hr=monday_to,
        )

        tuesday = LecturerAvailability.objects.create(
            lecturer=lec,
            day=day_tuesday,
            from_hr=tuesday_from,
            to_hr=tuesday_to,
        )

        wednesday = LecturerAvailability.objects.create(
            lecturer=lec,
            day=day_wednesday,
            from_hr=wednesday_from,
            to_hr=wednesday_to,
        )

        thursday = LecturerAvailability.objects.create(
            lecturer=lec,
            day=day_thursday,
            from_hr=thursday_from,
            to_hr=thursday_to,
        )

        friday = LecturerAvailability.objects.create(
            lecturer=lec,
            day=day_friday,
            from_hr=friday_from,
            to_hr=friday_to,
        )
        monday.save()
        tuesday.save()
        wednesday.save()
        thursday.save()
        friday.save()
        return HttpResponse('availability submited successfully')

    return render(request, 'availability.html',)


def notify_lecturers(request):
    if request.method == 'POST':
        form = MessageBroadCastForm(request.POST)
        if form.is_valid():
            lecturers = Lecturer.objects.all()
            recipient = []
            for lecturer in lecturers:
                phone_number = str(lecturer.phone_number)
                recipient.append(phone_number)
            try:
                message = form.cleaned_data['message']
                username = settings.AT_USERNAME
                api_key = settings.AT_API_KEY
                sender = str(settings.AT_SENDER)
                gateway = AfricasTalkingGateway(username, api_key, sender)
                phone_numbers = ','.join(recipient)
                gateway.sendMessage(phone_numbers, message)
                return HttpResponse("Message sent")
            except AfricasTalkingGatewayException, e:
                print'Encountered an error while sending: %s' % str(e)
                return HttpResponse('error occurred {}'.format(str(e)))
    else:
        form = MessageBroadCastForm()
    return render(request, 'send_sms.html', {'form': form, })


def index(request):
    return render(request, 'index.html', {})