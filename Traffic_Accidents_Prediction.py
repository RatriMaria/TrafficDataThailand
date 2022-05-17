import urllib.request
import json
import os
import ssl

from tkinter import *
from tkinter.filedialog import asksaveasfile

def check():
    data = {
        "Inputs": {
             "input1": [
          {
           "sex": int(sex.get()),
            "age": int(age.get()),
            "occu": occu.get(),
            "aplace": aplace.get(),
            "aampur": aampur.get(),
            "atumbon": atumbon.get(),
            "injby": int(injby.get()),
            "injoccu": int(injoccu.get()),
            "injp": int(injp.get()),
            "injt": int(injt.get()),
            "risk1": int(risk1.get()),
            "risk2": int(risk2.get()),
            "risk3": int(risk3.get()),
            "risk4": int(risk4.get()),
            "risk5": int(risk5.get())
          }    
        ]
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))
    
#     http = urllib3.PoolManager()

    url = 'http://1c140c9e-f17e-4107-920e-722e1c381c98.australiaeast.azurecontainer.io/score'
    api_key = 'oTTgIVqUFroZ8WNcsgpOFKm5zagrrqfr' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        print(response)
        
        result = response.read().decode('utf-8')
        json_obj = json.loads(result)
        print(json_obj['Results']['WebServiceOutput0'][0]['Scored Labels']) 
        disp_tf.insert(0,json_obj['Results']['WebServiceOutput0'][0]['Scored Labels'])
        disp_prob.insert(0,json_obj['Results']['WebServiceOutput0'][0]['Scored Probabilities'])

        print(json_obj)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))

 
window = Tk()
window.geometry('800x500')
window.title('Mass Casualty Prediction')
 
Sex = Label(window, text="Sex:", font=("Arial", 10))
sex = Entry(window)
Age = Label(window, text="Age:", font=("Arial", 10))
age = Entry(window)
Occu = Label(window, text="Occu (Occupation):", font=("Arial", 10))
occu = Entry(window)
Aplace = Label(window, text="aplace (Place of Accident):", font=("Arial", 10))
aplace = Entry(window)
Aampur = Label(window, text="aampur (District of accident):", font=("Arial", 10))
aampur = Entry(window)
Atumbon = Label(window, text="atumbon (Subdistrict of accident):", font=("Arial", 10))
atumbon = Entry(window)
Injby = Label(window, text="injby (Cause of accident):", font=("Arial", 10))
injby = Entry(window)
Injoccu = Label(window, text="injoccu (Accident obtained at work):", font=("Arial", 10))
injoccu = Entry(window)
Injp = Label(window, text="injp (Type of injured person):", font=("Arial", 10))
injp = Entry(window)
Injt = Label(window, text="injt (Type of vehicles):", font=("Arial", 10))
injt = Entry(window)
Risk1 = Label(window, text="Risk1 (Did the injured person drink alcohol?):", font=("Arial", 10))
risk1 = Entry(window)
Risk2 = Label(window, text="Risk2 (Did the injured person use any drug that affected their nervous system):", font=("Arial", 10))
risk2 = Entry(window)
Risk3 = Label(window, text="Risk3 (Did the injured person fasten seat belt?):", font=("Arial", 10))
risk3 = Entry(window)
Risk4 = Label(window, text="Risk4 (Did the injured person wear safety hat / helmet ?):", font=("Arial", 10))
risk4 = Entry(window)
Risk5 = Label(window, text="Risk5 (Was the injured person using a cellphone?):", font=("Arial", 10))
risk5 = Entry(window)
submit = Button(window,text='Submit',command = check).grid(row=22, column=1)

Disp_tf = Label(window, text="Predicted Output:")
Disp_prob = Label(window, text="Predicted Output Probability:")
 
def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

        
Sex.grid(row=0, column=0)
Age.grid(row=1,column=0)
Occu.grid(row=2,column=0)
Aplace.grid(row=3,column=0)
Aampur.grid(row=4,column=0)
Atumbon.grid(row=5,column=0)
Injby.grid(row=6,column=0)
Injoccu.grid(row=7,column=0)
Injp.grid(row=8,column=0)
Injt.grid(row=9,column=0)
Risk1.grid(row=10,column=0)
Risk2.grid(row=11,column=0)
Risk3.grid(row=12,column=0)
Risk4.grid(row=13,column=0)
Risk5.grid(row=14,column=0)
Disp_tf.grid(row = 25, column = 0)
Disp_prob.grid(row = 26, column = 0)

sex.grid(row=0, column=1)
age.grid(row=1, column=1)
occu.grid(row=2, column=1)
aplace.grid(row=3, column=1)
aampur.grid(row=4, column=1)
atumbon.grid(row=5, column=1)
injby.grid(row=6, column=1)
injoccu.grid(row=7, column=1)
injp.grid(row=8, column=1)
injt.grid(row=9,column=1)
risk1.grid(row=10, column=1)
risk2.grid(row=11, column=1)
risk3.grid(row=12, column=1)
risk4.grid(row=13, column=1)
risk5.grid(row=14, column=1)

disp_tf = Entry(
    window, 
    width=30,
    font=('Arial', 14)
    )

disp_tf.grid(row=25, column=1)

disp_prob = Entry(
    window, 
    width=30,
    font=('Arial', 14)
    )

disp_prob.grid(row=26, column=1)

mainloop()