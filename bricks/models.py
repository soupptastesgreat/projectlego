from django.db import models

class thebricks(models.Model):
	black = "black"
	brick_yellow = "brick yellow"
	bright_blue = "bright blue"
	bright_green = "bright green"
	bright_orange = "bright orange"
	bright_purple = "bright purple"
	bright_red = "bright red"
	bright_reddish_violet = "bright reddish violet"
	bright_yellow = "bright yellow"
	bright_yellowish_green = "bright yellowish green"
	cool_yellow = "cool yellow"
	dark_azure = "dark azure"
	dark_green = "dark green"
	dark_orange = "dark orange"
	dark_stone_grey = "dark stone grey"
	earth_blue = "earth blue"
	earth_green = "earth green"
	flame_yellowish_orange = "flame yellowish orange"
	light_nougat = "light nougat"
	light_purple = "light purple"
	medium_azure = "medium azure"
	medium_lavender = "medium lavender"
	medium_lilac = "medium lilac"
	medium_nougat = "medium nougat"
	medium_stone_grey = "medium stone grey"
	new_dark_red = "new dark red"
	pink = "pink"
	reddish_brown = "reddish brown"
	sand_blue = "sand blue"
	sand_yellow = "sand yellow"
	silver_ink = "silver ink"
	silver_metallic = "silver metallic"
	spring_yellowish_green = "spring yellowish green"
	titanium_metallic = "titanium metallic"
	transparent = "transparent"
	transparent_blue = "transparent blue"
	transparent_bright_green = "transparent bright green"
	transparent_bright_orange = "transparent bright orange"
	transparent_green = "transparent green"
	transparent_light_blue = "transparent light blue"
	transparent_medium_reddish_violet = "transparent medium reddish violet"
	transparent_red = "transparent red"
	transparent_yellow = "transparent yellow"
	warm_gold = "warm gold"
	white = "white"
	color_choices = (
		(black, "black"),
		(brick_yellow, "brick yellow"),
		(bright_blue, "bright blue"),
		(bright_green, "bright green"),
		(bright_orange, "bright orange"),
		(bright_purple, "bright purple"),
		(bright_red, "bright red"),
		(bright_reddish_violet, "bright reddish violet"),
		(bright_yellow, "bright yellow"),
		(bright_yellowish_green, "bright yellowish green"),
		(cool_yellow, "cool yellow"),
		(dark_azure, "dark azure"),
		(dark_green, "dark green"),
		(dark_orange, "dark orange"),
		(dark_stone_grey, "dark stone grey"),
		(earth_blue, "earth blue"),
		(earth_green, "earth green"),
		(flame_yellowish_orange, "flame yellowish orange"),
		(light_nougat, "light nougat"),
		(light_purple, "light purple"),
		(medium_azure, "medium azure"),
		(medium_lavender, "medium lavender"),
		(medium_lilac, "medium lilac"),
		(medium_nougat, "medium nougat"),
		(medium_stone_grey, "medium stone grey"),
		(new_dark_red, "new dark red"),
		(pink, "pink"),
		(reddish_brown, "reddish brown"),
		(sand_blue, "sand blue"),
		(sand_yellow, "sand yellow"),
		(silver_ink, "silver ink"),
		(silver_metallic, "silver metallic"),
		(spring_yellowish_green, "spring yellowish green"),
		(titanium_metallic, "titanium metallic"),
		(transparent, "transparent"),
		(transparent_blue, "transparent blue"),
		(transparent_bright_green, "transparent bright green"),
		(transparent_bright_orange, "transparent bright orange"),
		(transparent_green, "transparent green"),
		(transparent_light_blue, "transparent light blue"),
		(transparent_medium_reddish_violet, "transparent medium reddish violet"),
		(transparent_red, "transparent red"),
		(transparent_yellow, "transparent yellow"),
		(warm_gold, "warm gold"),
		(white, "white"),
	)
	my_color = models.CharField(max_length=40, choices=color_choices, default=black)
	brick_type = models.CharField(max_length=40)
	brick_length = models.IntegerField(default=1)
	brick_width = models.IntegerField(default=1)
	brick_height = models.IntegerField(default=1)