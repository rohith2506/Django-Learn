from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from books.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def search_form(request):
	return render(request,'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def contact(request):
	if request.method == "POST":
			form = ContactForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				send_mail(
					cd['subject'],
					cd['message'],
					cd.get('email', 'noreply@example.com'),
					['rohith.uppala369@gmail.com'],
					)
				return HttpResponseRedirect('/contact/thanks')
	else:
		form = ContactForm()
	return render(request,'contact_form.html',{'form':form})
	
def thanks(request):
	return render(request,'thank_you.html')