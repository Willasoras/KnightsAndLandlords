from django.shortcuts import render


def landing(request):
    context = dict()
    if request.method == 'POST':
        context['data'] = request.POST['words']
        return render(request, 'index.html', context)
    return render(request, 'index.html')