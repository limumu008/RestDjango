from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .serializers import TalkSerializer
from .models import Talk


class TalksPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class TalkList(ListAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'speaker')
    pagination_class = TalksPagination

    def get_queryset(self):
        on_site = self.request.query_params.get('on_site', None)
        if on_site is None:
            return super().get_queryset()
        queryset = Talk.objects.all()
        if on_site.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                talk_start__lte=now,
                talk_end__gte=now,
            )
        return queryset


class TalkCreate(CreateAPIView):
    serializer_class = TalkSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class TalkRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Talk.objects.all()
    lookup_field = 'id'
    serializer_class = TalkSerializer

    def delete(self, request, *args, **kwargs):
        talk_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(talk_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            talk = response.data
            cache.set('talk_data_{}'.format(talk['id']), {
                'name': talk['name'],
                'speaker': talk['speaker'],
                'venue': talk['venue'],
                'talk_start': talk['talk_start'],
                'talk_end': talk['talk_end'],
            })
        return response



