To connect to the desktop of a Microsoft Windows instance:

In the EC2 console, choose Instances and then choose the instance that you want to connect to.
From the Actions menu, choose Get Windows Password.
Next to Key Pair Path, choose Browse.
Browse to and select the labsuser.pem file that you downloaded earlier.
Choose Decrypt Password.
The connection information should display, including the instance's public Domain Name System (DNS), administrator user name, and the decrypted password.
Use a Remote Desktop Protocol (RDP) client to connect to the desktop of the EC2 instance by using these connection details.