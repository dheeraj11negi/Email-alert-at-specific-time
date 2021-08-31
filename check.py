import smtplib, ssl
import datetime as dt
import time
import json
import logging
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def sendMail():

    logging.basicConfig(filename="test.log",filemode='w',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

    logging.info("welocme to india")
    logging.info("url is  -----")
 
    sender_email="samsalerts@solytics-partners.com"
    password=""
    Subject="Daily-Log-Files"

    reciever_email=["prithivinath.p@solytics-partners.com","tauseef.sagari@solytics-partners.com","gaurav.kumar@solytics-partners.com","dheeraj.negi@solytics-partners.com",'prateek.rajvats@solytics-partners.com','joginder@solytics-partners.com']

    msg=MIMEMultipart()
    msg['From']=sender_email
    #msg['To']=reciever_email
    msg['Subject']=Subject
    print("++++++++",type(msg))
    

    '''smtp_server='smtp.office365.com'
    port=465'''

    servername=""
    port=587


    filename='test.log'
    attachment=open(filename,'rb')
    part= MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename="+filename)

    msg.attach(part)
    mytext=msg.as_string()

    


    context=ssl.create_default_context()
    with smtplib.SMTP(servername,port) as email:
        email.starttls()
        email.login(sender_email,password) 
        now=dt.datetime.now()
        year=now.year
        month=now.month
        day=now.day
        hour=now.hour
        minute=now.minute
        second=now.second

        print(year," ",month," ",day," ",hour,":",minute,second)
        print(type(year),type(hour))



        
        send_time=dt.datetime(year,month,day,23,59,59)
        print(send_time.timestamp())
        print(time.time())
        x=time.sleep(send_time.timestamp()-time.time())
        print(x)

        for go in reciever_email:
        
          email.sendmail(sender_email,go,mytext) 
            
        #email.send_message(mymsg)
        print("email sent")
        email.quit()





if __name__=="__main__":
    sendMail()

