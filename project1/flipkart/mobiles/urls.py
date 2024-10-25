from django.urls import path
from mobiles import views
urlpatterns=[
    path('',views.func1,name="homep"),
    path('aboutPage',views.func2,name="aboutp"),
    path('contact',views.func3,name="contactp"),
]