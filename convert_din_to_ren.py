import os
import sys
import glob
import numpy as np
import re
import cv2
import math
from PIL import ImageFont, ImageDraw, Image, ImageFilter
from multiprocessing import Process, Pool, Manager

# Number of threads to use
NUM_THREADS = 12

THUMB_HEIGHT = 600
THUMB_TEXT_AREA = 150
THUMB_NUM_COL = 6

MAIN_HEIGHT = 1000

SIDE_H = 700
SIDE_W = 500

dir_path = os.path.dirname(os.path.realpath(__file__))

DIN_FOLDER_USUAL = os.path.join(dir_path, "Arts")

OUT_FOLDER_GAME = os.path.join(dir_path, "Bienvenue A La Cosy Academie", "game")
OUT_FOLDER_IMG = os.path.join(OUT_FOLDER_GAME, "images")


def build_montages(image_list, montage_shape):

	thumbs_enlarged = []
	# start with black canvas to draw images onto
	biggest_width = -1
	biggest_height = -1
	cursor_pos = [0, 0]
	start_new_img = False
	for img in image_list:
		height, width = img.shape[:2]

		if width > biggest_width:
			biggest_width = width
		if height > biggest_height:
			biggest_height = height		


	montage_image = np.ones(shape=(biggest_height * (montage_shape[1]), biggest_width * montage_shape[0], 4), dtype=np.uint8)

	for img in image_list:
		height, width = img.shape[:2]
		montage_image[cursor_pos[1]:cursor_pos[1] + height, cursor_pos[0]:cursor_pos[0] + width] = img
		cursor_pos[0] += biggest_width  # increment cursor x position
		if cursor_pos[0] >= montage_shape[0] * biggest_width:
			cursor_pos[1] += biggest_height  # increment cursor y position
			cursor_pos[0] = 0

	return montage_image

def find_first_row_colored(img):
	rows, cols = img.shape [:2]
	for i in range(rows):
		for j in range(cols):
			pixel = img[i,j]
			if pixel[3] != 0:
				return i
	return 0

def process_din_art(imgs):
	perso = None
	thumbs = []
	max_width_tb = -1
	img_definitions = []
	img_side_definitions = []
	for img in imgs:
		file_name = os.path.basename(img)
		#print(file_name)
		perso, mainPose, pose = file_name.split(".")[0].split("_")

		if mainPose.lower() == "posestandard":
			mainPose = "Standard"
		numpose, pose = pose.replace("BadBoy", "Badboy").replace("YeuxFermes", "Yeuxfermes").split("-")
		poses_keys = re.findall('[A-Z][^A-Z]*', pose)


		img_obj = cv2.imread(filename = img, flags = cv2.IMREAD_UNCHANGED )
		height, width = img_obj.shape[:2]

		# create folder
		out_folder = os.path.join(OUT_FOLDER_IMG, perso)
		if not os.path.exists(out_folder):
			os.makedirs(out_folder)

		# resize for main
		ratio_main =  height / MAIN_HEIGHT
		new_main_width = math.ceil(width / ratio_main)
		main_resized = cv2.resize(img_obj, (new_main_width, MAIN_HEIGHT), interpolation = cv2.INTER_CUBIC)		
		out_file = os.path.join(out_folder, "main_%s_%s_%s.png" % (mainPose, numpose, "_".join(poses_keys)))
		out_file_def = perso + "/"+ "main_%s_%s_%s.png" % (mainPose, numpose, "_".join(poses_keys))
		cv2.imwrite(out_file , main_resized)

		from_X = math.floor((width / 2) - (SIDE_W / 2))
		from_Y = find_first_row_colored(img_obj)

		cropped_side = img_obj[from_Y:from_Y+SIDE_H, from_X:from_X+SIDE_W]
		out_file_side = os.path.join(out_folder, "side_%s_%s_%s.png" % (mainPose, numpose, "_".join(poses_keys)))
		out_file_side_def = perso + "/"+ "side_%s_%s_%s.png" % (mainPose, numpose, "_".join(poses_keys))

		cropped_side = cv2.resize(cropped_side, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)	

		cv2.imwrite(out_file_side , cropped_side)

		#write image definition line
		img_def = "image %s %s %s = ConditionSwitch(\"persistent.ultra_quality\", \"%s\", \"True\", \"%s_low.png\")\n" % (perso, mainPose, " ".join(poses_keys), out_file_def, perso)
		
		props = ""
		if perso == "Von":
			props = "xoffset = 1700"

		img_side_def = "image side %s %s %s =Image(\"%s\", %s)\n" % (perso, mainPose, " ".join(poses_keys), out_file_side_def, props)
		
		cmd = "show %s %s %s\n" % (perso, mainPose, " ".join(poses_keys))

		out_def_file = os.path.join(OUT_FOLDER_GAME, "images_%s_generated.rpy" % perso)

		with open(out_def_file, 'a') as def_file:
			def_file.write(img_def)
			def_file.write(img_side_def)

		with open(os.path.join(DIN_FOLDER_USUAL, "commands.txt"), 'a') as cmd_file:
			cmd_file.write(cmd)

		# Thumbnail creation
		ratio =  height / THUMB_HEIGHT
		new_width = math.ceil(width / ratio)
		if new_width > max_width_tb:
			max_width_tb = new_width
		thumb = cv2.resize(img_obj, (new_width, THUMB_HEIGHT), interpolation = cv2.INTER_CUBIC)

		trans_mask = thumb[:,:,3] == 0
		thumb[trans_mask] = [125, 125, 125, 255]

		thumb = cv2.copyMakeBorder(thumb, 0, THUMB_TEXT_AREA, 0, 0, borderType=cv2.BORDER_CONSTANT, value=(255,255,255,255))
		text = mainPose + "\n" + "\n".join(poses_keys)
		cv2_im_rgb = cv2.cvtColor(thumb, cv2.COLOR_BGRA2RGBA)
		pil_im = Image.fromarray(cv2_im_rgb)
		draw = ImageDraw.Draw(pil_im)	
		font = ImageFont.truetype(r"c:\Windows\Fonts\Arial.TTF", 25)
		w, h = draw.textsize(text, font=font)
		draw.text((( (thumb.shape[1] - w) / 2 ), THUMB_HEIGHT + 5), text, font=font, fill=(0,0,0,255))
		thumb = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGBA2BGRA)

		thumbs.append(thumb)



	
	numRows = math.ceil(len(thumbs) / THUMB_NUM_COL)


	montage = build_montages(thumbs, (THUMB_NUM_COL, numRows))
	cv2.imwrite(r"d:\workspace\cosyacademie\Arts\%s.png" % perso , montage)


if __name__ == '__main__':
	pool = Pool(NUM_THREADS)

	# first delete older generated files
	old_files = (glob.glob(OUT_FOLDER_GAME + "\\*_generated.rpy"))
	for f in old_files:
		os.remove(f) 


	if os.path.exists(os.path.join(DIN_FOLDER_USUAL, "commands.txt")):
		os.remove(os.path.join(DIN_FOLDER_USUAL, "commands.txt"))
	
	persos = (glob.glob(DIN_FOLDER_USUAL +"\\*- *"))

	for perso in persos:
		print(perso)
		perso_img = (glob.glob(perso +"\\*\\*.png"))
		#print(perso_img)
		process_din_art(perso_img)
	#process_din_art(din_arts_chuen)