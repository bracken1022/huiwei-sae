

from weibo import *

from oauth_config import WEIBO_CONFIG

from flask import g


class SinaWeibo(object):
	"""docstring for SinaWeibo"""
	def __init__(self, app_key, app_secret, redirect_uri):
		self.app_key = app_key
		self.app_secret = app_secret
		self.redirect_uri = redirect_uri
		self.client = APIClient( app_key, app_secret, redirect_uri )

	def GetWeiboClient( self ):
		return self.client

	def LoginWeibo( self ):
		GetWeiboClient()
		return self.client.get_authorize_url()

	def GetAccessToken( self, code ):
		rec = self.client.request_access_token( code )
		self.client.set_access_token( rec.access_token, rec.expires_in )
		return rec.access_token

	def GetTimelineData( self ):
		content = self.client.statuses.user_timeline.get()
		return content


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