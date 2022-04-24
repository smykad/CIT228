from django.shortcuts import redirect, render

from .models import Bloggit
from .forms import BloggitForm

# Create your views here.
def index(request):
    """The home page for Bloggits"""
    return render(request, 'bloggits/index.html')

def bloggits(request):
    """Show all bloggits."""
    bloggits = Bloggit.objects.order_by('date_added')
    context = {'bloggits': bloggits}
    return render(request, 'bloggits/bloggits.html', context)

def bloggit(request, bloggit_id):
    """Show a single bloggit and its entries"""
    bloggit = Bloggit.objects.get(id=bloggit_id)
    entries = bloggit.entry_set.order_by('-date_added')
    context = { 'bloggit': bloggit, 'entries': entries}
    return render(request, 'bloggits/bloggit.html', context)

def new_bloggit(request):
    """Add a new bloggit"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BloggitForm()
    else:
        # POST data submitted; process data.
        form = BloggitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloggits:bloggits')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'bloggits/new_bloggit.html', context)