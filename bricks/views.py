import json
from django.core import serializers
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django import template
from django.db.models import Count, Q
from django.db import connection
from bricks.models import thebricks
from bricks.forms import thebricksForm
register = template.Library()
import matplotlib
import MySQLdb
from django.views.generic import *
from json import dumps
from django.http import JsonResponse

def index(request):
	return render(request, 'bricks/index.html')

def bricksize(request):
	datasetLength = thebricks.objects.values('brick_length') \
		.annotate(size_count=Count('brick_length', filter=Q(brick_length=True))) \
		.order_by('brick_length')

	datasetHeight = thebricks.objects.values('brick_height') \
		.annotate(size_count=Count('brick_height', filter=Q(brick_height=True))) \
		.order_by('brick_height')

	categories = list()

	for entry in datasetHeight:
		categories.append('%s Class' % entry['brick_height'])

	for entry in datasetLength:
		categories.append('%s Class' % entry['brick_length'])

	return render(request, 'bricks/size.html', {
		'categories': json.dumps(categories),
	})

def bricktype(request):
	dataset = thebricks.objects.values('brick_type') \
		.order_by('brick_type')

	categories = list()

	for entry in dataset:
		categories.append('%s Class' % entry['brick_type'])

	return render(request, 'bricks/type.html', {
		'categories': json.dumps(categories)
	})

def brickcolor(request):
	dataset = thebricks.objects.values('my_color') \
		.annotate(color_count=Count('my_color', filter=Q(my_color=True))) \
		.order_by('my_color')

	categories = list()
	survived_series = list()
	not_survived_series = list()

	for entry in dataset:
		categories.append('%s Class' % entry['my_color'])
		survived_series.append(entry['color_count'])

	return render(request, 'bricks/color.html', {
		'categories': json.dumps(categories),
	})

def submitbrick(request):
	return render(request, 'bricks/submit.html')