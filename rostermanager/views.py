from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Season
from .forms import PlayerForm, SeasonForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'rostermanager/rosterhome.html')

# List of all players for roster
class PlayerList(LoginRequiredMixin, ListView):
    model = Player
    template_name = "rostermanager/roster.html"
    context_object_name = 'roster'

    def get_queryset(self):
        queryset = super().get_queryset()
        season_year = self.request.GET.get('season', '2022-23')
        if season_year:
            queryset = queryset.filter(user=self.request.user)
            queryset = queryset.filter(season__year=season_year)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.objects.all()
        season_year = self.request.GET.get('season')
        if season_year:
            context['selected_year'] = season_year
        return context

# Allows the user to add new players
class CreatePlayer(LoginRequiredMixin, CreateView):
    model = Player
    form_class = PlayerForm
    template_name = "rostermanager/add_player.html"
    success_url = reverse_lazy('roster')

    def form_valid(self, form):
        # Check if there are any other validation errors on the form
        if form.errors:
            return self.form_invalid(form)
        
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# Update player information
class UpdatePlayer(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'rostermanager/update_player.html'
    success_url = reverse_lazy('roster')

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

# Test - Delete a player
class DeletePlayer(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = 'rostermanager/delete_player.html'
    success_url = reverse_lazy('roster')

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

# Allows the user to add new seasons
@login_required
def add_season(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SeasonForm()
    return render(request, 'rostermanager/add_season.html', {'form': form})

# Lineup view
class viewlineup(LoginRequiredMixin, ListView):
    model = Player
    template_name="rostermanager/lineup.html"
    context_object_name = 'players'
    empty_message = 'No data available'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

# To save the lineup - don't know if it will work but will need to see when site is live
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def save_lineup(request):
    if request.method == 'POST':
        positions = json.loads(request.body)
        for player_name, position in positions.items():
            player = Player.objects.get(last_name=player_name)
            player.position = position
            player.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})