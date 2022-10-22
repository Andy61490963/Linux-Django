from django.contrib import admin
from .models import information
from .models import Interest
from .models import paper
from .models import all_aboutus
from .models import Portfolio
from .models import homepost

#admin.site.register(information)
admin.site.register(Interest)

@admin.register(homepost)
class homepost(admin.ModelAdmin):
    list_display = ('postname','introduction','post_date')

@admin.register(information)
class informationAdmin(admin.ModelAdmin):
    #Database 選擇性預覽內容
    list_display = ('name','introduction','refresh_date')
    #Database 上下排序根據
    #ordering = ('name')
    #Database search tool
    search_fields = ('name', 'address')

@admin.register(paper)
class paper(admin.ModelAdmin):
    list_display = ('papername','papercontent','image')
    
@admin.register(all_aboutus)
class all_aboutus(admin.ModelAdmin):
    list_display = ('experience','content','image')
    
@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('title','content','image')