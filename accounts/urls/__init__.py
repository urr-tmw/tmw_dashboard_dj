from django.urls import include, path

urlpatterns = [

    path(
        "departments/",
        include("accounts.urls.department_urls"),
    ),

    # Coming Next
    # path(
    #     "designations/",
    #     include("accounts.urls.designation_urls"),
    # ),

    # path(
    #     "employees/",
    #     include("accounts.urls.employee_urls"),
    # ),

    # path(
    #     "auth/",
    #     include("accounts.urls.auth_urls"),
    # ),
]