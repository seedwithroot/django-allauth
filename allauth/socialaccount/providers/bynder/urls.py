from allauth.socialaccount.providers.oauth.urls import default_urlpatterns

from .provider import BynderOAuth2Provider

urlpatterns = default_urlpatterns(BynderOAuth2Provider)
