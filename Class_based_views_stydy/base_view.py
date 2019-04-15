"""
View
# ————————————————————————————
class django.views.generic.base.View
    所有其他基于类的视图都从此基类继承。不是严格意义上的通用视图，也可以从django.views中导入。
# ————————————————————————————
属性：
（1）http_method_names
    此视图将接受的HTTP方法名称列表。
    默认：['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
# ————————————————————————————
方法：
（1）as_view(**initkwargs)
    返回一个可调用的视图，该视图接收请求并返回响应。在请求/响应周期内调用视图时，setup()方法将HttpRequest视图的request
属性以及从URL模式捕获的任何位置和关键词参数分别分配给args和kwargs属性，然后调用dispatch()
（2）dispatch(request, *args, **kwargs)
    view视图的一部分，接受request参数和参数的方法，并返回HTTP响应。默认实现将检查HTTP方法并尝试指派到与HTTP方法匹配的方法
去处理：一个GET请求将指派给get()，一个POST请求将指派给post()等等。
    默认情况下，一个HEAD请求将指派给get()。如果你想要HEAD请求和GET请求处理方法不同，你可以重写head()方法。
（3）http_method_not_allowed(request, *args, **kwargs)
    如果使用不支持的HTTP方法调用视图，则会调用此方法。
    默认返回纯文本形式的允许的方法列表的HttpResponseNotAllowed。
（4）setup(request, *args, **kwargs)
    在dispatch()之前初始化查看实例属性：self.request，self.args，self.kwargs。
    重写此方法允许mixins设置实例属性以便在子类中使用。覆盖此方法时，必须调用super()。
（5）options(request, *args, **kwargs)
    OPTIONS HTTP请求的句柄响应。返回一个Allow响应，包含视图允许的HTTP方法名称列表的标头的响应。
（6）head()
# ————————————————————————————
方法流程图
setup() --> dispatch() --> http_method_not_allowed() --> options()
"""
# ————————————————————————————————————————————————————————————
"""
TemplateView
# ————————————————————————————
class django.views.generic.base.TemplateView
祖先：
（1）django.views.generic.base.TemplateResponseMixin                  （simple_mixins.py）
（2）django.views.generic.base.ContextMixin                           （simple_mixins.py）
（3）django.views.generic.base.View                                   （base_view.py）
# ————————————————————————————
属性：
（1）content_type                                                     （TemplateResponseMixin）
（2）response_class[render_to_reponse()]                              （TemplateResponseMixin）
（3）template_engine                                                  （TemplateResponseMixin）
*（4）template_name[get_template_names()]                             （TemplateResponseMixin）
（5）extra_context                                                    （ContextMixin）
（6）http_method_names                                                （View）
# ————————————————————————————
方法：
（1）as_view()                                                        （View）
（2）dispatch()                                                       （View）
（4）setup()                                                          （View）
（6）http_method_not_allowed()                                        （View）
（7）render_to_response()                                             （TemplateResponseMixin）
（8）get_template_names()                                             （TemplateResponseMixin）
（9）get_context_data()                                               （ContextMixin）
（10）get()
（11）head()
# ————————————————————————————
方法流程图：
setup() --> dispatch() --> http_method_not_allowed() --> get_context_data()
"""
# ————————————————————————————————————————————————————————————
"""
RedirectView
# ————————————————————————————
class django.views.generic.base.RedirectView
    重定向到给定的URL。给定的URL可能包含字典样式的字符串格式，它将根据URL中捕获的参数进行插值。因为关键字插值总是会完成
（即使没有传入参数）。URL中的“%”必须写成“%%”，这样Python才能把它们转换为%。
    如果给定的URL是None，Django将返回一个HttpResponseGone(410)
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                   （base_view.py）
# ————————————————————————————
属性：
（1）url[get_redirect_url()]
    要重定向到的url的字符串。如果是None，将会引发HttpResponseGone(410)
（2）pattern_name
    要重定向到的URL模式的名称。reverse函数将会根据传入此视图的args和kwargs进行反向解析
（3）permanent
    重定向是否应该是永久性的。这里唯一的区别是返回HTTP状态码。如果是True，那么重定向将使用状态码301，如果是False，那么
重定向将使用状态码302。
    默认是False。
（4）query_string
    是否将GET查询字符串传递给新位置。如果是True，那么查询字符串将附加到URL。如果是False，则丢弃查询字符串。
    默认是False。
（5）http_method_names                                                （View）
# ————————————————————————————
方法：
（1）get_redirect_url(*args, **kwargs)
    构造重定向的目标URL。
    默认使用属性url作为开始字符串，通过在URL中捕获的命名组字符串的%关键字参数进行扩展。
    如果没有设置url属性，get_redirect_url()将会试图反向解析属性pattern_name去捕获URL。
    如果通过query_string请求，它还会将查询字符串附加到生成的URL。
    子类可以实现他们希望的任何行为，只要改方法返回一个可重定向的URL字符串即可。
（2）as_view()                                                        （View）
（3）dispatch()                                                       （View）
（4）http_method_not_allowed()                                        （View）
（5）setup()                                                          （View）
（6）get()
（7）head()
（8）post()
（9）put()
# ————————————————————————————
方法流程图
setup() --> dispatch() --> http_method_not_allowed -->get_redirect_url()
"""
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from articles.models import Article


class ArticleCounterRedicrectView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = "article-detail"

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)






























