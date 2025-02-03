from django.urls import path
from .views.category_views import CategoryListCreateView, CategoryDetailView
from .views.nominees_view import NomineesListCreateView#, NomineesDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(),
         name='category-list-create'),
    path('categories/<uuid:pk>/',CategoryDetailView.as_view(),
         name='category-detail'),
    path("nominees/", NomineesListCreateView.as_view(),
         name="All nominees"),
    path("nominees/<uuid:pk>", NomineesListCreateView.as_view(),
         name="Nominee")
]
