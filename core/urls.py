from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    #admin auto added by material app no need to include it
    url(r'', include('material.frontend.urls')),
]
# urlpatterns += i18n_patterns(


# )
