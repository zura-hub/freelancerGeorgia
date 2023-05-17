from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import  DetailView

def vacancy(request):
    jobs = Articles.objects.all()
    return render(request, 'vacancy/vacancy.html', {'jobs': jobs})


class jobsDetailView(DetailView):
    model = Articles
    template_name = 'jobs/detail_view.html'
    context_object_name = 'article'


def create(request):
    error = ''

    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy')
        else:
            error = 'Fill Forms correctly'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'vacancy/create.html', data)