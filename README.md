# docker-dash

Run a Dash app with a docker image on AWS ECS.

## Notes

This is a basic Dash app that pulls two images from http://picsum.photos, displays a graph, and echoes input to an output div. 

!example.gif

More detail at this excellent tutorial: https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/

## Steps to deploy

```
git clone https:/github.com/russellromney/docker-dash

cd docker-dash
```

#### Reqs: Python 3, AWS CLI, Docker

Install Docker, Python 3, and  AWS CLI if not already done.

If needed, configure AWS CLI with `aws configure`.


#### Build the Docker image locally and teset

Build:

`docker build -t docker-dash .`

Test:

`docker run -p 8050:8050 docker-dash` 

#### Send image to AWS ECR (Elastic Container Registry)

Create a repository in AWS ECR:

`aws ecr create-repository --repository-name <my-repo-name>`

Get login auth token:

`aws ecr get-login --region us-east-1 --no-include-email`

Copy and paste the output of the above command back into the terminal. You're authenticated locally for 12 hours.

Tag the image to the ECR repo with:

`docker tag docker-dash:latest ACCT_ID.dkr.ecr.us-east-1.amazonaws.com/<my-repo-name>`

Push the image to AWS ECR with:

`docker push ACCT_ID.dkr.ecr.us-east-1.amazonaws.com/<my-repo-name>`

Finally, you're done with the command line!

#### Deploy the Dash app with ECS (Elastic Container Service)

Follow the instructions in step 4 here:  https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/

While doing this, I find it easier to change the names to match <my-thing>-service, <my-thing>-cluster, etc. to make it consistent to refer back to later.


## Updating

If you need to make changes later, you need to build, test, login (if token expired), tag, and push to get the image to ECR. Then run the following command in the terminal:

`aws ecs update-service --cluster <cluster name> --service <service name> --force-new-deployment`

This will force the service to reload with the new code.

