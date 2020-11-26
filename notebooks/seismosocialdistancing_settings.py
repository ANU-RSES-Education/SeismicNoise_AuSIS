# ## Settings for this repository
#

import pandas as pd
from obspy import UTCDateTime


# Set these values to control the notebook behaviour

# Make sure you take at least a full week (>=7 days) before the first "ban"
# (These are hard-wired around the bans in the setting below)

start = UTCDateTime("2019-12-01")

# Leaving UTCDateTime() empty means "now":
# and this means 24 hours ago: UTCDateTime() - 24*3600
end = UTCDateTime("2020-06-15")



# This is the time it takes to be sure the data that we download is a complete record that
# we can reliably cache in the archive
safety_window = pd.Timedelta('2 days')


network = "S1"
station = "AUKSC"              #,sydney,brisbane jump, adelaide," # Urban stations
location = "*"
channel = "BHZ"
dataset = "Australia_AUKSC"
time_zone = "Australia/Melbourne"
sitedesc = "Keysborough Secondary College, Victoria"

data_provider = "http://auspass.edu.au:8080"
logo = None # 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_SED_2014.png/220px-Logo_SED_2014.png'
bans = {"2019-12-20 00:00":"Start of School Summer Holiday",
        "2020-01-28 00:00":"End of School Summer Holiday",
        "2020-03-18 00:00":'No Large Gatherings',
        "2020-03-25 12:00":'Restaurants/Bars/Schools closed',
        "2020-04-10 00:00":"Easter", 
        "2020-05-18 00:00":"Schools open (VIC/NSW)", 
        "2020-07-07 00:00":"Restrictions re-imposed (VIC)"
        }

reference = {"start": "2020-01-28 00:00",
              "end":  "2020-03-18 00:00"}

summer_hol = {"start":"2019-12-20 00:00",
              "end":  "2020-01-28 00:00"}

lockdown   = {"start":"2020-03-19 00:00",
              "end":  "2020-06-01 00:00"}

reopening    = {"start":"2020-06-01 00:00"}

