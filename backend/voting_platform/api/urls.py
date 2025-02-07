from django.urls import path
from .views.category_views import CategoryListCreateView, CategoryDetailView
from .views.nominees_view import (NomineesListCreateView, NomineesDeleteView,
                                  NomineesUpdateView)
from .views.awards_view import (AwardsListCreateView, AwardsDeleteView,
                                AwardsUpdateView)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(),
         name='category-list-create'),
    path('categories/<uuid:pk>/',CategoryDetailView.as_view(),
         name='category-detail'),
    path("nominees/", NomineesListCreateView.as_view(),
         name="All nominees"),
    path("nominees/<uuid:pk>", NomineesListCreateView.as_view(),
         name="Nominee"),
    path("nominees/delete/<uuid:pk>", NomineesDeleteView.as_view(),
         name="Delete Nominee"),
    path("nominees/put/<uuid:pk>", NomineesUpdateView.as_view(),
         name="Nominee Edit"),
    path("awards/", AwardsListCreateView.as_view(),
         name="All Awards"),
    path("awards/<uuid:pk>", AwardsListCreateView.as_view(),
         name="Award"),
    path("awards/delete/<uuid:pk>", AwardsDeleteView.as_view(),
         name="Delete Award"),
    path("awards/put/<uuid:pk>", AwardsUpdateView.as_view(),
         name="Edit Award")
]
