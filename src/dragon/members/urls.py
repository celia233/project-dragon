from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('clubmembers/', views.clubmembers, name='clubmembers'),
    path('clubmember_form/', views.clubmember_form, name='clubmember_form'),
    path('add_clubmember/', views.add_clubmember, name='add_clubmember'),
    path('clubmember/<int:clubmember_id>/', views.clubmember_detail, name='clubmember_detail'),
    path('remove_clubmember/<int:clubmember_id>/', views.remove_clubmember, name='remove_clubmember'),

    path('nonmembers/', views.nonmembers, name='nonmembers'),
    path('nonmember_form/', views.nonmember_form, name='nonmember_form'),
    path('add_nonmember/', views.add_nonmember, name='add_nonmember'),
    path('nonmember/<int:nonmember_id>/', views.nonmember_detail, name='nonmember_detail'),
    path('remove_nonmember/<int:nonmember_id>/', views.remove_nonmember, name='remove_nonmember'),
    
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
