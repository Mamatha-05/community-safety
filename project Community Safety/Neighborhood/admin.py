from django.contrib import admin

from .models import Safty_instruction,Report_issue

@admin.register(Safty_instruction)
class Safty_instructionAdmin(admin.ModelAdmin):
    list_display=['id','Title']
    
@admin.register(Report_issue)
class Report_issueAdmin(admin.ModelAdmin):
    list_display=['id','Incident']


