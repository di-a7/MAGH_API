from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail

@receiver(post_save, sender=Order)
def notify(sender, instance, created, **kwargs):
   print("New order has been created.")
   
   send_mail(
      "New Order",
      "New Order has been created.",
      "demo@gmail.com",
      ['a@gmail.com'],
      fail_silently = True 
   )