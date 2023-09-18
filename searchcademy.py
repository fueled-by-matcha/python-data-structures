def sparse_search(data, search_val):
  first = 0
  last = len(data) - 1 
  while first < last:
    mid = (first + last) // 2
    if mid == None:
      left = mid - 1
      right = mid + 1
      if search_val < data[mid]:
        last = mid - 1
      if search_val > data[mid]:
        first = mid + 1
      while True:
        if left < first and right > last:
          print(f'{search_val} is not in the data set')
          return None
        elif right <= last and data[right] != None:
          mid = right
          break
        elif left >= first and data[left] != None:
          mid = left
          break
        right += 1
        left -= 1
      if data[mid] == search_val:
        print(f'{search_val} found at position {mid}')
        return
      print(f'{search_val} is not in the dataset')

print("Data: " + str(data))
print("Search Value: " + str(search_val))
