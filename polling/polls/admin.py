from django.contrib import admin

from .models import Question,Choice

admin.site.site_header = "Polling Admin"
admin.site.site_title = "Polling Admin Area"
admin.site.site_index_title = "Welcome to the Polling Admin area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
                 ('Date Information', {'fields' : ['pub_date'], 'classes':
                 ['collapse']}), ]
    inlines = [ChoiceInLine]

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

