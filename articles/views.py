from django.shortcuts import render, redirect
from articles.models import Articles
from articles.forms import CreateNewArticleForm, SearchArticles, ModifyArticleForm

def get_last_articles(request):
    
    title_search= request.GET.get('titulo', None)
    
    if (title_search):
        articles=Articles.objects.filter(titulo__icontains=title_search)
    else:
        articles= Articles.objects.all()
        
    form_search= SearchArticles()
    
    return render(request, r'index.html', {'arts': articles,'form': form_search})


def create_new_article(request):
    
   
    if(request.method == 'POST'):  
        form= CreateNewArticleForm(request.POST)
        if(form.is_valid()):
            data_cleaned= form.cleaned_data
            
            new_article= Articles(titulo=data_cleaned['titulo'], subtitulo=data_cleaned['subtitulo'], contenido=data_cleaned['contenido'], cat=data_cleaned['categoria']);
            new_article.save()
            
            return redirect("article:home")
    
    form= CreateNewArticleForm()
    
    
    return render(request,r'creator_article.html', {'form': form} )

def delete_article(request, id_article):
    art_deleted= Articles.objects.get(id=id_article)
    art_deleted.delete()
    
    return redirect('article:home')

def modify_article(request, id_article):
    art_modify=Articles.objects.get(id=id_article)
    
    if(request.method == "POST"):
        form= ModifyArticleForm(request.POST)
        
        if(form.is_valid()):
            data_clean=form.cleaned_data
            art_modify.titulo= data_clean['titulo']
            art_modify.subtitulo= data_clean['subtitulo']
            art_modify.contenido= data_clean['contenido']
            art_modify.categoria= data_clean['categoria']
            art_modify.save()
            return redirect('article:home')
        else:
            return render(request, 'modify_article.html', {'form':form,'id':id_article})
    
    form= ModifyArticleForm(initial={'titulo':art_modify.titulo, 'subtitulo':art_modify.subtitulo, 'contenido':art_modify.contenido, 'categoria':art_modify.cat})
    return render(request, 'modify_article.html', {'form':form,'id':id_article})

def get_article(request, id_article):
    article= Articles.objects.get(id=id_article)
    
    return render(request, r'article_layout.html', {'article_details': article})

