# EC2 Auto Start/Stop Scheduler

## Overview
Automated AWS solution that starts and stops EC2 instances on a schedule to save costs.

## Architecture
EventBridge (Cron Schedule) → Lambda (Python) → EC2

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

## Setup Instructions
1. Create IAM role with EC2 and CloudWatch permissions
2. Deploy lambda_function.py as a Lambda function
3. Create two EventBridge schedules:
   - Stop schedule: triggers with `{"action": "stop"}`
   - Start schedule: triggers with `{"action": "start"}`

## Skills Demonstrated
- Python (boto3)
- AWS Lambda
- Amazon EventBridge
- Infrastructure automation
- Cost optimization