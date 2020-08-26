from django.contrib import admin
from .models import Contact
from django.utils.html import format_html


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "name", "email",
                    "phone", "date", "actions_")
    list_display_links = ("title", "name", "email", "phone")
    list_per_page = 30

    def actions_(self, obj):
        return format_html('<a class="btn" href="/admin/contact/contact/{}/change/"><i class="fas fa-edit"></i></a> ' +
                           '<a class="btn" href="/admin/contact/contact/{}/delete/"><i class="far fa-trash-alt"></a>', obj.id, obj.id)


admin.site.register(Contact, ContactAdmin)
