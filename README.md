# EC2 Auto Start/Stop Scheduler

## Overview
Automated AWS solution that starts and stops EC2 instances on a schedule to save costs.

## Architecture
EventBridge (Cron Schedule) → Lambda (Python) → EC2

This project automates EC2 instance start and stop operations using:

- **Amazon EventBridge** – triggers on a schedule (cron)
- **AWS Lambda** – executes Python code using boto3
- **Amazon EC2** – instances are started or stopped based on the schedule

The system helps reduce costs by ensuring instances only run when needed.



```mermaid
flowchart LR
    A["EventBridge Schedule<br>(Cron Job)"] --> B["Lambda Function<br>(Python boto3)"]
    B -->|Start/Stop| C[EC2 Instances]

    subgraph AWS Cloud
        A
        B
        C
    end

    D[CloudWatch Logs] --> B



## AWS Services Used
- AWS Lambda - runs the start/stop logic
- Amazon EventBridge - triggers Lambda on a schedule
- Amazon EC2 - the instance being scheduled
- AWS IAM - permissions for Lambda to control EC2

## How It Works
1. EventBridge triggers the Lambda function at scheduled times
2. Lambda receives the action (start or stop)
3. Lambda uses boto3 to start or stop the EC2 instance

## Cost
Nearly $0/month - all services used are within AWS free tier limits

## 💡 Features
- Automated EC2 start/stop
- Serverless (no infrastructure to manage)
- Cost optimization
- Uses AWS native services

## How to Recreate This Project

### Step 1 — Launch EC2 Instance
- Go to AWS Console → EC2 → Launch Instance
- AMI: Amazon Linux 2023
- Instance type: t3.micro
- Region: ap-southeast-1 (Singapore)

### Step 2 — Create IAM Role
- Go to IAM → Roles → Create Role
- Trusted entity: AWS Service → Lambda
- Attach policies: AmazonEC2FullAccess, CloudWatchLogsFullAccess
- Role name: ec2-scheduler-role

### Step 3 — Deploy Lambda Function
- Go to Lambda → Create Function
- Name: ec2-scheduler
- Runtime: Python 3.13
- Assign the ec2-scheduler-role
- Upload the lambda_function.py code
- Or deploy via CLI:

aws lambda create-function 
--function-name ec2-scheduler 
--runtime python3.13 
--role arn:aws:iam::YOUR_ACCOUNT_ID:role/ec2-scheduler-role 
--handler lambda_function.lambda_handler 
--zip-file fileb://ec2-scheduler.zip

### Step 4 — Create EventBridge Schedules
- Go to EventBridge → Scheduler → Create Schedule
- Schedule 1 (Stop):
  - Name: ec2-stop
  - Cron: 0 22 * * ? * (10PM Manila time)
  - Target: Lambda → ec2-scheduler
  - Input: {"action": "stop"}
- Schedule 2 (Start):
  - Name: ec2-start
  - Cron: 50 21 * * ? * (9:50PM Manila time)
  - Target: Lambda → ec2-scheduler
  - Input: {"action": "start"}

### Step 5 — Test It
Test stop
aws lambda invoke --function-name ec2-scheduler 

--payload "eyJhY3Rpb24iOiAic3RvcCJ9" response.json
Test start
aws lambda invoke --function-name ec2-scheduler 

--payload "eyJhY3Rpb24iOiAic3RhcnQifQ==" response.json


## Skills Demonstrated
- Python (boto3)
- AWS Lambda
- Amazon EventBridge
- Infrastructure automation
- Cost optimization