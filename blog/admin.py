from django.contrib import admin
from blog.models import post,tag,Author
# Register your models here.

class PostAdmin(admin.ModelAdmin):
			prepopulated_fields = {"slug": ("title",)}

admin.site.register(post,PostAdmin)
admin.site.register(tag)
admin.site.register(Author)
