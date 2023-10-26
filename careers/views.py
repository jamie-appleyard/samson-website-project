from django.shortcuts import render, redirect
from .models import Career, JobApplication
from accounts.models import CustomUser
from careers.forms import ApplicationForm, TrainingInterestForm
from django.http import HttpResponse, JsonResponse
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form


#Function based view for the rendering of the careers page and the training interest form at the foot of the page, data from form
#submitted via ajax to database, some control in between in JS.
def careers_page(request):
    form = TrainingInterestForm(request.POST or None)
    model = Career
    careers = model.objects.all()
    context = {
        'careers' : careers,
        'form' : form,
    }
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['success'] = True
            data['name'] = form.cleaned_data['name']
            return JsonResponse(data)
        else:
            data['success'] = False
    else:       
        return render(request, 'careers/careers.html', context)


#Funciton based view for the application form page, submitting the application form to the database through AJAX, checking
#for form validation
def apply_view(request, pk):
    context = {}
    career = Career.objects.get(id = pk)
    context['career'] = career
    form = ApplicationForm(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            application = form.save(commit=False)
            application.job_reference = Career.objects.get(pk=pk)
            application = application.save()
            job_reference = Career.objects.get(pk=pk)
            job_reference.number_of_applications += 1
            job_reference.save()
            data['success'] = True
            return JsonResponse(data)
        else:
            data = {}
            data['success'] = False
            ctx = {}
            ctx.update(csrf(request))
            form_html = render_crispy_form(form, context=ctx)
            data['form_html'] = form_html
            return JsonResponse(data)
    else:
        context['form'] = form
        return render(request, "careers/apply.html", context)