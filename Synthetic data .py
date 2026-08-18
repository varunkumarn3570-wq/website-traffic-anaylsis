import pandas as pd
import numpy as np
from datetime import datetime
import os
n = 5000
session_id = [f"ses{str(i).zfill(4)}" for i in range(1, n+1)]
User_id = [f"usd{str(i).zfill(4)}" for i in range(1, n+1)]
Visit_date = np.random.choice(pd.date_range("2025-01-01", "2026-01-01"), size=n)
device_type = np.random.choice(["Desktop","Mobile","Tablet"], size=n)
browser = np.random.choice(["Chrome","Firefox","Edge","Safari","Opera"], size=n)
operating_system = np.random.choice(["Windows","MacOS","Linux","Android","iOS"], size=n)
traffic_source = np.random.choice(["Organic search","Direct","Social media","Email marketing","Referral","Paid search"], size=n)
country = np.random.choice(["India","US","UK","Canada","Australia","Singapore","Germany"], size=n)
city = np.random.choice(["Hyderabad","Bangalore","Mumbai","Delhi","Chennai","New York","London","Sydney","Singapore"], size=n)
landing_page = np.random.choice(["Home","Products","Services","About us","Blog","Pricing","Contact","Login"], size=n)
exit_page = np.random.choice(["Home","Products","Services","Blog","Pricing","Contact",""], size=n)
bounce = np.random.choice(["Yes","No"], size=n)
New_or_returning = np.random.choice(["New Visitor","Returning Visitor"], size=n)
conversation = np.random.choice(["Yes","No"], size=n)
pages_visited = np.random.randint(1, 100, size=n)
session_durationp = np.random.randint(1, 60, size=n)
page_views = np.random.randint(1, 25, size=n)
clicks = np.random.randint(1, 50, size=n)
Revenue = np.random.randint(0, 10000, size=n)
data = pd.DataFrame({
    "Session_ID": session_id,
    "User_ID": User_id,
    "Visit_date": Visit_date,
    "Device_Type": device_type,
    "Browser": browser,
    "Operating_System": operating_system,
    "Traffic_Source": traffic_source,
    "Country": country,
    "City": city,
    "Landing_Page": landing_page,
    "Exit_Page": exit_page,
    "Bounce": bounce,
    "New_or_Returning": New_or_returning,
    "Conversation": conversation,
    "Pages_Visited": pages_visited,
    "Session_Duration": session_durationp,
    "Page_Views": page_views,
    "Clicks": clicks,
    "Revenue": Revenue
})
print(data)
print(data.to_csv("Website_Traffic_Analysis.csv"))
print(os.getcwd())