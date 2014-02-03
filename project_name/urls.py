from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
import os.path

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailimages import urls as wagtailimages_urls
from wagtail.wagtailembeds import urls as wagtailembeds_urls
from wagtail.wagtaildocs import admin_urls as wagtaildocs_admin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsnippets import urls as wagtailsnippets_urls
from wagtail.wagtailsearch.urls import frontend as wagtailsearch_frontend_urls, admin as wagtailsearch_admin_urls
from wagtail.wagtailusers import urls as wagtailusers_urls
from wagtail.wagtailredirects import urls as wagtailredirects_urls

admin.autodiscover()


# Signal handlers
from wagtail.wagtailsearch import register_signal_handlers as wagtailsearch_register_signal_handlers
wagtailsearch_register_signal_handlers()


urlpatterns = patterns('',
    url(r'^django-admin/', include(admin.site.urls)),

    # TODO: some way of getting wagtailimages to register itself within wagtailadmin so that we
    # don't have to define it separately here
    url(r'^admin/images/', include(wagtailimages_urls)),
    url(r'^admin/embeds/', include(wagtailembeds_urls)),
    url(r'^admin/documents/', include(wagtaildocs_admin_urls)),
    url(r'^admin/snippets/', include(wagtailsnippets_urls)),
    url(r'^admin/search/', include(wagtailsearch_admin_urls)),
    url(r'^admin/users/', include(wagtailusers_urls)),
    url(r'^admin/redirects/', include(wagtailredirects_urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_frontend_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += patterns('',
        (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'demo/images/favicon.ico'))
    )
