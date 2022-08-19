import json
from django.shortcuts import render, HttpResponse
import requests
from ratelimit import limits, RateLimitException, sleep_and_retry
from datetime import datetime
import time

ONE_MINUTE = 60


# Create your views here.
def demo_url(request):
    return HttpResponse("success")


def home_url(request):
    return render(request, "index.html")


# @sleep_and_retry
@limits(calls=5, period=ONE_MINUTE)
def stack_req_url(request):
    try:
        page = "" if request.GET.get('page') is None else request.GET.get('page')
        pagesize = "" if request.GET.get('pagesize') is None else request.GET.get('pagesize')
        fromdate = "" if request.GET.get('fromdate') is None else request.GET.get('fromdate')
        todate = "" if request.GET.get('todate') is None else request.GET.get('todate')
        order = "desc" if request.GET.get('order') is None else request.GET.get('order')
        min_ = "" if request.GET.get('min') is None else request.GET.get('min')
        max_ = "" if request.GET.get('max') is None else request.GET.get('max')
        sort = "activity" if request.GET.get('sort') is None else request.GET.get('sort')
        nottagged = "" if request.GET.get('nottagged') is None else request.GET.get('nottagged')
        intitle = "" if request.GET.get('intitle') is None else request.GET.get('intitle')
        tagged = "" if request.GET.get('tagged') is None else request.GET.get('tagged')
        url = "" if request.GET.get('url') is None else request.GET.get('url')

        url = f"https://api.stackexchange.com/2.3/search/advanced?" \
              f"page={page}&" \
              f"pagesize={pagesize}&" \
              f"fromdate={fromdate}&" \
              f"todate={todate}&" \
              f"order={order}&" \
              f"min={min_}&" \
              f"max={max_}&" \
              f"sort={sort}&" \
              f"tagged={tagged}&" \
              f"nottagged={nottagged}&" \
              f"intitle={intitle}&" \
              f"site=stackoverflow"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        # print("response--------->", response.text)
        dataRes = json.loads(response.text)
        # print("dataRes-------------->", dataRes)
        if dataRes is not None:
            for item in dataRes:
                if item == "items":
                    items = dataRes[item]
            return HttpResponse(json.dumps(items))
        return HttpResponse("No Data Found")
    except Exception as e:
        print("Error ----------->", e)
        return HttpResponse(str(e))
    

