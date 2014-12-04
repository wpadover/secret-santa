import sys
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import itertools
import smtplib
from person import Person
import argparse

def valid(a, b):
    for i, j in zip(a, b):
        if not (i.canGiveTo(j) and j.canGiveTo(i)):
            return False
    return True

def parseInput(file_name):
  people = []

  f = open(file_name, 'r')

  for line in f:
      parsed = line.split("|")
      if not len(parsed) == 4:
          print("ERROR: Line " + line + " formatted incorrectly.")
          print("Format should be: 'NAME|EXCLUDED PARTNERS NAMES|EMAIL|ADDRESS")
          quit()
      restrictions = parsed[1].strip().split(",")
      people.append(Person(parsed[0].strip(), restrictions, parsed[2].strip(), parsed[3].strip()))
  return people

parser = argparse.ArgumentParser(description='Mails out secret santa assignments')
parser.add_argument('-e', '--sender_email', help='Email to send from', required=True)
parser.add_argument('-p', '--sender_password', help='Password of email account', required=True)
parser.add_argument('-t', '--test_mode', help='Sends email to yourself',
  action='store_true', default=False)
parser.add_argument('recipients_file')

args = parser.parse_args()

people = parseInput(args.recipients_file);
a = list(people)
b = list(people)

while not valid(a, b):
    random.shuffle(a)
    random.shuffle(b)


username = args.sender_email
password = args.sender_password
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(username, password)
for i, j in zip(a, b):
    senders_first_name = i.name.split(" ")[0]

    #TODO - Make this message configurable
    messageplain = "Dearest %s,\n\nIt's Secret Santa time! Again! Yayyyyyyyyyyyyyyyy\n\nYou are going to be getting a gift for %s. His/her address is %s. Remember to keep the gift around $30!\n\nHappy Holidays!! Hope to see you soon!" % (senders_first_name, j.name, j.address)
    messagehtml = "Dearest %s,<br><br>It's Secret Santa time! Again! Yayyyyyyyyyyyyyyyy<br><br>You are going to be getting a gift for <b>%s</b>. His/her address is %s. Remember to keep the gift around $30!<br><br>Happy Holidays!! Hope to see you soon!" % (senders_first_name, j.name, j.address)
    text = ""
    html = """\
    <html>
    <head></head>
    <body>
    """
    text = text + messageplain
    html = html + messagehtml
    html = html + """\
        </body>
        </html>
        """

    # If we are testing, send this to ourselves
    to_email = args.sender_email if args.test_mode else i.email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Secret Santa Assignment!"
    msg['From'] = username
    msg['To'] = to_email
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    try:
        s.sendmail(username, to_email, msg.as_string())
    except:
        print("MESSAGE SEND FAILED: " + text)

s.quit()
