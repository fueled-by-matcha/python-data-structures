def linear_search(search_list, target_value):
  matches = []
  for item in range(len(search_list)):
    print(search_list[item])
    if search_list[item] == target_value:
      matches.append(item)
  if matches != None:
    return matches
  else:
    raise ValueError(f'{target_value} not in list')

def linear_search_max (search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    print(search_list[idx])
    if maximum_score_index == None or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

values = [54, 22, 46, 99]
print(linear_search(values, 22))
