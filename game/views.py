from django.shortcuts import render, redirect
from .models import Event

# Create your views here.
def live_game(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        forward1 = request.POST.get('forward1')
        forward2 = request.POST.get('forward2')
        forward3 = request.POST.get('forward3')
        defense1 = request.POST.get('defense1')
        defense2 = request.POST.get('defense2')
        goalie = request.POST.get('goalie')
        ext_attacker = request.POST.get('ext_attacker')
        special_teams = request.POST.get('special_teams')
        extra_attacker = request.POST.get('extra_attacker')
        event_type = request.POST.get('event_type')

        # Create a new GameEvent instance with the appropriate event_type value
        

        if request.user.is_authenticated:
            game_event = Event.objects.create(user = request.user, date=date, forward1=forward1, forward2=forward2, forward3=forward3, defense1=defense1, defense2=defense2, goalie=goalie, ext_attacker=ext_attacker, special_teams=special_teams, extra_attacker=extra_attacker, event_type=event_type)
            # Set the user attribute of the GameEvent instance to the currently authenticated user
            #game_event.user = request.user
        
        game_event.save()

    last_events = Event.objects.order_by('-id')[:5]
    context = {
        'last_events': last_events,
    }

    # Render the live game page
    return render(request, 'game/live_game.html', context)


def add_toi(request):
    if request.method == 'POST':
        

        # Create a new GameEvent instance with the appropriate event_type value
        

        if request.user.is_authenticated:
            game_event = Event.objects.create(user = request.user, )
            # Set the user attribute of the GameEvent instance to the currently authenticated user
            #game_event.user = request.user
        
        game_event.save()

    # Render the live game page
    return render(request, 'game/toi.html')


def delete_event(request, event_id):
    # Retrieve the event from the database
    event = Event.objects.get(id=event_id)

    # Delete the event
    event.delete()

    # Redirect back to the same page
    return redirect('live_game.html')