aws ec2 get-password-data `
  --instance-id i-0031758c6811ff3c1

  PS C:\Projects\inacap> aws ec2 get-password-data `
>>   --instance-id i-0031758c6811ff3c1
{
    "InstanceId": "i-0031758c6811ff3c1",
    "Timestamp": "2025-06-25T20:52:47+00:00",
    "PasswordData": "iSpios5m2f0IFXtBScKwM/K9s/5jOkTwxxlNwhUppXFGaKB2CKWhTDNwFWwz1ohRcj4hGDOOUJ3y70ZMyETEQ0WR49y9JwP4BZzNFr4NTDKnDr48JzBAF/OtT5Yr07iCPYDCOEkNFjzylNhxS2kJ7iJKqWcRh25uKoY7AKb1NLVPTQEZLGWeq0Qm+1WM+TNt+3xw1+DkKyuLf/RoSZ8lQgyJoPJP672ybu2rrSNNrzYOcNi1vj/9BRnVxUSr0bo/fIP0saBW/n1/UrW+UpOaBSiqLV9FLZ3veYeNOqBLjnz+rBPpBEfQrZfcxiduZ+G7VZ2sN8GbXJFd3fSG2BCjmw=="
}

aws ec2 get-password-data `
  --instance-id i-0031758c6811ff3c1 `
  --priv-launch-key .\MiClaveWindows2.pem `
  --query PasswordData `
  --output text

aws ssm start-session --target i-0031758c6811ff3c1
An error occurred (TargetNotConnected) when calling the StartSession operation: i-0031758c6811ff3c1 is not connected.