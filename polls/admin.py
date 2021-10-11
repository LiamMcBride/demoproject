from django.contrib import admin

from .models import Question, Choice
from django.utils import timezone
import datetime

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', "pub_date", "was_published_recently")

    # @admin.display(
    #     boolean = True,
    #     ordering = 'pub_date',
    #     description = 'Published recently?',
    # )
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now


admin.site.register(Question, QuestionAdmin)
