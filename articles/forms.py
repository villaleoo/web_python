from django import forms

class FormEditArticle(forms.Form):
    CHOICES=(('politica', 'politica'), ('economia', 'economia'), ('psicologia', 'psicologia'), ('filosofia', 'filosofia'))
    titulo= forms.CharField(max_length=60)
    subtitulo= forms.CharField(max_length=100)
    contenido=forms.CharField(widget=forms.Textarea(attrs={'name':'contenido', 'rows':10, 'cols':50}))
    categoria=forms.ChoiceField(choices=CHOICES) 

class CreateNewArticleForm(FormEditArticle):
    ...
    
class ModifyArticleForm(FormEditArticle):
    ...
    
class SearchArticles(forms.Form):
    titulo=forms.CharField(max_length=60)
    