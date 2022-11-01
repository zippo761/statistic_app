from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .as_dash import dispatcher
from .models import DashboardData



def company_article_list(request):
    return render(request, "plotly.html", {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        dataset = dict()
        for data in DashboardData.objects.all():
            dataset[data.data_x] = data.data_y

        data_set = sorted(dataset.items(), key=lambda x: x[1])
        data_set = dict(data_set)

        data = {
            "article_labels": data_set.keys(),
            "article_data": data_set.values(),
        }

        return Response(data)


### dash ###

def dash(request, **kwargs):
    return Response(dispatcher(request))


@csrf_exempt
def dash_ajax(request):
    return HttpResponse(dispatcher(request), content_type='application/json')
