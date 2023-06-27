from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # host(r'api', settings.ROOT_URLCONF, name='api'),
    host(r'live', 'linky.hostsconf.urls', name='live'),
    host(r'(?!www).*', 'linky.hostsconf.urls', name='wildcard'),
)