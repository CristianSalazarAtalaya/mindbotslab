"""People URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# View
from people import views


urlpatterns = [

    # Management
    path(
        route='adviser/register/',
        view=views.adviser_register,
        name='adviser_register'
    ),
    path(
        route='adviser/update/',
        view=views.adviser_update,
        name='adviser_update'
    ),
    path(
        route='adviser/list/',
        view=views.AdviserListView.as_view(),
        name='adviser_list'
    ),

]
