# tts_googlecloudapi
Building tts using Google Cloud API

Step 1: Create a Google Cloud Project

Go to console.cloud.google.com
Sign in with your Google account
Click "Select a project" → "New Project"
Give it a name (e.g., wavenet-tts) and click Create

Step 2: Enable the Text-to-Speech API

In the search bar at the top, type "Cloud Text-to-Speech API"
Click on it from the results
Click the blue "Enable" button

Step 3: Create Your API Key

In the left menu, go to APIs & Services → Credentials
Click "+ Create Credentials" → "API Key"
Your key is generated — copy it
Click "Edit API Key" to restrict it:

Under API restrictions, select "Cloud Text-to-Speech API" only

Step 3: Play with the code

Pre-requicites : pip install requirements.txt
Select and paste api key in the code

