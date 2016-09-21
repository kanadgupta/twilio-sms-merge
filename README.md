Twilio SMS Mail Merge
===================

Use this basic script to easily read a CSV of phone numbers and bulk send SMS text messages via the Twilio API (without necessarily needing to read the responses). This is great for organizations that want to quickly and easily send out basic mobile communications to large groups of people.

Twilio is a service that allows us to set up the necessary infrastructure for sending and receiving SMS messages easily and at a low-cost. You can read about SMS pricing [here](https://www.twilio.com/sms/pricing).

Very little coding knowledge is required to use this, though basic Unix command familiarity and Python experience will be helpful.

> Note: Only U.S. phone numbers are currently supported with this script.


----------
Basic Requirements:
--------------

 - Python 2.7+ installed (see [here](https://www.python.org/downloads/))
 - pip (see [here](https://pip.pypa.io/en/latest/))
 - Twilio account and phone number (sign up [here](https://www.twilio.com/try-twilio))
 - Basic knowledge of Unix commands (see [here](https://www.tutorialspoint.com/unix/unix-useful-commands.htm))

----------

Setup
-------------
First, [download the files](https://github.com/kanadgupta/twilio-sms-merge/archive/master.zip) and unzip them. All the files must be in the same folder on your machine in order for this to run, so make sure they're all in one place!

The first requirement after to obtain the following three things from your Twilio account (all of which can be found [here](https://twilio.com/user/account)):

 1. Account SID
 2. Auth Token
 3. Twilio number

Update the `config.txt` file with these values.

#### Preparing the CSV
The CSV file used in this example is called `input.csv`. Feel free to edit this file (Google Docs, MS Excel, or any basic text editor would work) or rename an existing CSV (after a few minor configurations).

| phone            | name    | appt_date      | doctor         |
|------------------|---------|----------------|----------------|
| 1 (888) 888-8888 | Kanye   | October 1st    | Dr. Kardashian |
| 444-444-4444     | Beyonce | October 3rd    | Dr. Phil       |
| 9876543210       | Rihanna | September 30th | Dr. Smith      |

Overall, there are really two main structural requirements in order to make your CSV readable.

 1. The **leftmost** column is where the phone numbers of the recipients go. There can be any number of columns to the right of this. (see below for a note on phone number requirements).
 2. There MUST be a header at the top of the CSV that labels the columns. It doesn't matter what you put in the header -- but make sure that a header is present.

##### Phone number requirements
The only requirement is that the phone numbers (which, as previously mentioned, MUST be in **the leftmost column** of the file) are valid in the United States. Meaning that as long as the phone number is ten digits long (or eleven including the U.S. country code, which is '1'), the phone number is readable by the script. Any rows with numbers that don't fit these requirements will be skipped and printed to the console.

Non-digit characters (parentheses, dashes, spaces, plus signs, etc.) will be ignored entirely, so don't worry about them.

#### Writing the message

Here is the example message in `config.txt`:

> Hello {{1}}! This is the doctor's office. Friendly reminder that your
> appointment is on {{2}}. Your doctor is: {{3}}\n\nSee you then!

As previously mentioned, the column headers of the CSV can say anything. In terms of how the columns get populated into your message, this is how the script reads the table:
| recipient_number | {{1}}   | {{2}}          | {{3}}          |
|------------------|---------|----------------|----------------|
| 1 (888) 888-8888 | Kanye   | October 1st    | Dr. Kardashian |

To add a column of data into your message, simply write `{{x}}` in it, where `x` refers to the column index number using the above notation.

If the message does not need to be personalized for each recipient, simply remove any `{{x}}` elements from your message and confine your CSV file to one column with phone numbers.

Executing the script
-------------
Once all of your files are properly configured, open up a Terminal and run the following command:

    $ pip install twilio

This downloads the necessary packages to properly interact with Twilio's API and send the text messages -- and only needs to be executed before the first time the script is used on your machine.

After double-checking that your CSV and configuration file have everything ready to go, navigate to the directory that contains these files and run the following command:

    $ python send_sms.py

### Reading incoming texts
If you want to see a log of the texts that your Twilio number is receiving, navigate [here](https://www.twilio.com/console/sms/logs).

Unfortunately, this script is designed to assist novice developers in sending bulk outgoing texts. Receiving and replying to texts will require more Python knowledge and more familiarity with the Twilio platform. Luckily, their documentation on doing this is **fantastic** and can be found [here](https://www.twilio.com/docs/quickstart/python/sms).

If you have any questions or problems with this script, please [create a GitHub Issue](https://github.com/kanadgupta/twilio-sms-merge/issues/new). Thanks!