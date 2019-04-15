"""
FormMixin
# ————————————————————————————
class django.views.generic.edit.FormMixin
    一个mixin类，提供创建和显示表单的工具。
# ————————————————————————————
祖先：
（1）django.views.generic.base.ContextMixin
# ————————————————————————————
属性：
（1）initial
    包含表单初始数据的字典。
*（2）form_class
    要实例化的表单类
*（3）success_url
    成功处理表单时重定向到的URL。
    有3种方式处理：
    ·success_url = "/thanks/"
    ·success_url = reverse_lazy("myApp:thanks")
    ·def get_success_url(self):
        return reverse("myApp:thanks")
（4）prefix
    生成表单的前缀
# ————————————————————————————
方法：
（1）get_initial()
    获取表单的初始数据。
    默认返回属性initial的值。
（2）get_form_class()
    返回要实例化的表单类。
    默认返回属性form_class
（3）get_form_kwargs()
    构建实例化表单所需的关键字参数。
    初始值是get_initial()的值，如果request是POST或PUT，则request.POST,request.FILES将会被使用。
（4）get_form(form_class=None)
    用ger_form_kwargs()实例化属性form_class的一个实例。如果没有提供属性form_class，则使用方法get_form
_class。
（5）get_prefix()
    默认返回属性prefix()的值。
（6）get_success_url()
    返回成功验证表单时要重定向到的URL。
    默认返回success_url的值。
（7）form_valid(form)
    重定向到get_success_url()
（8）form_invalid(form)
    呈现响应，将无效表单作为上下文提供。
（9）get_context_data(**kwargs)
    调用方法get_form()并将结果添加到名为"form"的上下文数据中。
"""
# ———————————————————————————————————————————————————————————
"""
ModelFormMixin
# ————————————————————————————
class django.views.generic.edit.ModelFormMixin
    可以使用ModelForms表单而不是独立表单的mixin，
    由于这是一个SingleObjectMixin的子类，因此mixin的实例可以访问model和queryset属性，表示ModelForm正在操作的对象的类型。
    如果同时制定fields和form_class属性，会引发ImproperlyConfigured异常。
# ————————————————————————————
祖先：
（1）django.views.generic.edit.FormMixin                                      （editing_mixins.py）
（2）django.views.generic.detial.SingleObjectMixin                            （single_object_mixins.py）
# ————————————————————————————
属性：
（1）model
    一个模型类，可以明确指定，如果没有提供，则根据self.object或者queryset来确定。
（2）fields
    字段名称列表，和ModelForm的Meta.fields相同。
    如果想要自动生成表单类，这是必须的属性，否则会导致ImproperlyConfigured异常。
（3）success_url
    成功处理表单时重定向到的URL。
    success_url可能包含字典字符串格式，将根据对象的字段属性进行插值。例如，可以使用success_url="/polls/{slug}/"重定向到
由模型上slug字段组成的URL 。
# ————————————————————————————
方法：
（1）get_form_class()
    检索要实例化的表单类。如果提供了属性form_class，则使用对应的类。否则，ModelForm将根据属性queryset或者属性model提供的
值来实例化。
（2）get_form_kwargs()
    将当前示例（self.object）添加到标准get_form_kwargs()。
（3）get_success_url()
    确定成功验证表单时要重定向的URL。如果提供了属性success_url，则使用这个值。否则调用该对象（模型类）的
get_absolute_url()。
（4）form_valid(form)
    根据当前视图的对象，保存表单实例，并重定向到get_success_url()。
（5）form_invalid(form)
    呈现响应，将无效表单作为上下文提供。
"""
# ———————————————————————————————————————————————————————————
"""
DeletionMixin
# ————————————————————————————
class django.views.generic.edit.deletionMixin
    启用http的DELETE操作
# ————————————————————————————
属性：
（1）success_url
    成功删除指定对象时重定向到的URL。
    success_url可能包含字典字符串格式，将根据对象的字段属性进行插值。例如，您可以使用success_url="/parent/{parent_id}/"
重定向到模型parent_id的字段组成的URL 
# ————————————————————————————
方法：
（1）delete(request, *args, **kwargs)
    检索目标对象并调用其delete()方法，然后重定向到成功URL。
（2）get_success_url()
    返回成功删除指定对象时要重定向的URL。
    默认返回success_url。
"""
# ———————————————————————————————————————————————————————————



















