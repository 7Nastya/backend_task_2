from rest_framework import viewsets
from .models import Ipoteka
from .serializers import IpotekaSerializer
from .services import IpotecaPaymentService


class IpotekaViewSet(viewsets.ModelViewSet):
    serializer_class = IpotekaSerializer
    queryset = Ipoteka.objects.all().order_by('rate_min')
    # filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ['bank_name']
    ordering_fields = ['rate_min', 'term_min', 'payment_min']

    def get_queryset(self):
        ipoteca_payment = IpotecaPaymentService()
        queryset = super().get_queryset()
        request = self.request.GET
        if request.get('price') and request.get('deposit') and request.get('term'):
            try:
                price = int(request['price'])
                deposit = float(request['deposit'])
                term = int(request['term'])
            except ValueError:
                print("Неправильные данные")
                return queryset

            queryset = ipoteca_payment.get(queryset, price, deposit, term)
        return queryset


