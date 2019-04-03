from django.shortcuts import render
from news.models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date_year=year)
    context = {'year':year, 'article_list':a_list}
    return render(request, 'news/year_archive.html', context)