from yapl_lexer import *
from yapl_parser import *
import sys

# other global variables
variable = []
functions_list = {}
global_var = {}

variable.append(global_var)

def exp_eval(p): # evaluate expression
    
    operator = p[0]
      
    #print(p)
    
    if operator == '+': 
        
        try:
            return ( exp_eval(p[1]) + exp_eval(p[2]) )
        
        except:
			
            print( "TypeError")
            #print(  exp_eval(p[1]),"    ", exp_eval(p[2])   )
            exit(1)
            			
    elif operator == 'NOT':
    
        try:
            if exp_eval(p[1]) == "TRUE":
                return "FALSE"
            else:
                return "TRUE"        
        
        
        except:
            print("Error")
            exit(1)
    
    elif operator == 'AND':
    
        try:
            if ((exp_eval(p[1]) == "TRUE") and (exp_eval(p[2]) == "TRUE")):
                return "TRUE"
            else:
                return "FALSE"        
        
        
        except:
            print("Error")
            exit(1)
            
    elif operator == 'OR':
    
        try:
            if ((exp_eval(p[1]) == "TRUE") or (exp_eval(p[2]) == "TRUE")):
                return "TRUE"
            else:
                return "FALSE"        
        
        
        except:
            print(" Error")
            exit(1)
    
    elif operator == '<':
    
        try:
            if ( exp_eval(p[1]) < exp_eval(p[2]) ):
                return "TRUE"
            else:
                return "FALSE"                
        except:
            print(" Error")
            exit(1)
    
    elif operator == '>':
    
        try:
            if ( exp_eval(p[1]) > exp_eval(p[2]) ):
                return "TRUE"
            else:
                return "FALSE"                
        except:
            print(" Error") 
            exit(1)
    
    elif operator == '<=':
    
        try:
            if ( exp_eval(p[1]) <= exp_eval(p[2]) ):
                return "TRUE"
            else:
                return "FALSE"                
        except:
            print(" Error") 
            exit(1)
    
    elif operator == '>=':
    
        try:
            if ( exp_eval(p[1]) >= exp_eval(p[2]) ):
                return "TRUE"
            else:
                return "FALSE"                
        except:
            print(" Error") 
            exit(1)
    
    elif operator == '==':
    
        try:
            
            if ( exp_eval(p[1]) == exp_eval(p[2]) ):
                return "TRUE"
            else:
                return "FALSE"                
        except:
            print(" Error") 
            exit(1)                 
    
    elif operator == '!=':
    
        try:
            if ( exp_eval(p[1]) != exp_eval(p[2]) ):
                return "TRUE"
            else:
                return "FALSE"                
        except:
            print(" Error")
            exit(1) 
    
    elif operator == '-':
    
        try:
            return exp_eval(p[1]) - exp_eval(p[2])
        except:    
            print ("TypeError")
            exit(1)
               
    elif operator == '*':
    
        try:
            return exp_eval(p[1]) * exp_eval(p[2])
        except:    
            print( "TypeError")
            exit(1)
            
    elif operator == '%':
    
        try:
            return exp_eval(p[1]) % exp_eval(p[2])
        except:    
            print ("TypeError")
            exit(1)
            
    elif operator == '^':
    
        try:
            return pow ( exp_eval(p[1]),  exp_eval(p[2]) )
        except:    
            print( "TypeError")
            exit(1)
            
    elif operator == '/':
        if exp_eval(p[2]) == 0:
            print("DivisionByZeroError")
            exit(1)      
        try:
            return exp_eval(p[1]) / exp_eval(p[2])
        except:    
            
            print ("TypeError")
            exit(1)
                        
    elif operator == ',': # for printing purposes only
        try:
            return ( str(exp_eval(p[1]))+ ' '  +  str(exp_eval(p[2])) ) 
        except:
            print("Error")
            exit(1)
            
    elif operator== 'str': # operator was 'NUM' so its just a number  FOR printing purposes
        return p[1]
    
    elif operator == 'NAME': # for printing purposes only 
        
        try:           
         
            for t in range(len(variable)-1, -1 , -1):	
                if p[1] in variable[t].keys():
                    return variable[t][p[1]][1]
        except:
            print( "error")
            exit(1)     
    
    elif operator == 'slice': # for printing purposes only 
        
        try:           
            check = False
            for t in range(len(variable)-1, -1 , -1):	
                if  p[3] in variable[t].keys() :
                    
                    if variable[t][p[3]][0] == "LIST":
                        if( ( p[2] > len(variable[t][p[3]][1]) ) or (p[1]<0) ):
                            print("IndexOutOfBoundsError")
                            check = True
                            exit(1)
                        
                        return variable[t][p[3]][1][p[1]:p[2]]
        except:
            if check == False:
                print( "slicing error")
            exit(1) 
    
    elif operator == 'INDEX': # for printing purposes only 
        
        try:           
            check = False
            for t in range(len(variable)-1, -1 , -1):	
                if  p[1] in variable[t].keys() :
                    
                    if variable[t][p[1]][0] == "LIST":
                        if( ( p[2] > len(variable[t][p[1]][1])-1 ) or (p[2]<0) ):
                            print("IndexOutOfBoundsError")
                            check = True
                            exit(1)
                        
                        return variable[t][p[1]][1][p[2]]
        except:
            if check == False:
                print( "error")
            exit(1)

    elif operator == 'POP': # for printing purposes only 
        
        try:           
            check = False
            for t in range(len(variable)-1, -1 , -1):	
                if  p[1] in variable[t].keys() :
                    
                    if variable[t][p[1]][0] == "LIST":
                        if( ( p[2] > len(variable[t][p[1]][1])-1 ) or (p[2]<0) ):
                            print("IndexOutOfBoundsError")
                            check = True
                            exit(1)
                        
                        return variable[t][p[1]][1].pop(p[2])
        except:
            if check == False:
                print( "error")
            exit(1)
 
    elif operator == 'CALL_FUNC': 
        try:
            #print(p)
            for x in functions_list.keys():
                check = True
                if (p[1] == x) and len(p[2]) ==  len(functions_list[p[1]][0]) :
                    #print("here")
                    dict_vars= {}
                    num = 0
                    for y in functions_list[p[1]][0]:
                        #print("y", y)
                        #print( variable)
                        #print(p)
                        #print("num ", num)
                        #print( " p" ,p[2][num][0][0])
                        #print(" exp eval" , exp_eval( p[2][num][0]))
                        #if ((y[0][0]== 'INT') and ( p[2][num][0][0]!= 'int')): 
                        #    check = False
                            #print( y[0][0] , " ", exp_eval( p[2][num][0][0])  )                          
                            #print("int ",check)
                            
                        #elif ( (y[0][0]== "STRING") and( p[2][num][0][0]!="str")): 
                        #    check = False  
                            #print("string ",check)
                            #print( y[0][0] , " ", p[2][num][0])
                            
                        #elif ((y[0][0]== "BOOL") and ( ( p[2][num][0][1]!="TRUE")  and ( p[2][num][0][1]!="FALSE")) ): 
                        #    check = False  
                            #print("bool ",check)
                            #print( y[0][0] , " ", p[2][num][0][1])
                            
                        #elif ((y[0][0]== "FLOAT") and( p[2][num][0][0]!="float")): 
                        #    check = False  	
                            #print("float ",check)
                            #print( y[0][0] , " ", p[2][num])	
                            					
                        #elif ( (y[0][0]== "CHAR") and ( len(p[2][num][0][1])!=1) ):
                        #    check = False  
                            #print("char ",check)  
                            #print( y[0][0] , " ", p[2][num][1]) 
                        #else:
                        #    dict_vars.update( {y[0][1] : [ y[0][0] ,p[2][num][0][1]   ] }  )             
                        dict_vars.update( {y[0][1] : [ y[0][0] , exp_eval( p[2][num][0]  ) ] }  )  
                        num= num+1
                #print(check) 
                #print(dict_vars)       
                if (check == True): 
					        
                    variable.append(dict_vars)
                  
                    for m in  functions_list[p[1]][1]:
                        if m != None:
                            #print(" printing from exp eval",m[0])
                            ans =  func_eval(m)
                            #print(" returnrf ans is " , ans)          
                            if(ans!=None):
                                variable.pop()
                                #print("variable has been popped")
                                return ans
                                exit(1) 
    
                else:
                    print("error")
                    exit(1)    
                         
			
        except:	 
            print(" function call error")
            exit(1)       
    
    else:
        return p[1] 

def func_eval(p):  
    stype = p[0]
    
    
    if stype == 'PRINT':	
        
        exp = p[1]        
        result = exp_eval(exp)
        print(result)
    
    elif stype == 'assign':
        
        if p[2] not in variable[-1].keys():
            variable[-1].update({p[2] : [   p[1]  , ' ' ] })
            #print(variable)
        else:
            print( "RedeclarationError" )
            exit(1)
             
    elif stype == 'assign_val':
        
        if p[1] not in variable[-1].keys():
            variable[-1].update({p[1] : [   p[3]  , exp_eval(p[2]) ] })
            #print(variable)
        else:
            print( "RedeclarationError" )
            exit(1)
    
    elif stype == 'update':
        
        try:
                    
          
            if p[1] in variable[-1].keys():                    
                variable[-1][p[1]][1]= exp_eval(p[2])      
                return
            elif p[1] in variable[0].keys(): 
                variable[0][p[1]][1]= exp_eval(p[2])      
                return
        
        
        except:
            print( "variable not found" )
            exit(1)	
    
    elif stype == 'increment':       
        try:
            if p[1] in variable[-1].keys():                    
                variable[-1][p[1]][1] = ( variable[-1][p[1]][1] + 1 )    
                return
            elif p[1] in variable[0].keys(): 
                variable[0][p[1]][1] = ( variable[0][p[1]][1] + 1 )    
                return
                             
           
        except:
            print(" increment error") 
            exit(1)
    
    elif stype == 'decrement':
        try:

            if p[1] in variable[-1].keys():                    
                variable[-1][p[1]][1] = ( variable[-1][p[1]][1] - 1 )    
                return
            elif p[1] in variable[0].keys(): 
                variable[0][p[1]][1] = ( variable[0][p[1]][1] - 1 )    
                return
        except:
            print(" decrement error") 
            exit(1)

    elif stype == 'IF':
        
        
        #print("HERE")
        try:
            #print ( exp_eval(h[1])  )
            #print("here") 
            h = p[1]
            else_if = p[2]
            if ((h[0] == 'IF') and (exp_eval(h[1])== "TRUE")):
                #print()
                #print(h[1])
                #print(" if here")
                for x in h[2]: # statements in proglist
                    if x != None:                         
                        ans = func_eval(x)
                        #print("ans is" , ans)
                        
                        if(ans!=None):
                            #variable.pop()
                            #print("variable has been popped")
                            return ans
                            exit(1)   
                            
                            
						
						
                                 
                        #func_eval(x) 
            elif len(else_if) != 0 :
                elseifDone = False
                #print("else if here")
                #print(else_if)
                for x in else_if:
                    #print(x) 
                    #print(" statemrnt that needs to be true is",x[1])  
                    #print( "variable", variable)
                    #print(exp_eval(x[1]) )
                    
                    if(( x[0] == 'ELSEIF' ) and  (exp_eval(x[1])== "TRUE")):   
                        elseifDone = True
                        #print("elseif is true")
                        for y in x[2]: # statements in proglist
                            #print(" the statmen being evaluated is",y)
                            if y != None:
                                
                                ans =  func_eval(y)
                                #print("ans is" , ans)
                                
                                if(ans!=None):
                                    #variable.pop()
                                    #print("variable has been popped")
                                    return ans
                                         
                                
                if elseifDone == False:
                    elsee = p[3]
                    #print("insdid else")
                    #print(elsee)
                    if (elsee[0] == 'ELSE'):
                        for x in elsee[1]:
                            #print()
                            #print(x)
                            if x != None:
                                ans =  func_eval(x)
                                #print("ans is" , ans)
                                if(ans!=None):
                                   #variable.pop()
                                   #print("variable has been popped")
                                   return ans
                                   #exit(1)                           
                                
                        #return 
            #print(len(p))
            elif len(p) == 4:
                elsee = p[3]
                #print("insdid else")
                #print(elsee)
                if (elsee[0] == 'ELSE'):
                    for x in elsee[1]:
                        #print()
                        #print(x)
                        if x != None:
                            ans =  func_eval(x)
                            #print("ans is" , ans)
                            if(ans!=None):
                                #variable.pop()
                                #print("variable has been popped")
                                return ans
                                #exit(1)                          
        except: 
            print("Error")    
            exit(1)
    
    elif stype == 'DO':
        try:
            while(True):
                variable.append({})
                
                for x in p[1]:
                    if x != None:
                        stmt_eval(x)
                variable.pop()
                if( exp_eval(p[2]) == "FALSE" ):
                    return
        except:		        
            print(" Do while Error")
            exit(1)    
    
    elif stype == 'assign_list': 
        try:
            val = p[2]
            toMake = []
            for l in val:
                toMake.append(exp_eval(l[0]) )
                #print(  exp_eval(l[0])   ) 
            
            variable[-1].update({ p[1] : [ 'LIST'  , toMake ] }) 
            #print(variable)
                  
        except:
            print("list decleration error")
    
    elif stype == 'assign_list_noVAl': 
        try:                       
            variable[-1].update({ p[1] : [ 'LIST'  , [ ] ] }) 
            #print(variable)
                 
        except:
            print("list decleration error") 
    
    elif stype == 'PUSH': 
        try:                         
           	
            if  p[1] in variable[-1].keys() :                   
                if variable[-1][p[1]][0] == "LIST":
                    variable[-1][p[1]][1].append( exp_eval( p[2] ) )   
            elif  p[1] in variable[0].keys() :                   
                if variable[0][p[1]][0] == "LIST":
                    variable[0][p[1]][1].append( exp_eval( p[2] ) )              
                       
        except:
            print( "push error")
            exit(1)

    elif stype == 'FUNCTION_DEFINE': 
        try:
            functions_list.update({ p[1]: (p[2],p[3])     } )
        except:
            print( "function definition error")
            exit(1)
    
    elif stype == 'RETURN': 
        try:
            #print(  "when n is 1 or zero", exp_eval( p[1] ) )
            return  exp_eval( p[1] )
            exit()
        
        except:
            print( "function definition error")
            exit(1)

def stmt_eval(p): # p is the parsed statement subtree / program   
    stype = p[0] # node type of parse tree
    #print(p[1])
    
    if stype == 'PRINT':	
        
        exp = p[1]        
        result = exp_eval(exp)
        print(result)
    
    elif stype == 'assign':
        
        if p[2] not in variable[-1].keys():
            
            variable[-1].update({p[2] : [   p[1]  , ' ' ] })
            #print(variable)
        else:
            print( "RedeclarationError" )
            exit(1)
             
    elif stype == 'assign_val':
        
        check = True
        #if ((p[3] == 'INT') and (  type(exp_eval(p[2])).__name__ != 'int')): 
        #    check = False                   
        #elif ((p[3]== "STRING") and( type(exp_eval(p[2])).__name__!="str")): 
        #    check = False                           
        #elif ((p[3]== "BOOL") and ( exp_eval(p[2]) !="TRUE")  and ( exp_eval(p[2]) !="FALSE")): 
        #    check = False   
        #elif ((p[3]== "FLOAT") and( type(exp_eval(p[2])).__name__!="float")): 
        #    check = False  	                           					
        #elif ((p[3]== "CHAR") and ( len(exp_eval(p[2]))!=1) ):
        #    check = False  
                          
                        
        
        if (check ==False):
            print( "Type Error" )
            exit(1)
        
        
        
        if p[1] not in variable[-1].keys():
            variable[-1].update({p[1] : [   p[3]  , exp_eval(p[2]) ] })
            
        else:
            print( "RedeclarationError" )
            exit(1)
    
    elif stype == 'update':
        
        try:
                             
            for t in range( len(variable)-1 , -1 , -1):
                if p[1] in variable[t].keys():                    
                    
                    
                    check = True
                    #if ((  variable[t][p[1]][0] == 'INT') and (  type(exp_eval(p[2])).__name__ != 'int')): 
                    #    check = False                   
                    #elif ((   variable[t][p[1]][0]== "STRING") and( type(exp_eval(p[2])).__name__!= "str")): 
                    #    check = False                           
                    #elif ((variable[t][p[1]][0]== "BOOL") and ( exp_eval(p[2]) !="TRUE")  and ( exp_eval(p[2]) !="FALSE")): 
                    #    check = False   
                    #elif ((variable[t][p[1]][0]== "FLOAT") and( type(exp_eval(p[2])).__name__!="float")): 
                    #    check = False  	                           					
                    #elif (( variable[t][p[1]][0]== "CHAR") and ( len(exp_eval(p[2]))!=1) ):
                    #    check = False 
                    
                    
                    
                    if check==True:
                        variable[t][p[1]][1]= exp_eval(p[2])      
                        return
                    else:
                        print( "Type Error" )
                        exit(1)
						
						
                    
        
        
        except:
            print( "variable not found" )
            exit(1)	
    
    elif stype == 'increment':       
        try:
                         
            for t in range( len(variable)-1 , -1 , -1):
                #print("here")
                if p[1] in variable[t].keys():                    
                    variable[t][p[1]][1] = ( variable[t][p[1]][1] + 1 )    
                    return
        except:
            print(" increment error") 
            exit(1)
    
    elif stype == 'decrement':
        try:

            for t in range( len(variable)-1 , -1 , -1):
                #print("here")
                if p[1] in variable[t].keys():                    
                    variable[t][p[1]][1] = ( variable[t][p[1]][1] - 1 )    
                    return
        except:
            print(" decrement error") 
            exit(1)

    elif stype == 'IF':
        
        h = p[1]
        else_if = p[2]
        
        try:
            #print ( exp_eval(h[1])  ) 
            
            if ((h[0] == 'IF') and (exp_eval(h[1])== "TRUE")):
                variable.append({})
                for x in h[2]: # statements in proglist
                    if x != None:          
                        stmt_eval(x) 
                variable.pop()
            elif len(else_if) != 0 :
                for x in else_if:    
                    if(( x[0] == 'ELSEIF' ) and  (exp_eval(x[1])== "TRUE")):   
                        variable.append({})
                        for y in x[2]: # statements in proglist
                            if y != None:          
                                stmt_eval(y)
                        variable.pop()
                        return 
            
            elif len(p) == 4:
                elsee = p[3]
                #print(elsee)
                if (elsee[0] == 'ELSE'):
                    variable.append({})
                    for x in elsee[1]:                      
                        if x != None:          
                            stmt_eval(x) 
                    variable.pop()                                 
        except: 
            print("Error")    
            exit(1)
    
    elif stype == 'DO':
        try:
            while(True):
                variable.append({})
                #print(variable)
                for x in p[1]:
                    if x != None:
                        stmt_eval(x)
                variable.pop()
                if( exp_eval(p[2]) == "FALSE" ):
                    return
        except:		        
            print(" Do while Error")
            exit(1)    
    
    elif stype == 'assign_list': 
        try:
            val = p[2]
            toMake = []
            for l in val:
                toMake.append(exp_eval(l[0]) )
                #print(  exp_eval(l[0])   ) 
            
            variable[-1].update({ p[1] : [ 'LIST'  , toMake ] }) 
            #print(variable)
                  
        except:
            print("list decleration error")
    
    elif stype == 'assign_list_noVAl': 
        try:                       
            variable[-1].update({ p[1] : [ 'LIST'  , [ ] ] }) 
            #print(variable)
                 
        except:
            print("list decleration error") 
    
    elif stype == 'PUSH': 
        try:           
            for t in range(len(variable)-1, -1 , -1):	
                if  p[1] in variable[t].keys() :                   
                    if variable[t][p[1]][0] == "LIST":
                        variable[t][p[1]][1].append( exp_eval( p[2] ) )   
                        
                       
        except:
            print( "push error")
            exit(1)

    elif stype == 'FUNCTION_DEFINE': 
        try:
            functions_list.update({ p[1]: (p[2],p[3])     } )
        except:
            print( "function definition error")
            exit(1)




def run_program(p): # p[0] == 'Program': a bunch of statements
    for stmt in p: # statements in proglist
        if stmt != None:
            #print(stmt)
            stmt_eval(stmt) # statement subtree as tuple
        



if len(sys.argv) == 1:
    print('File name/path not provided as cmd arg.')
    exit(1)



while True:
    fileHandler = open(sys.argv[1],"r")
    userin = fileHandler.read()
    fileHandler.close()

    print("Welcome to your YAPL's Interpreter!")
    parsed = parser.parse(userin)
    if not parsed:
        continue
    
    for line in userin.split('\n'):
        print(line)
    print("=========================================\n{OUTPUT}")
    try:
        #print(parsed)
        print()
        run_program(parsed)
        
    except Exception as e:
        print(e)
    
    input("Press any key to run code again.")


exit()
