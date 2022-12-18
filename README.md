# Top Apple Apps
**************

The service, written on Flask, scrapes the official Apple app store website and extracts the information for the top 100 
free apps. Also, it classifies each app into one of the following categories: TV app, Music app (that is not TV), 
Game, or Other and examines the app's data page and determines whether or not it is suitable for children.

This simple service runs on port 8080 and gets top 100 free apps from Apple Store for United State. 
Limit and county can be change.

### **Implementation Details:**

1. In terminal run `docker run -p 5000:5000 -d python-top-apple-apps`
2. Go to [localhost:5000]()
3. For close docker:
  * `docker ps`  (get id like 9cdf1a43f4a2)
  * `docker stop <id>`

