import datetime
import requests
import os
from urllib.parse import quote
from zoneinfo import ZoneInfo

# WhatsApp credentials from environment variables
PHONE = os.getenv("PHONE")
APIKEY = os.getenv("APIKEY")

# Get daily message content
def get_message():
    now = datetime.datetime.now(ZoneInfo("Asia/Dhaka"))

    is_leap = now.year % 4 == 0 and (now.year % 100 != 0 or now.year % 400 == 0)
    total_days_in_year = 366 if is_leap else 365
    day_of_year = now.timetuple().tm_yday
    week_number = now.isocalendar().week
    next_month = now.month % 12 + 1
    next_month_year = now.year if next_month != 1 else now.year + 1
    total_days_in_month = (datetime.date(next_month_year, next_month, 1) - datetime.timedelta(days=1)).day
    days_left_month = total_days_in_month - now.day
    days_left_year = total_days_in_year - day_of_year
    date_str = now.strftime("%B %d, %Y")

    message = f"""🌞 *Good Morning, Tanvir*

════ *{date_str}* ════
*Day*                        : {now.strftime('%A')}
*Week Number*     : {week_number}
*Day of Year*          : {day_of_year}
*Days Left Month* : {days_left_month} days
*Days Left Year*     : {days_left_year} days
═══════════════

😎 *Dream big. Start small. Act now.*"""

    return quote(message)

# Send WhatsApp message via CallMeBot
def send_whatsapp_message():
    message = get_message()
    url = f"https://api.callmebot.com/whatsapp.php?phone={PHONE}&text={message}&apikey={APIKEY}"
    response = requests.get(url)

    if 'queued' in response.text.lower():
        print("✅ Message queued successfully.")
    else:
        print("❌ Error sending message:", response.text)

if __name__ == "__main__":
    send_whatsapp_message()
