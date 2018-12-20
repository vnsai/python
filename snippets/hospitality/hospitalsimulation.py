import pandas as pd
import numpy as np
def registration(desease_rate):
	print "Patient registration:"
	patient_name=raw_input("Enter patient name: ")
	for (i,j) in zip(desease_rate.index,desease_rate['desease']):
		print str(i)+' '+str(j)
	desease_index=raw_input("Select one desease index: ")
	return {'name':patient_name,'desease':desease_index}
def patinetdetails(current_patients):
			for i in current_patients:
				print i
def staff_signin(staff_data,current_staff):
	for (i,j) in zip(staff_data.index,staff_data['staff']):
		if str(i) not in current_staff:
			print i,j
	staff_index=raw_input("Enter staff to sign in: ")
	return staff_index
def staff_details(staff_data,current_staff):
	for (i,j) in zip(staff_data.index,staff_data['staff']):
		status=  'in' if str(i) in current_staff else 'out' 
		print i,j,status
def patient_signoff(current_patients):
	index=-1
	for i in current_patients:
		index+=1
		print index,i
	ind=raw_input('Enter index of patient: ')
	current_patients.pop(int(ind))
	return current_patients
def staf_signoff(staff_data,current_staff):
	index=-1
	for i in current_staff:
		index+=1
		print index,staff_data['staff'][int(i)]
	ind=raw_input('Enter index of staff: ')
	current_staff.pop(int(ind))
	return current_staff
def number_hours(current_patients,current_staff,desease_rate):
	current_staf_len=len(current_staff)
	desease_hour_sum=0
	for current_patient in current_patients:
		curent_des_rate=desease_rate['hours'][int(current_patient['desease'])]
		desease_hour_sum=desease_hour_sum+curent_des_rate
	return (desease_hour_sum/current_staf_len)
def number_staff_required(current_patients,current_staff,desease_rate,staff_data):
	hours=int(raw_input('In howmany hours want to finish the serve: '))
	current_staf_len=len(current_staff)
	desease_hour_sum=0
	for current_patient in current_patients:
		curent_des_rate=desease_rate['hours'][int(current_patient['desease'])]
		desease_hour_sum=desease_hour_sum+curent_des_rate

	print "total sign in staff members:",current_staf_len
	print "total hours required for the current staff: ",(desease_hour_sum/current_staf_len)
	key=desease_hour_sum/hours
	if key-current_staf_len<=0:
		print "Current Staff enough"
	elif key-current_staf_len>0:
		extra_staf=key-current_staf_len
		print "extra staff required to server the current patients in",hours,"hours is: ",extra_staf
		contract=extra_staf-(len(staff_data)-current_staf_len)
		if contract>0:
			print "Need to recruit: ",contract,



try:
	desease_rate=pd.read_csv('desease-rate.csv')
	staff_data=pd.read_csv('staff.csv')
	current_patients=[]
	current_staff=[]
	token=0
	while 1:
		print """
		1.Patient sign in
		2.Patient signoff
		3.Staff signin
		4.Staff signoff
		5.Number of hours needed to serve current patinets with current staff
		6.Number of staff required to complete serve in hours
		7.Patient Details
		8.Staff details
		9.Quit
		"""
		flag=raw_input("Enter Option->: ")
		if flag=='1':
			token=token+1
			patient=registration(desease_rate)
			patient.update({'token':token})
			current_patients.append(patient)
		if flag=='2':
			current_patients=patient_signoff(current_patients)
		elif flag=='3':
			staff_in=staff_signin(staff_data,current_staff)
			current_staff.append(staff_in)
		elif flag=='4':
			current_staff=staf_signoff(staff_data,current_staff)
		elif flag=='5':
			print number_hours(current_patients,current_staff,desease_rate),"hours needed to serve the patients"
		elif flag=='6':
			number_staff_required(current_patients,current_staff,desease_rate,staff_data)
		elif flag=='7':
			patinetdetails(current_patients)
		elif flag=='8':
			staff_details(staff_data,current_staff)
		elif flag=='9':
			break
		else:
			print "Invalid option"
except Exception as err:
	print err
