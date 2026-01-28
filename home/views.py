from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home_view(request):
    return render(request, 'home/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # adăugăm clase Bootstrap
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

        # ȘI AICI (pentru GET)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

    return render(request, 'registration/signup.html', {'form': form})

