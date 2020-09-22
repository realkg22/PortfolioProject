from django.contrib import admin
from home_page.models import Owner, Education, Skills, WorkExperience, ProgrammingApplication, Project

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    pass

class EducationAdmin(admin.ModelAdmin):
    pass

class SkillsAdmin(admin.ModelAdmin):
    pass

class ProgrammingApplicationAdmin(admin.ModelAdmin):
    pass

class WorkExperienceAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(ProgrammingApplication, ProgrammingApplicationAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Project, ProjectAdmin)

