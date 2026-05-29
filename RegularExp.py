
import re

result = re.search("[0-9]*th", "a35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "a35th")
# print(result)
# print(result.group())



result = re.search("\d{4}", "This year is 2024.")
print(result.group())

result = re.search("\d{5}", "The postal code of New York is 10001.")
print(result.group())