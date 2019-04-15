# 下面的所有视图都假定定义了Author模型。
from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    # 编辑视图对应的模型都要有get_absolute_url方法。
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
# ———————————————————————————————————————————————————————————
"""
FormView
# ————————————————————————————
class django.views.generic.edit.FormView
    显示表单的视图。出错时，重新显示带有验证错误的表单；成功时重定向到新的URL。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                  （base_view.py）
（2）django.views.generic.base.TemplateResponseView                  （base_view.py）
（3）django.views.generic.edit.FormMixin                             （editing_mixins.py）
# ————————————————————————————
属性：
（1）http_method_names                                                (View)
（2）success_url[get_success_url()]                                  （FormMixin）
（3）extra_context                                                   （FormMixin）
（4）form_class[get_form_class()]                                    （FormMixin）
（5）initial[get_initial()]                                          （FormMixin）
（6）prefix[get_prefix()]                                            （FormMixin）
（7）response_class[render_to_response()]                            （TemplateResponseView）
（8）template_engine                                                 （TemplateResponseView）
（9）template_name[get_template_names()]                             （TemplateResponseView）
（10）content_type                                                   （TemplateResponseView）
# ————————————————————————————
方法：
（1）as_view()                                                        (View)
（2）dispatch()                                                       (View)
（3）http_method_not_allowed()                                        (View)
（4）setup()                                                          (View)
（5）form_invalid()                                                  （FormMixin）
（6）form_valid()                                                    （FormMixin）
（7）get_context_data()                                              （FormMixin）
（8）get_form()                                                      （FormMixin）
（9）get_form_kwargs()                                               （FormMixin）
（10）get()
（11）post()
（12）put()
"""
# ———————————————————————————————————————————————————————————
"""
CreateView
# ————————————————————————————
class django.views.generic.edit.CreateView
    显示用于创建对象的表单的视图，如果有错误，使用验证错误重新显示表单并保存对象
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                       （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                      （base_view.py）
（3）django.views.generic.detail.SingleObjectMixin                        （single_object_mixins.py）
（4）django.views.generic.detail.SingleObjectTemplateResponseMixin        （single_object_mixins.py）
（5）django.views.generic.edit.FormMixin                                  （editing_mixins.py）
（6）django.views.generic.edit.ModelFormMixin                             （editing_mixins.py）
# ————————————————————————————
属性：
（1）object
    使用时，CreateView可以访问self.object,这是正在创建的对象。如果尚未创建对象，则值为None。
（2）template_name_suffix
    默认情况下CreateView显示给GET请求的页面使用的template_name_suffix是"_form"。
    例如：改变该属性为"_create_form"，那么对于模型Aurhor使用的默认template_name是myapp/author_created_form,html。
（3）http_method_names                                                     （View）
（4）prefix[get_prefix()]                                                  （FormMixin）
（5）form_class[get_form_class()]                                          （FormMixin）
（6）initial[get_initial()]                                                （FormMixin）
（7）context_object_name[get_context_object_name()]                        （SingleObjectMixin）
（8）extra_context                                                         （SingleObjectMixin）
（9）pk_url_kwarg                                                          （SingleObjectMixin）
（10）queryset[get_queryset()]                                             （SingleObjectMixin）
（11）slug_field[get_slug_field()]                                         （SingleObjectMixin）
（12）slug_url_kwarg                                                       （SingleObjectMixin）
（13）fields                                                               （ModelFormMixin）
（14）model                                                                （ModelFormMixin）
（15）success_url[get_success_url()]                                       （ModelFormMixin）
（16）content_type                                                         （TemplateResponseMixin）
（17）response_class[render_to_response()]                                 （SingleObjectTemplateResponseMixin）
（18）template_engine                                                      （SingleObjectTemplateResponseMixin）
（19）template_name[get_template_names()]                                  （SingleObjectTemplateResponseMixin）
（20）template_name_field                                                  （SingleObjectTemplateResponseMixin）
（21）template_name_suffix                                                 （SingleObjectTemplateResponseMixin）
# ————————————————————————————
方法：
（1）as_view()                                                             （View）
（2）dispatch()                                                            （View）
（3）http_method_not_allowed()                                             （View）
（4）setup()                                                               （View）
（5）get_context_data()                                                    （FormMixin）
（6）get_form()                                                            （FormMixin）
（7）get_object()                                                          （SingleObjectMixin）
（8）form_invalid()                                                        （ModelFormMixin）
（9）form_valid()                                                          （ModelFormMixin）
（10）get_form_kwargs()                                                    （ModelFormMixin）
（11）render_to_response()                                                 （TemplateResponseMixin）
（12）get()
（13）head()
（14）post()
（15）put()
"""
# ———————————————————————————————————————————————————————————
"""
UpdateView
# ————————————————————————————
class django.views.generic.edit.UpdateView
    显示用于编辑现有对象的表单的视图，使用验证错误（如果有）重新显示表单并保存对对象的更改。从对象的模型类自动生成表单
（除非手动指定表单类）。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                       （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                      （base_view.py）
（3）django.views.generic.detail.SingleObjectMixin                        （single_object_mixins.py）
（4）django.views.generic.detail.SingleObjectTemplateResponseMixin        （single_object_mixins.py）
（5）django.views.generic.edit.FormMixin                                  （editing_mixins.py）
（6）django.views.generic.edit.ModelFormMixin                             （editing_mixins.py）
# ————————————————————————————
属性：
（1）object
    使用时，CreateView可以访问self.object,这是正在创建的对象。如果尚未创建对象，则值为None。
（2）template_name_suffix
    默认情况下CreateView显示给GET请求的页面使用的template_name_suffix是"_form"。
    例如：改变该属性为"_update_form"，那么对于模型Aurhor使用的默认template_name是myapp/author_update_form.html。
（3）http_method_names                                                    （View）
（4）prefix[get_prefix()]                                                 （FormMixin）
（5）form_class[get_form_class()]                                         （FormMixin）
（6）initial[get_initial()]                                               （FormMixin）
（7）context_object_name[get_context_object_name()]                       （SingleObjectMixin）
（8）extra_context                                                        （SingleObjectMixin）
（9）pk_url_kwarg                                                         （SingleObjectMixin）
（10）queryset[get_queryset()]                                            （SingleObjectMixin）
（11）slug_field[get_slug_field()]                                        （SingleObjectMixin）
（12）slug_url_kwarg                                                      （SingleObjectMixin）
（13）fields                                                              （ModelFormMixin）
（14）model                                                               （ModelFormMixin）
（15）success_url[get_success_url()]                                      （ModelFormMixin）
（16）content_type                                                        （TemplateResponseMixin）
（17）response_class[render_to_response()]                                （SingleObjectTemplateResponseMixin）
（18）template_engine                                                     （SingleObjectTemplateResponseMixin）
（19）template_name[get_template_names()]                                 （SingleObjectTemplateResponseMixin）
（20）template_name_field                                                 （SingleObjectTemplateResponseMixin）
（21）template_name_suffix                                                （SingleObjectTemplateResponseMixin）
# ————————————————————————————
方法：
（1）as_view()                                                            （View）
（2）dispatch()                                                           （View）
（3）http_method_not_allowed()                                            （View）
（4）setup()                                                              （View）
（5）get_context_data()                                                   （FormMixin）
（6）get_form()                                                           （FormMixin）
（7）get_object()                                                         （SingleObjectMixin）
（8）form_invalid()                                                       （ModelFormMixin）
（9）form_valid()                                                         （ModelFormMixin）
（10）get_form_kwargs()                                                   （ModelFormMixin）
（11）render_to_response()                                                （TemplateResponseMixin）
（12）get()
（13）head()
（14）post()
（15）put()
# ————————————————————————————
注意：
如果更新后跳转到ListView那么定义属性success_url=reverse_lazy("myApp: list_view")
如果更新后跳转到DetailView那么定义方法
deg get_success_url(self):
    return reverse("myApp: detail_view", kwargs=self.kwargs)
"""
# ———————————————————————————————————————————————————————————
"""
DeleteView
# ————————————————————————————
class django.views.generic.edit.DeleteView
    显示确认页面删除现有对象的视图。只有请求方法是POST才会删除给定的对象。如果通过GET方法获取此视图，它将显示一个确认页
面，其中应包含POST到同一URL的表单。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                       （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                      （base_view.py）
（3）django.views.generic.detail.SingleObjectMixin                        （single_object_mixins.py）
（4）django.views.generic.detail.SingleObjectTemplateResponseMixin        （single_object_mixins.py）
（5）django.views.generic.edit.DeletionMixin                              （editing_mixins.py）                  
# ————————————————————————————
属性：
（1）template_name_suffix
    默认情况下CreateView显示给GET请求的页面使用的template_name_suffix是"_confirm_delete"。
    例如：改变该属性为"_check_delete"，那么对于模型Aurhor使用的默认template_name是myapp/author_check_delete.html。
（2）http_method_names                                                    （View）
（3）context_object_name[get_context_object_name()]                       （SingleObjectMixin）
（4）extra_context                                                        （SingleObjectMixin）
（5）pk_url_kwarg                                                         （SingleObjectMixin）
（6）queryset[get_queryset()]                                             （SingleObjectMixin）
（7）slug_field[get_slug_field()]                                         （SingleObjectMixin）
（8）slug_url_kwarg                                                       （SingleObjectMixin）
（9）model                                                                （SingleObjectMixin）
（10）content_type                                                        （TemplateResponseMixin）
（11）response_class[render_to_response()]                                （SingleObjectTemplateResponseMixin）
（12）template_engine                                                     （SingleObjectTemplateResponseMixin）
（13）template_name[get_template_names()]                                 （SingleObjectTemplateResponseMixin）
（14）template_name_field                                                 （SingleObjectTemplateResponseMixin）
（15）template_name_suffix                                                （SingleObjectTemplateResponseMixin）
# ————————————————————————————
方法：
（1）as_view()                                                            （View）
（2）dispatch()                                                           （View）
（3）http_method_not_allowed()                                            （View）
（4）setup()                                                              （View）
（5）get_context_data()                                                   （SingleObjectMixin）
（6）render_to_response()                                                 （TemplateResponseMixin）
（7）delete()                                                             （DeletionMixin）    
（8）get()
（9）head()
（10）post()
（11）put()
"""
# ———————————————————————————————————————————————————————————












