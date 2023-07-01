from django.urls import path
from . import views
from .views import HomeView,HomeLocationView,HomeCategoryView,AboutView,ContactView,ProfileCartView,ProfileView,ProfileManagerView,ProfileHistoryView,ProfileManagerInventory,OrderView , add_to_cart , remove_from_cart

urlpatterns = [
    path('' , views.HomeView , name='home'),
    path('<int:id_city>/' , views.HomeLocationView , name='homeLocation'),
    path('Category/<int:id_category>/' , views.HomeCategoryView , name='homeCategory'),
    path('about/' , views.AboutView , name='about'),
    path('contact/' , views.ContactView , name='contact'),
    path('<str:username>/' , views.ProfileCartView , name='profileCart'),
    path('<int:pk>/Profile/' , ProfileView.as_view() , name='profile'),
    path('<str:username>/ProfileHistory/' , views.ProfileHistoryView , name='profileHistory'),
    path('<int:pk>/ProfileManager/' , ProfileManagerView.as_view() , name='profileManager'),
    path('<str:username>/ProfileManagerHistory/' , views.ProfileManagerInventory, name='profileManagerInventory'),
    path('<int:inventory_id>/Product/' , views.OrderView , name='order'),
    path('add_to_cart/<int:inventory_id>' , add_to_cart , name='addToCart'),
    path('remove_from_cart/<int:inventory_id>' , remove_from_cart , name='removeFromCart'),
]