from django.db import models


class Ipoteka(models.Model):
    # payment": null,
    bank_name = models.CharField(max_length=200, default='', verbose_name="Наименование банка")
    term_min = models.IntegerField(default=0, verbose_name="Срок ипотеки, ОТ")
    term_max = models.IntegerField(default=0, verbose_name="Срок ипотеки, ДО")
    rate_min = models.FloatField(default=0, verbose_name="Ставка, ОТ")
    rate_max = models.FloatField(default=0, verbose_name="Ставка, ДО")
    payment_min = models.BigIntegerField(default=0, verbose_name="Сумма кредита, ОТ")
    payment_max = models.BigIntegerField(default=0, verbose_name="Сумма кредита, ДО")

    def __str__(self):
        return self.bank_name
