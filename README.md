# PY-BITCOIN

                                                    PyBitcoin 

Introduction
    This is a Python program that intends to send Bitcoin exchange rates on WhatsApp on a daily basis. These rates are in INR(Indian Rupees) by default but can be changed to USD,Euro etc if required.

Purpose
    This project has a purpose to learn Python from basics to advanced.


Overall Description
    This project will have two main modules, one would fetch a Bitcoin exchange rates from a  Alpha Vantage API and send a WhatsApp text using a Third Party Service. The other module will be a cron scheduler that will schedule these WhatsApp texts for everyday.

System Features and Requirements

	Functional Requirements
        Python 3.10-dev / 3.8 (For heroku Deployment)
        Requests
        Twilio
        APScheduler


	External Interface Requirements
        Alpha Vantage API
        Twilio Dashboard for WhatsApp
        Visual Studio Code
        GitHub
        Heroku

	System Features
        get_rate_of_bitcoin
            - Gets Bitcoin value in particular using Rest Api by to_currency parameter.
            - takes to_currency as parameter and returns value in that Currency using alpha-vantage api.

        set_twilio_connection
            - Sets twilio connection for whatsapp and sends message on Whatsapp.
            - takes account_sid and account_token as parameter and returns client object.

        send_whatsapp_text
            - takes message and twilio client connection as parameters and returns message ID      

        background_cron_job
            - takes send_whatsapp_text as a job to execute everyday in background

Assumptions and Dependencies
    As the service for sending and receiving Quotes depends on Third party applications, it is assumed that they are always Up and Running.

    The Project initially aims for learning Python by its latest version i.e 3.10-dev but this version is not available for Heroku 
    hence we would need to downgrade the python version to 3.8 for supporting heroku deployment.

    Other Non Functional Requirements
        Security - All the keys and passwords to be stored as Environment variables
        Quality - Code quality and PEP8 Standards
        Performance - Deployment on Heroku for scaling, newer Python version with updated Libraries


    Industry Practices
        Clean, modularised code
        Snake case as per PEP 8
        Config is Seperate
        Proper Documentation
        DRY - Don’t Repeat yourself
