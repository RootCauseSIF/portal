from django.conf.urls import patterns, include, url
import forms_builder.forms.urls
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from snapp.views import index, faq
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rootcause.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', 'snapp.views.index', name='index'), # todo: change to include all from snapp
    url(r'^admin_application_dashboard/', 'snapp.views.admin_application_dashboard', name='admin_application_dashboard'),
    url(r'^evaluation_dashboard/', 'snapp.views.evaluation_dashboard', name='evaluation_dashboard'),
    url(r'^evaluations/form/([0-9]+)', 'snapp.views.evaluation_form', name='evaluation_form'),
    url(r'^track/([0-9]+)/application/', 'snapp.views.application', name='application'),
    url(r'^submitted_form_entries/([0-9]+)', 'snapp.views.submitted_form_entry', name='submitted_form_entry'),
    # url(r'^submitted_form_entries/track([0-9]+)', 'snapp.views.form_entries_by_track', name='form_entries_by_track'),
    url(r'^index/', index, name="index"),
    url(r'^faq/', faq, name="faq"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
