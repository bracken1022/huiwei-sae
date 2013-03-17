
from qqweibo import APIClient

from oauth_config import QQ_CONFIG




def GetClient():
    client = APIClient( QQ_CONFIG['APP_KEY'], QQ_CONFIG['APP_SECRET'], redirect_uri=QQ_CONFIG['REDIRECT_URI'] )
    return client

def loginQq():
    client = GetClient()
    return client.get_authorize_url()

def getQQAccessToken( code, open_id ):
    client = GetClient()
    rec = client.request_access_token( code )
    client.set_access_token(rec.access_token, open_id, rec.expires_in)
    content = client.get.statuses__home_timeline()
    return content