from base import *
 
DEBUG = True
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_ehLvAcTuMRNOETWLiWX3dh6y')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_DTljbH6TXFcvZURKl8MB2Ryk')