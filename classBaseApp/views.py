from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Frm_Customer


class MyView(View):

    def get(self, request):
        # only static call
        return HttpResponse('Hi this is get method in class base view.')


class CustomerView(View):
    form_class = Frm_Customer
    initial = {'key': 'value'}
    template_name = 'customer.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customer/')
        return render(request, self.template_name, {'form': form})
