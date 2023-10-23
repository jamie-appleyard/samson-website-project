from django.shortcuts import render, redirect
from accounts.models import CustomUser, UserType, VettingStatus
from careers.models import Career, JobApplication
from careers.forms import NewVacancyForm
from news.models import Article
from news.forms import ArticleForm
from pages.models import Enquiry
from django.http import HttpResponse

def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/mandash.html')
    else:
        return redirect('login')

def vacancy_tab(request):
    if request.user.is_authenticated:
        careers = Career.objects.all()
        if request.method == 'POST':
            form = NewVacancyForm(request.POST)
            if form.is_valid():
                vacancy = form.save(commit=False)
                vacancy.job_posted_by = CustomUser.objects.get(pk=request.user.id)
                vacancy.save()
                return redirect('vacancy')
            else:
                return render(request, 'dashboard/vacancy.html', context= {'form':form,'careers':careers})
        else:
            form = NewVacancyForm()
            context = {
                'form' : form,
                'careers' : careers,
            }
            return render(request, 'dashboard/vacancy.html', context)
    else:
        return redirect('login')

def applications_view(request, pk):
    if request.user.is_authenticated:
        queryset = JobApplication.objects.filter(job_reference__pk=pk)
        context = {
            "applications" : queryset
        }
        return render(request, 'dashboard/applications.html', context)
    else:
        return redirect('login')

def applicant_view(request, pk):
    if request.user.is_authenticated:
        applicant = JobApplication.objects.get(pk=pk)
        context = {
            'applicant' : applicant,
        }
        return render(request, 'dashboard/applicantdetail.html', context)
    else:
        return redirect('login')

def news_room(request):
    if request.user.is_authenticated:
        previous = Article.objects.filter(status=0)
        drafts = Article.objects.filter(status=1)
        if request.method == "POST":
            if "draft_post" in request.POST:
                pk = request.POST["draft_post"]
                article = Article.objects.get(pk=pk)
                article.status = Article.Status.LIVE
                article.save()
                return redirect('news_room')
            elif "draft_delete" in request.POST:
                pk = request.POST["draft_delete"]
                article = Article.objects.get(pk=pk)
                article.status = Article.Status.DELETED
                article.save()
                return redirect('news_room')
            elif "live_delete" in request.POST:
                pk = request.POST["live_delete"]
                article = Article.objects.get(pk=pk)
                article.status = Article.Status.DELETED
                article.save()
                return redirect('news_room')
        else:   
            context = {
                'previous' : previous,
                'drafts' : drafts,
                }
            return render(request, 'news/newsroom.html', context)
    else:
        return redirect('login')

def news_editor(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                if 'post' in request.POST:
                    art = form.save(commit=False)
                    art.status = Article.Status.LIVE
                    art.save()
                    return redirect('news_room')
                else:
                    form.save()
                    return redirect('news_room')
            else:
                return render(request, 'news/editor.html', context = {'form' : form})
        else:
            form = ArticleForm()
            return render(request, 'news/editor.html', context = {'form' : form})
    else:
        return redirect('login')

def news_update(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                if 'post' in request.POST:
                    article.delete()
                    art = form.save(commit=False)
                    art.status = Article.Status.LIVE
                    art.save()
                    return redirect('news_room')
                else:
                    form.save()
                    return redirect('news_room')
            else:
                return render(request, 'news/editor.html', context = {'form' : form})
        else:
            return render(request, 'news/editor.html', context = {'form' : form})
    else:
        return redirect('login')

def enquiries_view(request):
    if request.user.is_authenticated:
        enquiries = Enquiry.objects.all()
        context = {'enquiries' : enquiries}
        return render(request, 'dashboard/enquiries.html', context)
    else:
        return redirect('login')
