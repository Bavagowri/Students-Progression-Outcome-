def input_credits():                               #To take inputs and check whether they are integers and in the given range
    global pass_credits
    global defer_credits
    global fail_credits
    global total
    global outcome_in_total
    try:
        pass_credits=int(input("Enter your total PASS credits:"))         #To take input for pass_credits    
        if pass_credits not in credits_range:                             #To output the message if pass_credits not in the defined credit range
            print("The crdits you entered are 'Out of Range'")
            print()  #To print a blank line
        else:
            defer_credits=int(input("Enter your total DEFER credits:"))
            if defer_credits not in credits_range:                        #To output the message if defer_credits not in the defined credit range
                print("The crdits you entered are 'Out of Range'")
                print()  #To print a blank line
            else:
                fail_credits=int(input("Enter your total FAIL credits:"))     
                if fail_credits not in credits_range:                         #To output the message if fail_credits not in the defined credit range
                    print("The crdits you entered are 'Out of Range'")
                    print()  #To print a blank line
                else:     
                    total= pass_credits+defer_credits+fail_credits         #If all inputs are valid then we have to add them all
                    if total!=120:                                          #If total not equal to 120 it will output the message below it
                        print("'Total incorrect'")
                        print()   #To print a blank line
                    if total==120:                                        # If total is equal to 120 then program will executes the user defined function progress_outcome
                        progress_outcome()                                #To validate the progression outcome
                        outcome_in_total+=1                               #To calculate the no.of students under all progression category
                        save_input()                                      #To save the valid inputs 
    
    except ValueError:                               
        print("Interger required")                                       # Outputs the message if input is not an integer
        print()        #To print a blank line

        


def progress_outcome():                         # To predict the progression outcome
    global pro_count
    global mod_tra_count
    global mod_ret_count
    global ex_count
    global progression_outcome
    global total_outcome
    if (pass_credits == 120 and (defer_credits == 0 and fail_credits == 0)):                  #Condition to get the progression outcome as 'Progress'
        progression_outcome=progression[0]
        print("progression outcome=",progression[0])                                          #To print the progression outcome
        pro_count +=1                                                                         #To calculate no.of students who got the progression outcome as 'Progress'
        total_outcome[0]=pro_count                                                            #To update the value in the list names as total_outcome
        print()                                                                               #To have a blank line before outputing the promt command
    elif (pass_credits == 100 and (defer_credits or fail_credits == 20)):                     #Condition to get the progression outcome as 'Progress(module trailer)'
        progression_outcome=progression[1]                                                    
        print("progression outcome=",progression[1])                                          #To print the progression outcome
        mod_tra_count +=1                                                                     #To calculate no.of students who got the progression outcome as 'Progress(module trailer)'
        total_outcome[1]=mod_tra_count                                                        #To update the value in the list names as total_outcome
        print()                                                                                #To have a blank line before outputing the promt command
    elif (0 <= pass_credits <= 80 and 0 <= fail_credits <= 60 and 0 <= defer_credits <= 120):  #Condition to get the progression outcome as 'Module retreiver'
        progression_outcome=progression[2]
        print("progression outcome=",progression[2])                                           #To print the progression outcome
        mod_ret_count +=1                                                                      #To calculate no.of students who got the progression outcome as 'Module retreiver' 
        total_outcome[2]=mod_ret_count                                                         #To update the value in the list names as total_outcome
        print()                                                                                #To have a blank line before outputing the promt command
    elif ((defer_credits and pass_credits == 40 or 20) and (80 <= fail_credits <= 120)):       #Condition to get the progression outcome as 'Exclude'
        progression_outcome=progression[3]
        print("progression outcome=",progression[3])                                           #To print the progression outcome
        ex_count +=1                                                                           #To calculate no.of students who got the progression outcome as 'Exc'
        total_outcome[3]=ex_count                                                              #To update the value in the list names as total_outcome
        print()                                                                                #To have a blank line before outputing the promt command
        
        
def histogram(): 
    global outcome
    print('-----------------------------------------------------------------')
    print("Horizontal Histogram")                                             #To print the message Horizontal histogram
    for i in range (len(progression)):                        #To print 4 rows
        print(f'{outcome[i]:10}{total_outcome[i]:1}:',end=' ')#To output progression category and no.of students under this progression category
        y=total_outcome[i]*'*'                                #To calculate how many stars to under this progression category
        print('{}'.format(y),end='\n')                        #To print those stars in same line                      
    print()
    print(outcome_in_total,'outcomes in total')              #To print the no.of students under all progression category
    print('-----------------------------------------------------------------')


def vertical_histogram():                     #User defined function to output a vertical histogram
    print('Vertical histogram')
    for m in range (len(progression)):                      #To print 4 columns[ columns are named progress,trailer,retriever,excluded]
        print(f'{outcome[m]:}{total_outcome[m]:<4}',end='')  #To print a column name and no.of students under that particular progression outcome 
    print() #To start on a new line after finish printing the columns                                  
    rows=max(total_outcome)       #To find which progression outcome has maximum no.of students and assigning it to a variable called rows to print that much of rows
    for n in range (rows):        #To print the output downwards
        for x in range (len(total_outcome)):  #To check the each progression category and print stars in a rows
            if total_outcome[x]>0:            #If a particular progression outcome is not equal to 0 then the codes below it will be executed
                e=1*'*'                       #To print one stars
                print(f"   {e:<10}",end='')     #If the above condition is true it will print one star under that category
                total_outcome[x] -= 1        #To deduct one from the total_outcome[x] to print the no.of stars correctly in each loop   
                #print(end='   ')
            elif total_outcome[x]==0:     #If a particular progression outcome is equal to 0 then the below codes will be excuted
                #print(end='   ')
                print(f"   {0*'*':<10}",end='') 
        print('\n')   #To start a new row
    
     
    
def save_input():               #User defined function to save the inputs and progression outcome
    global pass_inputs
    global defer_inputs
    global fail_inputs
    global input_outcome
    if outcome_in_total > 0:                     #To check the no.of total progression outcome validated if that is greater than 0 then,
        input_outcome.append(progression_outcome) #Append the progression_outcome to the list named input_outcome
        pass_inputs.append(pass_credits)          #Append the pass_credits value to the list named pass_inputs
        defer_inputs.append(defer_credits)        #Append the defer_credits value to the list named defer_inputs          
        fail_inputs.append(fail_credits)          #Append the fail_credits value to the list named fail_inputs

    
def display_input():    #User defined function to display the saved data
    global a
    for x in range (0,len(input_outcome)):         #To check how many rows to print
        a="{} - {},{},{}".format(input_outcome[x],pass_inputs[x],defer_inputs[x],fail_inputs[x])#Used to format the output as "Progress-120,0,0"
        print(a) 


def create_text_file():                   #To create a text file named 'progression_data.txt'
    f=open('progression_data.txt','w')     
    f.close()

def append_in_text_file():              #To write the data inputed
    #create_text_file()
    f=open('progression_data.txt','w')  #Opening the file to appen the saved data
    global a
    for x in range (0,len(input_outcome)):         #To check how many rows to print
        a="{} - {},{},{} \n".format(input_outcome[x],pass_inputs[x],defer_inputs[x],fail_inputs[x])  #Formatting how to write in text file
        f.write(a)        #To write all input data into text file after user exit the program
    f.close()       #To close the text file
    print_text_file()
    
def print_text_file():
    f=open('progression_data.txt','r')     #Reference:Lecture materials
    display_input()
    f.close()
    
def main():
    while True:                               #To run the program several times
        prompt=input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' for quit and view results:")
        while prompt!='q' and prompt!='y':    #To make sure that it takes prompt until user enters 'y'
            print()              #To print a blank line
            prompt=input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' for quit and view results:")
        if prompt=='q':            #To quit the program when user enters 'q'
            print()                #To print a blank line
            histogram()            #Calling the user defined function to print horizontal histogram after user exit the program
            print()                #To print a blank line      
            vertical_histogram()   #Calling the user defined function to execute
            print()
            display_input()
            print()
            append_in_text_file()
            break              #To stop excuting the program after user enters 'q'
        if prompt=='y':         #To make sure that it takes input only if user enters 'y'
            print()             #To print a blank line
            input_credits()     #Calling the user defined funtion input_credits only if user enters 'y' 
            
a=''            
pass_credits=0              #To assign the input taken for no.of credits at pass
defer_credits=0             #To assign the input taken for no.of credits at defer
fail_credits=0              #To assign the input taken for no.of credits at fail
pro_count=0                  #To assign the number of students got progression_outcome as 'Progress'
mod_tra_count=0              #To assign the number of students got progression_outcome as 'Progress(module trailer)' 
mod_ret_count=0              #To assign the number of students got progression_outcome as 'Module retreiver'
ex_count=0                   #To assign the number of students got progression_outcome as 'Exclude '                                       
outcome_in_total=0                                  #To assign the total number of students for all progression outcomes
progression_outcome=''                              #To assign progression outcome
credits_range=[0,20,40,60,80,100,120]               #To check whether input is similar to one of the value in the credits_range list
outcome=['Progress','Trailer','Retriever','Excluded'] #Created to print the progression outcome category for horizontal histogram
progression=['Progress','Progress (module trailer)','Module retriever','Exclude'] #To output progression_outcome from this list
total_outcome=[pro_count,mod_tra_count,mod_ret_count,ex_count] #To store the no.of students in each progression_outcome category
pass_inputs=[]       #To store the pass_credits input values after validating progression_outcome 
defer_inputs=[]      #To store the defer_credits input values after validating progression_outcome
fail_inputs=[]       #To store the fail_credits input values after validating progression_outcome
input_outcome=[]     #To store the progression_outcome after validation
main()               #Calling the function to run the code
