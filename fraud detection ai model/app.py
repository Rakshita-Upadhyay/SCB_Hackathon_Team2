from flask import Flask, render_template, request
import numpy as np
import pickle

# load the model from disk
filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup.html')
def signup():
	return render_template('signup.html')

@app.route('/home.html')
def home():
	return render_template('home.html')

@app.route('/signin.html')
def signin():
	return render_template('signin.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		transaction_id = request.form['transaction-id']
		customer_id = request.form['customer-id']
		receiver_id = request.form['receiver-id']
		amount = request.form['amount']

		# Perform any necessary data preprocessing or feature engineering here

		# Create a feature vector using the input values
		message = [float(transaction_id), float(customer_id), float(receiver_id), float(amount)]
		vect = np.array(message).reshape(1, -1)

		# Make the prediction using the loaded model
		my_prediction = clf.predict(vect)

	return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
	app.run(debug=True)
