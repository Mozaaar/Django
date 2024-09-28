from django.contrib import admin
from .models import Cliente
from .models import Envio
from .models import Realiza
from .models import Factura
from .models import Paquete
from .models import Envio_paq
from .models import Transportista
from .models import Sucursal
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Envio)
admin.site.register(Realiza)
admin.site.register(Factura)
admin.site.register(Paquete)
admin.site.register(Envio_paq)
admin.site.register(Transportista)
admin.site.register(Sucursal)