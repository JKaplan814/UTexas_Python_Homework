import os
import csv
import datetime

Headers = ["Emp ID, First Name, Last Name, DOB, SSN, State"]

csvpath = os.path.join('employee_data.csv')

empid = ["EmpID"]
first = ["First Name"]
last = ["Last Name"]
dob = ["DOB"]
ssn = ["SSN"]
state = ["State"]


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvfile, None)

    for rows in csvreader:
        empid.append(rows[0])
        first.append(rows[1].split()[0])
        last.append(rows[1].split()[1])

        dob.append(datetime.datetime.strptime(rows[2], '%Y-%m-%d').strftime('%m/%d/%y'))

        ssn.append("***-**-" + str(rows[3].split("-")[2]))

        state.append(us_state_abbrev[rows[4]])

new_csv = zip(empid,first,last,dob,ssn,state)

with open("New_Employee_Data", "w") as f:
    writer = csv.writer(f)
    writer.writerows(new_csv)