# reminder_DjangoApp

As of right now, it is in its' infant stage. Simple Django app, intended to be a place for users to
create, update, delete, review reminders. These reminders can be of any kind, and emails will *eventually* be 
able to be forwarded to the user. 

## Not deployable...yet, only works on current machine as of now.

### Current progress
Initial shell is in place.
Log in works using django.contrib.auth.urls
Users can log in, create reminders, and then see a list of them displayed on-screen.


### To-do
Finish links to register new users instead of doing so via the admin site.
Add the ability to delete reminders
Add the ability to set an auto-delete field so reminders that are past due are removed (make a default life=span as well)
Add the ability to update the reminder in case appointments/due dats have been changed.
Add in profile customization?
Get the email reminder system running (Django email or a third party perhaps?)
