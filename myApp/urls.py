from django.urls import path
from . import views

app_name = "myApp"
urlpatterns = [
    path('view/', views.MyView.as_view(), name="view"),
    path('template_view/', views.BlogTemplateView.as_view(), name="template_view"),
    path('redirect_view/', views.BlogRedirectView.as_view(), name="redirect_view"),
    path('detail_view/<int:pk>/', views.BlogDetailView.as_view(), name="detail_view"),
    path('list_view/', views.BlogListView.as_view(), name="list_view"),
    path('form_view/', views.BlogFormView.as_view(), name="form_view"),
    path('create_view/', views.BlogCreateView.as_view(), name="create_view"),
    path('update_view/<int:pk>', views.BlogUpdateView.as_view(), name="update_view"),
    path('delete_view/<int:pk>', views.BlogDeleteView.as_view(), name="delete_view"),
    path("date_view/", views.BlogArchiveIndexView.as_view(), name="archive_index_view"),
    path("date_view/<int:year>/", views.BlogYearArchiveView.as_view(), name="year_archive_view"),
    path("date_view/<int:year>/<int:month>/", views.BlogMonthArchiveView.as_view(), name="month_archive_view"),
    path("date_view/<int:year>/<int:month>/<int:day>/", views.BlogDayArchiveView.as_view(), name="day_archive_view"),
    path("date_view/<int:year>/week/<int:week>/", views.BlogWeekArchiveView.as_view(), name="week_archive_view"),
    path("today/", views.BlogTodayArchiveView.as_view(), name="today_archive_view"),
    path("today/<int:pk>", views.BlogDateDetailView.as_view(), name="date_detail_view"),

]