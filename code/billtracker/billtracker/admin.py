from django.contrib import admin
import models

class GovInfoScraperAdmin(admin.ModelAdmin):
    pass

class BillStageAdmin(admin.ModelAdmin):
    pass

class BillAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.GovInfoScraper, GovInfoScraperAdmin)
admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.BillStage, BillStageAdmin)
