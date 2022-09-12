from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.http import *
from .models import Books
from django.contrib.auth.models import User
from .forms import Addbook_form


def base(HttpRequest):
    data = Books.objects.all()
    return render(HttpRequest, 'home.html', context={'data': data})


class ArticleDetailView(DetailView):
    model = Books
    template_name = 'article_details.html'


# class base(ListView):
#     model = Books
#     template_name = 'base.html'

class CreateForm:
    pass


class AddBook(CreateView):
    model = Books
    form_class = Addbook_form
    template_name = 'add_post.html'

    def post(self, request, *args, **kwargs):
        DBsave = dict(QueryDict.copy(request.POST))  # Получаем запроc в Dict вместо QueryDict
        DBsave = {k: v[0] for k, v in DBsave.items()}  # Убираем у Value тип list
        DBsave['Create_id'] = DBsave.pop('Create')  # Меняем поле Create на Create_id
        DBsave.pop('csrfmiddlewaretoken')  # Удаляем лишнее поле которого нет в таблице Library_books
        DBsave['Create_id'] = User.objects.get(last_name='Dmitriy').id  # Получем ID ссылку из таблицы auth_user
        Book = Books.objects.create(**DBsave)  # Сохраняем в базу через перменную Book она нужна для возврата ID номера

        # form = Addbook_form(request.POST)
        # book = form.save()
        # book.save()

        return HttpResponseRedirect(reverse_lazy('article-detail', args=[Book.id]))
        # return render(request, self.template_name, {'form': form})

# def AddBook(request):
#     form = Addbook_form
#     context = {'form': form}
#     return render(request, 'add_post.html', context)
