from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def main(request):
 			return render(request, 'blog/ТОО НТК Sfera-S.html', {})
def news(request):
	posts =	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/новости.html', {'posts': posts})
	
def clean(request):
 			return render(request, 'blog/чистка.html', {})
def services(request):
 			return render(request, 'blog/наши услуги.html', {})
def outsourcing(request):
 			return render(request, 'blog/аутсорсинг.html', {})
def repairs_laptop(request):
 			return render(request, 'blog/ремонт-комп.html', {})
def repairs(request):
 			return render(request, 'blog/ремонт.html', {})
def recovery(request):
 			return render(request, 'blog/восстановление.html', {})
def assembly(request):
 			return render(request, 'blog/сборка.html', {})
def price(request):
 			return render(request, 'blog/прайст-лист.html', {})
def contacts(request):
 			return render(request, 'blog/контакты.html', {})