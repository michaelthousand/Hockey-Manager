from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy

# Create your views here.
class ViewNotes(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/notes.html"
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notes')
    else:
        form = NoteForm()
    return render(request, 'notes/notes.html', {'form': form})