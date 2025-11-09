from django.db import models
from .validators import validate_debt, validate_product_release_date


class NetworkNode(models.Model):
    """ Модель сети из 3 объектов (завод, розничная сеть, ИП) """
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень сети')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=15,
                               decimal_places=2,
                               default=0,
                               validators=[validate_debt])
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150,
                            verbose_name='Название предприятия',
                            unique=True,
                            blank=False,
                            null=False,
                            help_text='Обязательное поле. Уникальное название предприятия'
                            )
    email = models.EmailField(verbose_name='Email',
                              blank=False,
                              help_text='Адрес электронной почты'
                              )
    country = models.CharField(max_length=150,
                               verbose_name='Страна',
                               blank=False,
                               )
    city = models.CharField(max_length=150,
                            verbose_name='Город',
                            blank=False,
                            )
    street = models.CharField(max_length=150,
                              verbose_name='Улица',
                              blank=False,
                              )
    house_number = models.CharField(max_length=150,
                                    verbose_name='Номер дома',
                                    blank=False, )

    product = models.CharField(max_length=200,
                               verbose_name='Название продукции',
                               blank=False, )
    product_model = models.CharField(max_length=100,
                                     verbose_name='Модель продукта',
                                     blank=False
                                     )
    product_release_date = models.DateField(verbose_name='Дата выхода продукта',
                                            validators=[validate_product_release_date])


    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'

    def __str__(self):
        return f"{self.get_level_display()}: {self.name}"
