from django.contrib import admin
import models

class BillAdmin(admin.ModelAdmin):
    pass

class BillStageAdmin(admin.ModelAdmin):
    pass

class PreparliamentaryStageAdmin(admin.ModelAdmin):
    pass

class ParliamentIntroductionAdmin(admin.ModelAdmin):
    pass

class ParliamentPortfolioCommitteeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.BillStage, BillStageAdmin)
admin.site.register(models.PreparliamentaryStage, PreparliamentaryStageAdmin)
admin.site.register(models.ParliamentIntroduction, ParliamentIntroductionAdmin)
admin.site.register(models.ParliamentPortfolioCommittee, ParliamentPortfolioCommitteeAdmin)
