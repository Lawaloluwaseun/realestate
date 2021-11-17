from django.urls import path


from  .import views



app_name = 'user'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('listings/', views.listings, name='listings'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('contact/', views.contact, name='contact'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),


]
