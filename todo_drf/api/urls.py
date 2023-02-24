from . import views
from django.urls import path

urlpatterns=[
    path('', views.tasklist.as_view(), name="tasklist"),
	path('<int:id>', views.taskdetail.as_view(), name="taskdetail"),
]