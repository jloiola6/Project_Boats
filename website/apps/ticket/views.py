from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from apps.ticket.models import *
from apps.route.models import RouteWeekday


@login_required
def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket/index.html', {'tickets': tickets})

@login_required
def add(request, id, date):
    routeweek = RouteWeekday.objects.get(id=id)

    return render(request, 'ticket/add.html', {'routeweek': routeweek, 'date': date})

@login_required
def create_ticket(request, id, date):
    if request.method == 'POST':
        routeweek = RouteWeekday.objects.get(id=id)

        client = request.POST['client']
        document = request.POST['document']
        birth_date = request.POST['birth_date']

        ticket = Ticket.objects.create(
            user_create = request.user,
            route_weekday = routeweek,
            date = date,
            name_client = client,
            docuemnt_client = document,
            birth_date_client = birth_date
        )
        ticket.save()
        
        return redirect(reverse('core:index'))

@login_required
def edit(request):
    return render(request, 'ticket/edit.html')

def view(request, pk):
    ticket = Ticket.objects.get(id=pk)
    routeweek = ticket.route_weekday

    return render(request, 'ticket/view.html', {'ticket': ticket, 'routeweek': routeweek})