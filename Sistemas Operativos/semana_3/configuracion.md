[default]<br>
aws_access_key_id=ASIAW64X3ENDWSRDK7WD <br>
aws_secret_access_key=9nw+HL7jI7NTeh7Ens8tsjQHB6nBzBmMwhhdTEw3<br>
aws_session_token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQD1gp1NvruspyQspA/U6WiV/HrPv38izQ4sNRMmT4lTxgIhAIO0b5SnamrsTtU9x9Pcq2vJB0qCXmG0qEnses42/j3xKq0CCEsQARoMNDc4NjcwNDMxMDQ3IgxwWiNHc9k0I5HAdroqigJYxvDH3a00t9JRyHrYwFhKrsXh3YdE0TssvygFPWpRHb+A4Z3YP9NY2n2GMRdsGcLj0txaeag7isXN7rc0lOTZo8nF+d24RXcelOIcflR3hENCJvTiCs1ux3pgFiwhVTvzUMk6t+ltF23o6hInmXbY4ysJNN+3YCoM+HIM613xofCD0dBRcB1jbrrnzQjgnbA979MewwFaGME8ocQWNned6j7ycHYVMjuD+ZJmjyU9bOoIdSuAMW02tKsglJty6nCmi4DZ9SXg5d5/GHpu5vYF2bYzKJ8PXmWW9eyqz8HIqWcIZXm8Vwdtys6eegUtAQQvf8It5F1Q0akSDk/Ljw3eGUgm1tNSyG5/6zD09vDCBjqcASigCBmuhfe67Sj2o4xGjGrkVC4Ncxh96VGcKFT17LqcD4szhlNNY9g3KZTGHiirTAlyVT4FnTeKCkcfxwRX0RXzCZbDLSByBsHbbR8W9XKg3lZrh0dL1bbbK2VGgu5nstw/f15KY78OglKDNh7TwBEYJ+vOVYyUPF1eGfQGzG0mEhtMuEXtT6Dmi2lZhk11VzvVRlXtRh+/5cJr9A==

aws sts get-caller-identity

aws ec2 describe-instances --region us-east-1 --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress]" --output table

-------------------------------------------
|            DescribeInstances            |
+----------------------+------------------+
|  i-01a648647e18ae34b |  34.229.7.169    |
* |  i-0ee051ae997b1f038 |  54.90.182.126   | No es instancia Windows
|  i-0266a97a0c701a232 |  44.203.162.184  |
|  i-057ed7393f0ad5e1e |  35.170.245.117  |
+----------------------+------------------+

aws ec2 get-password-data --instance-id i-0ee051ae997b1f038 --priv-launch-key .\labsuser.pem --query PasswordData --output text

aws ec2 describe-instances --instance-ids i-0ee051ae997b1f038 --query "Reservations[*].Instances[*].Platform" --output text

ssh -i .\labsuser.pem Administrator@54.90.182.126
