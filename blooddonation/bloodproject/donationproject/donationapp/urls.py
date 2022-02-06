from . import views
from django.urls import path
app_name = 'donationapp'
urlpatterns = [
    path('', views.allDistCen, name='allDistCen'),
    path('register', views.register, name='register_form'),
    path('login', views.login, name='login_page'),
    path('logout', views.logout, name='logout_page'),
    path('form', views.form, name='donation_form'),
    path('<slug:c_slug>/', views.allDistCen, name='districts_by_center'),
    path('<slug:c_slug>/<slug:district_slug>/', views.distDetail, name='distCendetail'),

]
