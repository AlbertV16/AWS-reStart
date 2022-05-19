# Create a EC2 instance

Bastion EC2 instance    35.86.81.214

WebSecurityGroup    	sg-0e445d3e6339e5465
PublicSubnet	        subnet-040dcbe92aee0cf50
MisconfiguredWebServer	54.191.85.242

# Does the following
# Obtain the region where the instance is running
# Store the AMI ID in a var called AMI
# Set the Region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}
# Obtain latest Linux AMI
AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
echo $AMI

# Retrieve Subnet ID
SUBNET=$(aws ec2 describe-subnets --filters 'Name=tag:Name,Values=Public Subnet' --query Subnets[].SubnetId --output text)
echo $SUBNET

# Obtain SG
SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=WebSecurityGroup --query SecurityGroups[].GroupId --output text)
echo $SG

# Installs a web server
# Downloads a zip file containing the web application
# Installs the web application
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RESTRT-1/171-lab-JAWS-create-ec2/s3/UserData.txt
# View script contents
cat UserData.txt

# Launch instance
INSTANCE=$(\
aws ec2 run-instances \
--image-id $AMI \
--subnet-id $SUBNET \
--security-group-ids $SG \
--user-data file:///home/ec2-user/UserData.txt \
--instance-type t3.micro \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Web Server}]' \
--query 'Instances[*].InstanceId' \
--output text \
)
echo $INSTANCE

# Obtain instance info
aws ec2 describe-instances --instance-ids $INSTANCE
# More specifically the instance status
aws ec2 describe-instances --instance-ids $INSTANCE --query 'Reservations[].Instances[].State.Name' --output text

# retrieve url of web server instance
aws ec2 describe-instances --instance-ids $INSTANCE --query Reservations[].Instances[].PublicDnsName --output text

===

Which method should you use?

Launch from the management console 
    when you quickly need to launch a one-off or temporary instance.
Launch via a script 
    when you need to automate the creation of an instance in a repeatable, reliable manner.
Launch via CloudFormation 
    when you wish to launch related resources together.

# DNS of Server
aws ec2 describe-instances --instance-ids $INSTANCE --query Reservations[].Instances[].PublicDnsName --output text

===

# Challenge 1: Connect to an Amazon EC2 Instance
Obtain the DNS name of the Misconfigured Web Server
    From AWS management console: ec2-54-191-85-242.us-west-2.compute.amazonaws.com

SSH into instance
    Need to get key to ssh to instance
    Unable to ssh into instance

Diagnostic
    From management console:
        Inbound rules only allow port 80 (HTTP) connections
        Need to add SSH inbout port to allow web server access
    
SSH CONNECTION WORKING!!!!
I do wonder how I would diagnose/fix the issue using only aws cli

# Challenge 2: Fix the Web Server Installation
Find out why the web site does not appear for the Misconfigured Web Server

    1. Check Security groups
        Can inbound http connections access the misconfigured web server?
            Security groups look good
    2. Cannot connect to EC2 instance

# User Data
#!/bin/bash
yum install -y httpd php
/usr/bin/systemctl enable httpd
/usr/bin/systemctl start httpdd 2>/tmp/errors.txt 

# User Data from working web server
#!/bin/bash
# Install Apache Web Server
yum install -y httpd

# Turn on web server
systemctl enable httpd.service
systemctl start  httpd.service

# Download App files
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/171-lab-%5BJAWS%5D-create-ec2/dashboard-app.zip
unzip dashboard-app.zip -d /var/www/html/

hboard-app.zip -d /var/www/html/
