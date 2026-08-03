name=input("Enter your name ")
gadget=input("Enter your favorite gadget ")
agtnum=5834
spdrat=9.8
mission_count=7
height=5.9
active_status=True
print("Name:",name,"type:",type(name)) 
print("Gadget:",gadget,"type:",type(gadget))
print("Speed_Rating:",spdrat,"type:",type(spdrat))
print("Active_status:",active_status,"type:",type(active_status))
mission_count_txt=str(mission_count)
agtnum_txt=str(agtnum)
active_status_txt=str(active_status)
first_three=name[0:3]
last_letter=name[-1:]
code_name=first_three + last_letter
print("First 3 letter of name:", first_three)
print("Last Letter of name:", last_letter)
print("Secret Code Name:" ,code_name)

reversed_gadget=gadget[::-1]
print("Resversed Gadget Name:", reversed_gadget)

badge_line_1="AGENT"+code_name.upper()
badge_line_2="ID"+agtnum_txt + "MISSION:"+ mission_count_txt
badge_line_3="ACTIVE_STATUS" +active_status_txt

print(badge_line_1)
print(badge_line_2)
print(badge_line_3)



