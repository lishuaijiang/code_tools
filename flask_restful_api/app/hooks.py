from flask import jsonify


def register_app_hooks(app):

    @app.before_first_request
    def app_before_first_request():
        """全局第一次请求处理"""
        pass

    @app.before_request
    def app_before_request():
        """全局请求前处理"""
        pass

    @app.after_request
    def app_after_request(response):
        """全局请求后处理"""
        return response

    @app.teardown_request
    def app_teardown_request(exception):
        """全局请求后清理资源(无论是否发生异常)"""
        pass

    @app.errorhandler(404)
    def app_handle_404(error):
        """全局 404 异常处理"""
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def app_handle_500(error):
        """全局 500 异常处理"""
        return jsonify({"error": "Internal Server Error"}), 500
