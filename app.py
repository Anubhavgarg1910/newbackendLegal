from flask import Flask, jsonify, request
import datetime
from flask_cors import CORS
from textSummary import summarizer
from assistant import legal_assistant
 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
 
# Route for seeing a data
@app.route('/')
def get_time():
    data={
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
    return jsonify(data)
@app.route('/test')
def get_time_test():
    data_test={
        'Name':"test", 
        "Age":"50",
        "Date":x, 
        "programming":"java"
        }
    return jsonify(data_test)




@app.route('/docs', methods=['GET','POST'])
def post_time_test():
    if request.method == 'POST':
        # If it's a POST request, read data from request.json
        data = request.json
        # Process the data as needed
        print("Received data:", data)  # This will print the data to the console where your Flask server is running
        return jsonify(data)
    elif request.method == 'GET':
        # If it's a GET request, you may handle it differently
        # For example, you might want to return some data or render a template
        return jsonify({'message': 'This is a GET request'})


@app.route('/assistant', methods=['GET','POST'])

def post_assist_data():
    if request.method == 'POST':
        a_data = request.json
        assistant_data = process_assist_data(a_data)
        return jsonify(assistant_data)
    elif request.method == 'GET':
        return jsonify({'message': 'This is a GET request'})

def process_assist_data(a_data):
    user_query = a_data.get('query', '')  
    response = legal_assistant(user_query)
    return {
        'response': response,
    }


# def process_query():
#     user_query = request.json.get('query')
#     response = legal_assistant(user_query)
#     return jsonify({'response': response})


@app.route('/analyse', methods=['GET','POST'])

def post_analyse_data():
    if request.method == 'POST':
        # If it's a POST request, read data from request.json
        data = request.json
        # Process the data as needed
        processed_data = process_data(data)
        # Return the processed data as a JSON response
        return jsonify(processed_data)
    elif request.method == 'GET':
        # If it's a GET request, you may handle it differently
        # For example, you might want to return some data or render a template
        return jsonify({'message': 'This is a GET request'})

def process_data(data):
    text = data.get('text', '')  
    summary, original_text, len_orig, len_summary = summarizer(text)
    return {
        'summary': summary,
        'original_text': original_text,
        'len_orig': len_orig,
        'len_summary': len_summary
    }

   
# Running app
if __name__ == '__main__':
    app.run(debug=True)