
# Algorithm Visualizer

Users can visualize each and every accessible working of algorithm using the Algorithm Visualizer.

A visual representation of each algorithm aids in a better understanding of the implementation.



## Deployment

a. To deploy this project first make changes in settings.py

```bash
  # Emailing settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_FROM = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
```
Please provide your email address in the fields `EMAIL_FROM` and `EMAIL_HOST_USER` USER. additionally, don't forget to add a password to `EMAIL_HOST_PASSWORD`.


 b.   You have to add your OpenAI Api in `/home/views.py`.

```bash
    openai.api_key = "YOU NEED TO ENTER YOUR OPEN AI KEY"
```

After all the changes run this command
```bash
  python manage.py runserver
```


## Demo

will eventually upload more pictures


## Tech Stack

**Client:** Javascript, Bootstrap, TailwindCSS

**Server:** Django

**Database:** SQLite

**API:** OpenAI



## Screenshots

* Sign Up using Email Address

![Sign up](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(6).png?raw=true)


* It generates the otp and will send to your email address.

![OTP](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(7).png?raw=true)

* After providing the right OTP, the account will successfully create.

![OTP](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(8).png?raw=true)

* After login with correct credential it will force you to dashboard, Where you can see multiple algorithms

![login](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(9).png?raw=true)

* You can select particular algorithm of your choice. I'll go with bubble Sort 

![dashboard](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(10).png?raw=true)

* here you can see multiple options such as 
    
    "Speed" : which will change amount of time require to sort the array. 
    
    "New Array" : will generate new array 

    "Visualize" : will start sortng the array. 
    
    "Size" : By changing size you can change array list like this. 

![new array](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(11).png?raw=true)

* You can see the code of the above algorithm. **Note** : Refresh will impact change in code.

![code](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(14).png?raw=true)


* You can change the language from the dropdown as below. Eventually change the code aswell

![language](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(15).png?raw=true)

* click on "Visualize" will start sorting the algorithm


![sorting](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(17).png?raw=true)

* After completing the sorting it will look like this.

![sorted](https://github.com/siddheshgarud/algovisualizer/blob/main/Screenshot/Screenshot%20(20).png?raw=true)


That's it. Thank You.



## Authors

- [@Siddhesh Garud](https://in.linkedin.com/in/siddheshgarud)

