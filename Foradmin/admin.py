from django.contrib import admin
from .models import *
admin.site.register(Users)
admin.site.register(puzzle_question)
admin.site.register(puzzle_answers)
admin.site.register(entry_questions)
admin.site.register(entry_answers)
admin.site.register(middle_questions)
admin.site.register(middle_answers)
admin.site.register(high_questions)
admin.site.register(high_answers)
# admin.site.register(AdminUser)