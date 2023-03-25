from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Season, Note
from .forms import PlayerForm, SeasonForm, NoteForm
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

        # Get the 'season' GET parameter and set the selected year accordingly
        selected_year = self.request.GET.get('season', '2022-23 Season') # set a default value
        if selected_year:
            queryset = queryset.filter(season__name=selected_year)

        return queryset.order_by('last_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.objects.all()
        season_year = self.request.GET.get('season')
        if season_year:
            context['selected_year'] = season_year
        else:
            context['selected_year'] = '2022-23 Season' # set a default value
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
class ViewLineup(LoginRequiredMixin, ListView):
    model = Player
    template_name = "rostermanager/lineup.html"
    context_object_name = "players"
    empty_message = "No data available"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        # Get the 'season' GET parameter and set the selected year accordingly
        selected_year = self.request.GET.get("season", "2022-23 Season")  # set a default value
        if selected_year:
            queryset = queryset.filter(season__name=selected_year)
        print(queryset)
        return queryset.order_by("last_name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seasons"] = Season.objects.all()
        season_year = self.request.GET.get("season")
        if season_year:
            context["selected_year"] = season_year
        else:
            context["selected_year"] = "2022-23 Season"  # set a default value
        return context

    def post(self, request, *args, **kwargs):
        player_ids = request.POST.getlist("player_ids[]")
        new_positions = request.POST.getlist("new_positions[]")
        for i in range(len(player_ids)):
            player = Player.objects.get(id=player_ids[i])
            player.position = new_positions[i]
            player.save()
        return JsonResponse({"success": True})


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

# Allow the user to view their roster notes
class ViewNotes(LoginRequiredMixin, ListView):
    model = Note
    template_name = "rostermanager/notes.html"
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class CreateNote(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "rostermanager/add_note.html"
    success_url = reverse_lazy('roster_notes')

    def form_valid(self, form):
        # Check if there are any other validation errors on the form
        if form.errors:
            return self.form_invalid(form)
        
        form.instance.user = self.request.user
        return super().form_valid(form)