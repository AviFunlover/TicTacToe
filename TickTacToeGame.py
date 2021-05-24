#!/usr/bin/env python
# coding: utf-8

# In[1]:


def show_grid(grid_list):
#passes a grid into show_grid function and displays the grid in a 3X3 form

    one=f"{grid_list[0]}"
    two=f"{grid_list[1]}"
    three=f"{grid_list[2]}"
    four=f"{grid_list[3]} "
    five=f"{grid_list[4]}"
    six=f"{grid_list[5]}"
    seven=f"{grid_list[6]}"
    eight=f"{grid_list[7]}"
    nine=f"{grid_list[8]}"
    
    print("The current grid is as follows")
    
    
#replcing each grid space value with the currespondinng value in grid_list
    print("       |       |       ")
    print(f"   {seven}   |   {eight}   |   {nine}  ")
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print(f"   {four}  |   {five}   |   {six}  ")
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print(f"   {one}   |   {two}   |   {three}  ")
    print("       |       |       ")


# In[15]:


def take_user_input_and_update(grid_list,player):
#gets value given by user for a grid space and checks if the value is available in grid
    check=False
    
    while check!=True:
        #will continue untill user gives a valid reference number for grid
        value=input("Give the reference number of the grid you want to replace:")
        
        if value.isdigit()==True:
            value=int(value)
        
            if value in range(1,10):

                if grid_list[value-1]==" ":
                    #will check if the space in the grid is empty or not
                    #if empty then will fill the grid value with player sign
                    grid_list[value-1]=player
                    check=True
                    return grid_list

                else:
                    print("The space is allready occupied")
                    check=False

            else:
                print("Wrong user input. Give between 1-9")
                check=False
                
        else:
            print("Invalid Input Give a proper reference number from 1-9")
            check=False


# In[16]:


def ask_sign_p1():
#asks player1 for the sign user wants to opt 
    check=False
    #for while loop
   
    while check!=True:
        #will repeat untill gives a valid sign
        p1_sign=input("Player1 which sign do you want to choose: ")
        
        if p1_sign=="x" or p1_sign=="X" or p1_sign=="1":
            p1_sign="X"
            check=True
        elif p1_sign=="o" or p1_sign=="O" or p1_sign=="0":
            p1_sign="O"
            check=True
        else:
            print("Wrong input given. Give your input in x,o or X,O or 1,0")
            check=False
    return p1_sign 


# In[17]:


def give_sign_p2(p1_sign):
    #assigns player2's sign opposite to player1's choice
    if p1_sign=="X":
        p2_sign="O"
    else:
        p2_sign="X"
    return p2_sign


# In[18]:


def intro():
    #intro for the players to understand the game and the how to play basics
    print("       |       |       ")
    print("   7   |   8   |   9                        This the Grid pattern we will be following for refernce you can use")
    print("       |       |                             The numpad pattern in your keyboard.")
    print("-----------------------")
    print("       |       |       ")
    print("   4   |   5   |   6                        This is a simple game of tick tac toe the player1 will be choosing the")
    print("       |       |                            The sign he/she wants to opt between X/O")
    print("-----------------------")
    print("       |       |                             When giving can choose between \"o\" \"O\" \"0\" or \"X\" \"x\" \"1\" ")
    print("   1   |   2   |   3                         The program will assign it to \"X\" or \"O\" accordingly")
    print("       |       |       ")         


# In[19]:


def show_user_sign(p1_sign,p2_sign):
    #shows users their choosen signs
    print(f"The Player 1 has been alloted \"{p1_sign}\".")
    print(f"The Player 2 has been alloted \"{p2_sign}\".")


# In[20]:


def user_game_quit():
    #asks user if he/she wants to quit the game or not
    
    c=False
    while c!=True:
        
        check=input("Do you want to continue playing? Give answer in Yes/No: ")
        
        if check=="y" or check=="Y" or check=="Yes" or check=="yes":
            c=True
            return True
        elif check=="n" or check=="N" or check=="No" or check=="no":
            c=True
            return False
        else:
            print("Invalid input please reply in yes/no")
            c=False


# In[21]:


def win(grid_list,player):
    #every possible win situation
    if grid_list[0]==grid_list[1]==grid_list[2]==player or grid_list[3]==grid_list[4]==grid_list[5]==player or grid_list[6]==grid_list[7]==grid_list[8]==player or grid_list[6]==grid_list[3]==grid_list[0]==player or grid_list[7]==grid_list[4]==grid_list[1]==player or grid_list[8]==grid_list[5]==grid_list[2]==player or grid_list[0]==grid_list[4]==grid_list[8]==player or grid_list[6]==grid_list[4]==grid_list[2]==player:
        return True
    else:
        return False
        


# In[22]:


intro()
#intro to my program

p1=ask_sign_p1()
#assigns sign X/O to player1 and player2 as wished
p2=give_sign_p2(p1)

grid_list=[" "," "," "," "," "," "," "," "," "]
#initialisation of empty grid

show_user_sign(p1,p2)
#shows users their chosen sign

w=False
#to continue the loop untill someone wins

p=False
#to know player1 won

q=False
#to know player2 won

i=0
#counter to give both the players alternate chances

while w!=True:
    if p==True:
        #when player 1 wins
        print("Congratulations Player 1 You have Won the Round.")
        w=True
        break
    
    elif q==True:
        #when player 2 wins
        print("Congratulations Player 2 You have Won the Round.")
        w=True
        break
    
    
        
    y=user_game_quit()
    #If player wants to continue playing
    if y==True:
        #if player wants to play
        
        
        if i==9:
            #will happen when all the boxes are filled
            #and print no specific winner
            #uses the counter to know when it happens
            print("The Round is tied between both players.")
            print("No-one Won The Round")
            break
        
        
        elif i%2==0:
            #when player1's chance
            print(f"Player 1 give your \'{p1}\'.")
            
            grid_list=take_user_input_and_update(grid_list,p1)
            #updates grid with choice
            
            p=win(grid_list,p1)
            #checks if player1 won
            
            i+=1
            #increment to go to player2
            
            print("\n"*100)
            
            show_grid(grid_list)
            #display grid

        elif i%2!=0:
            #when player2's chance
            print(f"Player 2 give your \'{p2}\'.")
            
            grid_list=take_user_input_and_update(grid_list,p2)
            #updates grid with choice
            
            q=win(grid_list,p2)
            #checks if player2 won
            
            i+=1
            #increment to go to player1
            
            print("\n"*100)
            
            show_grid(grid_list)
            #display grid
            
            
        
        
                    
    elif y==False:
        #if player doesn't wish to play anymore
        print("Game Over, Player quit the game.")
        break
        
        
print("Thank you for playing hope you liked the game. Restart the game when you wish to play again.")
        


# In[ ]:





# In[ ]:




