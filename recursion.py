#!/usr/bin
#recursion with modulus expression
#
#recursion input
recursion_limit=int(input("Enter recursion level limit:"))
#Defined list 
#suffixes
suffix=['st','nd','rd','th']

#Lists
mod_list=[]
mod_list_temp=[]
mod_divisible=[]
mod_not_divisible=[]

def recursion(start,flags,div_,not_div_):
    if not flags:
        for idx in range(len(suffix)):
            mod=input("Enter your %d%s modulus:"%(idx+1,suffix[idx]))
	    dup=False
	    
	    if len(mod_list) == 0:
		mod_list.append(mod)
		
	    else :
		mod_list_temp.append(mod_list[0])
		mod_list_temp.sort()
		for check_idx in range(len(mod_list_temp)):
		    
		    if mod_list_temp[check_idx] == mod:
			
			dup=True
			flags=1
		    else:
			mod_list_temp.append(mod)
		
		if not dup:
		    mod_list.append(mod)
			
		    flags=1
		flags=1    
            
    if start<=recursion_limit:
	mod_list.sort()
	for mod_idx in range(len(mod_list)):
	       
	    if start %mod_list[mod_idx]==0:
		mod_divisible.append(mod_list[mod_idx])               
		div_=True    
	    else:
		mod_not_divisible.append(mod_list[mod_idx])
		not_div_=True
		       #Check duplicates before appending
		      
		
			   
	if div_:
	    if not len(mod_divisible)==0:
		print "%d is divisible by %s" %(start,mod_divisible)
	if not_div_:
	    if not len(mod_not_divisible)==0:
		print "%d is not divisible by %s" %(start,mod_not_divisible)
	       
	       #recursion level update
	start=start+1
	       
	    #clear list content
	mod_divisible[:]=[]
	mod_not_divisible[:]=[]	
	
        #recursion statement caller   
        recursion(start,flags,div_,not_div_)

#recursion initialization
recursion(start=0,flags=0,div_=False,not_div_=False)

