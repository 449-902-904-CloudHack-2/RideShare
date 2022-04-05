# CloudHack_2

## Team members details
- PES2UG19CS449 - Vedanth Mohan
- PES2UG19CS902 - Jacob Bosco
- PES2UG19CS904 - Lavanya Yavagal

## Project Details
[Link to problem statement](https://github.com/Teaching-Assistants-of-Cloud-Computing/CloudHack/tree/master/Problem%20Statement%202)

## Instructions to run
1. Start the containers using 
```
docker-compose up
````
2. To send a request for a new ride, after the containers have started, send a post request using
```
curl -X POST -d "location=hsr&destination=btm&time=7&seat=4&cost=100" localhost:54321/new_ride
```
3. This will be listening to POST requests from new consumers that contains the consumer_id and store their IP address and name.
```
curl -X POST localhost:54321/new_ride_matching_consumer
```
