from flask import Flask, json

app = Flask(__name__)

# Opening and reading jsonfile
with open("data.json", 'r') as jsonfile:
	json_data = json.loads(jsonfile.read())
	
# Converting json_data into dictionary
dict_data = {}
for i in range(len(json_data)):
	dict_data[i+1] = json_data[i]

# Home page
@app.route("/")
def home():
	return dict_data

# Sorting by employers and employeesCount
employers_list = []	
employeesCount_list = []
for i in range(len(json_data)):
	employers_list.append(json_data[i]['employer'])
	employeesCount_list.append(json_data[i]['employeesCount'])

employers_list.sort()
employeesCount_list.sort()

# Creating new dictionary sorted by employers
new_dict_data = {}
key = 1
for employer in employers_list:
	for i in range(len(json_data)):
		if json_data[i]['employer'] == employer:
			new_dict_data[key] = json_data[i]
			key += 1

# Employers page
@app.route('/data/employers')
def employers():
	return new_dict_data
	
# Creating new dictionary sorted by employeesCount
new_dict_data_2 = {}
key_2 = 1
for employeeCount in employeesCount_list:
	for i in range(len(json_data)):
		if json_data[i]['employeesCount'] == employeeCount:
			new_dict_data_2[key_2] = json_data[i]
			key_2 += 1

# EmployeesCount page
@app.route('/data/count')
def employeesCount():
	return new_dict_data_2

	
if __name__ == "__main__":
	app.run()
