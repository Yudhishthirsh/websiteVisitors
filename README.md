# websiteVisitors
Download pycharm and setup virtual enviroment in your pycharm inside the folder facebookDataScraper using Command in terminal below.

pip install virtualenv or can follow the below link to create virtual Environment

https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements

After creating virtual environment in your project. install scrapy package in pycharm , install instaloader package using pip install instaloader , install pandas into the terminal using pip install pandas command in the Terminal To install all these packages use command:

pip install -r requirements.txt

Now Open terninal and run command 

python getIPAddress.py

After Running this command there will ve two links generated on localhost.

Open those link and the IPaddress of the visitos will be fetched.

Note:
1) For production deployment use WSGI server.

2) This program works only for local machines.

3) To deploy this code in public servers need to follow below mentioned process.
    To use a domain name instead of relying solely on the IP address for your Flask application, you'll need to follow these steps:

Register a domain: Choose and register a domain name from a domain registrar. There are many domain registrars available where you can search for available domain names and purchase them.

Set up DNS records: Log in to the domain registrar's website and configure the DNS (Domain Name System) records for your domain. You'll need to create an "A" record or a "CNAME" record to point your domain to the IP address of your server. The specific steps for setting up DNS records will depend on the registrar you choose.

If you have a static IP address for your server, you can create an "A" record that associates your domain name with the IP address.
If your IP address is dynamic or subject to change, you can use a dynamic DNS service or a service like DDNS (Dynamic DNS) to automatically update the DNS records when your IP address changes.
Configure your Flask application: Update the app.run() line in your Flask application to listen on the appropriate host and port. Instead of using the IP address, you can use '0.0.0.0' to listen on all available network interfaces. 

For example:
app.run(host='0.0.0.0', port=4000)

Test your domain: Once the DNS records are set up and propagated, you can test your domain by entering it into a web browser. It should now resolve to your Flask application running on the server.

If the DNS records are correctly set up, your domain should be accessible, and users will see your Flask application when they visit the domain URL.
If the domain doesn't resolve or you encounter any issues, double-check your DNS records and ensure they are correctly configured.
Remember that DNS changes may take some time to propagate across the internet, so it might take a few minutes or hours for your domain to be fully accessible after making the DNS record updates.

By using a domain name, you provide a more user-friendly and memorable URL for your Flask application, making it easier for others to access your website without having to rely solely on the server's IP address.
