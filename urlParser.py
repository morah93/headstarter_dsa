from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
# response = requests.get(url)

# if response.status_code == 200:
#     # The request was successful
#   content = response.text
#     # print(content)
# else:
#     # The request was unsuccessful
#   print(f"Failed to fetch data. Status code: {response.status_code}")

# html_content = response.content
# soup = BeautifulSoup(html_content, 'html.parser')

# table = soup.find('table')
# data = []
# for row in table.find_all('tr'):
#   cols = [col.text for col in row.find_all('td')]
#   data.append(cols)
# print(cols)

# df = pd.DataFrame(data)
  # print(data)

# def create_character_grid(url):


#   # Parse the data and create the grid
#   max_x = -1  # Initialize to -1 to ensure it gets updated correctly
#   # max_x = max(int(row[1]) for row in data[1:])
#   max_y = max(int(row[2]) for row in data[1:])
#   grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

#   print(max_x)
#   print(max_y)

#   for row in data[1:]:
#         try:
#             char, x, y = row
#             max_x = max(max_x, int(x))  # Update max_x only if conversion is successful
#             grid[int(y)][int(x)] = chr(int(char, 16))
#         except ValueError:
#             pass  # Ignore errors and continue processing other rows


#   print(grid)

#   return grid

def create_character_grid(url):

  url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
  response = requests.get(url)

  if response.status_code == 200:
    # The request was successful
    content = response.text
    # print(content)
  else:
    # The request was unsuccessful
    print(f"Failed to fetch data. Status code: {response.status_code}")

  html_content = response.content
  soup = BeautifulSoup(html_content, 'html.parser')

  table = soup.find('table')
  data = []
  for row in table.find_all('tr'):
    cols = [col.text for col in row.find_all('td')]
    data.append(cols)
  print(cols)

  df = pd.DataFrame(data)

  max_x = max(x for _, x, _ in data)
  max_y = max(y for _, _, y in data)

  grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

  for char, x, y in data:
      grid[y][x] = char

  print(grid)
  return grid

def print_grid(grid):
  """
    Prints the character grid in a visually appealing format.

    Args:
        grid (list): The 2D list representing the character grid.
  """

  for row in grid:
    print(''.join(row))

  if __name__ == "__main__":
    # url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
    grid = create_character_grid(url)
    print_grid(grid)

# print(create_character_grid('https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'))
#



  # for i in range (len(scores) - 2):
  #   if scores[i+2]-scores[i] <= 2 and scores[i+2]-scores[i+1]<=2:
  #     return True

  # return False
