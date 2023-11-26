from blogs.models import Categorias


def categorias_processor(request):
    categorias = Categorias.objects.all()
    return {
        'categorias': categorias
    }