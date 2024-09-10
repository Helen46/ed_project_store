from django.shortcuts import render


def base(request):
    return render(request, "base.html")


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print (f"{name} {phone} {message}")
    return render(request, "contacts.html")
