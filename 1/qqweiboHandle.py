
from qqweibo import APIClient

from oauth_config import QQ_CONFIG


class QqWeibo(object):
    """docstring for QqWeibo"""
    def __init__(self, app_key = "", app_secret = "", redirect_uri = "" ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.redirect_uri = redirect_uri

    def CreateClient( self, app_key, app_secret, redirect_uri ):
        self.client = APIClient( app_key, app_secret, redirect_uri = redirect_uri )
        return self.client

    def LoginToQq( self ):
        client = self.CreateClient( self.app_key, self.app_secret, self.redirect_uri )
        return client.get_authorize_url()

    def GetQqAccessToken( self, code, open_id ):
        client = self.CreateClient( self.app_key, self.app_secret, self.redirect_uri )
        recived = self.client.request_access_token( code )
        self.client.set_access_token( recived.access_token, open_id, recived.expires_in )
        return recived.access_token

    def GetClient( self ):
        return self.client
        
        
        