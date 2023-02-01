
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




## Authors

- [@Siddhesh Garud](https://in.linkedin.com/in/siddheshgarud)

