from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/',views.about),
    path('word',views.word),
    path('english_hindi',views.english_hindi),
    path('hindi_word',views.hindi_word),
    # path('about/',views.about),
    # path('add_form/',views.show_form),
]