from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from .forms import Login, SignUp, UpdateProfile
from django.contrib.auth import login, authenticate, logout
from core.models import Diet, Profile, Food, Meal


def index(request):
    return render(request, 'index.html')


def header_view(request):
    return render(request, 'header.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


@login_required(login_url='/login/')
def profile(request):
    context = {}
    context['page'] = 'Update Profile'
    flg = False
    print(request.user)
    if request.method == 'POST':
        print('post-profile')
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            print('valid-profile')
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.diet = Diet.objects.filter(name='Omnivore').first()
            user_profile.save()
            return redirect("/diet")
        else:
            flg = True
    if request.method == 'GET' or flg:
        if flg:
            messages.error(request, "Invalid data.")
        form = UpdateProfile()
        context['form'] = form
    return render(request, 'signup.html', context)


@login_required(login_url='/login/')
def diet(request):
    context = {}
    user = request.user
    if request.user.profile.diet:
        meals = user.profile.meal_set.all()
        print(meals)
        # Show diet
        if meals:
            context['meals'] = meals
        # Show foods
        else:
            print('show food')
            chosen_diet = Diet.objects.get(id=user.profile.diet.id)
            foods = list(Food.objects.filter(diet=chosen_diet))
            context['foods'] = foods
            print(user.profile.diet)
    else:
        diets = Diet.objects.all()
        context['diets'] = diets
    return render(request, 'diet.html', context)

    if request.GET.get('create_diet', None):
        # Create meals
        fav_foods = request.GET.getlist('fav_foods[]')
        print(fav_foods)
        if not fav_foods:
            # No food chosen
            messages.error(request, "Must choose some food.")
            show_food = True

    if chosen_diet is None:
        if user.profile.diet is None:
            diets = Diet.objects.all()
            context['diets'] = diets
        else:
            # show me food
            show_food = True
    else:
        show_food = True
        user.profile.diet = Diet.objects.get(id=chosen_diet)
        user.profile.save()
    if show_food:
        print('show food')
        chosen_diet = Diet.objects.get(id=user.profile.diet.id)
        foods = list(Food.objects.filter(diet=chosen_diet))
        context['foods'] = foods
        print(user.profile.diet)
    return render(request, 'diet.html', context)


def signup_view(request):
    context = {}
    context['page'] = 'Sign Up'
    if request.method == 'POST':
        form = SignUp(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile')
        else:
            form = SignUp()
    else:
        form = SignUp()
    context['form'] = form
    return render(request, 'signup.html', context)

def aboutus_view(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def update_diet(request):
    chosen_diet = request.POST('chosen_diet', None)
    request.user.profile.diet = Diet.objects.get(id=chosen_diet)
    request.user.profile.save()
    return redirect('/diet')


def favorite_food(request):
    m = Meal()
    profile = request.user.profile
    foods_selected = request.POST.getlist('fav_foods[]')
    breakfast_foods = []
    dinner_foods = []
    snack_foods = []
    lunch_foods = []
    # Sorting foods into 4 main categories
    for food in foods_selected:
        for food_type in food.type:
            if food_type == 'Breakfast':
                breakfast_foods.append(food)
            elif food_type == 'Lunch':
                lunch_foods.append(food)
            elif food_type == 'Dinner':
                dinner_foods.append(food)
            elif food_type == 'Snack':
                snack_foods.append(food)
    # Calculate needed calories per day
    total_calories_needed = 2500
    bmi = profile.height / (profile.weight * profile.weight)
    if profile.gender == 'Male':
        if bmi < 18.5:
            total_calories_needed = 3500
        elif bmi >= 18.5 and bmi <= 25:
            total_calories_needed = 3000
        elif bmi > 25:
            total_calories_needed = 1800
    else:
        if bmi < 18.5:
            total_calories_needed = 3000
        elif bmi >= 18.5 and bmi <= 25:
            total_calories_needed = 2500
        elif bmi > 25:
            total_calories_needed = 1500
    # Precentge for each meal
    breakfast_calories_needed = total_calories_needed * 0.2
    lunch_calories_needed = total_calories_needed * 0.5
    dinner_calories_needed = total_calories_needed * 0.3
    # Making meal plans for 7 days breakfast
    i = 0
    for _ in range(7):
        m = Meal()
        m.profile = profile
        m.type = 'Breakfast'
        total = 0
        while total < breakfast_calories_needed:
            food = Food.objects.get(pk=breakfast_foods[i % len(breakfast_foods)])
            i += 1
            m.foods.add(food)
            total += food.calories
        m.save()
    # Making meal plans for 7 days lunch
    i = 0
    for _ in range(7):
        m = Meal()
        m.profile = profile
        m.type = 'Lunch'
        total = 0
        while total < lunch_calories_needed:
            food = Food.objects.get(pk=lunch_foods[i % len(lunch_foods)])
            i += 1
            m.foods.add(food)
            total += food.calories
        m.save()
    # Making meals for 7 days dinner
    i = 0
    for _ in range(7):
        m = Meal()
        m.profile = profile
        m.type = 'Dinner'
        total = 0
        while total < dinner_calories_needed:
            food = Food.objects.get(pk=dinner_foods[i % len(dinner_foods)])
            i += 1
            m.foods.add(food)
            total += food.calories
        m.save()
    return redirect('/diet')

