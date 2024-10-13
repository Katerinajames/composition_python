class Date :
	daysPerMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
	def __init__(self,month,day,year):
		if 0 < month <= 12:
			self.month = month
		else:
			raise ValueError("Invalid value for month: %d" % (month))
		if year >= 0:
			self.year = year
		else:
			raise ValueError("Invalid value for year: %y" %( year))
			self.day = self.checkDay( day )
			self.display()
	def checkDay( self, testDay ):
		if 0 < testDay <= Date.daysPerMonth[ self.month ]:
		     return testDay  
		elif self.month == 2 and testDay == 29 and  self.year % 400 == 0 or self.year % 100 != 0 and (self.year % 4 == 0 ):
			 return testDay
		else:
			raise ValueError("Invalid day: %d for month: %d" % ( testDay, self.month ))                         
        
             
print("-----------------------------------------------------------------------")                
        
class Employee:
	def __init__( self, firstName, lastName, birthMonth,birthDay, birthYear, hireMonth, hireDay, hireYear ):
         self.birthDate = Date( birthMonth, birthDay, birthYear )
         self.hireDate = Date( hireMonth, hireDay, hireYear )  
         self.lastName = lastName
         self.firstName = firstName
 
    
		

    
     
    
	       

    
    
		 
         
    

      
              
print("-------------------------------------------------------------------")                
     
employee = Employee( "Bob", "Jones", 7, 24, 1949, 3, 12, 1988 )
print   

      
         
