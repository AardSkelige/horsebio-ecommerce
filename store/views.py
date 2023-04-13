from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import UserRegisterForm, UserLoginForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


def home(request):
    root_dog = Category.objects.get(name='Собаки')
    dog_series = root_dog.get_descendants(
        include_self=True).filter(level__lte=1)
    dog_tree = root_dog.get_descendants(include_self=True)
    dog_pharma = [node for node in dog_tree if len(
        node.get_descendants(include_self=True)) == 1]

    root_horse = Category.objects.get(name='Лошади')
    horse_series = root_horse.get_descendants(
        include_self=True).filter(level__lte=1)
    horse_tree = root_horse.get_descendants(include_self=True)
    horse_pharma = [node for node in horse_tree if len(
        node.get_descendants(include_self=True)) == 1]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],'mystmuse@mail.ru', ['mystmuse@mail.ru'], fail_silently=False )
            if mail:
                messages.success(request, 'Отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки!')        
        else:
            messages.error(request, 'Ошибка отправки...')
    else:
        form = ContactForm()

    context = {
        'dog_series': dog_series,
        'horse_series': horse_series,
        'dog_pharma': dog_pharma,
        'horse_pharma': horse_pharma,
        'form': form,
    }
    return render(request, 'store/index.html', context)


def get_category(request, product_slug):
    category = Category.objects.get(slug=product_slug)
    categories = Category.objects.all()
    # предки
    ancestors = category.get_ancestors()
    # все потомки
    descendants = category.get_descendants()
    category_descendants = [i.slug for i in descendants]
    category_descendants.append(product_slug)
    products = Product.objects.filter(
        category__slug__in=category_descendants).select_related('category')
    context = {
        'category': category,
        'categories': categories,
        'ancestors': ancestors,
        'products': products,
    }

    return render(request, 'store/products.html', context)


def get_product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    category = product.category
    categories = Category.objects.all()
    ancestors = category.get_ancestors()
    context = {
        'category': category,
        'categories': categories,
        'ancestors': ancestors,
        'product': product,
    }
    return render(request, 'store/view_product.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'store/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    print('User logg')
    return render(request, 'store/login.html', context)
