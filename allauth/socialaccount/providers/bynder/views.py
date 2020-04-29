from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
import requests

from .provider import BynderOAuth2Provider



class BynderOAuth2Adapter(OAuth2Adapter):
    bynder_domain = ""
    provider_id = BynderOAuth2Provider.id
    access_token_url = 'https://{}/v6/authentication/oauth2/{}'.format(
        bynder_domain, 'token')
    authorize_url = 'https://{}/v6/authentication/oauth2/{}'.format(
        bynder_domain, 'auth')
    profile_url = 'https://api.Bynder.com/1/account/info'
    redirect_uri_protocol = 'https'

    def complete_login(self, request, app, token, **kwargs):
        extra_data = requests.get(self.profile_url, params={
            'access_token': token.token
        })

        # This only here because of weird response from the test suite
        if isinstance(extra_data, list):
            extra_data = extra_data[0]

        return self.get_provider().sociallogin_from_response(
            request,
            extra_data.json()
        )


oauth_login = OAuth2LoginView.adapter_view(BynderOAuth2Adapter)
oauth_callback = OAuth2CallbackView.adapter_view(BynderOAuth2Adapter)
