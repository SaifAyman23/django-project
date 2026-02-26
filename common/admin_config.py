from django.contrib.admin import AdminSite
from django.urls import path
from unfold.admin import UnfoldAdminSite

class CustomAdminSite(UnfoldAdminSite):
    site_header = "Project Administration"
    site_title = "Project Admin"
    index_title = "Welcome to Project Admin"

admin_site = CustomAdminSite(name='custom_admin')