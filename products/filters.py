from django_filters import rest_framework as filters
from .models import Games

class GamesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    score_gte = filters.NumberFilter(field_name="score", lookup_expr="gte")
    score_lte = filters.NumberFilter(field_name="score", lookup_expr="lte")
    price_gte = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_lte = filters.NumberFilter(field_name="price", lookup_expr="lte")
    class Meta:
        model = Games
        fields = ['price', 'score', 'name']
