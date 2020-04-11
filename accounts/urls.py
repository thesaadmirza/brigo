
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from accounts.views import views


# app_name = "organizations"

urlpatterns = [
    url(
        r"^$",
        view=login_required(views.OrganizationList.as_view()),
        name="organization_list",
    ),
    url(
        r"^add/$",
        view=login_required(views.AccountCreate.as_view()),
        name="account_add",
    ),
    url(
        r"^(?P<organization_pk>[\d]+)/",
        include(
            [
                url(
                    r"^$",
                    view=login_required(views.OrganizationDetail.as_view()),
                    name="organization_detail",
                ),
                url(
                    r"^edit/$",
                    view=login_required(views.OrganizationUpdate.as_view()),
                    name="organization_edit",
                ),
                url(
                    r"^delete/$",
                    view=login_required(views.OrganizationDelete.as_view()),
                    name="organization_delete",
                ),
                url(
                    r"^people/",
                    include(
                        [
                            url(
                                r"^$",
                                view=login_required(
                                    views.OrganizationUserList.as_view()
                                ),
                                name="organization_user_list",
                            ),
                            url(
                                r"^add/$",
                                view=login_required(
                                    views.OrganizationUserCreate.as_view()
                                ),
                                name="organization_user_add",
                            ),
                            url(
                                r"^(?P<user_pk>[\d]+)/remind/$",
                                view=login_required(
                                    views.OrganizationUserRemind.as_view()
                                ),
                                name="organization_user_remind",
                            ),
                            url(
                                r"^(?P<user_pk>[\d]+)/$",
                                view=login_required(
                                    views.OrganizationUserDetail.as_view()
                                ),
                                name="organization_user_detail",
                            ),
                            url(
                                r"^(?P<user_pk>[\d]+)/edit/$",
                                view=login_required(
                                    views.OrganizationUserUpdate.as_view()
                                ),
                                name="organization_user_edit",
                            ),
                            url(
                                r"^(?P<user_pk>[\d]+)/delete/$",
                                view=login_required(
                                    views.OrganizationUserDelete.as_view()
                                ),
                                name="organization_user_delete",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
