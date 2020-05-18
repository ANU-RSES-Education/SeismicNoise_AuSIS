# ## Settings for this repository
#

import pandas as pd
from obspy import UTCDateTime


# Set these values to control the notebook behaviour

# Make sure you take at least a full week (>=7 days) before the first "ban"
start = UTCDateTime("2020-01-15")

# Leaving UTCDateTime() empty means "now":
# and this means 24 hours ago: UTCDateTime() - 24*3600
end = UTCDateTime("2020-02-15")


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

data_provider = "IRIS"
logo = None # 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_SED_2014.png/220px-Logo_SED_2014.png'
bans = {
        "2020-01-28 00:00":"End of School Summer Holiday"
        }


