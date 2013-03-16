import sae

from routers import app

application = sae.create_wsgi_app(app)