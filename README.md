# phishing_detector_api
Backend for hosting my API. Takes post requests containing an email field in json. Returns True if the email is predicted to be phishing, and False otherwise.

Uses distilbert trained on the following dataset: https://www.kaggle.com/datasets/subhajournal/phishingemails
