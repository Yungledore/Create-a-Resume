from flask import Flask, render_template, request

app = Flask(__name__)

# 1. This route shows the input form (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# 2. This route handles the form submission and shows the resume
@app.route('/submit', methods=['POST'])
def resume():
    # These MUST match the 'name' attribute in your <input> tags
    data = {
        "full_name": request.form.get('full_name', 'Faris Nukman'), # Default if missing
        "email_id": request.form.get('email_id', 'example@mail.com'),
        "date_of_birth": request.form.get('date_of_birth'),
        "father_name": request.form.get('father_name'),
        "mother_name": request.form.get('mother_name'),
        "hobbies": request.form.get('hobbies'),
        "grade": request.form.get('grade'),
    }
    
    # Pass the dictionary to your resume template
    return render_template('resume.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)