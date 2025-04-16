
def register_v1_api_hooks(v1_api):

    @v1_api.before_request
    def v1_api_before_request():
        """v1 蓝图中请求前处理"""
        pass

    @v1_api.after_request
    def v1_api_after_request(response):
        """v1 蓝图中请求后处理"""
        return response

    @v1_api.teardown_request
    def v1_api_teardown_request(exception):
        """v1 蓝图中清理资源"""
        pass
