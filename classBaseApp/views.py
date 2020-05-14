from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Frm_Customer
from .models import customerModal
from django.views.generic import ListView
import logging

# Get an instance of a logger
logger = logging.getLogger('mylog')


class MyView(View):

    def get(self, request):
        # only static call
        response = """
                    Hi this is get method in class base view.
                """
        return HttpResponse(response)


class CustomerView(View):
    form_class = Frm_Customer
    initial = {'key': 'value'}
    template_name = 'customer.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        objects = customerModal.objects.all()
        logger.info("Test")
        return render(request, self.template_name, {'form': form, 'objects': objects})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customer/')
        logger.error('Something went wrong!')
        return render(request, self.template_name, {'form': form})


class CustomerListView(ListView):
    model = customerModal

