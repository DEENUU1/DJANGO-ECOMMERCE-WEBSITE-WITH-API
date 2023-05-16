from django.contrib import admin
from .models import Contact
from import_export.admin import ExportActionMixin


# Registering contact model for admin.
# In admin panel it's displaying subject, email and date of contact sent.
# I used import_export django library it allows to download all data
# In the admin panel you can choose Action
# Export selected contacts -> allows to download chosen data
# Delete selected contacts -> allows to delete chosen data


@admin.register(Contact)
class ContactAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["subject", "email", "sent_date"]
    list_filter = ["subject", "sent_date"]
