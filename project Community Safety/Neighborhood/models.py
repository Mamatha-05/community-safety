from django.db import models
from django.contrib.auth.models import User
class Safty_instruction(models.Model):
    Title=models.TextField()
    Details=models.TextField()
    Instruction_pass_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Title
class Report_issue(models.Model):
    Report_by=models.ForeignKey(User, on_delete=models.CASCADE)
    Incident=models.TextField()
    Location=models.TextField()
    Description=models.TextField()
    Date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Incident
    