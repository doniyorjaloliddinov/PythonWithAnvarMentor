import datetime as dt
import re
# # Get the current date
today = dt.date.today()

# # Calculate the date two weeks from now
# two_weeks_from_today = today + dt.timedelta(days=14)

# # Print out the dates for the next 10 weeks
# for i in range(10):
#     print(two_weeks_from_today)
#     two_weeks_from_today += dt.timedelta(days=7)


# b_date = dt.date(2003,1,9)
# days_lived = today - b_date
# month_lived = days_lived/365
# hours_lived = days_lived*24
# print(f"{today.year - b_date.year} years i have lived. {month_lived} monthes i have lived!\n{days_lived} i have lived")
# print(hours_lived)


# b_date = dt.date(2003, 1, 9)
# # Calculate the difference between the two dates
# diff = today - b_date
# # Calculate the number of days
# days_lived = diff.days
# # Calculate the number of years
# years_lived = today.year - b_date.year
# # Calculate the number of months
# months_lived = diff.days // 30
# # Calculate the number of hours
# hours_lived = diff.days * 24

# print(f"{years_lived} years i have lived. {months_lived} months i have lived!")
# print(f"{days_lived} days i have lived. {hours_lived} hours i have lived.")


# phone_template = "^\+9989\d{8}$"
# my_number = "+998901234567"

# match = re.match(phone_template, my_number)

# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

# import re

# url_template = r"(http|https):\/\/(\w+\.)?[\w@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}(\/[\w()!@:%_\+.~#?&\/\/=]*)?"
# url = "https://python.sariq.dev/testing/37-klass-test"

# matched = re.match(url_template, url)

# if matched:
#     print("Match found!")
# else:
#     print("Match not found.")


import re
import webbrowser

def extract_urls(text):
    url_pattern = r"(http|https):\/\/(\w+\.)?[\w@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}(\/[\w()!@:%_\+.~#?&\/\/=]*)?"
    urls = [match[0].encode('utf-8') for match in re.findall(url_pattern, text)]
    return urls

text = "Here is some text with URLs: https://www.youtube.com, https://www.google.com"
urls = extract_urls(text)

for url in urls:
    webbrowser.open(url.decode('utf-8')+"://www.youtube.com")