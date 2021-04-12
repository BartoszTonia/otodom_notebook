from datetime import timedelta
from time import time
import pandas as pd
import requests

t = time()
path = 'data/rent_wroclaw_20210403_13_28_53.csv'
df = pd.read_csv(path)


# Function check if offer is alive based on status code reply:
def validate_state( url ):
    response = requests.head(url)
    print(response.url, response.status_code, end='')
    if response.status_code == 200:
        print('live')
        return 'live'
    else:
        print('sold')
        return 'sold'


# Then apply answer to column 'status'
df['status'] = df['url'].apply(lambda x: validate_state(x))
print(df['status'].value_counts())

# Save updated file in the same path
df.to_csv(path, index=False)

elapsed = time() - t
time_format = timedelta(seconds=elapsed)
print('>>> Executed in {} s'.format(time_format, 2))
