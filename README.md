secret-santa
============

Secret Santa Emailer

###Description

Takes in a list of participants and sends an email to them with their secret santa assignments. Each person will get one person to give a gift to and will be the recipient for one more person.

###Usage

```
$ python lib/secret_santa.py --h
usage: secret_santa.py [-h] -e SENDER_EMAIL -p SENDER_PASSWORD [-t]
                       recipients_file

Mails out secret santa assignments

positional arguments:
  recipients_file

optional arguments:
  -h, --help            show this help message and exit
  -e SENDER_EMAIL, --sender_email SENDER_EMAIL
                        Email to send from
  -p SENDER_PASSWORD, --sender_password SENDER_PASSWORD
                        Password of email account
  -t, --test_mode       Sends email to yourself

```

###Recipients File

Of the format:
```
Name|Name of Restrictions|Email|Address
```
with each person separated by a new line.

Ex:
```
John Doe|Jane Doe|johndoe@gmail.com|123 First Street, New York, NY 10028
Jane Doe|John Doe, Grumpy Jim|janedoe@gmail.com|456 Second Street, New York, NY 10028
Grumpy Jim||grumpyjim@gmail.com|789 Second Street, New York, NY 10028
```

###TODO

+ Make the e-mail message customizable
+ Improve robustness of name parsing
