from django.contrib import admin
from django.urls import path, include
from main.views import HomeView, consent, daily_emails, autologin, logout_user, take_survey, FaqView, VisionView, \
    AboutView, DataView, TeamView, set_language_custom, delete_all_openhuman_files, delete_all

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("autologin/<int:oh_id>/", autologin, name="autologin"),
    path("consent/", consent, name="consent"),
    path("daily_emails/", daily_emails, name="daily_emails"),
    path("logout/", logout_user, name="logout"),
    path("survey/", take_survey, name="take_survey"),
    path("team/", TeamView.as_view(), name="team"),
    path("faq/", FaqView.as_view(), name="faq"),
    # path("vision/", VisionView.as_view(), name="vision"),
    path("about/", AboutView.as_view(), name="about"),
    path("data/", DataView.as_view(), name="data"),

    path("delete-all-openhuman-files/", delete_all_openhuman_files, name="delete_all_openhuman_files"),
    path("delete-all/", delete_all, name="delete_all"),

    path("i18n/", set_language_custom, name="set_language_custom"),
]

urlpatterns += [path("openhumans/", include("openhumans.urls"))]
