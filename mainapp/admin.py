from django.contrib import admin
from mainapp import models as mainapp_models
from django.utils.translation import gettext_lazy as _


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preamble", "body"]


@admin.register(mainapp_models.Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    list_per_page = 5
    list_filter = ["course", "created_at", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name
    
    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "get_courses"]
    list_select_related = True
    
    def get_courses(self, obj):
        return ", ".join((i.name for i in obj.course.all()))
    
    get_courses.short_description = _("Courses")