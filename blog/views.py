from django.shortcuts import render

def main(request):
 			return render(request, 'blog/ТОО НТК Sfera-S.html', {})
def news(request):
 			return render(request, 'blog/новости.html', {})
def clean(request):
 			return render(request, 'blog/чистка.html', {})
def services(request):
 			return render(request, 'blog/аутсорсинг.html', {})
def outsourcing(request):
 			return render(request, 'blog/восстановление.html', {})
def repairs_laptop(request):
 			return render(request, 'blog/контакты.html', {})
def repairs(request):
 			return render(request, 'blog/наши услуги.html', {})
def recovery(request):
 			return render(request, 'blog/ремонт.html', {})
def assembly(request):
 			return render(request, 'blog/ремонт-комп.html', {})
def price(request):
 			return render(request, 'blog/сборка.html', {})
def contacts(request):
 			return render(request, 'blog/сборка.html', {})