'''
django admin pages for courseware model
'''

from courseware.models import StudentModule, OfflineComputedGrade, OfflineComputedGradeLog
from ratelimitbackend import admin

from django.db.models import Count, Avg

class StudentModuleAdmin(admin.ModelAdmin):
    # https://www.elements.nl/2015/03/16/getting-the-most-out-of-django-admin-filters/
    # form = FlatpageForm
    # fieldsets = (
    #     (None, {'fields': ('url', 'title', 'content', 'sites')}),
    #     (_('Advanced options'), {'classes': ('collapse',),
    #     'fields': ('enable_comments', 'registration_required', 'template_name')}),
    # )
    list_display = ('course_id', 'module_type', 'student',
                    #'grade', 'max_grade', 'created', 'modified', 'num_grades_count',
                     'course_id_offering', 'module_state_key2')
    list_filter = ('module_type',)
    search_fields = ('course_id', 'student__email')

    def course_id_offering(self, obj):
        return "%s" % obj.course_id.offering

    def module_state_key2(self, obj):
        return ("%s" % obj.module_state_key).split('+type@')[0]


    def queryset(self, request):
        qs = super(StudentModuleAdmin, self).queryset(request)
        return qs.annotate(num_grades=Count('grade'))

    def num_grades_count(self, obj):
        return obj.student.email

    num_grades_count.short_description = 'Fixture Count'
    num_grades_count.admin_order_field = 'num_fixture_metas'
    #
    # def aget_username(self, obj):
    #     return obj.result.runner.agegroup


admin.site.register(StudentModule, StudentModuleAdmin)

admin.site.register(OfflineComputedGrade)

admin.site.register(OfflineComputedGradeLog)
