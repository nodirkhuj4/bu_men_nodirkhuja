import django_filters
from common.models import News

class NewsFilter(django_filters.FilterSet):
    exclude = django_filters.NumberFilter(field_name="id", lookup_expr="exact", exclude=True)
    top = django_filters.BooleanFilter(field_name="top", lookup_expr="exact")

    class Meta:
        model=News
        fields=['exclude', 'top']