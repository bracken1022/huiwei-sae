

from weibo import *

from oauth_config import WEIBO_CONFIG

from flask import g

def GetWeiboClient():
	client = APIClient( app_key = WEIBO_CONFIG['APP_KEY'], app_secret = WEIBO_CONFIG['APP_SECRET'], 
		redirect_uri = WEIBO_CONFIG['REDIRECT_URI'] )
	return client

def loginWeibo():
	client = GetWeiboClient()

	return client.get_authorize_url()

def getAccessToken( code ):
	client = GetWeiboClient()
	rec = client.request_access_token( code )
	client.set_access_token(rec.access_token, rec.expires_in)
	content = client.statuses.user_timeline.get()
	return content