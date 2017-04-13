
import os,sys,re
from PIL import Image,ImageDraw

tiles = """
	d_stamina	916 752
	d_turns		1964 720
	d_treasure	567 685
	d_combat	1293 720
	d_psi		1037 790
	d_exp		1685 718

	frame		527 531
	castle 		684 365
	path_base	1266 458
	forest		399 592
	tower		622 502
	floor 		464 428
	grass 		1462 433
	treasure	1391 1462
	stairsd		488 498
	stairsu 	1355 496
	building	519 498
	swamp		272 624
	tree 		430 591
	gold 		563 686
	wall 		742 540
	door		688 501
	water		1135 629
	p_wizard	913 53
	p_thinker	881 54 
	p_barbarian 40 75
	p_cleric	1044 50
	p_warrior	756 49

""".replace("\t"," ").split("\n")

img = Image.open("tiles.png")
for t in tiles:
	if t.strip() != "":
		m = re.match("^\\s*([a-z\\_]+)\\s*(\d+)\\s*(\d+)\\s*$",t)
		assert m is not None,"error "+t
		x = int(int(m.group(2))/32)*32
		y = int(int(m.group(3))/32)*32
		name = "source"+os.sep+m.group(1).lower()+".png"
		#print(name,x,y)
		newImg = img.crop((x,y,x+32,y+32))
		newImg.save(name)
		if m.group(1) == "path_base":
			for i in range(0,4):
				newImg = img.crop((x,y,x+32,y+32))
				draw = ImageDraw.Draw(newImg)
				for yc in range(0,32):
					x1 = yc if i < 2 else 31-yc
					x2 = 31 if i < 2 else 0
					y2 = yc if i % 2 == 0 else 31-yc
					draw.line((x1,y2,x2,y2),fill = (0,0,0,0))
					draw.line((x1,y2,x1,y2),fill = (0,0,0,255))
				del draw
				newImg.save("source"+os.sep+"path_"+str(i)+".png")

