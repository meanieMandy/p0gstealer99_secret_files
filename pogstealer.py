import smtplib, ssl

port = 465  # For SSL
password = '1mM34n13M4NDY!!!'


sender_email = "meaniemandythebestnumber1nocyap@gmail.com"
receiver_email = "admin@poggedupbois.com"
message = """\
Subject: Unauthorized Credit Suisse Bank Transaction

Dear Poggedupbois,

We apoligize for any inconvienience this may couse, but we have notised an unautorized transcation on your Credit Suisse acount. Our records indicate that a larg sum of mony has been transferd to an unkown acount without your autorization.

To prevent any further unautorized transcations, we kindly request that you confirm your acount details by clicking on the following link: [insert link]. This will take you to our secure server, where you will be promptd to enter your acount information. Once you have provided this information, we will be able to confirm your acount and investigate the unautorized transcation.

Please note that failiure to confirm your acount details may result in the suspencion of your acount until further notice. We apoligize for any inconvienience this may couse, but we take the securitiy of your acount very seriusly and want to ensure that your funds are safe.

Thank you for your prompt attention to this matter.

Sincerly,
The Credit Suisee Team

This message is sent from Python."""
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("meaniemandythebestnumber1nocyap@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
