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

def about(request):
	return render_to_response('about.html', {})

def services(request):
	return render_to_response('services.html', {})

def products(request):
	retail= Category.objects.get(title__exact='retail')
	retail_object= scales.objects.filter(category=retail)
	# platform=Category.objects.get(title__exact='platforms')
	# platform_object=scales.objects.filter(category=platform)
	# hanging_scale=Category.objects.get(title__exact='hanging')
	# hanging_scale_object=scales.objects.filter(category=hanging_scale)
	# personal_weigher=Category.objects.get(title__exact='personal')
	# personal_weigher_object=scales.objects.filter(category=personal_weigher)
	# lab_scale=Category.objects.get(title__exact='labs')
	# lab_scale_object=scales.objects.filter(category=lab_scale)
	# weigh_bridges=Category.objects.get(title__exact='weighbridge')
	# weigh_bridges_object=scales.objects.filter(category=weigh_bridges)
	# crane_object=scales.objects.filter(category=hanging_scale)
	# scales_indicators=Category.objects.get(title__exact='indicators')
	# scales_indicators_object=scales.objects.filter(category=scales_indicators)
	# checking_scales=Category.objects.get(title__exact='checking')
	# checking_scales_object=scales.objects.filter(category=checking_scales)
	return render_to_response('products.html',{
		'retail_object':retail_object,
		# 'platform_object':platform_object,
		# 'hanging_scale_object':hanging_scale_object,
		# 'personal_weigher_object':personal_weigher_object,
		# 'lab_scale_object':lab_scale_object,
		# 'weigh_bridges_object':weigh_bridges_object,
		# 'crane_object':crane_object,
		# 'scales_indicators_object':scales_indicators_object,
		# 'checking_scales_object':checking_scales_object


	})

def view_more(request, slug):
	current_item=scales.objects.get(slug=slug)
	current_id=current_item.pk
	next_item=current_id+1
	last_id=scales.objects.latest('id')
	last_id=last_id.pk
	if next_item > last_id:
		next_item= scales.objects.get(id=current_id)
	else:
		next_item=scales.objects.get(id=next_item)
	previous_item=current_id-1
	if previous_item == 0:
		previous_item= scales.objects.get(id=current_id)
	else:
		previous_item=scales.objects.get(id=previous_item)

	return render_to_response('max.html',{
	'object':get_object_or_404(scales, slug=slug),
		'next_item':next_item.slug,
		'previous_item':previous_item.slug


	},RequestContext(request))
def accesories(request):
	return render_to_response('accesories.html', {})
def contact(request):
	context=RequestContext(request)

	return render_to_response('contact.html', {}, context_instance=context)
def contactus(request):
	context=RequestContext(request)
	if request.method=='POST':
		name=request.POST['name']
		from_email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']
		form=ContactForm(request.POST)
		if form.is_valid():
			try:
				send_mail(subject,message,from_email,['ben@i254.co.ke'])
			except BadHeaderError:
				print ("Invalid Header")
			#form.save(commit=False)
			print (name, subject,message)
			return contact(request)
		else:
			print (form.errors)
	else:
		form=ContactForm()
	return render_to_response('contact.html',{'form':form}, context_instance=context)
