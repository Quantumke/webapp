from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from app.models import *
from app.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from  django.conf import settings


# Create your views here.

def home(request):
	retail= Category.objects.get(title__exact='retail')
	retail_object= scales.objects.filter(category=retail)
	platform=Category.objects.get(title__exact='platforms')
	platform_object=scales.objects.filter(category=platform)
	hanging_scale=Category.objects.get(title__exact='hanging')
	hanging_scale_object=scales.objects.filter(category=hanging_scale)
	personal_weigher=Category.objects.get(title__exact='personal')
	personal_weigher_object=scales.objects.filter(category=personal_weigher)
	lab_scale=Category.objects.get(title__exact='labs')
	lab_scale_object=scales.objects.filter(category=lab_scale)
	weigh_bridges=Category.objects.get(title__exact='weighbridge')
	weigh_bridges_object=scales.objects.filter(category=weigh_bridges)
	crane_object=scales.objects.filter(category=hanging_scale)
	scales_indicators=Category.objects.get(title__exact='indicators')
	scales_indicators_object=scales.objects.filter(category=scales_indicators)
	checking_scales=Category.objects.get(title__exact='checking')
	checking_scales_object=scales.objects.filter(category=checking_scales)
	return render_to_response('index.html',{
		'retail_object':retail_object,
		'platform_object':platform_object,
		'hanging_scale_object':hanging_scale_object,
		'personal_weigher_object':personal_weigher_object,
		'lab_scale_object':lab_scale_object,
		'weigh_bridges_object':weigh_bridges_object,
		'crane_object':crane_object,
		'scales_indicators_object':scales_indicators_object,
		'checking_scales_object':checking_scales_object


	})


