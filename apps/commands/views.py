from django.template.loader import render_to_string
from django.http import HttpResponse 
import weasyprint


def pdf_generate_view(request):
    html_string = render_to_string('pdf/commands-base.html', {'order': 'pass'})
    html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(presentational_hints=True)
    return HttpResponse(pdf, content_type='application/pdf')
