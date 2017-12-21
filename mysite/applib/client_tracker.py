class ClientTracker:

    def __init__(self):
        pass

    def get_client_device(self,request):
        D = {
            'pc':request.user_agent.is_pc,
            'mobile':request.user_agent.is_mobile,
            'tablet':request.user_agent.is_tablet,
            'touch_capable':request.user_agent.is_touch_capable,
            'bot':request.user_agent.is_bot,
            'device':request.user_agent.device,
            'device_family':request.user_agent.device_family
        }
        return D

    def get_client_browser(self,request):
        D = {
            'browser':request.user_agent.browser,
            'browser_family':request.user_agent.browser.family,
            'browser_version':request.user_agent.browser.version,
            'browser_version_string':request.user_agent.browser.version_string
        }
        return D

    def get_client_os(self,request):
        D = {
            'os':request.user_agent.os,
            'os_family':request.user_agent.os.family,
            'os_version':request.user_agent.os.version,
            'os_version_string':request.user_agent.os.version_string
        }
        return D

    def get_client_full(self,request):
        D = {
            'device':self.get_client_device(request),
            'browser':self.get_client_browser(request),
            'os':self.get_client_os(request)
        }
        return D
