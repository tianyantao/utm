from config.config_env import get_env


class ConfigCase:
    ENV = get_env()
    PROTOCOL = "https" if ENV == 'prod' else "http"
    HOST_STUDY = "study.ewt360.com" if ENV == 'prod' else "study.{}.mistong.com".format(ENV)
    HOST_TIKU = "gateway.ewt360.com" if ENV == 'prod' else "gateway.{}.mistong.com".format(ENV)
    HOST_TEACHER = "teacher.ewt360.com" if ENV == 'prod' else "teacher.{}.mistong.com".format(ENV)
    HOST_WX = "wx.ewt360.com" if ENV == 'prod' else "wx.test.mistong.com"
    HOST_GATEWAY = "gateway.ewt360.com" if ENV == 'prod' else "gateway.test.mistong.com"
    HOST_WEB = "web.ewt360.com" if ENV == 'prod' else "web.test.mistong.com"
    HOST_INSIDEGATEWAY = "insidegateway.ewt360.com" if ENV == 'prod' else "insidegateway.test.mistong.com"
    HOST_ADMIN = "admin.mistong.com" if ENV == 'prod' else "admin.test.mistong.com"
    HOST_PASSPORT = "passport.ewt360.com" if ENV == 'prod' else "my.{}.mistong.com".format(ENV)
    HOST_QBANK = "admin.mistong.com" if ENV == 'prod' else "admin.{}.mistong.com".format(ENV)

    QQopenId = "B7A0621A87508E323DD098F279499336" if ENV == 'prod' else "72F8A3C4625EE2171814CF078000D883"



