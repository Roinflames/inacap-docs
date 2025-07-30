[default]<br>
aws_access_key_id=ASIAW64X3ENDXLV2NTTE<br>
aws_secret_access_key=7hTmRxDQKXoHp7Zz03Dh3YIiMHv4/2BAx0+EwOYB<br>
aws_session_token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDC2XQndxvt2thrkjMrdGuOcdijsWCkzEGh/59kZPQeGQIhAIVw/8bwGmfgJjs4iJJXeB+1lxjEkd9f22N6mnUsPsMxKq0CCFEQARoMNDc4NjcwNDMxMDQ3IgwZ6AUuRrk03du2l4cqigKbpBLKkmlmmYdAT98UorNUhRzqr7yX8saOzPfD20x5GPzEbLw/rHhXRnRYxGbEugEterF9E85J10xpyjqNlZVBNuiZI+9cD7NLJDMK8DKhFXMKahDsyRrOboG+OZy1mP5Nz4eIsRSjxgWo25j4MX14P6sSLCxT3oQzNkftXfFYD29ZpfkpVoACWJk9M+jsQCl3lTQLsdTupNHSb+r1lvnCROT7vQI8yQ2mqqrhQC8IS+LmV8V0Ur9rgLN3zPXF7il9NhTVmtBoDJQrgvhBbqrnEeyThPWzu4R+9IPQWt8uS69Ps2xsWLlG5RwK/+0YCZPcrMtKdudahtpSF+2d/N449KZLQCyfFXLurjCHi/LCBjqcAXIe+z9ZrEUZsapscwVSRj7EgVLbG1vAWSvSpUvw5V8+k5pAjlrTtwcyYGCVtFmK3LrzjuLDbw0nGsq32SpaamV1jv1D2s3Prw/ljnMkyeXTf/OLWfEWrcnESTqYhPdTQ7c3nlZfr8R1hoy+YeDTEYNrD1l2nPj41CVts8FOkEI7QgzvGyqsxg4SQ9FY+kzBDMQeIoQygtQDjwRyGw==

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
