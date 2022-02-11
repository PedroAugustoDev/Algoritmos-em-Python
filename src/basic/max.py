# Fuction to get max number in vector
def get_max(number_list):
  var1 = 0
  for i in range(0, len(number_list)):
    if(i == 0):
      var1 = number_list[i]
    else:
      if(number_list[i] >= var1):
        var1 = number_list[i]
  return var1


number_list = [100, 200, 800, 400, 500, 600]


print(f"The max value in list is: {get_max(number_list)}")