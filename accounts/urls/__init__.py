from django.urls import include, path

urlpatterns = [
    path(
        "auth/",
        include("accounts.urls.auth_urls"),
    ),
    path(
        "departments/",
        include("accounts.urls.department_urls"),
    ),

  
    path(
        "designations/",
        include("accounts.urls.designation_urls"),
    ),

    path(
        "permissions/",
        include("accounts.urls.permission_urls"),
    ),

    path(
        "roles/",
        include("accounts.urls.role_urls"),
    ),
    path(
        "employees/",
        include("accounts.urls.employee_urls"),
    ),



]