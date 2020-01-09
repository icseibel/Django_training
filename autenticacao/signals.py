from django.db.models.signals import post_save
from django.dispatch import receiver
from lancamento.models import Lancamento
from .models import RegistroMovimento


@receiver(post_save, sender=Lancamento)
def update_registro(sender, instance, created,**kwargs):
    if created:
        RegistroMovimento.objects.create(id_objeto=instance.id,
                                         processo='Lançamento',
                                         valor=instance.valor)