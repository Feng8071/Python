from django.contrib import admin

from .models import Question,Choice

# Register your models here.

# user-defined worksheet

# sample date question location moving
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#class ChoiceInline(admin.StackedInline): # 竖着排列
class ChoiceInline(admin.TabularInline):  # 横在排列
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Data information',{'fields':['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text'] #搜索

admin.site.register(Question, QuestionAdmin)

#admin.site.register(Question)
#admin.site.register(Choice)
