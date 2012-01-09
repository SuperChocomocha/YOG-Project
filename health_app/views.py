from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from health_app.models import Personal_Data, Health_Data, Health_Info, Dynamic_Info
from django.contrib import messages
import datetime

def start(request):
    # need to take care of logout post (HttpResponseRedirect somewhere)
    return render_to_response('health_app/start.html',
                              context_instance = RequestContext(request))

# Create a Recover Account option that will send the password to the specified email.
# This means I have to create a change password option.

def login(request): # create this
    return render_to_response('health_app/login.html')

def signup(request):
    return render_to_response('health_app/signup.html',
                              context_instance = RequestContext(request))
def redirect(request):
    r = request.POST

    if r[u'email'] == '' or r[u'pass'] == '' or r[u'cpass'] == '' or not r[u'gender']:
        messages.error(request, 'Please fill out all the fields.')
        return HttpResponseRedirect('/signup/')
    else:
        try:
            p_data_email = Personal_Data.objects.get(email_addr = r[u'email'])
        except (Personal_Data.DoesNotExist):
            if r[u'pass'] == r[u'cpass']:
                new_acc = Personal_Data(email_addr = r[u'email'], password = r[u'pass'],
                                        time_modified = datetime.datetime.now(),
                                        gender = r[u'gender'], age = 0, race = '')
                new_acc.save()
                selected_acc = Personal_Data.objects.get(email_addr = r[u'email'])
                
                # check for valid email/pass eventually

                messages.success(request, 'Account created successfully!')
                return HttpResponseRedirect('/app/' + str(selected_acc.acc_id) + '/homepage/')
            else:
                messages.error(request, 'The passwords do not match.')
                return HttpResponseRedirect('/signup/')
        else:
            messages.error(request, 'Your account already exists. Please sign in or use the recover password feature.')
            return HttpResponseRedirect('/start/')

def homepage(request, acc_id):
    return render_to_response('health_app/homepage.html',
                              context_instance = RequestContext(request))
    # need logout button

def input_hr(request, acc_id):
    return render_to_response('health_app/input_hr.html')

def details(request, acc_id):
    return render_to_response('health_app/details.html')

