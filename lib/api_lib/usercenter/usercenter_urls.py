from config.config_case import ConfigCase

class UCUrls():
    def __init__(self):
        self.__init_urls()

    def __init_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_WEB)
        passport_url = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_PASSPORT)
        gatewayurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_GATEWAY)
        self.prelogin = baseurl + "/login/prelogin"
        self.get_user = baseurl + "/Ajax/GetUser"
        self.app_login = passport_url + "/apinewmember/login"
        self.verify_is_expired_member = baseurl + "/Login/VerifyIsExpiredMember"
        self.auth_login = baseurl + "/api/authcenter/oauth/login"

        self.auth_pc_login = gatewayurl + "/api/authcenter/oauth/login"
        self.auth_app_login = gatewayurl + "/api/authcenter/oauth/login/app"
        self.auth_thirdApp_login = gatewayurl + "/api/usercenter/user/login/third/app/openId/login"
        self.auth_visitor_login = gatewayurl + "/api/usercenter/user/login/visitor/login"
        self.sendcode = gatewayurl + "/api/usercenter/user/login/sms/sendcode"
        self.bindmobile = gatewayurl + "/api/usercenter/user/login/mobile/bind"
        self.get_province = gatewayurl + "/api/commondata/area/getProvinces"
        self.get_usermobiletype = gatewayurl + "/api/usercenter/authentication/mobiletype/list"
        self.get_accountinfo = gatewayurl + "/api/authcenter/account/get/info"
        self.get_trialinfo = gatewayurl + "/api/usercenter/member/onTrialInfo"
        self.get_baseinfo = gatewayurl + "/api/usercenter/user/baseinfo"
        self.update_avatar = gatewayurl + "/api/usercenter/user/update/avatarUrl"
        self.update_userinfo = gatewayurl + "/api/usercenter/user/update"
        self.get_userid= gatewayurl +"/api/usercenter/user/queryUserId"
