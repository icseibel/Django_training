from django.contrib import admin
from .models import Lancamento, TipoLancamento, Receita
# Register your models here.

admin.site.register(Lancamento)
admin.site.register(TipoLancamento)
admin.site.register(Receita)
