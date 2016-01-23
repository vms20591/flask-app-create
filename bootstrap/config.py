import os
import base64

class Config(object):

	#secret key for csrf purpose and etc.,
	SECRET_KEY = os.environ.get('SECRET_KEY') or base64.b64encode(os.urandom(20))

	#default debug setting
	DEBUG=True
	TESTING=False

class DevelopmentConfig(Config):
	#switching off test config
	TESTING=False

class TestingConfig(Config):
	#switching to test config
	TESTING=True
	
class ProductionConfig(Config):
	#swtiching off debug and testing
	DEBUG=False
	TESTING=False

#configuration factor object
app_config={
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	'default':DevelopmentConfig,
}
