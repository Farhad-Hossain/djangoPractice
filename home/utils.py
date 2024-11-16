from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render

def hx_render(request, template, context={}):

    if request.headers.get('HX-Request'):
        is_hx_request = True
    else:
        is_hx_request = False

    response_string = render_to_string(template, request=request, context=context)

    if is_hx_request:
        return HttpResponse(response_string)
    else:
        context['page_content'] = response_string
        return render(request, 'global_template.html', context)