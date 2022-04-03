create table RideData
(
    id          int primary key,
    pickup      varchar[100],
    destination varchar[100],
    wait_time   int,
    ride_cost   int,
    seats       int

);
