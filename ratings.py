"""Restaurant rating lister."""


# put your code here
import random
import os 
def choose_list():  
  # scores = open('./lists/scores.txt','r')
  print("Choosing files\n")
  print("lists available "+str(os.listdir("./lists")))
  choice=input("which filename would you like?\n")
  scores = open(("./lists/"+choice),'r')

  new_dict={}
  scores_dict={}

  #parse in data
  for line in scores:
    key, value = line.rstrip('\n').split(":")
    scores_dict[key]=value

  #initial sort data
 
  sorted_dict=sorted(scores_dict.items())
  for item in sorted_dict:
    key, value=item
    new_dict[key]=value
  return new_dict

# print the info
def print_info(new_dict):
  for printed in new_dict:
    print(printed+" is rated at "+new_dict[printed])

# sort it again
def sort_again(new_dict):
  #resort data
  added_dict={}
  added_arr=sorted(new_dict.items())
  for each in added_arr:
    added_dict[each[0]]=each[1]

  #print new list
  for thelist in added_dict:
    print(thelist+" is rated at "+new_dict[thelist])

# add new entry
def new_entry(new_dict):
    
  #add new place name
  def new_place():
    print('Add a new Restaurant')
    rest_name=input('what is the name of the restaurant?\n')
    return rest_name

  #restraunt rating
  def rating():
    rate_input=int(input('What rating 1 to 5 would you give this restaurant?\n'))
    if (rate_input>5) or (rate_input<1):
      print('please keep your ratings between 1 and 5')
      return rating()
    else: return str(rate_input)
  place=new_place()
  new_dict[place]=rating()
# end of entry function

#update entry
def update_entry(new_dict):
  entry_to_update=input('What is the name of the restaurant you want to update?\n')
  entry_rating=input('What rating should it be?\n')
  new_dict[entry_to_update]=entry_rating

#update random
def random_edit(new_dict):
  make_list=list(new_dict.items())
  random_item=random.choice(make_list)
  new_item=input("what should the new rating be?\n")
  new_dict[random_item[0]]=new_item
  print('the random rating changed was '+random_item[0]+", "+random_item[1]+" changed to "+new_item)

# Menu options
def menu():
  new_dict=choose_list()
  menu_choice=int(input('MENU:\nEnter an option number:\n1.See all ratings\n2.Add a new restaurant and rating\n3.Update a rating\n4.Update a random review\n5.Choose what lists to examine\n6.Quit\n'))
  if menu_choice==1:
    sort_again(new_dict)
    return menu()
  elif menu_choice==2:
    new_entry(new_dict)
    sort_again(new_dict)
    return menu()
  elif menu_choice==3:
    update_entry(new_dict)
    sort_again(new_dict)
    return menu()
  elif menu_choice==4:
    random_edit(new_dict)
    sort_again(new_dict)
    return menu()
  elif menu_choice==5:
    choose_list()
    return menu()
  elif menu_choice==6:
    exit()
  else:
    print('sorry only numbers 1 to 6 available at this time')
    return menu()
menu()