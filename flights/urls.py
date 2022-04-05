from django.urls import path
from . import views 
app_name="flights"
urlpatterns = [
   path('',views.index,name="index"),
   path('<int:abc_id>',views.flight,name="flight"),
   path('passenger/',views.passenger,name="passenger"),
   path('<int:flight_id/book',views.book,name="book")

]
