from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=255, help_text="项目名称")
    project_img = models.CharField(max_length=255, help_text="项目图片")
    project_link = models.CharField(max_length=255, help_text="项目链接")
    # project_number = models.IntegerField(help_text="所属批次")

    def __str__(self):
        return f"{self.project_name}"
