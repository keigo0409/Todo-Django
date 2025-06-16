from django.shortcuts import render
from django.views import View
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect


class IndexView(View):
    def get(self, request):
        filter = request.GET.get("filter")

        if filter == "complete":
            todo_list = Task.objects.filter(complete=True).order_by("end_date")
        elif filter == "incomplete":
            todo_list = Task.objects.filter(complete=False).order_by("end_date")
        else:
            todo_list = Task.objects.all().order_by("complete", "end_date")

        context = {
            "todo_list": todo_list,
            "filter": filter,
        }

        return render(request, "mytodo/index.html", context)


index = IndexView.as_view()


class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        # 入力データをフォームに格納
        form = TaskForm(request.POST)
        # 誤りがないかチェック
        is_valid = form.is_valid()
        # バリデーションチェック
        if is_valid:
            # モデルを保存
            form.save()
            return redirect("/")
        return render(request, "mytodo/add.html", {"form": form})


add = AddView.as_view()


class TaskUpdateView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        return render(request, "mytodo/update.html", {"form": form, "task": task})

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "mytodo/update.html", {"form": form, "task": task})


update = TaskUpdateView.as_view()


class TaskDeleteView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        return render(request, "mytodo/delete.html", {"task": task})

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect("/")


delete = TaskDeleteView.as_view()


class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect("/")


update_task_complete = Update_task_complete.as_view()
