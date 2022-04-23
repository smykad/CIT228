from django.shortcuts import render

from .models import Bloggit

# Create your views here.
def index(request):
    """The home page for Bloggits"""
    return render(request, 'bloggits/index.html')

def bloggits(request):
    """Show all bloggits."""
    bloggits = Bloggit.objects.order_by('date_added')
    context = {'bloggits': bloggits}
    return render(request, 'bloggits/bloggits.html', context)