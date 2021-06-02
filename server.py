from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)



@app.route("/")
def home():
	return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
	return render_template(page_name)


# Writes Data in 'database.csv' file
def write_to_csv(data):
	with open('./database.csv', mode='a', newline='') as database2:

		email = data['email']
		subject = data['subject']
		message = data['message']

		csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


# Submitting Form, when the send button is hit
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thanku.html')
    	except:
    		return 'Unable to connect to database!  :('
    		
    else:
        return 'Something went wrong!  :('
