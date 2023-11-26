from django import forms 

from blogs.models import Comment, Post




class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label='Ingrese su comentario')

    class Meta:
        model = Comment
        fields = ['content']
        
class NuevoPost(forms.ModelForm):
    pass
    
    class Meta:
        model = Post  # Modelo del cual importa
        fields = [
            'titulo',
            'slug',
            'descripcion',
            'contenido',
            'autor',
            'categorias',
            'destacado',
            'image',
            'pub_date',
            
            ]
        #  Widget para agrandar el area de texto(TextField) a 80 columnas
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}