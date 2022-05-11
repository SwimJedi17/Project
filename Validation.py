#============================================================
#This module was written by Jade Coleman (she/they)
#Contact details: 07536393584  z26480@sfc.potteries.ac.uk
#Date:  09/05/2022 Bugs: NONE
#============================================================

# only for validation #

# length checker:
# specific values
# more than certain length
# less than certain length

# character validation


def is_length_valid (data, specific_value, option):
    if option == 1:
        if len(data) == specific_value:
            return True
        else:
            return False
    elif option == 2:
        if len(data) >= specific_value:
            return True
        else:
            return False
    elif option == 3:
        if len(data) <= specific_value:
            return True
        else:
            return False


def is_character_valid(data, different_characters, option):
    pass





try:
  print(f"Yes"+1/0)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
### proceeds to show a message but not an error message and crashing










