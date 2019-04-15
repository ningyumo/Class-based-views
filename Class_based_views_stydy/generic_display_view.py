"""
DetailView
# ————————————————————————————
class django.views.generic.detail.DetailView
    执行此视图时，self.object将包含视图正在操作的对象。
# ————————————————————————————
祖先：
（1）django.views.generic.detail.BaseDetailView
（2）django.views.generic.detail.SingleObjectMixin                    （single_object_mixins.py）
（3）django.views.generic.detail.SingleObjectTemplateResponseMixin    （single_object_mixins.py）
（4）django.views.generic.base.View                                   （base_view.py）
# ————————————————————————————
属性：
（1）http_method_names                                                （View）
（2）extra_context                                                    （SingleObjectMixin）
（3）context_object_name[get_context_object_name()]                   （SingleObjectMixin）
（4）model                                                            （SingleObjectMixin）
（5）pk_url_kwarg                                                     （SingleObjectMixin）
（6）queryset[get_queryset()]                                         （SingleObjectMixin）
（7）slug_field[get_slug_field()]                                     （SingleObjectMixin）
（8）slug_url_kwarg                                                   （SingleObjectMixin）
（9）query_pk_and_slug                                                （SingleObjectMixin）
（10）response_class[render_to_response()]                            （SingleObjectTemplateResponseMixin）
（11）content_type                                                    （SingleObjectTemplateResponseMixin）
（12）template_engine                                                 （SingleObjectTemplateResponseMixin）
（13）template_name[get_template_names()]                             （SingleObjectTemplateResponseMixin）
（14）template_name_field                                             （SingleObjectTemplateResponseMixin）
（15）template_name_suffix                                            （SingleObjectTemplateResponseMixin）
# ————————————————————————————
方法：
（1）as_view()                                                         （View）
（3）dispatch()                                                        （View）
（4）http_method_not_allowed()                                         （View）
（5）setup()                                                           （View）
（6）get_context_data()                                                （SingleObjectMixin）
（7）get_object()                                                      （SingleObjectMixin）
（8）get_context_object_name()                                         （SingleObjectMixin）
（9）get_queryset()                                                    （SingleObjectMixin）
（10）get_slug_field()                                                  （SingleObjectMixin）
（11）render_to_response()                                              （SingleObjectTemplateResponseMixin）
（12）get_template_names()                                              （SingleObjectTemplateResponseMixin）
（13）get()
（14）head()
# ————————————————————————————
方法流程图
（1）setup()
（2）dispatch()
（3）http_method_not_allowed()
（4）get_template_names()
（5）get_slug_field()
（6）get_queryset()
（7）get_object()
（8）get_context_object_name()
（9）get_context_data()
（10）get()
（11）render_to_response()
"""
# —————————————————————————————————————————————————————————————
"""
ListView
# ————————————————————————————
class django.views.generic.list.ListView
    表示对象列表的页面。
    在执行此视图时，self.object_list将包含视图正在操作的对象列表（通常但不一定是查询集）。
# ————————————————————————————
祖先：
（1）django.views.generic.list,BaseListView
（2）django.views.generic.list.View
（3）django.views.generic.list.MultipleObjectMixin
（4）django.views.generic.list.MultipleObjectTemplateResponseMixin
# ————————————————————————————
属性：
（1）http_method_names                                     （View）
（2）allow_empty[get_allow_empty]                          （MultipleObjectMixin）
（3）context_object_name[get_context_object_name()]        （MultipleObjectMixin）
（4）extra_context                                         （MultipleObjectMixin）
（5）model                                                 （MultipleObjectMixin）
（6）ordering[get_ordering()]                              （MultipleObjectMixin）
（7）paginate_by[get_paginate_by()]                        （MultipleObjectMixin）
（8）paginate_orphans[get_paginate_orphans()]              （MultipleObjectMixin）
（9）paginator_class                                       （MultipleObjectMixin）
（10）queryset[get_queryset()]                             （MultipleObjectMixin）
（11）response_class[render_to_response()]                 （MultipleObjectTemplateResponseMixin）
（12）template_engine                                      （MultipleObjectTemplateResponseMixin）
（13）template_name[get_template_names()]                   （MultipleObjectTemplateResponseMixin）
（14）template_name_suffix                                （MultipleObjectTemplateResponseMixin）
（15）content_type                                         （MultipleObjectTemplateResponseMixin）
# ————————————————————————————
方法：
（1）as_view()                                              （View）
（2）dispatch()                                             （View）
（3）setup()                                                （View）
（4）http_method_not_allowed()                              （View）
（5）get_context_data()                                     （MultipleObjectMixin）
（6）get_paginator()                                        （MultipleObjectMixin）
（7）paginate_queryset()                                    （MultipleObjectMixin）
（8）render_to_response()                                   （MultipleObjectTemplateResponseMixin）
（9）get()
（10）head()
# ————————————————————————————
方法流程图
（1）setup()
（2）dispatch()
（3）http_method_not_allowed()
（4）get_template_names()
（5）get_queryset()
（6）get_context_object_name()
（7）get_context_data()
（8）get()
（9）render_to_response
"""