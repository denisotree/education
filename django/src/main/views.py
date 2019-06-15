from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


def index(request):
    template = get_template(
        'main/index.html'
    )
    context = {
        'name': 'Denis'
    }
    return HttpResponse(
        template.render(context)
    )


def about(request):
    return render(
        request,
        'main/about.html',
        {
            'about_text': 'Info about company'
        }
    )


def contacts(request):
    rendered_page = render_to_string(
        'main/contacts.html',
        {
            'contacts': [
                'Contact 1',
                'Contact 2',
                'Contact 3',
                'Contact 4',
                'Contact 5',
                'Contact 6',
                'Contact 7',
            ]
        }
    )
    return HttpResponse(rendered_page)
