class Patient:
  admitted = True  ### 7.4.1 class attribute
  
  def __init__(self, fname, lname, age, ss, critical_condition=None):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.ss = ss
    self.critical_condition = critical_condition

  def name(self):
    return self.fname + ' ' + self.lname
  
  def set_critical_condition(self, condition):
    self.critical_condition = condition
  
  def is_critical(self):
    if self.critical_condition is not None:
      return True
    else:
      return False 

class Doctor:
  def __init__(self, fname, lname, specialty, on_call=False):
    self.fname = fname
    self.lname = lname
    self.specialty = specialty
    self.on_call = on_call

  def name(self):
    return self.fname + ' ' + self.lname


###### Main
# Doctor class instantiations
doctor01 = Doctor('Hawkeye', 'Pierce', 'Cardiologist', on_call=True)
doctor02 = Doctor('Greg', 'House', 'Neurologist')

doctors = [doctor01, doctor02]

doctor_on_call = None

for doctor in doctors:
  if doctor.on_call:
    doctor_on_call = doctor
    print(f'Setting {doctor.fname} {doctor.lname} to on call\n')

# Patient class instantiations
patient01 = Patient('Dan', 'Lloyd', 49, '123-45-6789', critical_condition='stroke')
patient02 = Patient('Marsha', 'Brady', 67, '987-65-4321')
patient03 = Patient('Bob', 'Marley', 36, '555-67-1267')
patient04 = Patient('Janet', 'Reno', 78, '010-43-9998')

patients = [patient01, patient02, patient03, patient04]

patient03.set_critical_condition('pneumonia')

for patient in patients:
  if patient.is_critical():
    print(f'Patient {patient.name()} is in critical condition: {patient.critical_condition}')
    
print(f'The doctor on call is {doctor_on_call.name()} ({doctor_on_call.specialty})')
