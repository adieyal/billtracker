from django.contrib import admin
import models

class GovInfoScraperAdmin(admin.ModelAdmin):
    list_display = ('bill_name', 'bill_code', 'comment_startdate', 'comment_enddate', 'reviewed') 
    list_filter = ('reviewed',) 

    actions = ['convert_to_bill']

    # TODOS
    # Perhaps not allow for changing the value of reviewed
    # Perhaps send a user message to inform that some already converted items were not converted
    # Test this?
    def convert_to_bill(self, request, queryset):
        for item in queryset.filter(reviewed=False):
            item.convert_to_bill()
    convert_to_bill.short_description = "Convert scraped items to bills"

class BillsBeforeParliamentScraperAdmin(admin.ModelAdmin):
    list_display = ('bill_name', 'bill_code', 'introduced_by', 'date_introduced', 'bill_stage', 'reviewed') 
    list_filter = ('reviewed', 'bill_stage') 
    actions = ['convert_to_bill']

    def convert_to_bill(self, request, queryset):
        for item in queryset.filter(reviewed=False):
            item.convert_to_bill()
    convert_to_bill.short_description = "Convert scraped items to bills"

admin.site.register(models.GovInfoScraper, GovInfoScraperAdmin)
admin.site.register(models.BillsBeforeParliamentScraper, BillsBeforeParliamentScraperAdmin)
