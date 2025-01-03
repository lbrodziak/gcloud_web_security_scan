<h1>Google cloud Web security scan</h1>

<h2>Description</h2>
One of cloud security professional's job is to prevent vulnerabilities in web apps deployed in the cloud. Cloud Service Providers equip security teams with various tools for the job. One of those tools in Google cloud is Web Security Scan(WSS).
This project showcases the deployment, scanning and remediation of XSS vulnerability in simple Python Flask app using WSS.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Google cloud platform</b>
- <b>Python</b> 

<h2>Project walk-through:</h2>


For WSS to work properly we first need to set a static ip address using command: ```gcloud compute addresses create ip_address_name --region="REGION"``` where "REGION" is the region we would like to create the ip address in.
 <br/>
 <p align="center">
   <img src="https://github.com/user-attachments/assets/d1bd1d64-1985-469d-9143-45a92934a024" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
 </p>
<br />
<br />
Intercepting packets:  <br/>
<img src="https://imgur.com/8hhRfYc.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sample output of packets.txt file: <br/>
<img src="https://imgur.com/W8LA49s.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>


