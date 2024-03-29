This UI is constructed based on a template created by Karan Bhanot.
For more detail, please go to: https://github.com/kb22/ML-React-App-Template and  
https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33

# Instruction

## Preparing the UI
Open  two terminals. In the first terminal, go inside the ui folder using cd ui. Make sure you are using the node version 10.4.1. Once inside the folder, run the command yarn install to install all dependencies.
To run the UI on server, we will use serve. We will begin by installing the serve globally, post which, we’ll build our application and then finally run the UI using serve on port 3000.

npm install -g serve
npm run build
serve -s build -l 3000

You can now go to localhost:3000 to see that the UI is up and running. 

## Preparing the service
On the second terminal, move inside the service folder using cd service. We begin by creating a virtual environment using virtualenv and Python 3. You can read about virtualenv here. We will then install all the required dependencies using pip after activating the environment. Finally, we’ll run the Flask app.

virtualenv -p Python3 .
source bin/activate
pip install -r requirements.txt
FLASK_APP=app.py flask run

This will start up the service on 127.0.0.1:5000.

Now, you can go back to localhost:3000! It is now interacting with the Flask service which is just set up.
