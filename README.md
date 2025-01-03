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
   <img src="https://github.com/user-attachments/assets/d1bd1d64-1985-469d-9143-45a92934a024" height="120%" width="120%" alt="Create static ip"/>
 </p>
<br />
Then we need to verify if the address was created properly
<br/> <br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1adf9a94-ac81-4ee0-abd4-f13d3f109ffb" height="80%" width="80%" alt="IP verification"/>
</p>
<br />
Next step is to create vm instance that will hos our web app. We can do this using command: ```gcloud compute instances create vm-instance-name --address=static-ip --no-service-account --no-scopes --machine-type=e2-micro --zone="ZONE" --metadata=startup-script='apt-get update; apt-get install -y python3-flask' ``` This command will create vm instance and give it the static ip we have created. The metadata part constains a script that will automatically install Flask upon VM startup. After the VM is created we can verify it under Compute Engine > VM instances in GCP navigation menu: <br/><br/> <p align="center">
<img src="https://github.com/user-attachments/assets/a5a5a316-80b9-4a32-9604-5926a566b00f" height="80%" width="80%" alt="VM verify"/></p>
<br />
Next step is to create vm instance that will hos our web app. We can do this using command: ```gcloud compute instances create vm-instance-name --address=static-ip --no-service-account --no-scopes --machine-type=e2-micro --zone="ZONE" --metadata=startup-script='apt-get update; apt-get install -y python3-flask' ``` This command will create vm instance and give it the static ip we have created. The metadata part constains a script that will automatically install Flask upon VM startup. After the VM is created we can verify it under Compute Engine > VM instances in GCP navigation menu: <br/><br/> <p align="center">
<img src="https://github.com/user-attachments/assets/a5a5a316-80b9-4a32-9604-5926a566b00f" height="80%" width="80%" alt="VM verify"/></p>
<br/>
Then we SSH into our instance and simply upload the app.py file:
<br/><br/> <p align="center">
 <img src="https://github.com/user-attachments/assets/e8db15f1-0cdd-448e-8d87-8fb7d7f39027" height="80%" width="80%" alt="VM verify"/></p>
<br/>
<br/>

In order to run the app we perform ```python3 app.py``` command
<br/><br/> <p align="center">
 <img src="https://github.com/user-attachments/assets/f9c192ff-ec4c-4682-a484-9c972f55cb2d" height="80%" width="80%" alt="VM verify"/></p>
<br/>
