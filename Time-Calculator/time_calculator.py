def add_time(start, duration, day=None):
  #time consts
  daysecs = 86400
  hoursecs = 3600
  #initialize counting variable
  days = 0
  hours = 0
  minutes = 0
  
  try:
    day = day.lower()
  except:
    day = None

  days_dict = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
  }
  days_dict_rev = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
  }

  #break up inputs into hrs, mins, am/pm
  starting_elements = start.split()
  time_elements = starting_elements[0].split(':')
  
  start_class = starting_elements[1]
  start_hrs = int(time_elements[0])
  start_mins = int(time_elements[1])

  #convert to seconds
  if (start_class == 'PM'):
    start_hrs += 12 
  st_secs = start_hrs * 60 * 60 + start_mins * 60
  
  #add time
  duration_elements = duration.split(':')
  d_secs = int(duration_elements[0]) * 60 * 60 + int(duration_elements[1]) * 60

  new_secs = st_secs + d_secs

  #calculate new days, hrs, mins
  while new_secs >= daysecs:
    days += 1
    new_secs = new_secs - daysecs

  while new_secs >= hoursecs:
    hours += 1
    new_secs -= hoursecs

  while new_secs >= 60:
    minutes += 1
    new_secs -= 60

  #determine am/pm
  daycode = start_class
  if hours > 0 and hours < 12 :
    daycode = "AM"
  elif hours == 12:
    daycode = "PM"
  elif hours > 12 :
    daycode = "PM"
    hours -= 12
  else :
    daycode = "AM"
    hours += 12
  

  
  #find new day
  try:
    current_day = days_dict_rev[(days_dict[day] + days) % 7]
  except:
    current_day = 'Error'

  if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)

  if day == None:
    if (days == 1):
      compiled_time = f"{hours}:{minutes} {daycode} (next day)"
    elif days < 1:
      compiled_time = f"{hours}:{minutes} {daycode}"
    elif days > 1:
      compiled_time = f"{hours}:{minutes} {daycode} ({days} days later)"
  else:
    if (days == 1):
      compiled_time = f"{hours}:{minutes} {daycode}, {current_day} (next day)"
    elif days < 1:
      compiled_time = f"{hours}:{minutes} {daycode}, {current_day}"
    elif days > 1:
      compiled_time = f"{hours}:{minutes} {daycode}, {current_day} ({days} days later)"

  #print('\n' + start, duration, day)
  #print(compiled_time)
  return compiled_time
