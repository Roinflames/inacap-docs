ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType,KeyName,Tags[?Key=='Name']|[0].Value,PublicIpAddress]" --output table
>> C:\Projects\inacap>
--------------------------------------------------------------------------------------------------------------
|                                              DescribeInstances                                             |
+---------------------+----------+------------+----------------------+--------------------+------------------+
|  i-01a648647e18ae34b|  running |  t3.medium |  MiClaveWindowsNueva |  WindowsServerCLI  |  34.229.7.169    |
|  i-0ee051ae997b1f038|  running |  t2.micro  |  vockey              |  Bastion Host      |  54.90.182.126   |
|  i-0266a97a0c701a232|  running |  t3.medium |  MiClaveWindows      |  WindowsServerCLI  |  44.203.162.184  |
|  i-057ed7393f0ad5e1e|  running |  t3.medium |  MiClaveWindowsNueva |  WindowsServerCLI  |  35.170.245.117  |
+---------------------+----------+------------+----------------------+--------------------+------------------+


aws ec2 get-password-data --instance-id i-01a648647e18ae34b --priv-launch-key .\labsuser.pem --query PasswordData --output text
