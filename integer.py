import streamlit as st
import datetime

# Function to get the date as day-month-year
def get_date_day_month_year():
    day = st.number_input("Введите день:", min_value=1, max_value=31)
    month = st.number_input("Введите месяц:", min_value=1, max_value=12)
    year = st.number_input("Введите год:")
    return day, month, year

# Function to get the date as day (~365)-year
def get_date_day_year():
    day = st.number_input("Введите число K (от 1 до 365):", min_value=1, max_value=365)
    year = st.number_input("Введите год:")
    return day, year

# Streamlit app
st.title("Определение номера дня недели")
st.write("Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, ..., 6 — суббота, 7 — воскресенье.")

# Get user input for the date format
option = st.selectbox("Выберите формат ввода даты:", ["День-месяц-год", "День (~365)-год"])

# Check the chosen option and get the date accordingly
if option == "День-месяц-год":
    day, month, year = get_date_day_month_year()
elif option == "День (~365)-год":
    day, year = get_date_day_year()

# Check if the year is a leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Calculate the maximum number of days in the year
max_days = 366 if is_leap_year else 365

# Check if the entered day is within the valid range
if day < 1 or day > max_days:
    st.error("Некорректное значение дня!")
else:
    # Calculate the date for the entered day and year
    date = datetime.date(year, 1, 1) + datetime.timedelta(days=day-1)

    # Get the day of the week for the calculated date
    day_of_week = date.strftime("%A")

    # Translate the day of the week to Russian
    days_of_week_russian = {
        "Monday": "понедельник",
        "Tuesday": "вторник",
        "Wednesday": "среда",
        "Thursday": "четверг",
        "Friday": "пятница",
        "Saturday": "суббота",
        "Sunday": "воскресенье"
    }

    day_of_week_russian = days_of_week_russian[day_of_week]

    # Print the result
    st.success(f"Номер дня недели для {day}-го дня года в {year} году: {day_of_week_russian}")
