##  KONG-Flask Integration
# Overview
This project integrates Flask and Kong Gateway to handle upload and download APIs. Follow the steps below to set up and test the system.

# Getting Started
**Set Up Kong Locally**: Start by running Kong locally using Docker with a database. For detailed instructions, refer to the [official documentation](https://docs.konghq.com/gateway/3.4.x/install/docker/#install-kong-gateway-with-a-database).

**Run Flask App**: The **app.py** contains Flask app which is up and running at [https://shivamjagdishsingh.pythonanywhere.com](https://shivamjagdishsingh.pythonanywhere.com). You can test its status at [https://shivamjagdishsingh.pythonanywhere.com/test](https://shivamjagdishsingh.pythonanywhere.com/test).

# API Testing
**Import Insomnia JSON**: Use [Insomnia](https://insomnia.rest/), a tool provided by Kong, or any API testing tool like Postman. Import the provided [JSON file](https://github.com/shivamjagdishsingh/KONG-Flask-interation/blob/main/insomnia/Insomnia_2023-09-22.json) to access all the test requests.

**Set Up Kong CDN Locally**: Configure Kong CDN by creating services and routes. Make the following requests in order:

Create a service:
![image](https://github.com/shivamjagdishsingh/KONG-Flask-interation/assets/33157915/09f7ed02-c777-4a63-98ae-f96415f9b9d3)
Create a route:
![image](https://github.com/shivamjagdishsingh/KONG-Flask-interation/assets/33157915/14e20c54-b9fa-430b-9496-5aac61ae8dee)

# Testing CDN
**Test CDN**: Your CDN should now be ready for testing. Access http://localhost:8000/pythonanywhere/test to receive a response like this:
![image](https://github.com/shivamjagdishsingh/KONG-Flask-interation/assets/33157915/91a23dc2-ff08-4f16-a466-cde6116edac3)

This demonstrates Kong CDN redirecting to the main website's test page.
**Upload and Download**: Both upload and download processes are available. Find the corresponding requests in the Insomnia collection under the **/flask** folder.

* For Download, use a GET request to retrieve a file (e.g., http://localhost:8000/pythonanywhere/download/img2.jpg).
* For Upload, make a POST request with the required parameters, such as name and filename. Refer to the post request in insomina for details.

 *With these steps completed, you should have successfully set up and tested the KONG-Flask integration for upload and download APIs.*:tada:
