from django.contrib import admin
from campus.models import *
# from django_object_actions import DjangoObjectActions
from django.utils.safestring import mark_safe
from django.core.mail import (send_mail, BadHeaderError, EmailMessage)
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
import threading



admin.site.register(stu_details)

# admin.site.register(dept_details)
# admin.site.register(Student_Details)
admin.site.register(comp_details)
admin.site.register(job_pos)
admin.site.register(applied_jobs)
admin.site.register(Quiz)

class AnswerInLine(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
    
admin.site.register(Marks_Of_User)
admin.site.register(Offer_letter)

# class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
#     def import(modeladmin, request, queryset):
#         print("Import button pushed")

#     changelist_actions = ('import', )

# class View(admin.ModelAdmin):
#     view = 'campus/view.html'

admin.site.register(Java)
admin.site.register(CN)
admin.site.register(OS)
admin.site.register(ALGO)
admin.site.register(OTHER)
admin.site.register(C)
admin.site.register(DBMS)
admin.site.register(DS)

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(
                self.subject,
                self.html_content,
                settings.EMAIL_HOST_USER,
                self.recipient_list
        )
        msg.content_subtype = "html"
        try:
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

class BroadCast_Email_Admin(admin.ModelAdmin):
    model = BroadCast_Email

    def submit_email(self, request, obj):
        # `obj` is queryset, so there we only 
        # use first selection, exacly obj[0]

        # this for exception: `if p.email != settings.EMAIL_HOST_USER`
        list_email_user = [ p.email for p in User.objects.all() ]
        obj_selected = obj[0]
        EmailThread(
            obj_selected.subject,
            mark_safe(obj_selected.message), 
            list_email_user
        ).start()

    submit_email.short_description = 'Submit BroadCast (1 Select Only)'
    submit_email.allow_tags = True

    actions = [ 'submit_email' ]
    list_display = ("subject", "created")
    search_fields = ['subject',]


admin.site.register(BroadCast_Email, BroadCast_Email_Admin)