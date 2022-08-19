from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.home_url),
    path('demo/', v.demo_url),
    path('stackReq/', v.stack_req_url),
]
