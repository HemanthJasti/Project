from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import TravelPlan
from .forms import TravelPlanForm
import pdb


def home(request):
    return render(request, 'home.html')

class TravelPlanListView(ListView):
    model = TravelPlan

    queryset = TravelPlan.objects.all()
    context_object_name = 'expense'
    template_name = 'expenses.html'
    paginate_by = 10
    pdb.set_trace

class TravelPlanDetailView(DetailView):
    model = TravelPlan
    template_name = 'expense.html'
    context_object_name = 'expense'

class TravelPlanCreateView(CreateView):
    model = TravelPlan
    form_class = TravelPlanForm
    template_name = 'create.html'
    success_url = reverse_lazy('expenselist')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TravelPlanUpdateView(UpdateView):
    model = TravelPlan
    form_class = TravelPlanForm
    template_name = 'edit.html'
    success_url = reverse_lazy('travelplan_list')

class TravelPlanDeleteView(DeleteView):
    model = TravelPlan
    template_name = 'travelplan_confirm_delete.html'
    success_url = reverse_lazy('travelplan_list')
