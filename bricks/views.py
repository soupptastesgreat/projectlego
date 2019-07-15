from django.views.generic import *
from bricks.models import thebricks
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.db.models import Q
import json

class Index(ListView):
	template_name = 'bricks/index.html'
	model = thebricks

	def get(self, request, *args, **kwargs):
		brick_color1 = self.get_queryset().filter(my_color__contains='black')
		brick_color2 = self.get_queryset().filter(my_color__contains='bright yellow')
		brick_color3 = self.get_queryset().filter(my_color__contains='bright blue')
		brick_color4 = self.get_queryset().filter(my_color__contains='bright green')
		brick_color5 = self.get_queryset().filter(my_color__contains='bright orange')
		brick_color6 = self.get_queryset().filter(my_color__contains='bright purple')
		brick_color7 = self.get_queryset().filter(my_color__exact='bright red')
		brick_color8 = self.get_queryset().filter(my_color__contains='bright reddish violet')
		brick_color9 = self.get_queryset().filter(my_color__exact='bright yellow')
		brick_color10 = self.get_queryset().filter(my_color__contains='bright yellowish green')
		brick_color11 = self.get_queryset().filter(my_color__contains='cool yellow')
		brick_color12 = self.get_queryset().filter(my_color__contains='dark azure')
		brick_color13 = self.get_queryset().filter(my_color__contains='dark green')
		brick_color14 = self.get_queryset().filter(my_color__contains='dark orange')
		brick_color15 = self.get_queryset().filter(my_color__contains='dark stone grey')
		brick_color16 = self.get_queryset().filter(my_color__contains='earth blue')
		brick_color17 = self.get_queryset().filter(my_color__contains='earth green')
		brick_color18 = self.get_queryset().filter(my_color__contains='flame yellowish orange')
		brick_color19 = self.get_queryset().filter(my_color__contains='light nougat')
		brick_color20 = self.get_queryset().filter(my_color__contains='light purple')
		brick_color21 = self.get_queryset().filter(my_color__contains='medium azure')
		brick_color22 = self.get_queryset().filter(my_color__contains='medium lavender')
		brick_color23 = self.get_queryset().filter(my_color__contains='medium lilac')
		brick_color24 = self.get_queryset().filter(my_color__contains='medium nougat')
		brick_color25 = self.get_queryset().filter(my_color__contains='medium stone grey')
		brick_color26 = self.get_queryset().filter(my_color__contains='new dark red')
		brick_color27 = self.get_queryset().filter(my_color__contains='pink')
		brick_color28 = self.get_queryset().filter(my_color__contains='reddish brown')
		brick_color29 = self.get_queryset().filter(my_color__contains='sand blue')
		brick_color30 = self.get_queryset().filter(my_color__contains='sand yellow')
		brick_color31 = self.get_queryset().filter(my_color__contains='silver ink')
		brick_color32 = self.get_queryset().filter(my_color__contains='silver metallic')
		brick_color33 = self.get_queryset().filter(my_color__contains='spring yellowish green')
		brick_color34 = self.get_queryset().filter(my_color__contains='titanium metallic')
		brick_color35 = self.get_queryset().filter(my_color__exact='transparent')
		brick_color36 = self.get_queryset().filter(my_color__contains='transparent blue')
		brick_color37 = self.get_queryset().filter(my_color__contains='transparent bright green')
		brick_color38 = self.get_queryset().filter(my_color__contains='transparent bright orange')
		brick_color39 = self.get_queryset().filter(my_color__contains='transparent green')
		brick_color40 = self.get_queryset().filter(my_color__contains='transparent light blue')
		brick_color41 = self.get_queryset().filter(my_color__contains='transparent medium reddish violet')
		brick_color42 = self.get_queryset().filter(my_color__contains='transparent red')
		brick_color43 = self.get_queryset().filter(my_color__contains='transparent yellow')
		brick_color44 = self.get_queryset().filter(my_color__contains='warm gold')
		brick_color45 = self.get_queryset().filter(my_color__contains='white')
		brick_typeA = self.get_queryset().filter(brick_type__contains='brick')
		brick_typeB = self.get_queryset().filter(brick_type__contains='plate')
		brick_typeC = self.get_queryset().filter(brick_type__contains='tile')
		brick_typeD = self.get_queryset().exclude(Q(brick_type__contains='brick')  | Q(brick_type__contains='plate')  | Q(brick_type__contains='tile'))
		brick_type = serializers.serialize('json', brick_typeA)
		plate_type = serializers.serialize('json', brick_typeB)
		tile_type = serializers.serialize('json', brick_typeC)
		other_type = serializers.serialize('json', brick_typeD)	
		color_b = serializers.serialize('json', brick_color1)
		color_by = serializers.serialize('json', brick_color2)
		color_bb = serializers.serialize('json', brick_color3)
		color_bg = serializers.serialize('json', brick_color4)
		color_bo = serializers.serialize('json', brick_color5)
		color_bp = serializers.serialize('json', brick_color6)
		color_br = serializers.serialize('json', brick_color7)
		color_brv = serializers.serialize('json', brick_color8)
		color_bry = serializers.serialize('json', brick_color9)
		color_byg = serializers.serialize('json', brick_color10)
		color_cy = serializers.serialize('json', brick_color11)
		color_da = serializers.serialize('json', brick_color12)
		color_dg = serializers.serialize('json', brick_color13)
		color_do = serializers.serialize('json', brick_color14)
		color_dsg = serializers.serialize('json', brick_color15)
		color_eb = serializers.serialize('json', brick_color16)
		color_eg = serializers.serialize('json', brick_color17)
		color_flo = serializers.serialize('json', brick_color18)
		color_ln = serializers.serialize('json', brick_color19)
		color_lp = serializers.serialize('json', brick_color20)
		color_ma = serializers.serialize('json', brick_color21)
		color_mla = serializers.serialize('json', brick_color22)
		color_mli = serializers.serialize('json', brick_color23)
		color_mn = serializers.serialize('json', brick_color24)
		color_msg = serializers.serialize('json', brick_color25)
		color_ndr = serializers.serialize('json', brick_color26)
		color_p = serializers.serialize('json', brick_color27)
		color_rb = serializers.serialize('json', brick_color28)
		color_sb = serializers.serialize('json', brick_color29)
		color_sy = serializers.serialize('json', brick_color30)
		color_si = serializers.serialize('json', brick_color31)
		color_sm = serializers.serialize('json', brick_color32)
		color_syg = serializers.serialize('json', brick_color33)
		color_tm = serializers.serialize('json', brick_color34)
		color_t = serializers.serialize('json', brick_color35)
		color_tb = serializers.serialize('json', brick_color36)
		color_tbg = serializers.serialize('json', brick_color37)
		color_tbo = serializers.serialize('json', brick_color38)
		color_tg = serializers.serialize('json', brick_color39)
		color_tlb = serializers.serialize('json', brick_color40)
		color_tmrv = serializers.serialize('json', brick_color41)
		color_tr = serializers.serialize('json', brick_color42)
		color_ty = serializers.serialize('json', brick_color43)
		color_wg = serializers.serialize('json', brick_color44)
		color_w = serializers.serialize('json', brick_color45)
		context = {
			"color_b": color_b,
			"color_by": color_by,
			"color_bb": color_bb,
			"color_bg": color_bg,
			"color_bo": color_bo,
			"color_bp": color_bp,
			"color_br": color_br,
			"color_brv": color_brv,
			"color_bry": color_bry,
			"color_byg": color_byg,
			"color_cy": color_cy,
			"color_da": color_da,
			"color_dg": color_dg,
			"color_do": color_do,
			"color_dsg": color_dsg,
			"color_eb": color_eb,
			"color_eg": color_eg,
			"color_flo": color_flo,
			"color_ln": color_ln,
			"color_lp": color_lp,
			"color_ma": color_ma,
			"color_mla": color_mla,
			"color_mli": color_mli,
			"color_mn": color_mn,
			"color_msg": color_msg,
			"color_ndr": color_ndr,
			"color_p": color_p,
			"color_rb": color_rb,
			"color_sb": color_sb,
			"color_sy": color_sy,
			"color_si": color_si,
			"color_sm": color_sm,
			"color_syg": color_syg,
			"color_tm": color_tm,
			"color_t": color_t,
			"color_tb": color_tb,
			"color_tbg": color_tbg,
			"color_tbo": color_tbo,
			"color_tg": color_tg,
			"color_tlb": color_tlb,
			"color_tmrv": color_tmrv,
			"color_tr": color_tr,
			"color_ty": color_ty,
			"color_wg": color_wg,
			"color_w": color_w,
			'brick_type': brick_type,
			'plate_type': plate_type,
			'tile_type': tile_type,
			'other_type': other_type,
		}
		return render(request, 'bricks/index.html', context)
