# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554917516.6291986
_enable_loop = True
_template_filename = 'C:/Users/grant/Desktop/INTEXtwo/infinite-atoll-72014/hello/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        utc_time = context.get('utc_time', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        utc_time = context.get('utc_time', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Congratulations -- you\'ve successfully created a new DMP app!</h3>\r\n        <h4 class="utc-time">Current time in UTC: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( utc_time ))
        __M_writer('</h4>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/grant/Desktop/INTEXtwo/infinite-atoll-72014/hello/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 8, "49": 3, "57": 3, "58": 6, "59": 6, "65": 59}}
__M_END_METADATA
"""
