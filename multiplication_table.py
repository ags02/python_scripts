#Multiplication table
#multiplication_table.py
##################
#Range limit=30  #
#@author:Abe     #
#@flags=Boolean  #
#@range=integer  #
##################

<<<<<<< HEAD
####################################
#Tested in python2.7 using WingIDE #
####################################
=======
######################
#Tested in python3.3 #
######################
>>>>>>> cd0537348b74da580369aa53c852c4a65480a959
flags=True
while flags:
    multi_table_range=int(input("Enter multiplication table range (max. is 30): "))
    if multi_table_range>=31:
        cont=input("Table range exceeded! \nContinue it anyway (yes/no)? :")
        if (cont.lower()=='yes' or cont.upper()=='YES' or
            cont.lower()=='y' or cont.upper()=='Y'):
            flags=True
        else:
            
            exit()
    else:
        flags=False
        #x_base
        #First x base position for multiplication
        for x_base in range(0,multi_table_range+1):
<<<<<<< HEAD
			
           
            #print (end='')
			print '',
            
			if(len(str(x_base))==2):
                    #print (result,end='   ')
				print str(x_base)+'  ',
                    
			elif (len(str(x_base))==3):
                     #print (result,end='  ')
				print str(x_base)+'  ',
                     
			else:
                   
				if x_base==0:
                    
                    #print ('#',end='    ')
                    #print (x_base,end='    ')
					print '#   ',str(x_base)+'   ',
				else:
                    
                    #print (x_base,end='    ')
					print str(x_base)+'   ',
=======
           
            print (end='')
            
            if(len(str(x_base))==2):
                
                print (x_base,end='   ')
            elif (len(str(x_base))==3):
              
                print (x_base,end='   ')
            else:
                
                if x_base==0:
                    
                    print ('#',end='    ')
                    print (x_base,end='    ')
                else:
                    
                    print (x_base,end='    ')
>>>>>>> cd0537348b74da580369aa53c852c4a65480a959
                    
                 
                

        #x and y base content
        #Multiplication loop
        #Range added by 1
        #to make it exactly
       
        for x in range(0,multi_table_range+1):
<<<<<<< HEAD
			
            
            #print()
				print
				if(len(str(x))==2):
                #print (x,end='   ')
					print str(x)+'   ',
                    
				elif (len(str(x))==3):
                #print (x,end='   ')
					print str(x)+'  ',
                     
				else:
                #print (x,end='    ')
					print str(x)+'    ',
            
				for y in range(0,multi_table_range+1):
                
                    
					result=x*y
            
					if(len(str(result))==2):
                    #print (result,end='   ')
						print str(result)+'   ',
                    
					elif (len(str(result))==3):
                     #print (result,end='  ')
						print str(result)+'  ',
                     
					else:
                   # print (result,end='    ')
						print str(result)+'    ',
=======
            
            print()
            if(len(str(x))==2):
                print (x,end='   ')
                    
            elif (len(str(x))==3):
                print (x,end='   ')
                     
            else:
                print (x,end='    ')
            
            for y in range(0,multi_table_range+1):
                
                    
                result=x*y
            
                if(len(str(result))==2):
                    print (result,end='   ')
                    
                elif (len(str(result))==3):
                     print (result,end='  ')
                     
                else:
                    print (result,end='    ')
>>>>>>> cd0537348b74da580369aa53c852c4a65480a959
        
           
        
