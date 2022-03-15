# function to find media
def get_media(array):
  arr_len = len(array)
  media = 0
  for i in range(arr_len):
    media += array[i]
  return media / arr_len


print(f'A média das notas de pedro é: {get_media([10, 5, 5, 10])}')