import gspread
# from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

def create_character_grid(doc_url):
  """
  Creates a character grid from a Google Sheet containing Unicode characters and their positions.

  Args:
    doc_url: The URL of the Google Sheet.

  Returns:
    A list of lists representing the character grid.
  """

  # Authenticate with Google Sheets API
  # scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
  # creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/mahbub/Downloads/decodemessage-6829166182a1.json', scope)
  # client = gspread.authorize(creds)

  scope = ['https://www.googleapis.com/auth/docs.readonly']
  creds = Credentials.from_service_account_file('/Users/mahbub/Downloads/decodemessage-6829166182a1.json', scopes=scope)
  client = gspread.authorize(creds)

  # Open the Google Sheet and get the data
  sheet = client.open_by_url(doc_url)
  data = sheet.get_all_values()

  # Parse the data and create the grid
  max_x = max(int(row[1]) for row in data[1:])
  max_y = max(int(row[2]) for row in data[1:])
  grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

  for row in data[1:]:
    char, x, y = row
    grid[int(y)][int(x)] = chr(int(char, 16))

  return grid

# Example usage
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
grid = create_character_grid(doc_url)

# Print the grid
for row in grid:
  print(''.join(row))
