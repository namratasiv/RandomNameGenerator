from django.urls import path
from randomness.views import RandomList
#URL CONFIGURATION
urlpatterns = [
    path("random/", RandomList.as_view(), name="random"),
]