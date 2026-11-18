# FILE NAME - approve_deny.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
import datetime
github = True
foundurl = False
#sets up the timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
attempted_url = input ("Enter a URL to access: ")
#debug opener for both github and codegrade
if github == True:
       #file names for github
       approvelist = open("09-files-folders/approve.txt")
       denylist = open("09-files-folders/deny.txt")
       logs = open("09-files-folders/log.txt", "a")
       reviewlist = open("09-files-folders/review.txt", "a")
else:
       #file names for codegrade
       approvelist = open("approve.txt")
       denylist = open("deny.txt")
       logs = open("log.txt")
       reviewlist = open("review.txt")

appr_list=approvelist.read()

#checks approvelist for url
if attempted_url in appr_list:
       foundurl = True
       status = "APPROVE"
       print(
                     f'''
                     
                     ACCESS GRANTED
                     --------------------------------------------------
                            CONTENT FROM: {attempted_url}
                     --------------------------------------------------
                     This website has been verified as safe by your organization.
                     Feel free to browse this content for business or educational purposes.
                     Remember to follow the organization's acceptable use policy.
                     --------------------------------------------------

                     This access attempt has been logged to log.txt
                     '''
              )
approvelist.close()
#checks deny list for url
deny_list=denylist.read()

#checks approvelist for url
if attempted_url in deny_list:
              foundurl = True
              status = "DENY"
              print(
                     f'''
                     
                     ACCESS DENIED
                     --------------------------------------------------
                            BLOCKED URL: {attempted_url}
                     --------------------------------------------------
                     This website has been blocked by your organization's web filter.
                     Reason: This URL is on the deny list.
                     If you believe this is an error, please contact IT support.
                     --------------------------------------------------

                     This access attempt has been logged to log.txt
                     '''
              )
denylist.close()
#if the url cant be found in either list, this resolves
if foundurl == False:
       status = "REVIEW"
       print(f'''
              URL UNDER REVIEW
              --------------------------------------------------
                     PENDING REVIEW: {attempted_url}
              --------------------------------------------------
              This website is not on the approve or deny lists.
              It has been submitted for review by the security team.
              Access is currently restricted until review is complete.
              Please check back later or contact IT if urgent access is needed.
              --------------------------------------------------

              URL has been added to review.txt for security team review.

              This access attempt has been logged to log.txt
       ''')
       reviewlist.write(f"\n{attempted_url}")
logs.write(f"\n{timestamp} - URL: {attempted_url} - STATUS: {status}")

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a URL to access: www.flcc.edu

ACCESS GRANTED
--------------------------------------------------
       CONTENT FROM: www.flcc.edu
--------------------------------------------------
This website has been verified as safe by your organization.
Feel free to browse this content for business or educational purposes.
Remember to follow the organization's acceptable use policy.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.phishingdemo.org

ACCESS DENIED
--------------------------------------------------
       BLOCKED URL: www.phishingdemo.org
--------------------------------------------------
This website has been blocked by your organization's web filter.
Reason: This URL is on the deny list.
If you believe this is an error, please contact IT support.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.opencompsci.com

URL UNDER REVIEW
--------------------------------------------------
       PENDING REVIEW: www.opencompsci.com
--------------------------------------------------
This website is not on the approve or deny lists.
It has been submitted for review by the security team.
Access is currently restricted until review is complete.
Please check back later or contact IT if urgent access is needed.
--------------------------------------------------

URL has been added to review.txt for security team review.

This access attempt has been logged to log.txt
'''

