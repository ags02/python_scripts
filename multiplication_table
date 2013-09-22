#Multiplication table
#multiplication_table.py
##################
#Range limit=30  #
#@author:Abe     #
#@flags=Boolean  #
#@range=integer  #
##################

######################
#Tested in python3.3 #
######################
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
                    
                 
                

        #x and y base content
        #Multiplication loop
        #Range added by 1
        #to make it exactly
       
        for x in range(0,multi_table_range+1):
            
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
        
           
        
