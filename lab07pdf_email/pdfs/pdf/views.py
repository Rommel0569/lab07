from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
             'today': "Today", 
             'amount': 1339.99,
            'customer_name': 'Cooper Mann',
            'invoice_id': 1233434,
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html',context)
        
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition']=content
            return response  

        return HttpResponse("Not Found")
