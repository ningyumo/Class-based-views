"""
MultipleObjectMixin
# ————————————————————————————
class django.views.generic.list.MultipleObjectMixin
    用于显示对象列表的mixin。如果指定paginate_by，Django将对此返回的结果进行分页。有两种防止在URL中指定页码：
    （1）在URLconf中使用page参数。例如：
    path('objects/page<int:page>/',PaginatedView.as_view())
    （2）通过request.GET来获取page参数。例如：
    /objects/?page=3
    这些值和列表时基于1的，而不是基于0的，因此第一页将表示为页面1
    对于最后一页，可以用last作为page的值
    /objects/?page=last
    page必须是有效的页码或last，任何其他值page都将导致404错误。
# ————————————————————————————
祖先：
（1）django.views.generic.base.ContextMixin                           （simple_mixins）
# ————————————————————————————
属性：
（1）extra_context                                                    （ContextMixin）
（2）allow_empty
    一个布尔值，指定在没有对象时是否显示页面。如果是False并且没有可用的对象，则视图将引发404而不是显示空白页面。
    默认为True。
*（3）model
    此视图将显示数据的模型。
*（4）queryset
    代表对象的queryset，如果提供了属性queryset的值，它会覆盖掉属性model的值。
    model = Foo 和 queryset = Foo.objects.all()相同。
    注意：
    queryset是一个可变值的类属性，所以使用它时要格外小心，用它时，要么用all()方法调用，要么用get_queryset()方法处理，这个
方法会处理幕后的克隆。
    model和queryset至少提供一个
（5）ordering
    字符串或字符串列表，指定queryset要根据哪些字段排序。和order_by()作用一样。
（6）paginate_by
    一个整数，指定每页应显示的对象数，如果给出了此属性，则试图将根据这个值对对象进行分页。具体显示哪一些则根据URLconf或者
request.GET来确定。
（7）paginate_orphans
    一个整数，指定最后一页可以包含多少个对象，如果小于等于这个值，则会显示在上一页中。
（8）page_kwarg
    一个字符串，指定用于page参数的名称。视图将根据这个值从request.GET或URLconf中获取kwarg变量。
    默认为page。
    例如：
    指定page_kwargs = 'aaa'，则URLconf：
    path('objects/<int:aaa>/',PaginatedView.as_view())
（9）paginator_class
    用于分页的Paginator类。
    默认是django.core.paginator.Paginator。
    如果自定义的paginator_class没有和django.core.paginator.Paginator相同的构造函数接口，则还需要提供get_paginator()
（10）context_object_name
    指定要在上下文中使用的变量的名称。
# ————————————————————————————
方法：
（1）get_queryset()
    获取此视图的对象列表。默认情况下返回属性query_set的值（如果已设置），否则根据属性model的默认管理器构建一个all()查询集
（Foo.objects.all()）如果要获取all()，那么只需要定义属性queryset，如果是filter等，就要定义get_queryset()。
（2）get_ordering()
    返回一个字符串（或字符串的迭代器），
    默认返回ordering。
（3）paginate_queryset(queryset, page_size)
    返回一个四元组(paginator, page, object_list, is_paginated)。根据page_size构建分页的queryset。如果request包含page参
数，无论是request.GET还是URLpattern捕获的，object_list都将对应该页面的对象。
（4）get_paginate_by(queryset)
    默认返回属性paginate_by的值，如果没分页返回None。
（5）get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)
    返回用于此视图的paginator实例。
    默认情况下，实例化一个属性paginator_class的实例。
（6）get_paginate_orphans()
    返回最后一页可以显示的数量。
    默认返回paginate_orphans的值。
（7）get_allow_empty()
    一个布尔值，指定在没有对象时是否显示页面。如果是False并且没有可用的对象，则视图将引发404而不是显示空白页面。
    默认返回allow_empty()的值。
（8）get_context_object_name(object_list)
    返回将用于包含此视图正在操作的数据列表的上下文变量名称。如果object_list是Django对象的查询集并且没有设置context_
object_name，那么默认的上下文变量名称将是model_name_list。
    例如：
    模型Article的上下文变量名称是article_list。
（9）get_context_data(**kwargs)
    返回用于显示对象列表的上下文数据
    上下文包括：
    ·object_list：此视图正在显示的对象列表。如果指定了context_object_name，那么这个变量也会显示在上下文中，值和
object_list相同。
    ·is_paginated：表示结果是否已分页的布尔值。如果没分页就是False。
    ·paginator：一个django.core.paginator.Paginator的实例。如果没分页，则为None。
    ·page_obj：一个django.core.paginator.Page的实例。如果没分页，则为None。
"""
# ————————————————————————————————————————————————————————————
"""
MultipleObjectTemplateResponseMixin
# ————————————————————————————
class django.views.generic.list.MultipleObjectTemplateResponseMixin
    一个用于对对象实例进行操作的视图渲染哪个模板的mixin类。要求与其混合的视图提供self.object_list，这是视图正在操作的对象
列表。self.object_list可能但不一定是QuerySet。
# ————————————————————————————
祖先：
（1）TemplateResponseMixin
# ————————————————————————————
属性：
 *（1）template_name                                  （simple_mixins）
（2）template_engine                                  （simple_mixins）
（3）response_class                                   （simple_mixins）
（4）content_type                                     （simple_mixins）
（5）template_name_suffix
    附加到自动生成的候选模板名称的后缀。
    默认是_list
# ————————————————————————————
方法：
（1）get_template_names()
    渲染模板时返回一个要搜索的模板名称的列表。第一个被找到的模板将会被使用。
    返回以下列表：
        ·视图的template_name的值（如果提供）
        ·<app_label>/<model_name><template_name_suffix>.html。例如：myApp下Article类：myApp/article_list.html
（2）render_to_response(context, **response_kwargs)  （simple_mixins）
"""