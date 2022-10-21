import django_filters.rest_framework

from rest_framework import generics
from rest_framework import status as response_status 
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from apps.vacancies.models import Vacancy

from .serializers import VacancySerializer

class VacancyArchiveToggleAPIView(APIView):

    '''
    200 - archived \n
    204 - unarchived \n
    406 - user is not owner or vacancy doesn't exist \n
    '''

    permission_classes = [IsAuthenticated]

    def _archive(self) -> bool :
        self.target.archived = not self.target.archived 
        self.target.save()
        return self.target.archived

    def get(self, request: Request, id:int) -> Response :
        self.target = request.user.vacancies.filter(id=id).first()
        self.status = 0

        if not self.target:
            return Response({}, status=406)

        return Response({}, status = 200 if self._archive() else 204 )


class VacancyDeleteAPIView(APIView):

    def get(self, request: Request, id:int) -> Response :
        self.target = request.user.vacancies.filter(id=id).first()

        if not self.target:
            return Response({}, status=406)

        # self.target.delete()
        return Response({}, status=200)


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.active.all()
    serializer_class = VacancySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id','position','location','tags','verified','hot']
