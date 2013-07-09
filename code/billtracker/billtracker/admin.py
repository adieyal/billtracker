from django.contrib import admin
import models

class GovInfoScraperAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.GovInfoScraper, GovInfoScraperAdmin)
