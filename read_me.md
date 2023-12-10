Limitations:
- The GitHub Actions will fail as I have not set up an ACR or an Azure Function, but will do everything before that, including Lint and Unit Testing
- I wanted to separate all the deployment scripts into different folders like you can with Azure DevOps (e.g. Dev scripts go in a dev folder) but GitHub actions have limitations and can only run in the vase ".github/worksflows" folder


Interview Exercises 

Create a python sample that can be used be used to determine hailstone numbers. See (https://www.youtube.com/watch?v=094y1Z2wpJg (Opens in new window or tab) for an explanation of what these are) 
This code needs to be modular to allow use by many products e.g. kubernetes, cloud functions and APIs. 

*DONE: Uses classes and Modular*

Interface 

Input 

Starting Number 

Outputs 

Number of steps 


List of steps 

Textual Summary 

Show how the code could be tested and demonstrate how supportable it is. 

*I have created a unit test script to test that the script is robust and can handle unexpected values, it will check that the application can handle non int inputs, unexpected values and handling numbers less than 1. It also ensures that the answers given are accurate*

Ideally provide an external git repo that can be used to walk through the codebase. 

Using the hailstone example code above, without creating the cloud components (as we don't want you to incur any additional cost) - how would you deploy this to both cloud native functions and docker containers as repeatable entities? 
This design would need to repeatable deployment into two environments dev and test? 

*Created CI pipelines using GitHub actions, these incorporate the unit and lint testing mentioned earlier into the pipeline. The pipelines will fail when it comes to deploying to azure resources as I have not deployed them to ensure additional costs are not incurred.
The two pipelines I have created are:*

*- "deploy-to-az-function.yml" this pipeline will test the code and then deploy it to an azure function*

*- "push-to-acr.yml" this pipeline will test the code and dockerize the app and push it to an Azure Container Registry*

*To be repeatable and to deploy to dev and test, each env will have a branch on github and an associated yml script for the environment*

Finally, how would you extend the solution to allow for additional environments of pre-prod and production. 

*Additional environments can be created through the additional of new yml files for the new environment and branches on github*

 