from django.urls import path
from .views.category_views import CategoryListCreateView, CategoryDetailView
from .views.nominees_view import NomineesListCreateView, NomineesDeleteView

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
         name="Delete Nominee")
]
