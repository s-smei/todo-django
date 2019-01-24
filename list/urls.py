from django.conf.urls import url

from .views import todo_show, add_task, todo_delete, add_todo


urlpatterns = [
    url(r'show/(?P<id>\d+)/$',
        todo_show,
        name='list_todo_show'),
    url(r'add$',
        add_todo,
        name='list_add_todo'),
    url(r'add/task/(?P<id>\d+)',
        add_task,
        name="list_add_task"),
    url(r'delete/(?P<id>\d+)',
        todo_delete,
        name="list_todo_delete"),
]
