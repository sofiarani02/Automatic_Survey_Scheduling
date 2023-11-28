from flask import Flask, request
import csv
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def survey_form():
    if request.method == 'POST':
        # Retrieve form data
        # Get the form data
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        mobile = request.form['mobile']
        time = request.form['time']
        location = request.form['location']
        return_time = request.form.get('return-time', '')
        interest = request.form['interests']
        date = request.form['date']
        
        # Write data to CSV file
        with open('survey_responses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # If file is empty, write column headers first
            if file.tell() == 0:
                writer.writerow(['FName', 'LName', 'Email', 'Contact', 'Time', 'interests', 'returnTime', 'Interest'])
            
            writer.writerow([first_name, last_name, email, mobile, time, location, return_time, interest])

        # Execute another Python file from the path
        subprocess.Popen(["python", "/path/to/another/python/file.py"])
        return '''<html>
                      <head>
                          <style>
                              body {
                                  text-align: center;
                              }
                          </style>
                      </head>
                      <body>
                        <div style="background-color: #c7f0db; padding: 10px;"><h2>Thank you for submitting the survey!</h2></div><br>
                      </body>
                  </html>'''
	
    # If request method is GET, render the survey form
    return '''<form method="post" style="font-family: Arial, sans-serif; font-size: 16px; color: #333; text-align: center; background: linear-gradient(to bottom right, #ffffff, #d9e2f3); border: 2px solid #ccc; padding: 20px; border-radius: 10px;">
                  <H1><center><b>Welcome to Automated Survey Scheduling!</b></center></H1><br>
                  <H2><center><b><i>&quot;An Initiative to fillout surveys with our personalized work&quot;</i></b></center></H2><br><br>
                  <label for="first-name">First Name:</label>
                  <input type="text" id="first-name" name="first-name" required style="margin-left: 10px;"><br>
                  <label for="last-name">Last Name:</label>
                  <input type="text" id="last-name" name="last-name" required style="margin-left: 11px;"><br>
                  <label for="email">Email:</label>
                  <input type="email" id="email" name="email" required style="margin-left: 27px;"><br>
                  <label for="mobile">Mobile:</label>
                  <input type="tel" id="mobile" name="mobile" required style="margin-left: 20px;"><br>
                  <label for="time">Time:</label>
                  <input type="datetime-local" id="time" name="time" required style="margin-left: 25px;"><br>
                  <label for="location">Location:</label>
                  <select id="location" name="location" required style="margin-left: 5px;">
                  <option value="">Select an option</option>
                  <option value="inside">Home</option>
                  <option value="outside">Outside</option>
                  </select><br>
                  <label for="return-time">Return Time:</label>
                  <input type="time" id="return-time" name="return-time" style="margin-left: 10px;"><br>
                  <label for="interests">Interests:</label>
                  <select id="interests" name="interests" required style="margin-left: 5px;">
                  <option value="">Select an option</option>
                  <option value="Music">Music</option>
                  <option value="Reading">Reading</option>
                  <option value="Sports">Sports</option>
                  <option value="Traveling">Traveling</option>
                  <option value="Photography">Photography</option>
                  <option value="Cycling">Cycling</option>
                  <option value="Painting">Painting</option>
                  </select><br>
                  <label for="date">Date:</label>
                  <input type="date" id="date" name="date" style="margin-left: 28px;"><br>
				  <input type="submit" value="Submit" style="margin-top: 10px; background-color: #4CAF50; color: #fff; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer;"><br><br><br>
			  </form>'''
if __name__ == '__main__':
	app.run(debug=True)
