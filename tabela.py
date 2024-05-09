#!/usr/bin/env python


import MySQLdb as db
from datetime import datetime, timedelta
import paramiko
from time import sleep


HOST = "banco_ap"
USER = "root"
PASSWORD = "Noki@500"
DB = "pup"
IP_AP = '192.168.1.1'
USER_AP = 'root'
PASSWORD_AP = 'Noki@600'


while(True):

	hora_atual = datetime.now() - timedelta(hours=3)
	string_data_hora = str(hora_atual.date())+' '+str(hora_atual.hour)+':'+str(hora_atual.minute)+':'+str(hora_atual.second)

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(IP_AP, username=USER_AP, password=PASSWORD_AP)

	stdin, stdout, stderr = ssh.exec_command("iw dev wlan1 station dump | grep Station | awk '{{print $2}}'")
	saida_iw = stdout.readlines()

	ssh.close()

	macs = [item[:-1] for item in saida_iw]
	#print(macs)

	membros = {}
	try:
		connection = db.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
		dbhandler = connection.cursor()
		dbhandler.execute("SELECT * FROM membros")
		results = dbhandler.fetchall()
		#print(results)
		for row in results:
			membros[row[0]] = {}
			membros[row[0]]['Nome'] = row[0]
			membros[row[0]]['MAC_Address'] = row[1].upper()
			membros[row[0]]['Departamento'] = row[2]
			membros[row[0]]['Visto_Ultima_Vez'] = row[3]
			membros[row[0]]['Presenca'] = 0
		#print('MEMBROS: ',membros)

		for mac in macs:
			for membro in membros.keys():
				print(membros[membro]['MAC_Address'], mac[0:len(mac)].upper())
				if membros[membro]['MAC_Address'] == mac[0:len(mac)].upper():
					membros[membro]['Presenca'] = 1
					membros[membro]['Visto_Ultima_Vez'] = string_data_hora
		#print('MEMBROS: ',membros)

		for membro in membros.keys():
			dbhandler.execute("UPDATE membros SET Presenca = %s, `Visto_Ultima_Vez` = %s WHERE Nome = %s", (membros[membro]['Presenca'], membros[membro]['Visto_Ultima_Vez'], membros[membro]['Nome']))
			#print(membros)
	except Exception as e:
		print(e)

	connection.commit()
	connection.close()
	sleep(30)
	