from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", default=0)


class SubTask(models.Model):
    subtask_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    summarized_text = models.TextField()
    bullet_text = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Dashboard(models.Model):
    dashboard_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="dashboard", default=0)


class DataVisualization(models.Model):
    visualization_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="data_visualization", default=0)
    types = models.CharField(max_length=255)
