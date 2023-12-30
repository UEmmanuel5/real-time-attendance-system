from db import is_attendance_marked
from datetime import datetime

result = is_attendance_marked(1, 'Image Understanding',datetime.now())

print(result)
