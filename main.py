import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_synthetic_data(num_users, num_files, num_activities):
    user_ids = [f"User_{i}" for i in range(1, num_users + 1)]
    file_ids = [f"File_{i}" for i in range(1, num_files + 1)]

    file_metadata = pd.DataFrame({
        'FileID': file_ids,
        'FileType': np.random.choice(['Document', 'Image', 'Spreadsheet'], num_files),
        'FileSize': np.random.randint(1024, 8192, num_files),
        'ParentDirectory': np.random.choice(['/Documents', '/Images', '/Spreadsheets'], num_files),
        'IsShared': np.random.choice([True, False], num_files)
    })
    activities = []
    for _ in range(num_activities):
        user = random.choice(user_ids)
        file = random.choice(file_ids)
        timestamp = datetime.now() - timedelta(days=random.randint(1, 365))
        activities.append([file, user, timestamp])

    user_activity_log = pd.DataFrame(activities, columns=['FileID', 'UserID', 'AccessTimestamp'])

    return file_metadata, user_activity_log

# Example: Generate synthetic data for 10 users, 50 files, and 500 activities
num_users = 10
num_files = 50
num_activities = 500
file_metadata, user_activity_log = generate_synthetic_data(num_users, num_files, num_activities)
file_metadata.to_csv('file_metadata.csv', index=False)
user_activity_log.to_csv('user_activity_log.csv', index=False)
