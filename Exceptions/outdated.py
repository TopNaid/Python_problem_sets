from datetime import datetime

while True:
    date = input('Date: ').strip()
    try:
        parsed_date = datetime.strptime(date, "%m/%d/%Y")
        break
    except ValueError:
        try:
           parsed_date = datetime.strptime(date, "%B %d, %Y")
           break
        except ValueError:
            pass
formatted_date = parsed_date.strftime("%Y-%m-%d")
print(formatted_date)
   