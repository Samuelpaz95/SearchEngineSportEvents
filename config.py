class Config:
    WTF_CSRF_ENABLED = True
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}