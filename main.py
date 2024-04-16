import pygame,time,json,pickle,sys,os

#RED = (255, 0, 0)
WHILE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

vars = []

try:
	file = open("data/setting/data.json", "r", encoding="utf-8")
except Exception as e:
	error_file = open("log.txt", "w", encoding="utf-8")
	error_file.write("Нету файла data.json")
	error_file.close()
	sys.exit()

try:
	main_file = open("data\scenes\main.scn", "r", encoding="utf-8")
except Exception as e:
	error_file = open("log.txt", "w", encoding="utf-8")
	error_file.write("Нету файла main.scn")
	error_file.close()
	sys.exit()

data = json.load(file)
records = {}
save = ""
save_text = ["", ""]
playing_file = None
opening_file = ""
file_open_with_if = False
months = ["Январь", "Февраль", "Март", "Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
new_main_file = False



try:
	save_file = open("data\save\info.txt", "rb")
	w = pickle.load(save_file)
	h = pickle.load(save_file)
	fps = pickle.load(save_file)
	finded_achievements = pickle.load(save_file)
	finded_records = pickle.load(save_file)
	save_file.close()
except Exception as e:
	w = 1200
	h = 800
	fps = 60
	finded_achievements = []
	finded_records = []
	save_file = open("data\save\info.txt", "wb")
	pickle.dump(w, save_file)
	pickle.dump(h, save_file)
	pickle.dump(fps, save_file)
	pickle.dump(finded_achievements, save_file)
	pickle.dump(finded_records, save_file)
	save_file.close()

x = 0+((w-1200)//2)
y = 0+((h-800)//2)

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((w, h))#, pygame.FULLSCREEN
pygame.display.set_caption("EW engine")


def read_en(file):
	try:
		loop = True
		while loop:
			string = file.read(3).replace("\n", "").replace(";", "")
			if string == "set":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "=":
						loop2 = False
					else:
						string += a
				var = string.replace(" ", "")
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле set.en")
						error_file.close()
						sys.exit()
					else:
						string += a
				value = string.replace("\n", "")
				data[var] = value
			elif string == "str":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "=":
						loop2 = False
					else:
						string += a
				var = string.replace(" ", "")
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле set.en")
						error_file.close()
						sys.exit()
					else:
						string += a
				value = string.replace("\n", "")
				data[var] = value
			elif string == "rec":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "=":
						loop2 = False
					else:
						string += a
				var = string.replace(" ", "")
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле set.en")
						error_file.close()
						sys.exit()
					else:
						string += a
				value = string.replace("\n", "").replace('"',"")
				records[var] = value
			elif string == "int":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "=":
						loop2 = False
					else:
						string += a
				var = string.replace(" ", "")
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле set.en")
						error_file.close()
						sys.exit()
					else:
						string += a
				value = string.replace("\n", "")
				try:
					data[var] = int(value)
				except TypeError:
					error_file = open("log.txt", "w", encoding="utf-8")
					error_file.write("Error in set.en\nЗадаваемое значение для команды int НЕ может быть текстом")
					error_file.close()
					sys.exit()
			elif string == "*//":
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == "\n" or a == "":
						loop2 = False
			elif string == "":
				file.read(1)
				file.close()
				return None
	except Exception as e:
		error_file = open("log.txt", "w", encoding="utf-8")
		error_file.write(str(e))
		error_file.close()
		sys.exit()

try:
	file_en = open("data/setting/set.en", "r", encoding="utf-8")
except Exception as e:
	error_file = open("log.txt", "w", encoding="utf-8")
	error_file.write("Нету файла set.en")
	error_file.close()
	sys.exit()

read_en(file_en)

a = pygame.font.Font(data["font"], 17)
font_b2 = pygame.font.Font(data["font"], 60)
font_c = pygame.font.Font(data["font"], 30)
d = pygame.font.Font(data["font"], data["size_font"])
font_e = pygame.font.Font("data/font/segoesc.ttf", 40)
font_a = pygame.font.Font("data/font/segoesc.ttf", 17)
font_b = pygame.font.Font("data/font/segoesc.ttf", 20)

def read_ath(file):
	try:
		ath = {}
		loop = True
		while loop:
			string = file.read(3).replace("\n", "").replace(";", "")
			if string == "ath":
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == "{":
						loop2 = False
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ",":
						loop2 = False
					else:
						string += a.replace('"', "")
				name = string
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "}":
						loop2 = False
						file.read(2)
					else:
						string += a
				descr = string
				ath[name] = descr.replace('"', "")
			elif string == "":
				file.close()
				return ath
	except Exception as e:
		error_file = open("log.txt", "w", encoding="utf-8")
		error_file.write(str(e))
		error_file.close()
		sys.exit()

try:
	file_en = open("data/setting/achievements.en", "r", encoding="utf-8")
except Exception as e:
	error_file = open("log.txt", "w", encoding="utf-8")
	error_file.write("Нету файла achievements.en")
	error_file.close()
	sys.exit()

achievements = read_ath(file_en)

def end():
	one = font_b2.render("Благодарности", False, WHILE)
	two = font_c.render("За работу над изображениями: "+data['photoshoper'], False, WHILE)
	three = font_c.render("За сценарий: "+data['scenest'], False, WHILE)
	four = font_c.render("За работу с музыкой: "+data['music_man'], False, WHILE)
	i = 0
	x = 200
	y = 100
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		i += 1
		if i == 150:
			return None
		sc.fill(BLACK)
		sc.blit(one, (x, y))
		sc.blit(two, (x, y+65))
		sc.blit(three, (x, y+100))
		sc.blit(four, (x, y+135))
		clock.tick(fps)
		pygame.display.update()

def questions(stringz, varz):
	choice_bg = pygame.image.load("data/image/system/choice_bg.png")
	x = 0
	y = 325
	size = 50
	while True:
		y = 325
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos[:]
				dy = 325
				for i in range(len(stringz)):
					if x <= pos[0] <= 1200 and dy <= pos[1] <= dy + 40:
						if varz[i] == "@zero":
							return None
						elif varz[i] in data:
							data[varz[i]] += 1
							return None
						else:
							error_file = open("log.txt", "w", encoding="utf-8")
							error_file.write("Переменная '"+varz[i-1]+"' не обьявлена!")
							error_file.close()
							sys.exit()
					dy+=size
					print(i)
		for i in range(len(stringz)):
			sc.blit(choice_bg, (x, y))
			sc.blit(c.render(stringz[i], False, WHILE), (x + 300, y))
			y += size
		clock.tick(fps)
		pygame.display.update()

def read(file, searching):
	try:
		loop = True
		global file_open_with_if
		global opening_file
		opening_with_if = False
		while loop:
			string = file.read(3).replace("\n", "").replace(";", "")
			if string == "fon":
				global bg
				file.read(1)
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a
				bg = pygame.image.load(data[string])
			elif string == "*ch":
				file.read(1)
				stringz = []
				varz = []
				loop = True
				while loop:
					string = ""
					var = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ".":
							loop2 = False
						else:
							string += a
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == "," or a == ";":
							loop2 = False
						elif a == "\n" or a == "":
							error_file = open("log.txt", "w", encoding="utf-8")
							error_file.write("Вы не поставили ';' в файле", opening_file)
							error_file.close()
							sys.exit()
						else:
							var += a
					if a == ";":
						loop = False
						file.read(1)
					stringz.append(string)
					varz.append(var)
				if not searching:
					questions(stringz, varz)
				loop = True
			elif string == "vid":
				pass
			elif string == "*tm":
				a = file.read(1)
				string = ""
				if a == ":":
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ".":
							loop2 = False
						else:
							string += a.replace(" ", "")
					day = string
					string = ""
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							loop2 = False
							file.read(1)
						elif a == "\n" or a == "":
							error_file = open("log.txt", "w", encoding="utf-8")
							error_file.write("Вы не поставили ';' в файле", opening_file)
							error_file.close()
							sys.exit()
						else:
							string += a.replace(" ", "")
					month = months[int(string)-1]
					timer_on = True
				elif a == " ":
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							loop2 = False
							file.read(1)
						elif a == "\n" or a == "":
							error_file = open("log.txt", "w", encoding="utf-8")
							error_file.write("Вы не поставили ';' в файле", opening_file)
							error_file.close()
							sys.exit()
						else:
							string += a
					if string == "off":
						timer_on = False
						day = ""
						month = ""
				global timer
				global timer_day
				global timer_month
				timer = timer_on
				timer_day = day
				timer_month = month
			elif string == "var":
				file.read(1)
				string = ""
				value = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == "=":
						loop2 = False
					else:
						string += a
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						value += a
				if not searching:
					data[string] = int(value)
					vars.append([string,int(value)])
			elif string == "*if":
				file.read(1)
				opening_with_if = True
				string = ""
				value = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == "=":
						loop2 = False
						file.read(1)
					else:
						string += a
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ":":
						loop2 = False
					else:
						value += a
				if data[string] == int(value):
					file.read(1)
					global arg_open_with_if
					arg_open_with_if = [string, value]
				else:
					loop2 = True
					while loop2:
						a = file.read(1)
						if a == ";":
							loop2 = False
							file.read(1)
						elif a == "\n" or a == "":
							error_file = open("log.txt", "w", encoding="utf-8")
							error_file.write("Вы не поставили ';' в файле", opening_file)
							error_file.close()
							sys.exit()
			elif string == "see":
				file.read(1)
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a
				global sprite
				if string != "off":
					if string in data:
						sprite = pygame.image.load(data[string])#.set_colorkey(WHILE)
				else:
					sprite = None
			elif string == "ath":
				file.read(1)
				global ath_blit, ath_name, finded_achievements, alternativ_w, alternativ_h, alternativ_fps
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a
				ath_name = string
				ath_blit = True
				if ath_name not in finded_achievements:
					finded_achievements.append(ath_name)
					save_file = open("data\save\info.txt", "wb")
					pickle.dump(alternativ_w, save_file)
					pickle.dump(alternativ_h, save_file)
					pickle.dump(alternativ_fps, save_file)
					pickle.dump(finded_achievements, save_file)
					pickle.dump(finded_records, save_file)
					save_file.close()
			elif string == "say":
				file.read(1)
				name = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ":":
						loop2 = False
					else:
						name += a
				if name in data:
					static = data[name]
					name = static + ":"
				else:
					error_file = open("log.txt", "w", encoding="utf-8")
					error_file.write(f"Имя {name} из файле {opening_file} не найдено.\nПожалуйста инициализируйте это имя в файле set.en")
					error_file.close()
					sys.exit()
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a
				phrase = string
				loop = False
			elif string == "rec":
				file.read(1)
				name = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						name += a
				if name in records and name not in finded_records:
					finded_records.append(name)
					save_file = open("data\save\info.txt", "wb")
					pickle.dump(alternativ_w, save_file)
					pickle.dump(alternativ_h, save_file)
					pickle.dump(alternativ_fps, save_file)
					pickle.dump(finded_achievements, save_file)
					pickle.dump(finded_records, save_file)
					save_file.close()
			elif string == "*pl":
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a.replace(" ", "")
				global playing_file
				if not searching:
					if string in data:
						m_file = data[string]
						playing_file = pygame.mixer.Sound(m_file)
						playing_file.play(1)
					elif string == "off":
						playing_file.stop()
					else:
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Сбой в настройке музыки.")
						error_file.close()
						sys.exit()
			elif string == "*ld":
				string = "data/scenes/"
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a.replace(" ", "")
				string += ".scn"
				global main_file
				opening_file = string
				main_file = open(string, "r", encoding="utf-8")
				global new_main_file
				new_main_file = True
				if opening_with_if:
					file_open_with_if = True
				loop = False
				name, phrase = read(main_file, False)
			elif string == "thg":
				name = ""
				file.read(1)
				string = ""
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					elif a == "\n" or a == "":
						error_file = open("log.txt", "w", encoding="utf-8")
						error_file.write("Вы не поставили ';' в файле", opening_file)
						error_file.close()
						sys.exit()
					else:
						string += a
				phrase = string
				loop = False
			elif string == "*//":
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == "\n" or a == "":
						loop2 = False
			elif string == "ret":
				file.read(1)
				#file.close()
				if data["titel"]:
					end()
				global end_scenes
				end_scenes = True
				return 0,0
			elif string == "":
				fl = str(main_file).replace("<_io.TextIOWrapper name='data/scenes/", "").replace(".scn' mode='r' encoding='utf-8'>", "")
				global save
				if file_open_with_if:
					save = "*if "+arg_open_with_if[0]+"="+arg_open_with_if[1]+": "+"*ld " + fl + ";\n"
				elif file_open_with_if == False:
					save = "*ld " + fl + ";\n"
				file_open_with_if = False
				return 0,0
			else:
				error_file = open("log.txt", "w", encoding="utf-8")
				error_file.write("Неправильный индификатор строки:\n")
				error_file.write(string)
				error_file.close()
				sys.exit()
		if file_open_with_if == False:
			file_open_with_if = False
		opening_with_if = False
		global save_text
		save_text = [name, phrase]
		return name, phrase
	except Exception as e:
		error_file = open("log.txt", "w", encoding="utf-8")
		error_file.write(str(e))
		error_file.close()
		sys.exit()

bg = pygame.image.load("data/image/system/on_bg.jpg")
load_loop = True
#i = 0
text = font_c.render("Нажмите любую клавишу, чтобы продолжить...", False, WHILE)

while load_loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			#if event.key == pygame.K_SPACE:
			load_loop = False
	sc.blit(bg, (x, y))
	sc.blit(text, (w/4.8, h-100))
	clock.tick(fps)
	pygame.display.update()

def read_menu_en(file):
	try:
		loop2 = True
		string = ""
		while loop2:
			a = file.read(1)
			if a == "{":
				loop2 = False
				file.read(2)
			else:
				string += a
		if w == 1200:
			if string == "laptop":
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "}":
						loop2 = False
						file.read(1)
				file.read(5)
		elif w == 1100:
			if string == "pc":
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == "}":
						loop2 = False
						file.read(1)
				file.read(5)
		global bttns, txts
		bttns = []
		txts = []
		loop = True
		while loop:
			string = file.read(3).replace("\n", "").replace(";", "").replace(" ", "")
			#print(string)
			if string == "fon":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(2)
					else:
						string += a
				global bg
				bg = pygame.image.load("data/image/local/"+string)
			elif string == "btn":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ",":
						loop2 = False
					else:
						string += a
				string.replace(" ", "")
				x = int(string)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ":":
						loop2 = False
					else:
						string += a
				string.replace(" ", "")
				y = int(string)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(2)
					else:
						string += a
				string = string.replace(" ", "")
				command = string
				bttns.append([x,y,command])
			elif string == "txt":
				file.read(1)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ",":
						loop2 = False
					else:
						string += a
				string.replace(" ", "")
				x = int(string)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ":":
						loop2 = False
					else:
						string += a
				string.replace(" ", "")
				y = int(string)
				loop2 = True
				string = ""
				while loop2:
					a = file.read(1)
					if a == ";":
						loop2 = False
						file.read(1)
					else:
						string += a
				text = string
				txts.append([x,y,text])
			elif string == "*//":
				loop2 = True
				while loop2:
					a = file.read(1)
					if a == "\n" or a == "":
						loop2 = False
						file.read(1)
			elif string == "" or string[0] == "}":
				file.close()
				loop = False
	except Exception as e:
		error_file = open("log.txt", "w", encoding="utf-8")
		error_file.write(str(e))
		error_file.close()
		sys.exit()

display_button = False
try:
	save_file = open("data\save\save.txt", "rb")
	save_file.close()
	display_button = True
except Exception as e:
	display_button = False

try:
	file_en = open("data/setting/menu.en", "r", encoding="utf-8")
except Exception as e:
	error_file = open("log.txt", "w", encoding="utf-8")
	error_file.write("Нету файла menu.en")
	error_file.close()
	sys.exit()

read_menu_en(file_en)

alternativ_w = w
alternativ_h = h
alternativ_fps = fps

def settings(bg):
	bttn = pygame.image.load("data/image/system/button1.png")
	back = pygame.image.load("data/image/system/Back.png")
	ok = pygame.image.load("data/image/system/ok_lbl_bttn.jpg")
	no_ok = pygame.image.load("data/image/system/lbl_bttn.jpg")
	text = font_a.render("Применить", False, WHILE)
	saving = False
	global alternativ_w, alternativ_h, alternativ_fps, sc, w, h
	i = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos[:]
				if 100 <=pos[0]<= 163 and 100 <=pos[1]<= 150:
					return None
				elif 800<=pos[0]<=960 and 650<=pos[1]<=680:
					save_file = open("data\save\info.txt", "wb")
					pickle.dump(alternativ_w, save_file)
					pickle.dump(alternativ_h, save_file)
					pickle.dump(alternativ_fps, save_file)
					pickle.dump(finded_achievements, save_file)
					pickle.dump(finded_records, save_file)
					save_file.close()
					saving = True
					text = font_a.render("Применено", False, WHILE)
					#sc = pygame.display.set_mode((alternativ_w, alternativ_h))
					#w = alternativ_w
					#h = alternativ_h
				elif 400<=pos[0]<=570 and 175<=pos[1]<=210:
					alternativ_w = 1200
					alternativ_h = 800
				elif 400<=pos[0]<=570 and 250<=pos[1]<=285:
					alternativ_w = 1100
					alternativ_h = 700

				elif 400<=pos[0]<=570 and 350+40<=pos[1]<=385+40:
					alternativ_fps = 60
				elif 400<=pos[0]<=570 and 425+40<=pos[1]<=460+40:
					alternativ_fps = 120
				elif 400<=pos[0]<=570 and 500+40<=pos[1]<=535+40:
					alternativ_fps = 240

		if saving:
			i += 1
		if saving and i == 1.5*fps:
			text = font_a.render("Применить", False, WHILE)
			saving = False
			i = 0

		sc.blit(bg, (x, y))
		sc.blit(back, (100, 100))
		sc.blit(font_e.render("Разрешение", False, WHILE), (400, 100))
		if alternativ_w == 1200:
			sc.blit(ok, (400, 175))
		else:
			sc.blit(no_ok, (400, 175))
		if alternativ_w == 1100:
			sc.blit(ok, (400, 250))
		else:
			sc.blit(no_ok, (400, 250))

		sc.blit(font_a.render("Пк", False, WHILE), (403, 181))
		sc.blit(font_a.render("Ноутбук", False, WHILE), (403, 256))

		sc.blit(font_e.render("Частота кадров", False, WHILE), (400, 275+40))
		if alternativ_fps == 60:
			sc.blit(ok, (400, 350+40))
		else:
			sc.blit(no_ok, (400, 350+40))
		if alternativ_fps == 120:
			sc.blit(ok, (400, 425+40))
		else:
			sc.blit(no_ok, (400, 425+40))
		if alternativ_fps == 240:
			sc.blit(ok, (400, 500+40))
		else:
			sc.blit(no_ok, (400, 500+40))
		sc.blit(font_a.render("60", False, WHILE), (403, 356+40))
		sc.blit(font_a.render("120", False, WHILE), (403, 431+40))
		sc.blit(font_a.render("240", False, WHILE), (403, 506+40))

		sc.blit(bttn, (800, 650))
		sc.blit(text, (800, 656))
		clock.tick(fps)
		pygame.display.update()

def view_finded_achievements(bg):
	loop = True
	dy = 325
	size = 50
	back = pygame.image.load("data/image/system/Back.png")
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos[:]
				if 100 <=pos[0]<= 163 and 100 <=pos[1]<= 150:
					return None

		sc.blit(bg, (x, y))
		sc.blit(back, (100, 100))
		sc.blit(font_e.render("Достижения:", False, WHILE), (470, 200))
		dy = 270
		a = 1
		for i in finded_achievements:
			sc.blit(font_a.render(str(a)+") "+i, False, WHILE), (470, dy))
			sc.blit(font_a.render(f"    {achievements[i]}", False, WHILE), (470, dy+20))
			dy+=size
			a+=1
		clock.tick(fps)
		pygame.display.update()

def view_finded_records():
	loop = True
	dy = 325
	size = 25
	back = pygame.image.load("data/image/system/Back.png")
	bg = pygame.image.load("data/image/system/notebook.jpg")
	text = font_a.render("Клавишами <- -> листайте дневник", False, BLACK)
	pages = max((len(finded_records)/2)+(len(finded_records)%1), 1)
	page = 1
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos[:]
				if 100 <=pos[0]<= 163 and 25 <=pos[1]<= 75:
					return None
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and page != 1:
					page -= 1
				if event.key == pygame.K_RIGHT and page != pages:
					page += 1


		sc.blit(bg, (x, y))
		sc.blit(back, (100, 25))
		sc.blit(text, (w-100-text.get_width(), h-100))
		sc.blit(font_a.render(f"Page {page}/{pages}", False, BLACK), (100, h-100))
		dx = 120
		dy = 110
		for i in finded_records[max(page-1, 0):page+1]:
			for j in records[i].split("/"):
				sc.blit(font_a.render(j, False, BLACK), (dx, dy))
				dy+=size
			dx = w//2 + 50
			dy = 110
		clock.tick(fps)
		pygame.display.update()



# начало самой игры

def transition():
	a = 0
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		a+=1
		if a == 5:
			return None
		sc.fill(BLACK)
		clock.tick(fps)
		pygame.display.update()

#del load_loop, text, display_button, menu_loop, bttn, save_text, file_en

def game():
	global main_file, new_main_file, save, end_scenes
	end_scenes = False
	playing_file.stop()
	saving = True
	if continue_save:
		save_file = open("data\save\save.txt", "rb")
		save = pickle.load(save_file).replace(".scn", "")
		save_text = pickle.load(save_file)
		vars = pickle.load(save_file)
		save_file.close()
		loop = True
		while loop:
			one, two = read(main_file, True)
			if [one, two] == save_text:
				loop = False
		for var in vars:
			data[var[0]]=var[1]

	timer = False
	timer_bg = pygame.image.load("data/image/system/timer_bg.png")
	timer_day = ""
	timer_month = ""
	
	n_text, ph_text = read(main_file, False)
	name_text = font_c.render(n_text, False, WHILE)
	string = ''
	b = 0
	for i in ph_text:
		if i == "/":
			loop = False
		else:
			string+=i
		b+=1
	phrase1 = d.render(string, False, WHILE)
	phrase2 = d.render(ph_text[b:-1], False, WHILE)
	
	lbl_bg = pygame.image.load("data/image/system/fon.png")
	micro_lbl_bg = pygame.image.load("data/image/system/micro_fon.png")
	ath_bg = pygame.image.load("data/image/system/ath.png")
	menu_bttn = a.render("Выйти", False, BLACK)
	save_bttn = a.render("Сохранить", False, BLACK)
	saving = False
	sprite = None
	
	sc.blit(bg, (x, y))
	sc.blit(lbl_bg, (20, w-200))
	pygame.display.update()
	game = True
	ath_blit = False
	blit_label = True
	i = 0
	ms = 0
	hour = 0
	m = 0
	s = 0
	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN and not end_scenes:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_F1:
					loop = True
					while loop:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()
							if event.type == pygame.MOUSEBUTTONDOWN:
								pos = event.pos[:]
								if w == 1200:
									if 1070 <= pos[0] <= 1170 and 740 <= pos[1] <= 740+19:
										main_file.close()
										main_file = open("data/scenes/main.scn", "r", encoding="utf-8")
										return None
									if 1070 <= pos[0] <= 1170 and 700 <= pos[1] <= 700+19:
										settings(bg)
									if 1070 <= pos[0] <= 1170 and 660 <= pos[1] <= 660+19:
										loop = False
								if w == 1100:
									if 970 <= pos[0] <= 1070 and 740-100 <= pos[1] <= 740+19-100:
										main_file.close()
										main_file = open("data/scenes/main.scn", "r", encoding="utf-8")
										return None
									if 970 <= pos[0] <= 1070 and 700-100 <= pos[1] <= 700+19-100:
										settings(bg)
									if 970 <= pos[0] <= 1070 and 660-100 <= pos[1] <= 660+19-100:
										loop = False
						sc.blit(bg, (x, y))
						if w == 1200:
							sc.blit(bttn, (1070, 660))
							sc.blit(bttn, (1070, 700))
							sc.blit(bttn, (1070, 740))
							sc.blit(font_a.render("Продолжить", False, WHILE), (1070, 660))
							sc.blit(font_a.render("Настройки", False, WHILE), (1070, 700))
							sc.blit(font_a.render("Выйти", False, WHILE), (1070, 740))
						if w == 1100:
							sc.blit(bttn, (970, 660-100))
							sc.blit(bttn, (970, 700-100))
							sc.blit(bttn, (970, 740-100))
							sc.blit(font_a.render("Продолжить", False, WHILE), (970, 660-100))
							sc.blit(font_a.render("Настройки", False, WHILE), (970, 700-100))
							sc.blit(font_a.render("Выйти", False, WHILE), (970, 740-100))

						clock.tick(fps)
						pygame.display.update()

				elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
					n_text, ph_text = read(main_file, False)
					if n_text == 0 and ph_text == 0:
						main_file = open("data\scenes\main.scn", "r", encoding="utf-8")
						loop = True
						while loop:
							check = main_file.readline()
							if check == save:
								loop = False
					else:
						if new_main_file:
							n_text, ph_text = read(main_file, False)
							new_main_file = False
						name_text = font_c.render(n_text, False, WHILE)
						transition()
						string = ''
						b = 0
						for z in ph_text:
							if z == "/":
								break
							else:
								string+=z
							b+=1
						phrase1 = d.render(string, False, WHILE)
						phrase2 = d.render(ph_text[b:].replace("/", ""), False, WHILE)
				elif event.key == pygame.K_s:
					if "Screenshots" not in os.listdir(os.getcwd()):
						os.mkdir("Screenshots")
					length = len(os.listdir("Screenshots"))
					pygame.image.save(sc, f"Screenshots/screenshot ({length}).jpg")
				elif event.key == pygame.K_h:
					blit_label = not blit_label
			elif event.type == pygame.MOUSEBUTTONDOWN and not end_scenes:
				pos = event.pos[:]
				if  w-120 <=pos[0]<= w-20 and h-71 <=pos[1]<= h-52:
					game = False
					main_file = open("data/scenes/main.scn", "r", encoding="utf-8")
				elif w-120 <=pos[0]<= w-20 and h-48 <=pos[1]<= h-29:
					save_file = open("data\save\save.txt", "wb")
					pickle.dump("*ld "+opening_file.replace("data/scenes/", "")+";\n", save_file)
					pickle.dump(save_text, save_file)
					pickle.dump(vars, save_file)
					save_file.close()
					saving = True
					save_bttn = a.render("Сохранено", False, BLACK)
		
		if end_scenes:
			main_file.close()
			main_file = open("data/scenes/main.scn", "r", encoding="utf-8")
			return None

		if saving or ath_blit:
			i += 1
		if saving and i == 1.5*fps:
			save_bttn = a.render("Сохранить", False, BLACK)
			saving = False
			i = 0
	
		ms += 1
		if ms == fps:
			ms = 0
			s+=1
		if s == 60:
			s = 0
			m +=1
		if m == 60:
			m = 0
			hour +=1
	
	
	
		sc.blit(bg, (x, y))
		sc.blit(timer_bg, (0,0))
		sc.blit(font_a.render(f"{hour}:{m}:{s}", False, WHILE), (10,0))
		if timer:
			sc.blit(font_a.render(timer_day, False, WHILE), (w-140, -1))
			sc.blit(font_a.render(timer_month, False, WHILE), (w-102, -1))
		if sprite != None:
			sc.blit(sprite, (w//3+50, h-620))
		if blit_label:
			if w == 1200:
				sc.blit(lbl_bg, (20, h-200))
				sc.blit(name_text, (40, h-190))
				sc.blit(phrase1, (30, h-140))
				sc.blit(phrase2, (30, h-110))
				sc.blit(menu_bttn, (w-120, h-71))
				sc.blit(save_bttn, (w-120, h-48))
			if w == 1100:
				sc.blit(micro_lbl_bg, (20, h-200))
				sc.blit(name_text, (40, h-190))
				sc.blit(phrase1, (30, h-140))
				sc.blit(phrase2, (30, h-110))
				sc.blit(menu_bttn, (w-120, h-71))
				sc.blit(save_bttn, (w-120, h-48))
		if ath_blit:
			sc.blit(ath_bg, (w-154, h-58))
			sc.blit(font_b.render(ath_name, False, BLACK), (w-154, h-52))
			sc.blit(font_a.render(achievements[ath_name], False, BLACK), (w-154, h-26))
			if i == 1.5*fps:
				i = 0
				ath_blit = False
		clock.tick(fps)
		pygame.display.update()
	

# МЕНЮ

playing_file = pygame.mixer.Sound(data["soundtrack"])
playing_file.play(1)
menu_loop = True
bttn = pygame.image.load("data/image/system/button1.png")
while menu_loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				if "Screenshots" not in os.listdir(os.getcwd()):
					os.mkdir("Screenshots")
				length = len(os.listdir("Screenshots"))
				pygame.image.save(sc, f"Screenshots/screenshot ({length}).jpg")
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos[:]
			for i in bttns:
				if i[0] <=pos[0]<= i[0]+120 and i[1] <=pos[1]<= i[1]+30 and i[2] == "play":
					continue_save=False
					game()
				elif i[0]<=pos[0]<=i[0]+120 and i[1]<=pos[1]<=i[1]+30 and i[2] == "continue" and display_button == True:
					continue_save=True
					game()
				elif i[0]<=pos[0]<=i[0]+120 and i[1]<=pos[1]<=i[1]+30 and i[2] == "setting":
					settings(bg)
				elif i[0]<=pos[0]<=i[0]+120 and i[1]<=pos[1]<=i[1]+30 and i[2] == "achievements":
					view_finded_achievements(bg)
				elif i[0]<=pos[0]<=i[0]+120 and i[1]<=pos[1]<=i[1]+30 and i[2] == "records":
					view_finded_records()
				elif i[0]<=pos[0]<=i[0]+120 and i[1]<=pos[1]<=i[1]+30 and i[2] == "exit":
					sys.exit()
	sc.blit(bg, (x, y))
	#sc.blit(pnl, (x, h-120))
	for i in range(len(bttns)):
		if bttns[i][2] == "play":
			sc.blit(bttn, (bttns[i][0], bttns[i][1]))
			sc.blit(font_a.render("Играть", False, WHILE), (bttns[i][0], bttns[i][1]+6))
		if bttns[i][2] == "setting":
			sc.blit(bttn, (bttns[i][0], bttns[i][1]))
			sc.blit(font_a.render("Настройки", False, WHILE), (bttns[i][0], bttns[i][1]+6))
		if display_button == True and bttns[i][2] == "continue":
			sc.blit(bttn, (bttns[i][0], bttns[i][1]))
			sc.blit(font_a.render("Продолжить", False, WHILE), (bttns[i][0], bttns[i][1]+6))
		if bttns[i][2] == "achievements":
			sc.blit(bttn, (bttns[i][0], bttns[i][1]))
			sc.blit(font_a.render("Достижения", False, WHILE), (bttns[i][0], bttns[i][1]+6))
		if bttns[i][2] == "records":
			sc.blit(bttn, (bttns[i][0], bttns[i][1]))
			sc.blit(font_a.render("Дневник", False, WHILE), (bttns[i][0], bttns[i][1]+6))
		if bttns[i][2] == "exit":
			sc.blit(bttn, (bttns[i][0], bttns[i][1]))
			sc.blit(font_a.render("Выход", False, WHILE), (bttns[i][0], bttns[i][1]+6))
	for i in txts:
		sc.blit(font_b2.render(i[2], False, WHILE), (i[0], i[1]))
	clock.tick(fps)
	pygame.display.update()