from django.shortcuts import render, get_object_or_404

from .models import Inmueble,InmuebleImage
def inmueble_view(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmueble.html', {'inmuebles':inmuebles})

def detalle_view(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    #Va a filtrar un inmueble en particular
    fotos = InmuebleImage.objects.filter(inmueble=inmueble)
    return render(request, 'detalle.html', {
        'inmueble':inmueble,
        'fotos':fotos
    })