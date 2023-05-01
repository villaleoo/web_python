from django import forms
from articles.models import Articles

class FormEditArticle(forms.ModelForm):
    CHOICES=(('politica', 'politica'), ('economia', 'economia'), ('psicologia', 'psicologia'), ('filosofia', 'filosofia'))
    titulo= forms.CharField(max_length=60)
    subtitulo= forms.CharField(max_length=100)
    contenido=forms.CharField(widget=forms.Textarea(attrs={'name':'contenido', 'rows':10, 'cols':50}))
    categoria=forms.ChoiceField(choices=CHOICES) ##aqui no esta funcionando, el select no guarda en la BBDD la opcion correspondiente
    class Meta:
        model=Articles
        fields=['titulo', 'subtitulo', 'contenido', 'categoria']

class CreateNewArticleForm(FormEditArticle):
    ...
   
    
class ModifyArticleForm(FormEditArticle):
    ...
    
class SearchArticles(forms.Form):
    titulo=forms.CharField(max_length=60)
    