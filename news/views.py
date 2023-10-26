from django.shortcuts import render
from news.models import Article
from django.template.loader import render_to_string
from django.http import JsonResponse

#view function for rendering the news page, filters all articles for first 6 articles to render via context in template.
# separates out the featured article to be rendered at the top of the page
def news_view(request):
    articles = Article.objects.filter(status = 0)
    data_total = len(articles)
    first_set = Article.objects.filter(status = 0).order_by('-date_posted')[:6]
    featured = articles.get(featured = True)
    context = {
        'articles' : first_set,
        'featured' : featured,
        'data_total': data_total,
    }
    return render(request, 'news/news.html', context)

#Function to fetch articles form the database and slice the list by index of current number of articles displayed (offset) 
#and the number of new articles to be displayed (hard set to 3 in the news.html template), ajax request triggered by onclick
#event in JS for .load-more-button
def load_articles(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    new_articles = Article.objects.filter(status = 0).order_by('-date_posted')[offset: offset+limit]
    context = {
        'articles' : new_articles,
    }
    t = render_to_string('ajax/load_articles.html', context)
    return JsonResponse({'new_articles' : t})

#view function for viewing full article pages
def article_view(request, pk):
    articles = Article.objects.filter(status = 0).order_by('-date_posted')[:3]
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
        'articles' : articles}
    return render(request, 'news/article.html', context)
