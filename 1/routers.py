
from flask import Flask, g, request, redirect, render_template, Response, session, url_for, jsonify

import urllib2

from oauth_config import QQ_CONFIG

import simplejson as json

from weiboHandle import *
from qqweiboHandle import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/wang/bracken/3yX R~XHH!jmN]LWX/,?RT'


class JsonObject(dict):
    '''
    general json object that can bind any fields but also act as a dict.
    '''
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value

def _obj_hook(pairs):
    '''
    convert json object to python object.
    '''
    o = JsonObject()
    for k, v in pairs.iteritems():
        o[str(k)] = v
    return o


@app.route('/')
def home_page():
    return render_template( 'home_page.html', content = 'hello world' )
    
@app.route('/login_to_weibo')
def login_to_weibo():
    sinaWeibo = SinaWeibo( WEIBO_CONFIG['APP_KEY'], WEIBO_CONFIG['APP_SECRET'], WEIBO_CONFIG['REDIRECT_URI'] )
    url = sinaWeibo.LoginWeibo()
    return redirect( url )
    #return jsonify( content_weibo = "weibo here")

@app.route('/oauth_weibo', methods = ['POST', 'GET'])
def oauth_weibo():
    if request.method == "GET":
        code = request.args.get("code")
        session['weibo_code'] = code

        sinaWeibo = SinaWeibo( WEIBO_CONFIG['APP_KEY'], WEIBO_CONFIG['APP_SECRET'], WEIBO_CONFIG['REDIRECT_URI'] )
        session['weibo_access_token'] = sinaWeibo.GetAccessToken( code )
        content = sinaWeibo.GetTimelineData()
        return render_template( 'home_page.html', content_weibo = content.statuses )

@app.route('/ajax_weibo_data')
def ajax_weibo_data():
    access_token = session['weibo_access_token']
    url_str = "https://api.weibo.com/2/statuses/public_timeline.json?access_token=%s" %access_token
    
    try:
        resp = urllib2.urlopen(urllib2.Request( url_str ) )
        body = resp.read()
        content_weibo = json.loads( body, object_hook = _obj_hook  )
        content_weibo = content_weibo.statuses
        
    except urllib2.HTTPError, e:
        body = e.read()

    return jsonify( content_weibo = content_weibo )


@app.route('/login_to_qq')
def login_to_qq():
    qqWeibo = QqWeibo( QQ_CONFIG['APP_KEY'], QQ_CONFIG['APP_SECRET'], QQ_CONFIG['REDIRECT_URI'])
    return redirect( qqWeibo.LoginToQq() )
    #return jsonify( content_qq = "qq here")

@app.route('/oauth_qq', methods = ['POST', 'GET'])
def oauth_qq():
    if request.method == "GET":
        code = request.args.get('code')
        session['qq_code'] = code
        open_id = request.args.get('openid')
        session['qq_openid'] = open_id

        qqWeibo = QqWeibo( QQ_CONFIG['APP_KEY'], QQ_CONFIG['APP_SECRET'], QQ_CONFIG['REDIRECT_URI'])
        session['access_token'] = qqWeibo.GetQqAccessToken( code, open_id )
        content = qqWeibo.GetClient().get.statuses__home_timeline()
        return render_template( 'home_page.html', content_qq = content.data.info )

@app.route('/ajax_qq_data')
def ajax_qq_data():
    code = session['qq_code']
    open_id = session['qq_openid']
    access_token = session['access_token']


    url_str = 'https://open.t.qq.com/api/statuses/home_timeline?oauth_consumer_key=%s&access_token=%s&openid=%s&clientip=%s&oauth_version=2.a&scope=all' %( QQ_CONFIG['APP_KEY'], str(access_token), open_id,
     "127.0.0.1" )

    try:
        resp = urllib2.urlopen(urllib2.Request( url_str ) )
        body = resp.read()
        content_qq = json.loads( body, object_hook = _obj_hook )
        #content_qq = json.dumps( content_qq['data']['info'] )
        content_qq =  content_qq.data.info 

    except urllib2.HTTPError, e:
        body = e.read()

    return jsonify( content_qq = content_qq )
    #return render_template( 'qq_homepage.html', content_qq = (body) )

        