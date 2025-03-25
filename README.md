# PP4 - Reservation

## Validation

CSS:
Validated, no errors
https://jigsaw.w3.org/css-validator/validator

HTML:
Validated, no errors apart from Django-specific values not recognized by validator
https://validator.w3.org/nu/#textarea

Python:
Validated using PEP8, no errors found
https://pep8ci.herokuapp.com/


## Testing

Manually tested creating, updating and deleting while logged out
Result: Redirected to login in each case, if logged out can only view bookings

Manually tested form validation:

Name: Must not be empty
Number of guests: Must be a whole number (field type itself enforces this), must be greater than zero
Reservation date/time: Must be a valid date, cannot be in the past (including the current day but a past time on that day)
Phone number: Must be between 8 and 15 digits, can contain + at start, spaces, or dashes, but these are not included in count, must not contain any other characters (e.g. letters)

Manually tested deleting and updating a record not made by user, as a non-admin:
Result: Change was not made, user is alerted that they don't have permission to do that

Manually tested deleting and updating a record not made by user, as an admin:
Result: Change was made, as admin has permission to change or delete any record
