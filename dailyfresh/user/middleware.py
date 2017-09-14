# coding=utf-8


class PreviousMiddleware:
    # process_request方法会捕获页面传递的如图片无法导入的错误
    # def process_request(self,request):
    def process_view(self,request,view_func,view_args,view_kwargs):
        full_path = request.get_full_path()
        if request.path not in [
            '/user/login/',
            '/user/login_check/',
            '/user/register/',
            '/user/register_log/',
            '/user/logout/',
        ]:
            request.session['full_path'] = full_path
