# AWS-Vanity-Number-Mid-Development
The purpose of this project was to generate vanity numbers based on a caller's number when they call the Amazon Connect Contact Center. We are to create a lambda function that stores the best 5 resulting vanity numbers and the caller’s number to a DynamoDB table. An Amazon Connect Contact Flow is created that will read off the best Vanity numbers from the caller’s number listed in the function.
### Installing VanityNumber

In order to use the `vanitynumber` module in AWS Lambda you would need to install `pip3` and python through Amazon EC2. The steps on how to do so could be found in this [AWS Import Module Resolution Page](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-import-module-error-python/).
 ### How I Implemented the Solution

I decided to import the `vanitynumber` library into my function because it seemed like the quickest way to accomplish the goal of the project, but it wasn’t as simple as I hoped. These modules and all of their documentation can be found at [vanitynumber](https://pypi.org/project/vanitynumber/) and [phonenumbers](https://pypi.org/project/phonenumbers/).  The `vanitynumber` library isn’t prepackaged in Lambda so I had to create a Amazon EC2 instance to create a Lambda layer. Once the layer was added to the function I used `all_wordifications` on the caller number I had in the function, **("1-800-266-5233")**, to show all possible vanity numbers with that number.   
### Struggles

Initially I thought having the `vanitynumber` library would make this task very simple but that wasn’t the case. Initially I ran into errors using **boto3.resource** until I switched to **boto3.client** and specified that my information was a string. I also ran into errors with the `all_wordifications` due to the results coming out as a list and not a string since the DB table took strings, numbers, and binary information. This was solved by converting the list to string but what was challenging was coming up with the “best” results of the vanity numbers. Eventually due to time constraints, I basically chose the best ones I saw manually to be placed into the DynamoDB table. Using the Amazon Connect Contact Flow I managed to get the call center to state the 5 vanity numbers in the DynamoDB table. 
### More Time 

If I had more time, I would’ve made a function that could create the vanity numbers from the number called instead of manually placing it in the function. Also, I would’ve have created some ranking system to select 5 vanity numbers and have the Contact Flow select 3 of the 5 vanity numbers when invoking the Lambda function. I definitely would’ve used the time to do more testing on the entire project and also try to test on non-US numbers.
