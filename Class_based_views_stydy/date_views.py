# 下面的所有视图都假定定义了Article模型。
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})


# ———————————————————————————————————————————————————————————
"""
ArchiveIndexView
# ————————————————————————————
class django.views.generic.dates.ArchiveIndexView
    按日期显示“最新”对象的定级索引页面。除非设置了allow_future=True，否则不包括具有将来日期的对象。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.list.MultipleObjectMixin                         （multiple_object_mixin）
（4）django.views.generic.list.MultipleObjectTemplateResponseView          （multiple_object_mixin）
（5）django.views.generic.dates.DateMixin                                  （date_based_minx.py）
（6）django.views.generic.dates.BaseDateListView                           （date_based_minx.py）
# ————————————————————————————
上下文Context：
    除了django.views.generic.list.MultipleObjectMixin()提供的上下文外，板的上下文还包括get_dated_items()提供的
上下文：
（1）date_list：一个QuerySet对象，包含所有可用对象的年份queryset，表示为datetime.datetime对象，按照降序排列。
    注意：date_list其实是由get_dated_items()提供的
# ————————————————————————————
Notes：
（1）默认的context_object_name是latest。
（2）默认的template_name_suffix是_archive。
（3）date_list默认按年提供。可以使用date_list_period改为月或日。这也适用于所有子类视图。
# ————————————————————————————
属性：
（1）http_method_names                                                      （View）
（2）allow_empty[get_allow_empty()]                                         （BaseDateListView）
（3）model                                                                  （MultipleObjectMixin）
（4）ordering[get_ordering()]                                               （MultipleObjectMixin）
（5）paginate_by[get_paginate_by()]                                         （MultipleObjectMixin）
（6）paginate_orphans[get_paginate_orphans()]                               （MultipleObjectMixin）
（7）paginator_class                                                        （MultipleObjectMixin）
（8）queryset[get_queryset()]                                               （MultipleObjectMixin）
（9）extra_context                                                          （MultipleObjectMixin）
（10）context_object_name[get_context_object_name()]                        （MultipleObjectMixin）
（11）allow_future[get_allow_future()]                                      （DateMixin）
（12）date_field[get_date_field()]                                          （DateMixin）
（13）date_list_period[get_date_list_period()]                              （BaseDateListView）
（14）content_type                                                          （MultipleObjectTemplateResponseView）
（15）response_class[render_to_response]                                    （MultipleObjectTemplateResponseView）
（16）template_engine                                                       （MultipleObjectTemplateResponseView）
（17）template_name[get_template_names()]                                   （MultipleObjectTemplateResponseView）
（18）template_name_suffix                                                  （MultipleObjectTemplateResponseView）
# ————————————————————————————
方法：
（1）as_view()                                                              （View）
（2）dispatch()                                                             （View）
（3）paginate_queryset()                                                    （View）
（4）setup()                                                                （View）
（5）http_method_not_allowed()                                              （View）
（6）get_paginator()                                                        （MultipleObjectMixin）
（7）get_context_data()                                                     （MultipleObjectMixin）
（8）get_date_list()                                                        （BaseDateListView）
（9）get_date_items()                                                       （BaseArchiveIndexView）
（10）get_dated_queryset()                                                  （BaseDateListView）
（11）render_to_response()                                                  （MultipleObjectTemplateResponseView）
（12）get()
（13）head()
# ————————————————————————————
注意：
如果不自定义get_context_data,那么ArchiveIndex的上下文中会包含date_list,如果自定义get_context_data，那么上下文
中没有date_list，原因是它super()的是MutipleObjectMixin的get_context_data，这个是时候想要用date_list，就需要通过
date_list = self.get_date_items()[0]来定义。对于接下来的几个View，他们有一些上下文也是需要这样定义
"""

# ——————————————————————————————————————————————————————————
"""
YearArchiveView
# ————————————————————————————
class django.views.generic.dates.YearArchiveView
    每年存档页面，显示给定年份中的所有可用月份。除非设置了allow_future=True，否则不包括具有将来日期的对象。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.list.MultipleObjectMixin                         （multiple_object_mixin）
（4）django.views.generic.list.MultipleObjectTemplateResponseView          （multiple_object_mixin）
（5）django.views.generic.dates.DateMixin                                  （date_based_minx.py）
（6）django.views.generic.dates.BaseDateListView                           （date_based_minx.py）
（7）django.views.generic.dates.YearMixin                                  （date_based_minx.py）
# ————————————————————————————
上下文Context：
    除了django.views.generic.list.MultipleObjectMixin()提供的上下文外，模板的上下文还包括get_dated_items()提供的
上下文,year、next_year、previous_year是get_dated_items()返回三元组的第3个元素（是一个字典）中的键：：
（1）date_list：一个QuerySet对象，包含所有可用对象的月份queryset，表示为datetime.datetime对象，按照升序排列。
（2）year：表示给定年份的date对象。
（3）next_year：一个代表明年第一天的date对象，根据allow_empty和allow_future来确定。
（4）previous_year：一个代表去年第一天的date对象，根据allow_empty和allow_future来确定。
# ————————————————————————————
Notes：
（1）默认的template_name_suffix是_archive_year。
# ————————————————————————————
属性：
（1）make_object_list
    一个布尔值，指定是否检索今年的完整对象列表并将其传递给模板。如果是True，对象列表将可用于上下文。如果是False，查询
集None将会用作对象列表。
    默认情况下是False。这个时候，上下文中就没有object_list，即便定义了属性context_object_name。
（2）http_method_names                                                      （View）
（3）allow_empty[get_allow_empty()]                                         （MultipleObjectMixin）
（4）model                                                                  （MultipleObjectMixin）
（5）ordering[get_ordering()]                                               （MultipleObjectMixin）
（6）paginate_by[get_paginate_by()]                                         （MultipleObjectMixin）
（7）paginate_orphans[get_paginate_orphans()]                               （MultipleObjectMixin）
（8）paginator_class                                                        （MultipleObjectMixin）
（9）queryset[get_queryset()]                                               （MultipleObjectMixin）
（10）extra_context                                                         （MultipleObjectMixin）
（11）context_object_name[get_context_object_name()]                        （MultipleObjectMixin）
（12）allow_future[get_allow_future()]                                      （DateMixin）
（13）date_field[get_date_field()]                                          （DateMixin）
（14）date_list_period[get_date_list_period()]                              （BaseDateListView）
（15）content_type                                                          （MultipleObjectTemplateResponseView）
（16）response_class[render_to_response]                                    （MultipleObjectTemplateResponseView）
（17）template_engine                                                       （MultipleObjectTemplateResponseView）
（18）template_name[get_template_names()]                                   （MultipleObjectTemplateResponseView）
（19）template_name_suffix                                                  （MultipleObjectTemplateResponseView）
（20）year[get_year()]                                                      （YearMixin）
（21）year_format[get_year_format()]                                        （YearMixin）
# ————————————————————————————
方法：
（1）get_make_object_list()
    确定是否将对象列表作为上下文的一部分返回。
    默认返回属性make_object_list的值。
（2）as_view()                                                              （View）
（3）dispatch()                                                             （View）
（4）http_method_not_allowed()                                              （View）
（5）setup()                                                                （View）
（6）paginate_queryset()                                                    （MultipleObjectMixin）
（7）get_paginator()                                                        （MultipleObjectMixin）
（8）get_context_data()                                                     （MultipleObjectMixin）
（9）get_date_list()                                                        （BaseDateListView）
（10）get_date_items()                                                      （BaseYearArchiveView）
（11）get_dated_queryset()                                                  （BaseDateListView）
（12）render_to_response()                                                  （MultipleObjectTemplateResponseView）
（13）get_year_format()                                                     （YearMixin）
（14）get_year()                                                            （YearMixin）
（15）get_next_year(date)                                                   （YearMixin）
（16）get_previous_year(date)                                               （YearMixin）
（17）get()
（18）head()
"""
# ——————————————————————————————————————————————————————————
"""
MonthArchiveView
class django.views.generic.dates.MonthArchiveView
    每月存档页面，显示给定月份中的所有对象。除非设置为allow_future=True， 否则不会显示具有将来日期的对象。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.list.MultipleObjectMixin                         （multiple_object_mixin）
（4）django.views.generic.list.MultipleObjectTemplateResponseView          （multiple_object_mixin）
（5）django.views.generic.dates.DateMixin                                  （date_based_minx.py）
（6）django.views.generic.dates.BaseDateListView                           （date_based_minx.py）
（7）django.views.generic.dates.YearMixin                                  （date_based_minx.py）
（8）django.views.generic.dates.MonthMixin                                 （date_based_minx.py）
# ————————————————————————————
上下文Context：
    除了django.views.generic.list.MultipleObjectMixin()提供的上下文外，板的上下文还包括get_dated_items()提供的
上下文。其中month、next_month、previous_month是get_dated_items()返回三元组的第3个元素（是一个字典）中的键：
（1）date_list：一个QuerySet对象，包含在给定月份内具有对象的所有日期，表示为datetime.datetime对象，按照升序排列。
（2）month：表示给定月份的date对象。
（3）next_month：一个代表下个月第一天的date对象，根据allow_empty和allow_future来确定。
（4）previous_month：一个代表上个月第一天的date对象，根据allow_empty和allow_future来确定。
# ————————————————————————————
Notes：
（1）默认的template_name_suffix是_archive_month。
# ————————————————————————————
属性：
（1）http_method_names                                                      （View）
（2）allow_empty[get_allow_empty()]                                         （MultipleObjectMixin）
（3）model                                                                  （MultipleObjectMixin）
（4）ordering[get_ordering()]                                               （MultipleObjectMixin）
（5）paginate_by[get_paginate_by()]                                         （MultipleObjectMixin）
（6）paginate_orphans[get_paginate_orphans()]                               （MultipleObjectMixin）
（7）paginator_class                                                        （MultipleObjectMixin）
（8）queryset[get_queryset()]                                               （MultipleObjectMixin）
（9）extra_context                                                          （MultipleObjectMixin）
（10）context_object_name[get_context_object_name()]                        （MultipleObjectMixin）
（11）allow_future[get_allow_future()]                                      （DateMixin）
（12）date_field[get_date_field()]                                          （DateMixin）
（13）date_list_period[get_date_list_period()]                              （BaseDateListView）
（14）content_type                                                          （MultipleObjectTemplateResponseView）
（15）response_class[render_to_response]                                    （MultipleObjectTemplateResponseView）
（16）template_engine                                                       （MultipleObjectTemplateResponseView）
（17）template_name[get_template_names()]                                   （MultipleObjectTemplateResponseView）
（18）template_name_suffix                                                  （MultipleObjectTemplateResponseView）
（19）year[get_year()]                                                      （YearMixin）
（20）year_format[get_year_format()]                                        （YearMixin）
（21）month[get_month()]                                                    （MonthMixin）
（22）month_format[get_month_format()]                                      （MonthMixin）
# ————————————————————————————
方法：
（1）as_view()                                                              （View）
（2）dispatch()                                                             （View）
（3）http_method_not_allowed()                                              （View）
（4）setup()                                                                （View）
（5）paginate_queryset()                                                    （MultipleObjectMixin）
（6）get_paginator()                                                        （MultipleObjectMixin）
（7）get_context_data()                                                     （MultipleObjectMixin）
（8）get_date_list()                                                        （BaseDateListView）
（9）get_date_items()                                                       （BaseDateListView）
    返回
（10）get_dated_queryset()                                                  （BaseDateListView）
（11）render_to_response()                                                  （MultipleObjectTemplateResponseView）
（14）get_next_year(date)                                                   （YearMixin）
（15）get_previous_year(date)                                               （YearMixin）
（16）get_previous_month(date)                                              （MonthMixin）
（17）get_next_month(date)                                                  （MonthMixin）
（18）get()
（19）head()
"""
# ——————————————————————————————————————————————————————————
"""
WeekArchiveView
# ————————————————————————————
class django.views.generic.dates.WeekArchiveView
    每周存档页面，显示给定周内的所有对象。除非设置allow_future=True， 否则不会显示具有将来日期的对象。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.list.MultipleObjectMixin                         （multiple_object_mixin）
（4）django.views.generic.list.MultipleObjectTemplateResponseView          （multiple_object_mixin）
（5）django.views.generic.dates.DateMixin                                  （date_based_minx.py）
（6）django.views.generic.dates.BaseDateListView                           （date_based_minx.py）
（7）django.views.generic.dates.YearMixin                                  （date_based_minx.py）
（8）django.views.generic.dates.WeekMixin                                  （date_based_minx.py）
# ————————————————————————————
上下文Context：
    除了django.views.generic.list.MultipleObjectMixin()提供的上下文外，板的上下文还包括get_dated_items()提供的
上下文。其中week、next_week、previous_week是get_dated_items()返回三元组的第3个元素（是一个字典）中的键，同时这个三元组
第一个元素是None：
（1）week：表示给定周的第一天的date对象。
（2）next_week：一个代表下个周第一天的date对象，根据allow_empty和allow_future来确定。
（3）previous_week：一个代表上个周第一天的date对象，根据allow_empty和allow_future来确定。
# ————————————————————————————
Notes：
（1）默认的template_name_suffix是_archive_week。
（2）属性week_format是解析州的strptime()格式化字符串。支持以下值：
    ·"%U"：基于美国周系统，周从星期日开始。这是默认值。
    ·"%W"：假设一周从星期一开始。
# ————————————————————————————
属性：
（1）http_method_names                                                      （View）
（2）allow_empty[get_allow_empty()]                                         （MultipleObjectMixin）
（3）model                                                                  （MultipleObjectMixin）
（4）ordering[get_ordering()]                                               （MultipleObjectMixin）
（5）paginate_by[get_paginate_by()]                                         （MultipleObjectMixin）
（6）paginate_orphans[get_paginate_orphans()]                               （MultipleObjectMixin）
（7）paginator_class                                                        （MultipleObjectMixin）
（8）queryset[get_queryset()]                                               （MultipleObjectMixin）
（9）extra_context                                                          （MultipleObjectMixin）
（10）context_object_name[get_context_object_name()]                        （MultipleObjectMixin）
（11）allow_future[get_allow_future()]                                      （DateMixin）
（12）date_field[get_date_field()]                                          （DateMixin）
（13）date_list_period[get_date_list_period()]                              （BaseDateListView）
（14）content_type                                                          （MultipleObjectTemplateResponseView）
（15）response_class[render_to_response]                                    （MultipleObjectTemplateResponseView）
（16）template_engine                                                       （MultipleObjectTemplateResponseView）
（17）template_name[get_template_names()]                                   （MultipleObjectTemplateResponseView）
（18）template_name_suffix                                                  （MultipleObjectTemplateResponseView）
（19）year[get_year()]                                                      （YearMixin）
（20）year_format[get_year_format()]                                        （YearMixin）
（21）week[get_week()]                                                      （WeekMixin）
（22）week[get_week_format()]                                               （WeekMixin）
# ————————————————————————————
方法：
（1）as_view()                                                              （View）
（2）dispatch()                                                             （View）
（3）http_method_not_allowed()                                              （View）
（4）setup()                                                                （View）
（5）paginate_queryset()                                                    （MultipleObjectMixin）
（6）get_paginator()                                                        （MultipleObjectMixin）
（7）get_context_data()                                                     （MultipleObjectMixin）
（8）get_date_list()                                                        （BaseDateListView）
（9）get_date_items()                                                       （BaseDateListView）
（10）get_dated_queryset()                                                  （BaseDateListView）
（11）render_to_response()                                                  （MultipleObjectTemplateResponseView）
（14）get_next_year(date)                                                   （YearMixin）
（15）get_previous_year(date)                                               （YearMixin）
（16）get_previous_week(date)                                               （WeekMixin）
（17）get_next_week(date)                                                   （WeekMixin）
（18）get()
（19）head()
# ————————————————————————————
注意：
如果不重写get_context_data()，那么上下week是一个日期，如果重写，那么week将根据get_week()获取值，可能会是整数，代表周。
"""
# ——————————————————————————————————————————————————————————
"""
DayArchiveView
# ————————————————————————————
class django.views.generic.dates.DayArchiveView
    日期存档页面，显示给定日期内的所有对象。除非设置allow_future=True， 否则将来的天数会抛出404错误，无论将来是否有任何对象。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.list.MultipleObjectMixin                         （multiple_object_mixin）
（4）django.views.generic.list.MultipleObjectTemplateResponseView          （multiple_object_mixin）
（5）django.views.generic.dates.DateMixin                                  （date_based_minx.py）
（6）django.views.generic.dates.BaseDateListView                           （date_based_minx.py）
（7）django.views.generic.dates.YearMixin                                  （date_based_minx.py）
（8）django.views.generic.dates.MonthMixin                                 （date_based_minx.py）
（9）django.views,generic.dates.DayMixin                                   （date_based_minx.py）
# ————————————————————————————
上下文Context：
    除了django.views.generic.list.MultipleObjectMixin()提供的上下文外，模板的上下文还包括：
（1）day：表示给定日期的date对象。
（2）next_day：一个代表下一天的date对象，根据allow_empty和allow_future来确定。
（3）previous_day：一个代表上一天的date对象，根据allow_empty和allow_future来确定。
（4）next_month：一个代表下个月第一天的date对象，根据allow_empty和allow_future来确定。
（5）previous_month：一个代表上个月第一天的date对象，根据allow_empty和allow_future来确定。
# ————————————————————————————
Notes：
（1）默认的template_name_suffix是_archive_day。
# ————————————————————————————
属性：
（1）http_method_names                                                      （View）
（2）allow_empty[get_allow_empty()]                                         （MultipleObjectMixin）
（3）model                                                                  （MultipleObjectMixin）
（4）ordering[get_ordering()]                                               （MultipleObjectMixin）
（5）paginate_by[get_paginate_by()]                                         （MultipleObjectMixin）
（6）paginate_orphans[get_paginate_orphans()]                               （MultipleObjectMixin）
（7）paginator_class                                                        （MultipleObjectMixin）
（8）queryset[get_queryset()]                                               （MultipleObjectMixin）
（9）extra_context                                                          （MultipleObjectMixin）
（10）context_object_name[get_context_object_name()]                        （MultipleObjectMixin）
（11）allow_future[get_allow_future()]                                      （DateMixin）
（12）date_field[get_date_field()]                                          （DateMixin）
（13）date_list_period[get_date_list_period()]                              （BaseDateListView）
（14）content_type                                                          （MultipleObjectTemplateResponseView）
（15）response_class[render_to_response]                                    （MultipleObjectTemplateResponseView）
（16）template_engine                                                       （MultipleObjectTemplateResponseView）
（17）template_name[get_template_names()]                                   （MultipleObjectTemplateResponseView）
（18）template_name_suffix                                                  （MultipleObjectTemplateResponseView）
（19）year[get_year()]                                                      （YearMixin）
（20）year_format[get_year_format()]                                        （YearMixin）
（21）month[get_month()]                                                    （MonthMixin）
（22）month_format[get_month_format()]                                      （MonthMixin）
（23）day[get_day()]                                                        （DayMixin）    
（24）day_format[get_day_format()]                                          （DayMixin）
# ————————————————————————————
方法：
（1）as_view()                                                              （View）
（2）dispatch()                                                             （View）
（3）http_method_not_allowed()                                              （View）
（4）setup()                                                                （View）
（5）paginate_queryset()                                                    （MultipleObjectMixin）
（6）get_paginator()                                                        （MultipleObjectMixin）
（7）get_context_data()                                                     （MultipleObjectMixin）
（8）get_date_list()                                                        （BaseDateListView）
（9）get_date_items()                                                       （BaseDateListView）
（10）get_dated_queryset()                                                  （BaseDateListView）
（11）render_to_response()                                                  （MultipleObjectTemplateResponseView）
（14）get_next_year(date)                                                   （YearMixin）
（15）get_previous_year(date)                                               （YearMixin）
（16）get_previous_month(date)                                              （MonthMixin）
（17）get_next_v(date)                                                      （MonthMixin）
（18）get_previous_day(date)                                                （DayMixin）
（19）get_next_day(date)                                                    （DayMixin）
（18）get()
（19）head()
"""
# ——————————————————————————————————————————————————————————
"""
TodayArchiveView
# ————————————————————————————
class django.views.generic.dates.TodayArchiveView
    日期存档页面，显示今天的的所有对象。和django.views.generic.dates.DayArchiveView完全相同，除了用今天的日期代替year/month/
day。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.list.MultipleObjectMixin                         （multiple_object_mixin）
（4）django.views.generic.list.MultipleObjectTemplateResponseView          （multiple_object_mixin）
（5）django.views.generic.dates.DateMixin                                  （date_based_minx.py）
（6）django.views.generic.dates.BaseDateListView                           （date_based_minx.py）
（7）django.views.generic.dates.YearMixin                                  （date_based_minx.py）
（8）django.views.generic.dates.MonthMixin                                 （date_based_minx.py）
（9）django.views,generic.dates.DayMixin                                   （date_based_minx.py）
# ————————————————————————————
上下文Context：
    除了django.views.generic.list.MultipleObjectMixin()提供的上下文外，模板的上下文还包括：
（1）day：表示给定日期的date对象。
（2）next_day：一个代表下一天的date对象，根据allow_empty和allow_future来确定。
（3）previous_day：一个代表上一天的date对象，根据allow_empty和allow_future来确定。
（4）next_month：一个代表下个月第一天的date对象，根据allow_empty和allow_future来确定。
（5）previous_month：一个代表上个月第一天的date对象，根据allow_empty和allow_future来确定。
# ————————————————————————————
Notes：
（1）默认的template_name_suffix是_archive_day。
# ————————————————————————————
属性：
（1）http_method_names                                                      （View）
（2）allow_empty[get_allow_empty()]                                         （MultipleObjectMixin）
（3）model                                                                  （MultipleObjectMixin）
（4）ordering[get_ordering()]                                               （MultipleObjectMixin）
（5）paginate_by[get_paginate_by()]                                         （MultipleObjectMixin）
（6）paginate_orphans[get_paginate_orphans()]                               （MultipleObjectMixin）
（7）paginator_class                                                        （MultipleObjectMixin）
（8）queryset[get_queryset()]                                               （MultipleObjectMixin）
（9）extra_context                                                          （MultipleObjectMixin）
（10）context_object_name[get_context_object_name()]                        （MultipleObjectMixin）
（11）allow_future[get_allow_future()]                                      （DateMixin）
（12）date_field[get_date_field()]                                          （DateMixin）
（13）date_list_period[get_date_list_period()]                              （BaseDateListView）
（14）content_type                                                          （MultipleObjectTemplateResponseView）
（15）response_class[render_to_response]                                    （MultipleObjectTemplateResponseView）
（16）template_engine                                                       （MultipleObjectTemplateResponseView）
（17）template_name[get_template_names()]                                   （MultipleObjectTemplateResponseView）
（18）template_name_suffix                                                  （MultipleObjectTemplateResponseView）
（19）year[get_year()]                                                      （YearMixin）
（20）year_format[get_year_format()]                                        （YearMixin）
（21）month[get_month()]                                                    （MonthMixin）
（22）month_format[get_month_format()]                                      （MonthMixin）
（23）day[get_day()]                                                        （DayMixin）    
（24）day_format[get_day_format()]                                          （DayMixin）
# ————————————————————————————
方法：
（1）as_view()                                                              （View）
（2）dispatch()                                                             （View）
（3）http_method_not_allowed()                                              （View）
（4）setup()                                                                （View）
（5）paginate_queryset()                                                    （MultipleObjectMixin）
（6）get_paginator()                                                        （MultipleObjectMixin）
（7）get_context_data()                                                     （MultipleObjectMixin）
（8）get_date_list()                                                        （BaseDateListView）
（9）get_date_items()                                                       （BaseDateListView）
（10）get_dated_queryset()                                                  （BaseDateListView）
（11）render_to_response()                                                  （MultipleObjectTemplateResponseView）
（14）get_next_year(date)                                                   （YearMixin）
（15）get_previous_year(date)                                               （YearMixin）
（16）get_previous_month(date)                                              （MonthMixin）
（17）get_next_v(date)                                                      （MonthMixin）
（18）get_previous_day(date)                                                （DayMixin）
（19）get_next_day(date)                                                    （DayMixin）
（18）get()
（19）head()
"""
# ——————————————————————————————————————————————————————————
"""
DateDetailView
# ————————————————————————————
class django.views.generic.dates.DateDetailView
    表示单个对象的页面。如果对象具有将来日期，则默认情况下抛出404错误，除非设置allow_future=Ture。
# ————————————————————————————
祖先：
（1）django.views.generic.base.View                                        （base_view.py）
（2）django.views.generic.base.TemplateResponseMixin                       （base_view.py）
（3）django.views.generic.detail.SingleObjectMixin                         （single_object_mixins.py）
（4）django.views.generic.detail.SingleObjectTemplateResponseMixin         （single_object_mixins.py）
（5）django.views.generic.dates.DateMixin                                  （date_based_mixin.py）
（6）django.views.generic.dates.YearMixin                                  （date_based_mixin.py）
（7）django.views.generic.dates.MonthMixin                                 （date_based_mixin.py）
（8）django.views,generic.dates.DayMixin                                   （date_based_mixin.py）
# ————————————————————————————
上下文Context：
（1）包括在DateDetailView中指定的与model关联的单个对象。
# ————————————————————————————
Notes：
（1）使用默认template_name_suffix的_detail。
# ————————————————————————————
属性：
（1）http_method_names                                                      （View）
（2）context_object_name[get_context_object_name]                           （SingleObjectMixin）
（3）extra_context                                                          （SingleObjectMixin）
（4）model                                                                  （SingleObjectMixin）
（4）pk_url_kwarg                                                           （SingleObjectMixin）
（5）queryset[get_queryset()]                                               （SingleObjectMixin）
（6）slug_field[get_slug_field()]                                           （SingleObjectMixin）
（7）slug_url_kwarg                                                         （SingleObjectMixin）
（8）response_class[render_to_response()]                                   （SingleObjectTemplateResponseMixin）
（9）template_engine                                                        （SingleObjectTemplateResponseMixin）
（10）content_type                                                          （SingleObjectTemplateResponseMixin）             
（11）template_name [get_template_names()]                                  （SingleObjectTemplateResponseMixin）
（12）template_name_field                                                   （SingleObjectTemplateResponseMixin）
（13）template_name_suffix                                                  （SingleObjectTemplateResponseMixin）
（14）allow_future[get_allow_future()]                                      （DateMixin）
（15）date_field[get_date_field()]                                          （DateMixin）
（16）date_list_period[get_date_list_period()]                              （BaseDateListView）
（17）year[get_year()]                                                      （YearMixin）
（18）year_format[get_year_format()]                                        （YearMixin）
（19）month[get_month()]                                                    （MonthMixin）
（20）month_format[get_month_format()]                                      （MonthMixin）
（21）day[get_day()]                                                        （DayMixin）    
（22）day_format[get_day_format()]                                          （DayMixin）
# ————————————————————————————
方法：
（1）as_view()                                                              （View）
（2）dispatch()                                                             （View）
（3）http_method_not_allowed()                                              （View）
（4）setup()                                                                （View）
（5）get_object()                                                           （SingleObjectMixin）      
（6）get_context_data()                                                     （SingleObjectMixin）
（7）render_to_response()                                                   （SingleObjectTemplateResponseMixin）
（8）get_next_year(date)                                                    （YearMixin）
（9）get_previous_year(date)                                                （YearMixin）
（10）get_previous_month(date)                                              （MonthMixin）
（11）get_next_v(date)                                                      （MonthMixin）
（12）get_previous_day(date)                                                （DayMixin）
（13）get_next_day(date)                                                    （DayMixin）
（14）get()
（15）head()
"""








