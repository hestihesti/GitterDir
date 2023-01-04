import os
import sys
from termcolor import colored
from tasks import mkdir



def dir():
	menu = '''

[22] Wifi

	'''

	user = input('What Is Your Username For This Computer:\n> ')
	m1 = 'mkdir Packages'
	os.chdir(f'/home/{user}/')
	os.system(m1)
	os.chdir(f'Packages')
	i = 0
	while i < 23:
		g = 'git clone https://github.com/'
		mv = 'mv -r '
		i += 1
		if i == 1:
			dir1 = '/home/d0c0b/Packages/GHRepo/AV-Bypass'
			m2 = 'sudo mkdir ' + dir1
			os.system(m2)
			av1 = g + 'klezVirus/inceptor.git'
			x1 = 'inceptor '
			av2 = g + 'G1ft3dC0d3/MsfMania.git'
			x2 = 'MsfMania '
			os.system(av1)
			os.system(av2)
			print(colored('[+] AV-Bypass Finished [+]'. 'green'))
			place = mv + x1 + dir1
			place2 = mv + x2 + dir1
			os.system(place)
			os.system(place2)

		elif i == 2:
			dir2 = '/home/d0c0b/Packages/GHRepo/bruteforce'
			m3 = 'sudo mkdir ' + dir2
			os.system(m3)
			bp = g + 'Oseid/FaceBoom.git'
			x1 = 'FaceBoom '
			bp2 = g + 'UltimateHackers/Blazy.git'
			x2 = 'Blazy '
			os.system(bp)
			os.system(bp2)
			print(colored('[+] bruteforce Finished [+]'. 'green'))
			place = mv + x1 + dir2
			place2 = mv + x2 + dir2
			os.system(place)
			os.system(place2)

		elif i == 3:
			dir4 = '/home/d0c0b/Packages/GHRepo/Forensic'
			m4 = 'sudo mkdir ' + dir4
			os.system(m4)
			f1 = g + 'volatilityfoundation/volatility'
			x1 = 'volatility '
			os.system(f1)
			print(colored('[+] Forensic Finished [+]', 'green'))
			place = mv + x1 + dir4
			os.system(place)

		elif i == 4:
			dir3 = '/home/d0c0b/Packages/GHRepo/Exploit'
			m5 = 'sudo mkdir ' + dir3
			os.system(m5)
			ex1 = g + 'v1s1t0r1sh3r3/airgeddon.git'
			x1 = 'airgeddon '
			ex2 = g + 'NullArray/AutoSploit.git'
			x2 = 'AutoSploit '
			ex3 = g + 'threat9/routersploit.git'
			x3 = 'routersploiot '
			ex4 = g + 'Screetsec/TheFatRat.git'
			x4 = 'TheFatRat '
			ex5 = g + 'AresS31/wirespy.git'
			x5 = 'wirespy '
			ex6 = g + 'jaxBCD/Zeebsploit.git'
			x6 = 'Zeebsploit '
			os.system(ex1)
			os.system(ex2)
			os.system(ex3)
			os.system(ex4)
			os.system(ex5)
			os.system(ex6)
#			print(colored('[+] Exploit Finished [+]', 'green'))
			place = mv + x1 + dir3
			place2 = mv + x2 + dir3
			place3 = mv + x3 + dir3
			place4 = mv + x4 + dir3
			place5 = mv + x5 + dir3
			place6 = mv + x6 + dir3
			os.system(place)
			os.system(place2)
			os.system(place3)
			os.system(place4)
			os.system(place5)
			os.system(place6)
			print(colored('[+] Exploit Finished [+]', 'green'))

		elif i == 5:
			dir5 = '/home/d0c0b/Packages/GHRepo/hestihesti'
			m6 = 'sudo mkdir ' + dir5
			os.system(m6)
			me1 = g + 'hestihesti/HackThemAll'
			x1 = 'HackThemAll '
			me2 = g + 'hestihesti/AtkBook'
			x2 = 'AtkBook '
			me3 = g + 'hestihesti/HackingComm'
			x3 = 'HackingComm '
			me4 = g + 'hestihesti/Passwurd'
			x4 = 'Passwurd '
			me5 = g + 'hestihesti/STEGr'
			x5 = 'STEGr '
			os.system(me1)
			os.system(me2)
			os.system(me3)
			os.system(me4)
			os.system(me5)
			place = mv + x1 + dir5
			place2 = mv + x2 + dir5
			place3 = mv + x3 + dir5
			place4 = mv + x4 + dir5
			place5 = mv + x5 + dir5
			os.system(place)
			os.system(place2)
			os.system(place3)
			os.system(place4)
			os.system(place5)
			print(colored('[+] hestihesti Finished', 'green'))

		elif i == 6:
			dir6 = '/home/d0c0b/Packages/GHRepo/InfoGather'
			m7 = 'sudo mkdir ' + dir6
			os.system(m7)
			ig1 = g + '1N3/BlackWidow'
			x1 = 'BlackWidow '
			ig2 = g + 'xadhrit/d9scan'
			x2 = 'd9scan '
			ig3 = g + 'C0MPL3XDEV/E4GL30S1NT'
			x3 = 'E4GL30S1NT '
			ig4 = g + 'gotr00t0day/Gsec'
			x4 = 'gsec '
			ig5 = g + 'AmshenShanu07/GRAB'
			x5 = 'GRAB '
			ig6 = g + 'Leviathan36/kaboom'
			x6 = 'kaboom '
			ig7 = g + 'mishakorzik/MailFinder'
			x7 = 'MailFinder '
			ig8 = g + 'aboul3la/Sublist3r.git'
			x8 = 'Sublist3r '
			ig9 = g + 'sherlock-project/sherlock'
			x9 = 'sherlock '
			ig10 = g + 'fabiodelgadopereira/wrecon'
			x10 = 'wrecon '
			ig11 = g + 'Screetsec/Sudomy'
			x11 = 'Sudomy '
			ig12 = g + 'Tuhinshubhra/RED_HAWK'
			x12 = 'RED_HAWK '
			os.system(ig1)
			os.system(ig2)
			os.system(ig3)
			os.system(ig4)
			os.system(ig5)
			os.system(ig6)
			os.system(ig7)
			os.system(ig8)
			os.system(ig9)
			os.system(ig10)
			os.system(ig11)
			os.system(ig12)
			place = mv + x10 + dir6
			place2 = mv + x1 + dir6
			place3 = mv + x2 + dir6
			place4 = mv + x3 + dir6
			place5 = mv + x4 + dir6
			place6 = mv + x5 + dir6
			place7 = mv + x6 + dir6
			place8 = mv + x7 + dir6
			place9 = mv + x8 + dir6
			place10 = mv + x9 + dir6
			place11 = mv + x11 + dir6
			place12 = mv + x12 + dir6
			os.system(place)
			os.system(place2)
			os.system(place3)
			os.system(place4)
			os.system(place5)
			os.system(place6)
			os.system(place7)
			os.system(place8)
			os.system(place9)
			os.system(place10)
			os.system(place11)
			os.system(place12)
			print(colored('[+] Info Gather Finished [+]', 'green'))

		elif i == 7:
			dir7 = '/home/d0c0b/Packages/GHRepo/Leak'
			mk8 = 'sudo mkdir ' + dir7
			os.system(mk8)
			l1 = g + 'DaVinci/Cr3dOv3r'
			x1 = 'DaVinci/Cr3dOv3r '
			os.system(l1)
			place = mv + x1 + dir7
			os.system(place)
			print(colored('[+] Leak Finished [+]', 'green'))

		elif i == 8:
			dir10 = '/home/d0c0b/Packages/GHRepo/Phone'
			mk14 = 'sudo mkdir ' + dir10
			os.system(mk14)
			ph1 = g + 'tegal1337/CiLocks'
			x1 = 'tegal1337/CiLocks '
			ph2 = g + 'thelinuxchoice/droidfiles'
			x2 = 'thelinuxchoice/droidfiles '
			ph3 = g + 'palera1n/palera1n'
			x3 = 'palera1n/palera1n '
			ph4 = g + 'EntySec/Ghost'
			x4 = 'EntySec/Ghost '
			os.system(ph1)
			os.system(ph2)
			os.system(ph3)
			os.system(ph4)
			place1 = mv + x1 + dir10
			place2 = mv + x2 + dir10
			place3 = mv + x3 + dir10
			place4 = mv + x4 + dir10
			os.system(place1)
			os.system(place2)
			os.system(place3)
			os.system(place4)
			print(colored('[+] Phone Finished [+]', 'green'))

		elif i == 9:
			dir8 = '/home/d0c0b/Packages/GHRepo/MITM'
			mk9 = 'sudo mkdir ' + dir8
			os.system(mk9)
			mitm1 = g + 'byt3bl33d3r/MITMf'
			x1 = 'byt3bl33d3r/MITMf '
			os.system(mitm1)
			place = mv + x1 + dir8
			print(colored('[+] MITM Finished [+]', 'green'))

		elif i == 10:
			dir9 = '/home/d0c0b/Packages/GHRepo/Phish
			mk13 = 'sudo mkdir ' + dir9
			os.system(mk13)
			fish1 = g + 'Ignitetch/AdvPhishing'
			x1 = 'Ignitetch/AdvPhishing '
			fish2 = g + 'Black-Hell-Team/LordPhish'
			x2 = 'Black-Hell-Team/LordPhish '
			fish3 = g + 'BiZken/PhishMailer'
			x3 = 'BiZken/PhishMailer '
			os.system(fish1)
			os.system(fish2)
			os.system(fish3)
			place1 = mv + x1 + dir9
			place2 = mv + x2 + dir9
			place3 = mv + x3 + dir9
			os.system(place1)
			os.system(place2)
			os.system(place3)
			print(colored('[+] Phish Finished [+]', 'green'))

		elif i == 11:
			dir11 = '/home/d0c0b/Packages/GHRepo/Ransomware'
			mk12 = 'sudo mkdir ' + dir11
			os.system(mk12)
			R1 = g + 'ScRiPt1337/ATANK'
			x1 = 'ScRiPt1337/ATANK '
			R2 = g + 'termuxhackers-id/SARA'
			x2 = 'termuxhackers-id/SARA '
			R3 = g + 'caronero/Z-ransom'
			x3 = 'caronero/Z-ransom '
			os.system(R1)
			os.system(R2)
			os.system(R3)
			place1 = mv + x1 + dir11
			place2 = mv + x2 + dir11
			place3 = mv + x3 + dir11
			os.system(place1)
			os.system(place2)
			os.system(place3)
			print(colored('[+] Ransomware Finished [+]', 'green'))

		elif i == 12:
			dir12 = '/home/d0c0b/Packages/GHRepo/Tools'
			mk10 = 'sudo mkdir ' + dir12
			os.system(mk10)
			t1 = g + 'd3vilbug/HackBar'
			x1 = 'd3vilbug/HackBar '
			t2 = g + '90N45-d3v/BetterSniff'
			x2 = '90N45-d3v/BetterSniff '
			os.system(t1)
			os.system(t2)
			place1 = mv + x1 + dir12
			place2 = mv + x2 + dir12
			os.system(place1)
			os.system(place2)
			print(colored('[+] Tools Finished [+], 'green'))

		elif i == 13:
			dir13 = '/home/d0c0b/Packages/GHRepo/virus'
			mk11 = 'sudo mkdir ' + dir13
			os.system(mk11)
			rus = g + 'Gameye98/vbug'
			x1 = 'Gameye98/vbug '
			os.system(rus)
			place = mv + x1 + dir13
			os.system(place)
			print(colored('[+] Virus Finished [+]', 'green'))

		elif i == 14:
			dir15 = '/home/d0c0b/Packages/GHRepo/Wifi'
			mk15 = 'sudo mkdir ' + dir15
			os.system(mk15)
			w1 = g + 'makdosx/wifi-agent'
			x1 = 'makdosx/wifi-agent '
			w2 = g + 'DeaDHackS/WiFiSpy'
			x2 = 'DeaDHackS/WiFiSpy '
			os.system(w1)
			os.system(w2)
			os.system(w3)
			place1 = mv + x1 + dir15
			place2 = mv + x2 + dir15
			place3 = mv + x3 + dir15
			os.system(place1)
			os.system(place2)
			os.system(place3)
			print(colored('[+] Wifi Finisished [+]', 'green'))

		elif i == 20:
			wifiphish = 'wifiphisher'
			os.system(wifiphish)
		else:
			print('Something Went Wrong')
