from django.urls import path
from .views import TravelPlanListView, TravelPlanDetailView, TravelPlanCreateView, TravelPlanUpdateView, TravelPlanDeleteView
from . import views

urlpatterns = [
    path('home/', views.home , name = 'aboutus'),
    path('', TravelPlanListView.as_view(), name='expenselist'),
    path('<int:pk>/', TravelPlanDetailView.as_view(), name='expensedetail'),
    path('create/', TravelPlanCreateView.as_view(), name='expensecreate'),
    path('<int:pk>/update/', TravelPlanUpdateView.as_view(), name='expenseupdate'),
    path('<int:pk>/delete/', TravelPlanDeleteView.as_view(), name='expensedelete'),
]
