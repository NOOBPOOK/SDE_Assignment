I am Vedant Shetye, and this is my Flask App Assignment for Corider SDE Internship

Clone this reposirtory on to the local machine

Once inside the root directory for the project, run the command <br>
`pip install -r requirements.txt`

Once the dependencies are downloaded, you have to create a `.env` file inside the folder <br>
`
MONGO_ENDPOINT = "Your mongodb database endpoint"
MONGO_DEFAULT_DB = "your mongodb database name"
`

After that if you want to run the api locally, run the command <br>
`python3 src/app.py` <br>
And the application will continue to work. Adjust the ports accordingly

I have also pushed my image to DockerHub which one can run easily by following these steps
<br>
`
docker pull noobpook/sde-api
docker run -p 8080:8080 noobpook/sde-api
`
<br>
In this case, you can directly interact with my database. 


