from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, \
    DayArchiveView, TodayArchiveView, DateDetailView
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from .models import Blog, Author
from .forms import BlogForm


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world!")


class BlogTemplateView(TemplateView):
    template_name = "myApp/template_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lastest_blog'] = Blog.objects.all()[:5]
        print("get_context_data:")
        print(type(context))
        print(context)
        print("---------")
        return context

    def get_template_names(self):
        a = super().get_template_names()
        print("get_template_names:")
        print(type(a))
        print(a)
        print("---------")
        return a

    def render_to_response(self, context, **response_kwargs):
        a = super().render_to_response(context, **response_kwargs)
        print("render_to_response:")
        print(type(a))
        print(a)
        print("---------")
        return a


class BlogRedirectView(RedirectView):
    # 如果url.py中as_view(url="...")或者定义了属性url,会覆盖掉这里的pattern_name。
    pattern_name = "myApp:view"
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        print("这里可以做任何事情")
        a = super().get_redirect_url(*args, **kwargs)
        print(type(a))
        print(a)
        return a


class BlogDetailView(DetailView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = "myApp/detail_view.html"
    context_object_name = "blog"

    def get_queryset(self):
        # 会覆盖掉属性queryset和model
        self.queryset = Blog.objects.filter(pk__gte=1)
        print("get_queryset")
        a = super().get_queryset()
        print(type(a))
        print(a)
        print("---------")
        return self.queryset

    def get_context_object_name(self, obj):
        print("get_context_object_name")
        a = super().get_context_object_name(obj)
        print(type(a))
        print(a)
        print("---------")
        return a

    def get_object(self, queryset=None):
        print("get_object")
        a = super().get_object()
        print(type(a))
        print(a)
        print("---------")
        return a

    def get_context_data(self, **kwargs):
        print("get_context_data")
        a = super().get_context_data(**kwargs)
        print(type(a))
        print(a)
        print("---------")
        return a

    def get_template_names(self):
        a = super().get_template_names()
        print("get_template_names")
        print(type(a))
        print(a)
        print("---------")
        return a


def my_paginator(context):
    # 创建分页
    paginator = context['paginator']
    page = context['page_obj']
    # 显示页码
    current_page_num = page.number
    if paginator.num_pages < 7:
        page_range = paginator.page_range
    else:
        if current_page_num < 5:
            page_range = range(1, 8)
        elif 5 <= current_page_num <= paginator.num_pages - 3:
            page_range = range(current_page_num - 3, current_page_num + 4)
        elif current_page_num > paginator.num_pages - 3:
            page_range = range(paginator.num_pages - 6, paginator.num_pages + 1)
    context['page_range'] = page_range
    return context


class BlogListView(ListView):
    queryset = Blog.objects.all()
    paginate_by = 5
    context_object_name = "blogs"
    ordering = "-created_time"
    template_name = "myApp/list_view.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = my_paginator(context)
        return context


class BlogFormView(FormView):
    initial = {}
    form_class = BlogForm
    success_url = reverse_lazy("myApp:list_view")
    template_name = "myApp/form_view.html"

    def form_valid(self, form):
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        pk = form.cleaned_data['author']
        author = Author.objects.get(pk=pk)
        Blog.objects.create(title=title, text=text, author=author)
        return super().form_valid(form)

    def get_form(self, form_class=None):
        print("get_form:")
        a = super().get_form()
        print(a)
        return a

    def get_form_kwargs(self):
        print("get_form_kwargs")
        a = super().get_form_kwargs()
        print(a)
        return a


class BlogCreateView(CreateView):
    model = Blog
    success_url = reverse_lazy("myApp:list_view")
    template_name = "myApp/form_view.html"
    fields = ['title', 'author', 'text']


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'text', 'author']
    template_name = "myApp/form_view.html"

    def get_success_url(self):
        return reverse_lazy("myApp:detail_view", kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        a = super().get_context_data()
        print(a)
        print(self.kwargs)
        return a


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("myApp:list_view")
    template_name = "myApp/form_view.html"

    def get_context_data(self, **kwargs):
        a = super().get_context_data()
        print(a)
        return a


class BlogArchiveIndexView(ArchiveIndexView):
    model = Blog
    date_field = "created_time"
    context_object_name = "latest_blogs"
    template_name = "myApp/archive_index_view.html"
    paginate_by = 5
    allow_future = False
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = my_paginator(context)
        context['date_list'] = self.get_dated_items()[0]
        return context


class BlogYearArchiveView(YearArchiveView):
    model = Blog
    template_name = "myApp/year_archive_view.html"
    allow_empty = True
    paginate_by = 5
    date_field = "created_time"
    context_object_name = "blogs"
    make_object_list = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = my_paginator(context)
        context['year'] = self.get_year()
        context['date_list'] = self.get_dated_items()[0]
        return context


class BlogMonthArchiveView(MonthArchiveView):
    model = Blog
    paginate_by = 5
    allow_future = False
    allow_empty = True
    template_name = "myApp/month_archive_view.html"
    date_field = 'created_time'
    month_format = "%m"
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = my_paginator(context)
        context["year"] = self.get_year()
        context["month"] = self.get_month()
        context["date_list"] = self.get_dated_items()[0]
        return context


class BlogWeekArchiveView(WeekArchiveView):
    model = Blog
    date_field = "created_time"
    allow_empty = True
    allow_future = False
    paginate_by = 5
    template_name = "myApp/week_archive_view.html"
    week_format = "%W"
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = my_paginator(context)
        context["year"] = self.get_year()
        context["week"] = self.get_week()
        return context


class BlogDayArchiveView(DayArchiveView):
    model = Blog
    paginate_by = 5
    context_object_name = "blogs"
    date_field = "created_time"
    allow_future = False
    allow_empty = True
    month_format = "%m"

    template_name = "myApp/day_archive_view.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = my_paginator(context)
        context['year'] = self.get_year()
        context['month'] = self.get_month()
        context['day'] = self.get_day()
        print(context)
        return context


class BlogTodayArchiveView(TodayArchiveView):
    model = Blog
    date_field = "created_time"
    context_object_name = "blogs"
    template_name = "myApp/today.html"
    allow_empty = True
    allow_future = False


class BlogDateDetailView(DateDetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "myApp/detail_view.html"














