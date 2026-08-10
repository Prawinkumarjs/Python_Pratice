import smtplib , mimetypes ,os
from email.message import EmailMessage

sender = "prawink554@gmail.com"
emailContainer = EmailMessage()
emailContainer['Subject'] = "Sample Email"
emailContainer['From'] = sender
# emailContainer['To'] = 'vigneshnatarajan1334@gmail.com'
emailContainer['To'] = 'Prawinkumar454@gmail.com'
# emailContainer['To'] = 'sri.rengasarathy.007@gmail.com'
emailContainer.set_content("Vanaka da Malpa Office la irunthu...Romba Jolly aah Iruka pola...")

files = r'C:\Users\WELCOME\Pictures\Saved Pictures\, AI generated.png'
if files: 
    with open(files,"rb") as file:data = file.read();fileName = file.name
    fileType = mimetypes.guess_type(fileName)[0]
    if fileType:maintype, subtype = fileType.split("/",1)
    else: maintype,subtype = 'application','octet-stream'
    emailContainer.add_attachment(data,maintype=maintype,subtype=subtype,filename = os.path.basename(files))

# medium for send email
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    with open(r'C:\Users\WELCOME\Documents\pvt\Python app.txt','r') as passwordFile:password = passwordFile.read()
    smtp.login(sender,password)
    smtp.send_message(emailContainer)
print("sent successfully")