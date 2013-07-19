from django.contrib import admin
import models

class BillAdmin(admin.ModelAdmin):
    pass

class BillStageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.BillStage, BillStageAdmin)
