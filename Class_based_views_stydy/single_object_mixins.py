"""
SingleObjectMixin
# ————————————————————————————
class django.views.generic.detail.SingleObjectMixin
    提供用于查找与当前HTTP请求关联的对象的机制。
# ————————————————————————————
祖先：
（1）django.views.generic.base.ContextMixin                           （simple_mixins）
# ————————————————————————————
属性：
*（1）model
    视图将要显示数据的模型。
*（2）queryset
    代表对象的queryset，如果提供了属性queryset的值，它会覆盖掉属性model的值。
    model = Foo 和 queryset = Foo.objects.all()相同。
    注意：
    queryset是一个可变值的类属性，所以使用它时要格外小心，用它时，要么用all()方法调用，要么用get_queryset()方法处理，这个方
法会处理幕后的克隆。
    model和queryset至少提供一个
（3）slug_field
    模型上包含slug的字段的名称。
    默认是"slug"。
（4）slug_url_kwarg
    URL模式包含slug的关键字参数的名称。
    默认是"slug"。
（5）pk_url_kwargs
    URL模式包含主键的关键字参数的名称。
    默认是"pk"。
（6）context_object_name
    指定要在上下文中使用的变量的名称
（7）query_pk_and_slug
    如果是True，get_object()会使用主键和slug执行查找。此属性可以帮助缓解不安全的直接对象引用攻击。当应用程序允许通过顺序主
键访问单个对象时，攻击者可以强制猜测所有URL; 从而获得应用程序中所有对象的列表。如果应阻止有权访问单个对象的用户获取此列表，则
设置query_pk_and_slug为True有助于防止猜测URL，因为每个URL都需要两个正确的非顺序参数。简单地使用独特的slug可能会起到同样的作
用，但是这种方案可以让你拥有非独特的slug。
    默认是False。
（8）extra_context                                     （ContextMixin）
# ————————————————————————————
方法：
（1）get_queryset()
    返回将会用于检索此视图将要显示的对象的查询集。
    默认情况下返回属性queryset的值（如果已设置），否则根据属性model的默认管理器构建一个all()查询集（Foo.objects.all()）
    如果要获取all()，那么只需要定义属性queryset，如果是filter等，就要定义get_queryset()。
（2）get_object(queryset=None)
    返回此视图将返回的单个对象。如果提供queryset，将会查找queryset中的对象，否则会使用get_queryset()的结果。get_object将
会根据"pk_url_kwargs"的值在视图的参数中查找，如果找到了，这个方法将会使用该值执行基于主键的查找。如果找不到这个参数，会使
用"slut_url_kwargs"的值在slug_field中执行一个slug查找。如果query_pk_and_slug是True，get_object()将同时使用主键和slug查
找。
（3）get_context_object_name(obj)
    返回将用于包含此视图正在操作的数据的上下文变量名称。
    默认返回属性context_object_name的值，如果未设置，则将根据组成查询集的模型名小写构造一个上下文名称。
    例如：
    模型Article将具有名为article的上下文。
（4）get_context_data(**kwargs)
    返回用于显示对象的上下文数据。
    此方法的基本实现要求视图设置self.object属性，即使是None。如果在没有内置视图的情况下使用此mixin，请务必执行此操作。
    它返回包含以下内容的字典：
    object：此视图正在显示的对象（self.object）
    context_object_name：self.object会被存储在get_context_object_name()中，默认是模型名的小写。
    注意：
    任何get_context_data()中的变量都会覆盖上下文处理器中的上下文变量。例如，如果属性model设置为User，则默认的上下文名称user
将会覆盖django.contrib.auth.context_processors.auth()中上下文处理器中的user变量。使用get_context_object_name()以避免冲
突。
（5）get_slug_field()
    返回用于通过slug查找的slug字段的名称。
    默认返回属性slug_field的值。
"""
# —————————————————————————————————————————————————————————————
"""
SingleObjectTemplateResponseMixin
# ————————————————————————————
class django.views.generic.detail.SingleObjectTemplateResponseMixin
    一个mixin类，它为对单个对象实例进行操作的视图执行基于模板的响应呈现。要求与其混合的视图提供self.object——视图正在操作
的对象实例。self.object通常是，但不一定是Django模型的实例，在视图正在构建新实例的过程中可能是None。
# ————————————————————————————
祖先：
（1）TemplateResponseMixin                                           （simple_mixins）
# ————————————————————————————
属性：
（1）template_name                                                   （TemplateResponseMixin）
（2）template_engine                                                  （TemplateResponseMixin）
（3）response_class                                                   （TemplateResponseMixin）
（4）content_type                                                     （TemplateResponseMixin）
（5）template_name_field
    当前对象实例上的字段，可用于确定候选模板的名称。如果其没有template_name_field或当前对象实例template_name_field的值是
None，则该对象将不会用于候选模板名称。
（6）template_name_suffix
    附加到自动生成的候选模板名称的后缀。
    默认后缀是_detail。
# ————————————————————————————
方法：
（1）render_to_response(context, **response_kwargs)                    （TemplateResponseMixin）
（2）get_template_names()                                              （覆盖TemplateResponseMixin）
    返回候选模板名称列表。包括：
    ·视图的template_name的值（如果提供）
    ·视图正在操作的对象实例的template_name_field的内容（如果可用）
    ·<app_label>/<model_name><template_name_suffix>.html。例如：myApp下Article类：myApp/article_detail.html
"""