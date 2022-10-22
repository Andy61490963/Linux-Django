from django.urls import path
from . import views

urlpatterns = [
    #path 自定義網址
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('info', views.all_info,name="all_infos"),
    path('add_information', views.add_information,name="add-information"), #分別對應網址後綴、views、html內容連結
    path('infoname_list', views.infoname_list,name="infoname-list"),
    path('show_information/<information_id>', views.show_information,name="show-information"),
    path('paper',views.all_paper, name="all_papers"),
    path('add_paper', views.add_paper,name="add-paper"),
    path('search_information', views.search_information,name="search-inofrmation"),
    path('update_information/<information_id>', views.update_information,name="update-information"),
    path('delete_information/<information_id>',views.delete_information, name="delete-information"),
    path('aboutus',views.aboutus, name="about-us"), #About me
    path('my_Portfolio',views.My_Portfolio, name="My-Portfolio") #My portfolio
]