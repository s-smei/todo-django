from django.conf.urls import url

from .views import todo_show, add_task, todo_delete, add_todo
from .views import task_delete, task_change_status

urlpatterns = [
    url(r'(?P<id>\d+)/show$',
        todo_show,
        name='list_todo_show'),
    url(r'add$',
        add_todo,
        name='list_add_todo'),
    url(r'(?P<id>\d+)/add/task$',
        add_task,
        name="list_add_task"),
    url(r'(?P<id>\d+)/delete$',
        todo_delete,
        name="list_todo_delete"),
    url(r'(?P<id>\d+)/task/delete$',
        task_delete,
        name='list_task_delete'),
    url(r'(?P<id>\d+)/task/change/status$',
        task_change_status,
        name='list_task_change_status')
]
