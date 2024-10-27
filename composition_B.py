import string

class Date1 :
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
			
	
		if 0 < day <= Date1.daysPerMonth[ self.month ]:
		      self.day=day
		elif self.month == 2 and testDay == 29 and  self.year % 400 == 0 or self.year % 100 != 0 and (self.year % 4 == 0 ):
			 self.day=day
		else:
			raise ValueError("Invalid day: %d for month: %d" % ( self.day, self.month )) 
		print( "Date constructor: %s, %s %s" % (  self.month,self.day, self.year))                        
       
print("-----------------------------------------------------------------------")                
        
class Employee:
		
	def __init__( self, firstName, lastName, birthMonth,birthDay, birthYear, hireMonth, hireDay, hireYear ):
         self.birthDate = Date1( birthMonth, birthDay, birthYear )
         self.hireDate = Date1( hireMonth, hireDay, hireYear )  
         self.lastName = lastName
         self.firstName = firstName
         print( "Employee constructor: %s, %s" % (  self.firstName,self.lastName))
    

 

        
        
	
    
			    
    
		  
        	

  
		
    
		 
		         
    
			
 
print("----------------------------------------------------------")    
		

    
     
    
	       

    
    
		 
         
    

      
              
print("-------------------------------------------------------------------")                

employee = Employee( "Bob", "Jones",7, 12, 1949, 3, 12, 1988 )
employee1 = Employee( "Bobby", "Jones",8, 12, 1949, 3, 12, 1988 )
employee3 = Employee( "Sarah", "Jones",6, 12, 1941, 4, 12, 1989 )





         
