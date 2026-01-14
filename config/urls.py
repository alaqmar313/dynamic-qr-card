from django.contrib import admin
from django.urls import path
from qr_app.views import home, view_card

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('card/<uuid:id>/', view_card, name='view_card'),
]
