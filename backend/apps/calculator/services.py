from django.db.models import Sum, Value, DecimalField, IntegerField, Q, F


class IpotecaPaymentService:
    def get_payment(self, summa, term, field):
        return (summa + summa * term * ((F(field)) / 12) / 100) / (term * 12)

    def get(self, queryset, price, deposit, term):
        if price > 0 and term > 0 and 0 <= deposit < 100:
            summa = (price - price * deposit / 100)
            queryset = queryset.filter(
                Q(payment_min__lte=summa) & Q(payment_max__gte=summa)
            )
            queryset = queryset.filter(
                Q(term_min__lte=term) & Q(term_max__gte=term)
            )
            queryset = queryset.annotate(
                payment_low=Sum(self.get_payment(summa, term, field='rate_min'))
            )
            queryset = queryset.annotate(
                payment_high=Sum(self.get_payment(summa, term, field='rate_max'))
            )
            queryset = queryset.annotate(
                price=Value(price, output_field=IntegerField())
            )
            queryset = queryset.annotate(
                deposit=Value(deposit, output_field=DecimalField(
                    max_digits=4, decimal_places=2
                ))
            )
            queryset = queryset.annotate(
                term=Value(term, output_field=IntegerField())
            )
        return queryset
