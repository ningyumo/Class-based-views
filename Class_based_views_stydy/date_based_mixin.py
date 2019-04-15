"""
DateMixin
# ————————————————————————————
class django.views.generic.dates.DateMixin
    为所有基于日期的视图提供通用行为。
# ————————————————————————————
属性：
（1）date_field
    QuerySet对应的模型的DateField、DateTimeField。该基于日期的归档使用它来确定显示在页面上的模型对象的列表。
    当启用时区支持（setting.py中设置USE_TZ = True），并且属性date_field是DateTimeField时，日期被认为是在当前时区。否则
查询集可以包括最终用户时区中前一天或后一天的对象。
    注意：上面情况下，相同的URL可能会显示不同的对象集，具体取决于最终用户的时区。要避免这种情况，应该使用DateField作为
date_field属性的值。
（2）allow_future
    一个布尔值，表示是否在此页面上包含“future”对象，“future”表示指定的字段date_field大于当前日期/时间的对象。
    默认为False
# ————————————————————————————
方法：
（1）get_date_field()
    返回包含次试图将在其上运行的日期数据的字段的名称。
    默认返回date_field.
（2）get_allow_future()
    表示是否在此页面上包含“future”对象，“future”表示指定的字段date_field大于当前日期/时间的对象。
    默认返回allow_future的值。
"""
# ———————————————————————————————————————————————————————————
"""
BaseDateListView
# ————————————————————————————
class django.views.generic.dates.BaseDateListView
    一个基类，为所有基于日期的视图提供通用行为。通常不会实例化这个类，而是实例化它的子类。
    当此视图（及其子类）正在执行时，self.object_list将包含视图正在操作的对象列表，self.date_list将包含可用数据的日期列
表。
# ————————————————————————————
祖先：
（1）django.views.generic.dates.DateMixin
（2）django.views.generic.list.MultipleObjectMixin
# ————————————————————————————
属性：
（1）allow_empty
    一个布尔值，指定在没有可用对象时是否显示页面。如果是True且没有可用的对象，则试图将显示空页而不是引发404错误。
    和django.views.generic.list.MultipleObjectMixin.allow_empty相同，除了默认值是False。
（2）date_list_period
    可选的一个字符串，date_list将根据这个值来聚合。
    可选值包括：“year”（默认）、“month”、“day”。
# ————————————————————————————
方法
（1）get_dated_items()
    返回一个三元组(date_list, object_list, extra_context)
    date_list是可用数据的日期列表。object_list是对象列表。extra_context是一个上下文数据字典，将会被添加到
MultipleObjectMixin提供的上下文数据字典中。
（2）get_dated_queryset(**lookup)
    返回一个查询集，使用lookup定义的查询参数进行过滤。对查询集强制执行任何限制，例如allow_empty和allow_future。
（3）get_date_list_period()
    date_list根据什么聚合，就返回什么。
    默认返回属性date_list_period的值。
（4）get_data_list(queryset, date_type=None, ordering="ASC")
    返回一个列表，这个列表是queryset中包含date_type类型日期的元素集合。
    例如：
    get_date_list(qs, "year")将会返回qs中包含year的元素集合。如果没有提供date_type，将会使用get_date_list_period()
的值。date_type和ordering和QuerySet.dates()使用方法一样。
"""
# ———————————————————————————————————————————————————————————
"""
YearMixin
# ————————————————————————————
class django.views.generic.dates.YearMixin
    可用于检索日期的年份并提供解析信息的mixin。
# ————————————————————————————
属性：
（1）year_format
    解析年份时使用的strftime()格式。
    默认是"%Y"
（2）year
    可选的年份的值，是一个字符串。
    默认是None，表示年份将使用其他方式确定。
# ————————————————————————————
方法：
（1）get_year_format()
    返回解析年份时要使用的strftime()格式。
    默认返回属性year_format。
（2）get_year()
    以字符串形式返回此视图将显示的数据的年份。按顺序尝试一下来源：
    ·YearMixin.year属性的值
    ·URL模式中捕获的year参数
    ·request.GET中捕获的year的值
    如果找不到有效的年份规范，则引发404
（3）get_next_year(date)
    返回包含提供日期之后的一年的第一天的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和allow
_future。
（4）get_previous_year(date)
    返回包含提供日期之前一年的第一天的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和allow
_future。
"""
# ———————————————————————————————————————————————————————————
"""
MonthMixin
# ————————————————————————————
class django.views.generic.dates.MonthMixin
    可用于检索日期的月份组件并提供解析信息的mixin。
# ————————————————————————————
属性：
（1）month_format
    返回解析月份时使用的strftime()格式。
    默认情况下是"%b"。还有一个"%m"可选
（2）month
    可选的月份值，是一个字符串。
    默认为None，表示月份将使用其他方式确定。
# ————————————————————————————
方法：
（1）get_month_format()
    返回解析月份时要使用的strftime()格式。
    默认返回month_format。
（2）get_month()
    以字符串形式返回此视图将显示数据的月份。按顺序尝试一下来源：
    ·MonthMixin.month属性的值
    ·URL模式中捕获的month参数
    ·request.GET中捕获的month的值
    如果找不到有效的月份规范，则引发404
（3）get_next_month(date)
    返回包含提供日期之后的一个月的第一天的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和
allow_future。
（4）get_previous_month(date)
    返回包含提供日期之前一月的第一天的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和allow
_future。
"""
# ———————————————————————————————————————————————————————————
"""
WeekMixin
# ————————————————————————————
class django.views.generic.dates.WeekMixin
    可用于检索日期的一周的组件并提供解析信息的mixin。
# ————————————————————————————
属性：
（1）week_format
    返回解析周时使用的strftime()格式。
    默认情况下是"%U"，意味着从一周周日开始，"%W"意味着一周从周一开始。
（2）week
    可选的周的值，是一个字符串。
    默认为None，表示周将使用其他方式确定。
# ————————————————————————————
方法：
（1）get_week_format()
    返回解析周时要使用的strftime()格式。
    默认返回week_format。
（2）get_week()
    以字符串形式返回此视图将显示数据的月份。按顺序尝试一下来源：
    ·WeekMixin.week属性的值
    ·URL模式中捕获的week参数
    ·request.GET中捕获的week的值
    如果找不到有效的月份规范，则引发404
（3）get_next_week(date)
    返回包含提供日期之后的一个周的第一天的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和
allow_future。
（4）get_previous_week(date)
    返回包含提供日期之前一周的第一天的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和allow
_future。
"""
# ———————————————————————————————————————————————————————————
"""
DayMixin
# ————————————————————————————
class django.views.generic.dates.WeekMixin
    可用于检索日期的组件并提供解析信息的mixin。
# ————————————————————————————
属性：
（1）day_format
    返回解析日期时使用的strftime()格式。
    默认情况下是"%d"。
（2）day
    可选的日期的值，是一个字符串。
    默认为None，表示日期将使用其他方式确定。
# ————————————————————————————
方法：
（1）get_day_format()
    返回解析日期时要使用的strftime()格式。
    默认返回day_format。
（2）get_day()
    以字符串形式返回此视图将显示数据的月份。按顺序尝试一下来源：
    ·DayMixin.day属性的值
    ·URL模式中捕获的day参数
    ·request.GET中捕获的day的值
    如果找不到有效的月份规范，则引发404
（3）get_next_day(date)
    返回包含提供日期下一个有效日期的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和
allow_future。
（4）get_previous_day(date)
    返回包含上一个有效日期的日期对象。该方法还可以返回None或者抛出一个Http404异常，取决与allow_empty和allow
_future。
"""





















