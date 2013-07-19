from django.contrib import admin
import models

class BillAdmin(admin.ModelAdmin):
    pass

class BillStageAdmin(admin.ModelAdmin):
    pass

class GovInfoScraperAdmin(admin.ModelAdmin):
    list_display = ('bill_name', 'bill_code', 'comment_startdate', 'comment_enddate', 'reviewed') 
    list_filter = ('reviewed',) 

admin.site.register(models.GovInfoScraper, GovInfoScraperAdmin)
admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.BillStage, BillStageAdmin)
