from django.shortcuts import render, redirect
from .forms import EnquiryForm
from news.models import Article
from django.http import JsonResponse

#view function for the return of the home page and news article loading
def home_view(request):
    articles = Article.objects.filter(status=0).order_by('-id')
    last_three = articles[:3]
    context = {'articles' : last_three,}
    return render(request, 'home.html', context)

#view function for the return of the contact us page and enquiry form functionality
def contact_view(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'contact.html', context={'form' : form})
    else:
        return render(request, 'contact.html', context={'form' : form})

#view function for the return of solutions pages and enquiry form functionality
def solutions_page(request, url_name, template):
    articles = Article.objects.filter(status=0).order_by('-id')
    last_three = articles[:3]
    form = EnquiryForm(request.POST or None)
    context = {
        'form' : form,
        'articles' : last_three,
    }
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['status'] = "ok"
            return JsonResponse(data)
    else:
        return render(request, template, context)

#view functions for the individiual services pages taking advantage of the base solutions page function
def solution_guarding(request):
    return solutions_page(request, 's_guards', 'solutions/s_guarding.html')

def solution_monitoring(request):
    return solutions_page(request, 's_monitoring', 'solutions/s_monitoring.html')

def solution_engineering(request):
    return solutions_page(request, 's_engineering', 'solutions/s_engineering.html')

def solution_key_management(request):
    return solutions_page(request, 's_keymanagement', 'solutions/s_keymanagement.html')

def solution_helpdesk(request):
    return solutions_page(request, 's_helpdesk', 'solutions/s_helpdesk.html')

def solution_professional(request):
    return solutions_page(request, 's_professional', 'solutions/s_professional.html')

def about_us(request):
    return render(request, 'about_us.html')

def about_quality(request):
    return render(request, 'about_quality.html')

def about_csr(request):
    return render(request, 'about_csr.html')

def about_accreditation(request):
    return render(request, 'about_accreditation.html')
