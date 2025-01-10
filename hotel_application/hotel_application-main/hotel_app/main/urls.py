from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:room_id>/', views.detail, name='detail'),
    path('reserve/<int:room_id>/', views.make_reservation, name='make_reservation'),
    path('reservation_list/', views.reservation_list, name='reservation_list'),
    path('about_us/', views.about_us, name='about_us'),
    path('search/', views.search, name='search'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)