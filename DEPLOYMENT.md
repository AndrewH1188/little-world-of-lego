Back to [README.md](README.md) file

## Deployment:

## Table of Contents
1. [Cloning or running my project](#cloning-or-running-my-project)
2. [Deploying to Heroku](#deploying-to-heroku)
3. [AWS - Amazon Web Services](#aws)
4. [Connecting Django to S3](#connecting-django-to-s3)
5. [Caching Media Files and Stripe](#caching-media-files-and-stripe)
6. [Other Processes](other-processes)
7. [Stripe Processes](#stripe-processes)
8. [Gmail Emails](gmail-emails)


#### Cloning or running my project:
In order to create this website I used GitPod to create files that enabled me to write the code in, upload and store images and all relevant folders that were required for this website to function, as well as show the testing, bugs, a live version of the deployed site which have been added to my README file to showcase these. GitPod is linked to GitHub which enables me to use the terminal in GitPod to add, commit and push the code and any changes to GitHub. My project has been deployed using [Heroku](https://www.heroku.com/) which has allowed my site to go live for people to use and view. This project serves as another part of my expanding portfolio that employers are able to view and see my coding skills and also my design skills. Having this site live also enables me to be able to look back at my journey over the course of studying with the Code Institute and see how far I have come on my journey from my first website [Go Tennis System](https://andrewh1188.github.io/go-tennis-ms1/) to my second website [War Heroes Remembered](https://andrewh1188.github.io/war-heroes-remembered-ms2/index.html) and third website [Talking Tinnitus](https://talking-tinnitus.herokuapp.com/) to becoming a Full Stack Web Developer. 

Having a live deployed site enables users to view my site without having to fork or clone this for themselves, but if users would rater clone my site for themselves I have added a section below to walk them through how to do this.

If you would like to run my project locally you are more than welcome to do so. In order to do this you will need to do the following:
1. Click on the little-world-of-lego link which is at the top of my Repository in GitHub.
2. Click on the drop down arrow where it says Code.
3. Click Clone, Open GitHub Desktop or Download ZIP.
4. Open in your preferred IDE.
5. Run on your preferred server.
6. You will need to install the required packages using the pip install -r requirements.txt command in the terminal. Installing the requirements.txt file will help when you run this on Heroku.
7. You will need to create a Procfile, this is a special file that tells Heroku how to run the project that you have created. To make a Procfile you will need to right click and select New File. Call this new file that you have just created Procfile with a capital P.
8. Open up the new Procfile that you have created type the following: 
web: gunicorn YOUR-PROJECT-NAME.wsgi:application
























#### Amazon Web Services - AWS:
1. Head to [Amazon Web Services](aws.amazon.com) click create an account.
2. Select the radio button for Personal Account and fill in your details. 
3. You will need to put in a credit card. You will see a $1 amount on your card, but this won’t be taken. This is just to verify your card. You will not be billed if you don’t go over the usage limit.
4. You have to enter your mobile number so that they are able to verify it is you. To do this AWS send a code to your phone that you will need to enter.
5. You will need to log into your account again. Once logged in type S3 in the search bar. The first result will be S3 in the list. Move your mouse over this and it will show Buckets. 
6. Click the Buckets link, then Create Bucket button.
7. Name your Bucket the same as your Heroku app name and select your region.
8. In the Object Ownership select ACLs enabled and Bucket owner preferred. Be sure not to block all public access by removing the tick that is in the box (You may have to tick a box that says that you understand the implications of unticking the block all public access) then click the Create Bucket button. We will see that we now have a bucket that has been created.
9. Click the bucket name, this will open up the Objects tab. We need to click the Properties tab and scroll right down to the bottom, to the last section that says Static Website Hosting. Click the edit button and enable static website hosting. Type in the Index document field index.html and in the Error document - (optional) field type error.html then click the Save Changes button.
10. Go to the Permissions tab and scroll down to the Cross-Origin Resource Sharing (CORS), click the edit button and paste in the following JSON code
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

    * The code above sets up the required access between Heroku and the S3 Bucket.
    * Make sure you click the Save Changes button before moving on.
11. Still on the Permissions tab scroll down to Bucket Policy, click Edit. 
    * Copy your Bucket ARN which looks like this arn:aws:s3:::YOUR-PROJECT-NAME
    * Click the Policy Generator Button (which will open in a new tab). 
    * In Step 1 in the drop down menu select S3 Bucket Policy.
    * In Step 2 select in the Effect to Allow.
    * In the Principle field type *
    * In the Actions on the dropdown menu select GetObject.
    * In the Amazon Resource Name (ARN) paste your Bucket ARN.
    * Click the Add Statement button.
    * Click the Generate Policy button.
    * Copy the JSON generated and paste this in the Bucket policy.
    * Make sure that you adapt the end of section for “Resource”: “arn:aws:s3:::YOUR-PROJECT-NAME/*”
    * Save your Changes
12. On the Permissions tab scroll down to Access Control List (ACL) and click the Edit button
    * Where it says Everyone, click the tick box.
    * Click the tick box to say that you understand (located at the bottom of the page) and then click the Save Changes button
13. Go to the Search box and type IAM.
    * Click the IAM that shows up first.
    * Click on User Groups in the side bar nav menu and create a user group
    * Give your group a name manage-YOUR-PROJECT-NAME
    * Click Create Group
14. Click Policies in the side menu tab
    * Click JSON tab
    * Import Managed Policy
    * Search S3
    * AmazonS3FullAccess
    * Import
    	* In the JSON file we will replace the “*” with the following: 
    	[
		“arn:aws:s3::YOUR-PROJECT-NAME”
		“arn:aws:s3::YOUR-PROJECT-NAME/*”
	]
    * Click the Next: tags button, then Next: review.
    * In the review policy page give your policy a name: YOUR-PROJECT-NAME-policy
    	* Description: Access to S3 bucket for YOUR-PROJECT-NAME static files.
    * Click the Create Policy button.
15. Go back to the User Groups on the Side navigation menu
    * Click manage-YOUR-PROJECT-NAME, Permissions, Add Permissions, Attach Policies
    	* Click the tick box next to YOUR-PROJECT-NAME-policy and click the Add permissions button.
    * Click the Users link on the side nav bar and then click the Add User button.
    	* Name: YOUR-PROJECT-NAME-staticfiles-user
    	* Click the tick box for Access Key - Programatic Access, then click the Next: Permissions button
    	* Leave the Add User Group tick box selected. Go and click the tick box next to manage-YOUR-PROJECT-NAME. Click the Next: tags, Next: review, Next: create user buttons.
16. ** IMPORTANT ** Be sure to click the Download .CSV file button . This contains the access and secret access key. Once you have gone through this process you will not be able to download them again, so it is important that whilst we are at this stage it is done now.


#### Connecting Django to S3
1. In GitPod (or your environment) you will need to install two packages
* pip3 install boto3
* pip3 install Django-storages
2. Make sure you remember to freeze your requirements using pip3 freeze > requirements.txt
3. Remember to add ’storages’ to your list of installed apps in your settings.py (your main project named folder)
4. Add your AWS Cache control, Bucket config, Static and media files as well as override static and media URLS in production.


#### Caching Media Files and Stripe
1. Go to your AWS - Amazon Web Services and search S3. Click the S3 and click on your bucket name  YOUR-PROJECT-NAME.
2. Click Create folder and follow these steps:
* Name: media
* Click Create Folder button
3. Click the media/ folder, click the Upload button, Add Files button, Select all images that you have used in your project, Open.
4. Scroll down to Permissions and under the Predefined ACLs click the radio button for Grant Public Read Access. Click the I understand and then click the Upload button.

#### Other Processes
1. Go to your Heroku deployed site and log in to your account, then at the end of your https://YOUR_PROJECT_NAME.herokuapp.com add /admin
* Log in and under Accounts heading you will see Email Addresses. Click the email addresses link and you should be able to see your email address that you used for your account there.

#### Stripe Processes
1. We need to add our Stripe Keys in Heroku’s config variables. We can get these from Stripe . We will need to add our STRIPE_PUBLIC_KEY as well as our STRIPE_SECRET_KEY
2. If you have used Webhooks we will need to go to Stripe, click Webhooks, add end point:
	* endpoint url: https://YOUR-PROJECT-NAME-herokuapp.checkout/wh/
3. Select All events and click the Add Events button, then click the Add endpoint button.
4. Click the Signing Secret, reveal and add this to Heroku’s Config Vars under STRIPE_WH_SECRET (SECRET CODE GENERATED BY STRIPE WEBHOOKS).


#### Gmail Emails:
To send real emails with Django you will need to do the following:
1. Sign up for or sign into a Gmail account
2. Click the cog in the top right hand corner and click See all settings
3. Click Accounts + Import, then Other Google Account Settings
4. Click the Security tab and scroll down to Signing into Google. Here you will need to turn on the Two Step Verification. 
* This will allow us to create an app password specific to our Django app that will allow it to send emails
5. Click the Get Started button and Enter then enter your Gmail password. Next you will need to send a verification code to your phone. I chose to do this by text.
	* Enter the code that you receive and then click Next, then Turn on.
6. Click the back arrow up at the top of the page where it says <— 2 Step Verification.
7. Scroll down to the Signing into Google and you will see the the 2 Step Verification is on and that App Passwords has appeared.
8. Click on App Passwords (You will need to sign in again)
9. In the Select App you will see on the dropdown menu Mail. Select this for the Select App. 
	* Then where it says Select app click Other from the drop down menu.
	* Then type Django.
	* Click the Generate button
10. This will generate a password for your device. Copy this password as this will be needed in Heroku’s Config Vars.
11. In Heroku we will need to add the following:
* EMAIL_HOST_PASS (Gmail generated password)
* EMAIL_HOST_USER (Your Gmail email address)
12. We will need to add some settings to our settings.py so that we are able to communicate with Heroku and so that Heroku can see what it needs from the code that we have written too.