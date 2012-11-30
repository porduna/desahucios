from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'webapp.views.index', name='index'),
    url(r'^line-chart/$', 'webapp.views.line_chart', name='line_chart'),
    url(r'^province/(\w+)$', 'webapp.views.province_json', name='province_json'),
    url(r'^province/(\w+)/(\w+)$', 'webapp.views.town_json', name='town_json'),
    url(r'^other_chart/$', 'webapp.views.other_chart', name='other_chart'),
    url(r'^focus_context/$', 'webapp.views.focus_context', name='focus_context'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)