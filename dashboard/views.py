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
        """
        GET api/chart/data return JSON:

                     article_labels: x
                     article_data: y

                     """
        # empty dict to take all data and return like response
        dataset = dict()
        # take from DashboardData all to send in front
        for data in DashboardData.objects.all():
            dataset[data.data_x] = data.data_y

        # sorted dict
        data_set = sorted(dataset.items(), key=lambda x: x[1])
        # change type from list --> dict again
        data_set = dict(data_set)

        # represent dict data_set like JSON 
        data = {
            "article_labels": data_set.keys(),
            "article_data": data_set.values(),
        }
        
        # return response
        return Response(data)


### dash ###

def dash(request, **kwargs):
    return Response(dispatcher(request))


@csrf_exempt
def dash_ajax(request):
    return HttpResponse(dispatcher(request), content_type='application/json')
