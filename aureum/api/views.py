# coding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from aureum.config import logutil
from aureum.service.riskrule_service import riskrule
logger = logutil.getLogger("view")

def index(request):
    return render(request,'index.html')


@csrf_exempt
def sel_rule(request):
    if request.method ==  "POST":
        ruleidobj = json.loads(request.body.decode())
        rule_name = ruleidobj['rule_name']
        logger.info("规则Id: %s" % rule_name)
        response_data = riskrule.sel_byrulename(rule_name);
    result = json.dumps(response_data,ensure_ascii=False)

    return  HttpResponse(result,content_type = "application/json")

@csrf_exempt
def del_rule_byid(request):
    if request.method ==  "POST":
        ruleidobj = json.loads(request.body.decode())
        ruleId = ruleidobj['id']
        logger.info("规则Id: %s" % ruleId)
        riskrule.del_byruleid(ruleId);
    result = json.dumps({},ensure_ascii=False)

    return  HttpResponse(result,content_type = "application/json")


