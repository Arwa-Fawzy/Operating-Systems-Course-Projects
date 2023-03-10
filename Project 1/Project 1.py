#import neccessary packages 
import psutil 
import os
import time
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#average CPU load perecent as measured over a period of 0.5 milliseconds
def cpu_usage_precent():
    return psutil.cpu_percent(interval=0.5)

#real-time value of the current CPU frequency
def cpu_frequency():
    return int(psutil.cpu_freq().current)

#the absolute number of RAM bytes by the system
def ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

 #the total amount of RAM in bytes available to the system
def ram_total():
    return int(psutil.virtual_memory().total)

#the absolute number of Swap bytes by the system
def swap_usage():
    return int(psutil.swap_memory().used)

#the total amount of Swap in bytes available to the system
def swap_total():
    return int(psutil.swap_memory().total)

#the system's current Swap usage
def swap_usage_percent():
    return psutil.swap_memory().percent

#Get the HDD usage info 
def hard_disk():
    return psutil.disk_usage('D:/CS/4th/os/projects/1/Q1.py')

#Return system-wide network I/O statistics 
def network_calls():
    return psutil.net_io_counters()

#Return system-wide network I/O statistics old and new values 
def old_and_new_calls():
    return psutil.net_io_counters(pernic=True)
    

def main():
    with open("OS Workload.txt", "w") as f:
        # save the current CPU load as a percentage
        f.write('System CPU load is {} %'.format(cpu_usage_precent()))
        #new line
        f.write('\n')

        # save current CPU frequency in MHz
        f.write('CPU frequency is {} MHz'.format(cpu_frequency()))
        f.write('\n')

        # save current RAM usage in MB
        f.write('RAM usage is {} MB'.format(int(ram_usage() / 1024 / 1024)))
        f.write('\n')

        # save total RAM in MB
        f.write('RAM total usage is {} MB'.format(int(ram_total() / 1024 / 1024)))
        f.write('\n')

        # save current Swap usage in MB
        f.write('Swap in memory usage is {} MB'.format(int(swap_usage() / 1024 / 1024)))
        f.write('\n')

        # save total Swap in MB
        f.write('Swap in memory total is {} MB'.format(int(swap_total() / 1024 / 1024)))
        f.write('\n')

        # save current Swap usage as a percentage.
        f.write('Swap in memory usage is {} %'.format(swap_usage_percent()))
        f.write('\n')

        #save HDD Hard disk Usage 
        f.write("The usage statistics of " + os.getcwd() + " is:")
        f.write('\n')
        f.write(str(psutil.disk_usage(os.getcwd())))
        f.write('\n')

        #save network usage info 
        f.write('System network calls are {} '.format(network_calls()))
        f.write('\n')
        f.write('System network old and new calls are {} '.format(old_and_new_calls()))
        f.write('\n')


    #sending the workload file by email 
    def send_workload_email():
        # Setting up the port number and server name

        # Standard secure SMTP port
        smtp_port = 587              
        # Google SMTP Server   
        smtp_server = "smtp.gmail.com"  

        # Setting up the email lists
        sender = "arwafawzi41@gmail.com"
        email_list = ["arwa.harhash@ejust.edu.eg"]

        # Define the password reference external from the mail password for privacy 
        pas = "chdcmrboejmrddkt" 

        # the email subject
        subject = "Operating System Workload"

        for mail in email_list:
            body = f"""
            Dear all,
            This email is regarding the operating system workload of Arwa Fawzy Laptop operating system.
            regards, 
            """
            # the MIME object is to define the email parts
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = mail
            msg['Subject'] = subject

            # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

            # Define the file to attach
            filename = "D:/CS/4th/os/projects/1/OS Workload.txt"

            # Open the file in python as a binary
            attachment= open(filename, 'rb')  # r for read and b for binary

            # Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(attachment_package)

            # Cast as string
            text = msg.as_string()

            # Connect with the server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(sender, pas)
            print("Succesfully connected to server")
            print('\n')

            # Send emails to "person" as list is iterated
            print(f"Sending an email to: {mail}...")
            TIE_server.sendmail(sender, mail, text)
            print(f"Email sent to: {mail}")
            print('\n')

        
            
    #sending the email evey 12 hours
    while True:
        send_workload_email()
        #this is in seconds so 60s x 12 hours
        time.sleep(60*12)



if __name__ == "__main__":
    main()
