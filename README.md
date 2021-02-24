# Activity_API

## https://activity-ft-api.herokuapp.com/

A REST api written in Django for monitoring the activity of members

# Dependencies
- Django v3.1.7
- REST Framework v3.12.2
- Bootstrap v5.0 (UI)

# UI 
An UI was built for POST-ing data to DB.

- Member Section: In memeber section, the user needs to input the following details for creating a member.
    - ID: String Field which accepts maximum of 50 Characters.
    - Name: String Field which accepts maximum of 50 Characters.
    - Time Zone: Select the timezone from the list of timezones

- Actitvity Section: In Activity section, the user needs to input the follwoing details for creating an activity.
    - Member: Select the member for which the activity needed to be added from the dropdown liast.
    - Start Time: Select the start time of the activity.
    - End Time: Select the End time of the activity.

# API
In REST Framework, the viewset used was Model Viewset which retreives the list of members and activities under each member.

The default method has been modified to retreive the list of objects in custom manner.

End Point for API: https://activity-ft-api.herokuapp.com/api/activity/


