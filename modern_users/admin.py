from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from modern_users.models import ModernUsers

class ModernUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'age',
                    'birthday',
                    'address',
                    'city',
                    'zipcode',
                ),
            },
        ),
    )
admin.site.register(ModernUsers, ModernUserAdmin)
