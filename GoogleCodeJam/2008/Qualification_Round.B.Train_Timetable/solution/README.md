# just simulate the trains from 00:00 to 23:59
## Suppose
Ares is the number of trains that must start at A

Bres is the number of trains that must start at B

AWait is the trains that are ready to go in A station

BWait is the trains that are ready to go in B station

Every train is represented with its time of starting to be ready

T0 is the earliest trip in A and B station now 

T0 is from A to B

## For a example

* If AWait exists train which's time is early than T0.depature_time, 
T0 can **reuse** the train R0, so Ares += 0, AWait.pop();

* Else, T0 must start a new train R0 at A, so Ares += 1

Whatever R0 is reused or new-started, R0 will always be added to BWait: BWait.push(T0.arrival_time + T)

## Some tips
* We need find the earliest trip in A and B, so firstly, we should sort A's trips and B's trips by its depature_time
* We need find the earliest train in AWait or BWait, so AWait and BWait is supposed to be a heap
