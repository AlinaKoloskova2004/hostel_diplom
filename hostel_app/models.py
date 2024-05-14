from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Guest(models.Model):
    name  = models.CharField(max_length=20,verbose_name="ФИО")
    age   = models.IntegerField(default=20, verbose_name="Возраст")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    score = models.IntegerField(default=20, verbose_name="Номер счёта")

    def __str__(self) -> str:
        return self.name
    

class Room(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(blank=False, verbose_name="Описание")
    price = models.FloatField(default=1000.0, verbose_name="Цена")
    is_booked = models.BooleanField(default=False, verbose_name="Есть в книге?")
    img = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение") 
    bed = models.IntegerField(default=1, verbose_name='Кровать кол-во')
    bath = models.IntegerField(default=1, verbose_name='Душ кол-во')
    hottest = models.BooleanField(default=False, verbose_name='Является горячим предложением')

    def __str__(self):
        return self.name

class Booking(models.Model):
    status_choices = (
              ('ожидание', 'Ожидание'),
              ('подтверждено', 'Подтверждено'),
              ('отменено', 'Отменено'),
        )
    name  = models.CharField(max_length=40,verbose_name="ФИО")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    room          = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Номер")
    num_of_guest  = models.IntegerField(default=1, verbose_name="Кол-во взрослых")
    num_of_child  = models.IntegerField(default=1, verbose_name="Кол-во детей")
    checkin_date  = models.DateTimeField(default=timezone.now, verbose_name="Дата заселения")
    checkout_date = models.DateTimeField(default=timezone.now, verbose_name="Дата выселения")
    status = models.CharField(max_length=255, verbose_name='Статус', choices=status_choices, default='ожидание')
    is_checkout   = models.BooleanField(default=True, verbose_name="Проверено")
    services   = models.BooleanField(default=True, verbose_name="Доп.услуги")

    def __str__(self) -> str:
        return self.name
   
    
class Images(models.Model):
    model_img = models.ImageField(upload_to='static/images')
    
    
class Staff(models.Model):
    name  = models.CharField(max_length=200,verbose_name="ФИО")
    img = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение") 
    data = models.DateField( verbose_name="Дата рождения")
    passport =  models.CharField(max_length=10,verbose_name="Паспортные данные")
    address =  models.CharField(max_length=100,verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    post =  models.CharField(max_length=100,verbose_name="Должность")
    login =  models.CharField(max_length=100,verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    
    def __str__(self) -> str:
        return self.name
    
class Duty(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Сотрудник")
    day = models.CharField(max_length=11,verbose_name="День недели")


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    data = models.DateField()
    
    
