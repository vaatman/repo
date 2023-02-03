#!/usr/bin/python3

import requests

nums = [ 1, 2, 3, 4, 5 ]

def my_func(nums):
  my_result = []
  for N in nums:
    api_url = "https://jsonplaceholder.typicode.com/todos/" + str(N)
    response = requests.get(api_url)
    my_result.append(response.json())
  return my_result

print(my_func(nums))
