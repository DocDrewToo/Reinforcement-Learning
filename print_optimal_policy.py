from tkinter import *

#setting up table output of optimal policy
def print_table(q_value_table):
        
    optimal_policy =Tk()
    optimal_policy.title('Optimal Policy')

    #finding 'max' value at each location
    optimal_policy_B2 = max(q_value_table["B2"]["NORTH"], q_value_table["B2"]["SOUTH"], q_value_table["B2"]["EAST"], q_value_table["B2"]["WEST"])
    optimal_policy_B3 = max(q_value_table["B3"]["NORTH"], q_value_table["B3"]["SOUTH"], q_value_table["B3"]["EAST"], q_value_table["B3"]["WEST"])
    optimal_policy_B4 = max(q_value_table["B4"]["NORTH"], q_value_table["B4"]["SOUTH"], q_value_table["B4"]["EAST"], q_value_table["B4"]["WEST"])
    optimal_policy_B5 = max(q_value_table["B5"]["NORTH"], q_value_table["B5"]["SOUTH"], q_value_table["B5"]["EAST"], q_value_table["B5"]["WEST"])
    optimal_policy_C3 = max(q_value_table["C3"]["NORTH"], q_value_table["C3"]["SOUTH"], q_value_table["C3"]["EAST"], q_value_table["C3"]["WEST"])
    optimal_policy_C4 = max(q_value_table["C4"]["NORTH"], q_value_table["C4"]["SOUTH"], q_value_table["C4"]["EAST"], q_value_table["C4"]["WEST"])
    optimal_policy_C6 = max(q_value_table["C6"]["NORTH"], q_value_table["C6"]["SOUTH"], q_value_table["C6"]["EAST"], q_value_table["C6"]["WEST"])
    optimal_policy_D3 = max(q_value_table["D3"]["NORTH"], q_value_table["D3"]["SOUTH"], q_value_table["D3"]["EAST"], q_value_table["D3"]["WEST"])
    optimal_policy_D6 = max(q_value_table["D6"]["NORTH"], q_value_table["D6"]["SOUTH"], q_value_table["D6"]["EAST"], q_value_table["D6"]["WEST"])
    optimal_policy_E2 = max(q_value_table["E2"]["NORTH"], q_value_table["E2"]["SOUTH"], q_value_table["E2"]["EAST"], q_value_table["E2"]["WEST"])
    optimal_policy_E3 = max(q_value_table["E3"]["NORTH"], q_value_table["E3"]["SOUTH"], q_value_table["E3"]["EAST"], q_value_table["E3"]["WEST"])
    optimal_policy_E4 = max(q_value_table["E4"]["NORTH"], q_value_table["E4"]["SOUTH"], q_value_table["E4"]["EAST"], q_value_table["E4"]["WEST"])
    optimal_policy_E5 = max(q_value_table["E5"]["NORTH"], q_value_table["E5"]["SOUTH"], q_value_table["E5"]["EAST"], q_value_table["E5"]["WEST"])
    optimal_policy_E6 = max(q_value_table["E6"]["NORTH"], q_value_table["E6"]["SOUTH"], q_value_table["E6"]["EAST"], q_value_table["E6"]["WEST"])

    #printing out the direction arrows based on the 'max' value
    if q_value_table["B2"]["NORTH"] == optimal_policy_B2:
        optimal_policy_B2_direction = "^^^^"
    elif q_value_table["B2"]["SOUTH"] == optimal_policy_B2:
        optimal_policy_B2_direction = "vvvv"
    elif q_value_table["B2"]["WEST"] == optimal_policy_B2:
        optimal_policy_B2_direction = "<<<<"
    else:
        optimal_policy_B2_direction = ">>>>"

    if q_value_table["B3"]["NORTH"] == optimal_policy_B3:
        optimal_policy_B3_direction = "^^^^"
    elif q_value_table["B3"]["SOUTH"] == optimal_policy_B3:
        optimal_policy_B3_direction = "vvvv"
    elif q_value_table["B3"]["WEST"] == optimal_policy_B3:
        optimal_policy_B3_direction = "<<<<"
    else:
        optimal_policy_B3_direction = ">>>>"

    if q_value_table["B4"]["NORTH"] == optimal_policy_B4:
        optimal_policy_B4_direction = "^^^^"
    elif q_value_table["B4"]["SOUTH"] == optimal_policy_B4:
        optimal_policy_B4_direction = "vvvv"
    elif q_value_table["B4"]["WEST"] == optimal_policy_B4:
        optimal_policy_B4_direction = "<<<<"
    else:
        optimal_policy_B4_direction = ">>>>"

    if q_value_table["B5"]["NORTH"] == optimal_policy_B5:
        optimal_policy_B5_direction = "^^^^"
    elif q_value_table["B5"]["SOUTH"] == optimal_policy_B5:
        optimal_policy_B5_direction = "vvvv"
    elif q_value_table["B5"]["WEST"] == optimal_policy_B5:
        optimal_policy_B5_direction = "<<<<"
    else:
        optimal_policy_B5_direction = ">>>>"

    if q_value_table["C3"]["NORTH"] == optimal_policy_C3:
        optimal_policy_C3_direction = "^^^^"
    elif q_value_table["C3"]["SOUTH"] == optimal_policy_C3:
        optimal_policy_C3_direction = "vvvv"
    elif q_value_table["C3"]["WEST"] == optimal_policy_C3:
        optimal_policy_C3_direction = "<<<<"
    else:
        optimal_policy_C3_direction = ">>>>"

    if q_value_table["C4"]["NORTH"] == optimal_policy_C4:
        optimal_policy_C4_direction = "^^^^"
    elif q_value_table["C4"]["SOUTH"] == optimal_policy_C4:
        optimal_policy_C4_direction = "vvvv"
    elif q_value_table["C4"]["WEST"] == optimal_policy_C4:
        optimal_policy_C4_direction = "<<<<"
    else:
        optimal_policy_C4_direction = ">>>>"

    if q_value_table["C6"]["NORTH"] == optimal_policy_C6:
        optimal_policy_C6_direction = "^^^^"
    elif q_value_table["C6"]["SOUTH"] == optimal_policy_C6:
        optimal_policy_C6_direction = "vvvv"
    elif q_value_table["C6"]["WEST"] == optimal_policy_C6:
        optimal_policy_C6_direction = "<<<<"
    else:
        optimal_policy_C6_direction = ">>>>"



    if q_value_table["D3"]["NORTH"] == optimal_policy_D3:
        optimal_policy_D3_direction = "^^^^"
    elif q_value_table["D3"]["SOUTH"] == optimal_policy_D3:
        optimal_policy_D3_direction = "vvvv"
    elif q_value_table["D3"]["WEST"] == optimal_policy_D3:
        optimal_policy_D3_direction = "<<<<"
    else:
        optimal_policy_D3_direction = ">>>>"

    if q_value_table["D6"]["NORTH"] == optimal_policy_D6:
        optimal_policy_D6_direction = "^^^^"
    elif q_value_table["D6"]["SOUTH"] == optimal_policy_D6:
        optimal_policy_D6_direction = "vvvv"
    elif q_value_table["D6"]["WEST"] == optimal_policy_D6:
        optimal_policy_D6_direction = "<<<<"
    else:
        optimal_policy_D6_direction = ">>>>"
        

    if q_value_table["E2"]["NORTH"] == optimal_policy_E2:
        optimal_policy_E2_direction = "^^^^"
    elif q_value_table["E2"]["SOUTH"] == optimal_policy_E2:
        optimal_policy_E2_direction = "vvvv"
    elif q_value_table["E2"]["WEST"] == optimal_policy_E2:
        optimal_policy_E2_direction = "<<<<"
    else:
        optimal_policy_E2_direction = ">>>>"
        
    if q_value_table["E3"]["NORTH"] == optimal_policy_E3:
        optimal_policy_E3_direction = "^^^^"
    elif q_value_table["E3"]["SOUTH"] == optimal_policy_E3:
        optimal_policy_E3_direction = "vvvv"
    elif q_value_table["E3"]["WEST"] == optimal_policy_E3:
        optimal_policy_E3_direction = "<<<<"
    else:
        optimal_policy_E3_direction = ">>>>"
        
    if q_value_table["E4"]["NORTH"] == optimal_policy_E4:
        optimal_policy_E4_direction = "^^^^"
    elif q_value_table["E4"]["SOUTH"] == optimal_policy_E4:
        optimal_policy_E4_direction = "vvvv"
    elif q_value_table["E4"]["WEST"] == optimal_policy_E4:
        optimal_policy_E4_direction = "<<<<"
    else:
        optimal_policy_E4_direction = ">>>>"
        
    if q_value_table["E5"]["NORTH"] == optimal_policy_E5:
        optimal_policy_E5_direction = "^^^^"
    elif q_value_table["E5"]["SOUTH"] == optimal_policy_E5:
        optimal_policy_E5_direction = "vvvv"
    elif q_value_table["E5"]["WEST"] == optimal_policy_E5:
        optimal_policy_E5_direction = "<<<<"
    else:
        optimal_policy_E5_direction = ">>>>"
        
    if q_value_table["E6"]["NORTH"] == optimal_policy_E6:
        optimal_policy_E6_direction = "^^^^"
    elif q_value_table["E6"]["SOUTH"] == optimal_policy_E6:
        optimal_policy_E6_direction = "vvvv"
    elif q_value_table["E6"]["WEST"] == optimal_policy_E6:
        optimal_policy_E6_direction = "<<<<"
    else:
        optimal_policy_E6_direction = ">>>>"
    
    #setting up printing the output of the optimal policy
    Optimal_policy_value_A1 = Label(optimal_policy, text=q_value_table["A1"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_A2 = Label(optimal_policy, text=q_value_table["A2"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_A3 = Label(optimal_policy, text=q_value_table["A3"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_A4 = Label(optimal_policy, text=q_value_table["A4"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_A5 = Label(optimal_policy, text=q_value_table["A5"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_A6 = Label(optimal_policy, text=q_value_table["A6"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_A7 = Label(optimal_policy, text=q_value_table["A7"]["NORTH"], padx=10, pady=10)

    Optimal_policy_value_B1 = Label(optimal_policy, text=q_value_table["B1"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_B2 = Label(optimal_policy, text=optimal_policy_B2_direction, padx=10, pady=10)
    Optimal_policy_value_B3 = Label(optimal_policy, text=optimal_policy_B3_direction, padx=10, pady=10)
    Optimal_policy_value_B4 = Label(optimal_policy, text=optimal_policy_B4_direction, padx=10, pady=10)
    Optimal_policy_value_B5 = Label(optimal_policy, text=optimal_policy_B5_direction, padx=10, pady=10)
    Optimal_policy_value_B6 = Label(optimal_policy, text="WALL", padx=10, pady=10)
    Optimal_policy_value_B7 = Label(optimal_policy, text=q_value_table["B7"]["NORTH"], padx=10, pady=10)

    Optimal_policy_value_C1 = Label(optimal_policy, text=q_value_table["C1"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_C2 = Label(optimal_policy, text="WALL", padx=10, pady=10)
    Optimal_policy_value_C3 = Label(optimal_policy, text=optimal_policy_C3_direction, padx=10, pady=10)
    Optimal_policy_value_C4 = Label(optimal_policy, text=optimal_policy_C4_direction, padx=10, pady=10)
    Optimal_policy_value_C5 = Label(optimal_policy, text="WALL", padx=10, pady=10)
    Optimal_policy_value_C6 = Label(optimal_policy, text=optimal_policy_C6_direction, padx=10, pady=10)
    Optimal_policy_value_C7 = Label(optimal_policy, text=q_value_table["C7"]["NORTH"], padx=10, pady=10)

    Optimal_policy_value_D1 = Label(optimal_policy, text=q_value_table["D1"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_D2 = Label(optimal_policy, text="WALL", padx=10, pady=10)
    Optimal_policy_value_D3 = Label(optimal_policy, text=optimal_policy_D3_direction, padx=10, pady=10)
    Optimal_policy_value_D4 = Label(optimal_policy, text=q_value_table["D4"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_D5 = Label(optimal_policy, text="WALL", padx=10, pady=10)
    Optimal_policy_value_D6 = Label(optimal_policy, text=optimal_policy_C6_direction, padx=10, pady=10)
    Optimal_policy_value_D7 = Label(optimal_policy, text=q_value_table["D7"]["NORTH"], padx=10, pady=10)

    Optimal_policy_value_E1 = Label(optimal_policy, text=q_value_table["E1"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_E2 = Label(optimal_policy, text=optimal_policy_E2_direction, padx=10, pady=10)
    Optimal_policy_value_E3 = Label(optimal_policy, text=optimal_policy_E3_direction, padx=10, pady=10)
    Optimal_policy_value_E4 = Label(optimal_policy, text=optimal_policy_E4_direction, padx=10, pady=10)
    Optimal_policy_value_E5 = Label(optimal_policy, text=optimal_policy_E5_direction, padx=10, pady=10)
    Optimal_policy_value_E6 = Label(optimal_policy, text=optimal_policy_E6_direction, padx=10, pady=10)
    Optimal_policy_value_E7 = Label(optimal_policy, text=q_value_table["E7"]["NORTH"], padx=10, pady=10)

    Optimal_policy_value_F1 = Label(optimal_policy, text=q_value_table["F1"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_F2 = Label(optimal_policy, text=q_value_table["F2"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_F3 = Label(optimal_policy, text=q_value_table["F3"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_F4 = Label(optimal_policy, text=q_value_table["F4"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_F5 = Label(optimal_policy, text=q_value_table["F5"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_F6 = Label(optimal_policy, text=q_value_table["F6"]["NORTH"], padx=10, pady=10)
    Optimal_policy_value_F7 = Label(optimal_policy, text=q_value_table["F7"]["NORTH"], padx=10, pady=10)

    #Assigning grid locations for optimal policy
    Optimal_policy_value_A1.grid(row=1, column=2)
    Optimal_policy_value_A2.grid(row=1, column=5)
    Optimal_policy_value_A3.grid(row=1, column=8)
    Optimal_policy_value_A4.grid(row=1, column=11)
    Optimal_policy_value_A5.grid(row=1, column=14)
    Optimal_policy_value_A6.grid(row=1, column=17)
    Optimal_policy_value_A7.grid(row=1, column=20)

    Optimal_policy_value_B1.grid(row=4, column=2)
    Optimal_policy_value_B2.grid(row=4, column=5)
    Optimal_policy_value_B3.grid(row=4, column=8)
    Optimal_policy_value_B4.grid(row=4, column=11)
    Optimal_policy_value_B5.grid(row=4, column=14)
    Optimal_policy_value_B6.grid(row=4, column=17)
    Optimal_policy_value_B7.grid(row=4, column=20)

    Optimal_policy_value_C1.grid(row=7, column=2)
    Optimal_policy_value_C2.grid(row=7, column=5)
    Optimal_policy_value_C3.grid(row=7, column=8)
    Optimal_policy_value_C4.grid(row=7, column=11)
    Optimal_policy_value_C5.grid(row=7, column=14)
    Optimal_policy_value_C6.grid(row=7, column=17)
    Optimal_policy_value_C7.grid(row=7, column=20)

    Optimal_policy_value_D1.grid(row=10, column=2)
    Optimal_policy_value_D2.grid(row=10, column=5)
    Optimal_policy_value_D3.grid(row=10, column=8)
    Optimal_policy_value_D4.grid(row=10, column=11)
    Optimal_policy_value_D5.grid(row=10, column=14)
    Optimal_policy_value_D6.grid(row=10, column=17)
    Optimal_policy_value_D7.grid(row=10, column=20)

    Optimal_policy_value_E1.grid(row=13, column=2)
    Optimal_policy_value_E2.grid(row=13, column=5)
    Optimal_policy_value_E3.grid(row=13, column=8)
    Optimal_policy_value_E4.grid(row=13, column=11)
    Optimal_policy_value_E5.grid(row=13, column=14)
    Optimal_policy_value_E6.grid(row=13, column=17)
    Optimal_policy_value_E7.grid(row=13, column=20)

    Optimal_policy_value_F1.grid(row=16, column=2)
    Optimal_policy_value_F2.grid(row=16, column=5)
    Optimal_policy_value_F3.grid(row=16, column=8)
    Optimal_policy_value_F4.grid(row=16, column=11)
    Optimal_policy_value_F5.grid(row=16, column=14)
    Optimal_policy_value_F6.grid(row=16, column=17)
    Optimal_policy_value_F7.grid(row=16, column=20)
    # return optimal_policy
    optimal_policy.mainloop()
