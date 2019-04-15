"""
TemplateResponseMixin
# ————————————————————————————
class django.view.generic.base.TemplateResponseMixin
提供一个构建TemplateResponse的机制，给出合适的上下文context。要使用的模板是可配置的，可以通过子类进一步自定义。
# ————————————————————————————
属性：
*（1）template_name
    要使用的模板的全称的字符串。如果没有定义会引发一个django.core.exceptions.ImproperlyConfigured异常。
（2）template_engine
    加载模板使用的模板引擎的名称。template_engine通过关键字using传递给response_class。
    默认是None，表示django在所有配置的引擎中搜索模板。
（3）response_class
    render_to_response方法返回的响应类。
    默认是TemplateResponse。
    TemplateResponse实例的模板和上下文可以在稍后修改（例如在模板响应中间件中修改）。
    如果需要自定义模板加载或者自定义上下文对象实例化，请创建一个TemplateResponse的子类并分配给response_class。
（4）content_type
    用于响应的内容类型。content_type通过一个关键字参数传递给response_class。
    默认是None，表示django使用DEFAULT_CONTENT_TYPE
# ————————————————————————————
方法：
（1）get_template_names()
    渲染模板时返回一个要搜索的模板名称的列表。第一个被找到的模板将会被使用。
（2）render_to_response(context, **response_kwargs)
    返回一个self.response_class的实例。如果提供了任何一个关键字参数，它们会被传递给响应类的构造函数。
    调用get_template_names()去获取将搜索的模板名称列表，以查找现有模板。
"""
# —————————————————————————————————————————————————————————————
"""
ContextMixin
# ————————————————————————————
class django.views.generic.base ContextMixin
# ————————————————————————————
属性：
（1）extra_context
    一个上下文中要包含的字典。这是一个在as_view()中确定一些简单的上下文的快捷方式。见例1。
方法：
# ————————————————————————————
（1）get_context_data(**kwargs)
    返回一个代表模板上下文的字典。提供的关键字参数将会构成返回的上下文。见例2。
"""
# 例1
from django.views.generic.base import TemplateView

TemplateView.as_view(extra_context={"title": "Custom Title"})

# 例2
import random


def get_context_data(**kwargs):
    context = super().get_context_data(**kwargs)
    context['number'] = random.randrange(1, 100)
    return context
# —————————————————————————————————————————————————————————————
