# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import csv, re

def readInputTxt():
    inputdict = {}

    file = open('config.txt', 'r')
    for line in file:
        var, val = line.split('=')
        val = val.rstrip() # removes ending white space

        inputdict.update({var : val})

    return inputdict

lookup = readInputTxt() # imports config file

def cleanNumber(num): # standardizes number format
    c_code = '1' # only supports US numbers for now
    extractednumlist = re.findall('\d+', num)
    extractednum = ''.join(extractednumlist)
    if extractednum[:len(c_code)] == c_code: # trims off country code
        extractednum = extractednum[len(c_code):]
    if len(extractednum) == 10: # number with no country code
        return "+" + c_code + extractednum
    else:
        print "Incorrect number length: " + num

def importCSV():
    file_name = 'input.csv'

    contactscsv = csv.reader(open(file_name, 'r'), delimiter=',')

    contactslist, contactsdict = [], {}

    for item in contactscsv: # imports CSV into python list
        contactslist.append(item)

    for line in contactslist[1:]: # builds dictionary with contacts list, skips header
        num = cleanNumber(line[0])
        contactsdict[num] = line[1:]

    return contactsdict

def buildTextString(body, values=[]):
    outputBody = body
    outputBody = outputBody.replace(str('\\n'), '\n')

    for i in range(0, len(values)):
        replace_old = '{{' + str(i + 1) + '}}'
        replace_new = values[i]
        outputBody = outputBody.replace(replace_old, replace_new)
    
    return outputBody

# Find these values at https://twilio.com/user/account
account_sid = lookup['twilio_account_sid']
auth_token = lookup['twilio_auth_token']
twilio_number = cleanNumber(lookup['twilio_number'])

numbers_dict = importCSV()

client = TwilioRestClient(account_sid, auth_token)

for number, values in numbers_dict.iteritems(): # for dict with values in body
    textBody = buildTextString(lookup['text_body'], values)

    message = client.messages.create(to=number, from_=twilio_number,
                                     body=textBody)
