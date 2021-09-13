from django.urls import path
from django.contrib import admin
from ninja import NinjaAPI

api = NinjaAPI(urls_namespace="api", docs_url="/docs/")

urlpatterns = [

    path("", api.urls),

]
