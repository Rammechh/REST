# Python
---
## [_Prototyping Score Alerts_](https://www.crio.do/projects/python-cricket-alerts/)

+ References
  * [REST](https://learn.crio.do/home/me/ME_REST.d)
    <p>REST stands for REpresentational State Transfer. Ex. An API is like a waiter in a restaurant. You don’t go into a cafe and walk straight into the kitchen to tell the chef what you wanna eat. The waiter does that for you, and that’s exactly what an API is - with the client being you, the customer and any resource that can send data, being the chef.
    <p>Client-Server model (one software program sends a request and the other responds with some data)</p>
    <p>Use HTTP protocol to send request & receive responses</p>
    <p>Data Format in REST is JSON (JavaScript Object Notation)</p>
    <p> We can analyse the network packets during the API calls to confirm this using Wireshark. Wireshark is a popular network analysis tool to capture network packets and display them at a granular level</p>
   * + [Understanding & using REST APIs](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)
         * The Anatomy Of A Request _1.The endpoint 2.The method 3.The headers 4.The data (or body)_
            * 1. Testing Endpoints With Curl in cmd * curl https://api.github.com/users/zellwk/repos
            * 2. The Method --> 1. GET(READ) 2. POST(CREATE) 3. PUT(UPDATE) 4. PATCH(UPDATE) 5. DELETE(DELETE)
            * 3. You can send HTTP headers with curl through the -H or --header option. To send header to Github’s API in cmd--> curl -H "Content-Type: application/json" https://api.github.com
            * 4. To send data through cURL, you can use the -d or --data option: curl -X POST <URL> -d property1=value1
---
  * [HTTP](https://learn.crio.do/home/me/ME_HTTP.md)
  * [Jackson](https://pypi.org/project/JackSON/.md)
    * pip install --user jackson
      * JAckson file uploaded
  * [Chrome Dev Tools](https://www.bitdegree.org/learn/chrome-developer-tools)
 
+ Fetching Live score and Parsing Data
  * [Read, Write and Parse JSON using Python](https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/)

+ Notifying the users
  * [Send message to Telegram user using Python](https://www.geeksforgeeks.org/send-message-to-telegram-user-using-python/)
  * [telegram-send · PyPI Documentation](https://pypi.org/project/telegram-send/)
  
+ Recurring Notifications
  * [How to Run or Repeat a Linux Command Every X Seconds Forever](https://www.tecmint.com/run-repeat-linux-command-every-x-seconds/)

+ Spice it up!
  * [How to Use Python Lambda Functions](https://realpython.com/python-lambda/)
  * + Chrome Extensions [Getting Started Tutorial](https://developer.chrome.com/extensions/getstarted)
  * [How to Send SMS Text Messages with Python](https://www.fullstackpython.com/blog/send-sms-text-messages-python.html)
  * [Send Emails Using Python](https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/)

+ Publish to GitHub
  * [How to add an existing project to Github](https://medium.com/@soufianerafik/how-to-add-a-local-project-to-github-on-macos-94a64659612b)
