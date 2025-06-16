from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add, name="add"),
    path("update/<int:pk>/", mytodo.update, name="update"),
    path("delete/<int:pk>/", mytodo.delete, name="delete"),
    path(
        "update_task_complete/",
        mytodo.update_task_complete,
        name="update_task_complete",
    ),
]
