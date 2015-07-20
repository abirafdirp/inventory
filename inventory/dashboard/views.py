from django.views.generic import View
from django.shortcuts import render


class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

