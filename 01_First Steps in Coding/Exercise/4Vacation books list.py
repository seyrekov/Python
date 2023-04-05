book_pages = int(input())
pages_for_hour = int(input())
days_for_one_book = int(input())
time_for_reading_a_book = book_pages / pages_for_hour
hours_reading_per_day = time_for_reading_a_book / days_for_one_book
rounded_hours_per_day = round(hours_reading_per_day)
print(rounded_hours_per_day)
