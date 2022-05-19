Activity: Create a Website on S3

SecretKey	Lcd2eW9MreC/tYSVN4CSS6z10VO461Lz313J57ov
LabRegion	us-west-2
PublicIP	54.244.69.74
AccessKey	AKIAT7XMGRU3QK2GS2GN

Account Number  274299522359

## VSCode note - Ctrl + m switches the tab mode between regular spacing and tabbing between windows
# Locate current dir in wsl
explorer . or explorer.exe - using Ubuntu

# change vi text color
https://mediatemple.net/community/products/grid/204644480/enabling-vi-syntax-colors

# SSH into EC2 instance
ssh -i labsuser.pem ec2-user@54.244.69.74

# Create bucket with name
aws s3api create-bucket --bucket <bucket-name> --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2

# Create new IAM user
aws iam create-user --user-name awsS3user

# Create user profile with password
aws iam create-login-profile --user-name awsS3user --password Training123!

# Search S3 policies
aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"

# Change iam permission for user <awsS3user>
aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name awsS3user

# Remove tar.gz file
Need to cd to upper dir
    ls to check for tar.gz file
rm tar.gz file
After, cd back to static website dir

# Upload files to S3
aws s3 website s3://<bucket-name>/ --index-document index.html

aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<bucket-name>/ --recursive --acl public-read

aws s3 ls avuong486

# vi update-website.sh
# Text file to contain the code that updates the website
#!/bin/bash
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<bucket-name>/ --recursive --acl public-read

# Sidenote to change the wsl Dark blue text color that's impossible to see
https://superuser.com/questions/1365258/how-to-change-the-dark-blue-in-wsl-to-something-brighter
# for vim
https://unix.stackexchange.com/questions/88879/better-colors-so-comments-arent-dark-blue-in-vim

# To search for text in vi
/.<text-to-find>

# vi move through found results
exit find mode and click 'n'
Can use 'Ctrl + t' and 'Ctrl + g' to move btwn matches without leaving search mode

# Challenge use aws s3 sync instead of aws s3 cp for more efficiency
Current line
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --recursive --acl public-read

# sync line
aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --acl public-read
# syncs directory with the bucket and gives it acl read permissions

# issue with line below was the website was not given read permissions
# troubleshooting with Chris gave the answer, only need to exclude the --recursive line from the copy section
aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ s3://avuong486/ --grants Permission=readacl

