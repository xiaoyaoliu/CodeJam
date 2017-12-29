# [Problem B. Train Timetable](https://code.google.com/codejam/contest/32013/dashboard#s=p1)

This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the [Quick-Start Guide](https://code.google.com/codejam/resources/quickstart-guide#gcj) to get started.

<table>
  <tr>
    <td>Small input
5 points</td>
    <td>Solve B-small</td>
  </tr>
  <tr>
    <td>Large input
20 points</td>
    <td>Solve B-large</td>
  </tr>
</table>


## Problem

A train line has two stations on it, A and B. Trains can take trips from A to B or from B to A multiple times during a day. When a train arrives at B from A (or arrives at A from B), it needs a certain amount of time before it is ready to take the return journey - this is the *turnaround time*. For example, if a train arrives at 12:00 and the turnaround time is 0 minutes, it can leave immediately, at 12:00.

A train timetable specifies departure and arrival time of all trips between A and B. The train company needs to know how many trains have to start the day at A and B in order to make the timetable work: whenever a train is supposed to leave A or B, there must actually be one there ready to go. There are passing sections on the track, so trains don't necessarily arrive in the same order that they leave. Trains may not travel on trips that do not appear on the schedule.

## Input

The first line of input gives the number of cases, **N**. **N** test cases follow.

Each case contains a number of lines. The first line is the turnaround time, **T**, in minutes. The next line has two numbers on it, **NA** and **NB**. **NA** is the number of trips from A to B, and **NB** is the number of trips from B to A. Then there are **NA** lines giving the details of the trips from A to B.

Each line contains two fields, giving the HH:MM departure and arrival time for that trip. The departure time for each trip will be earlier than the arrival time. All arrivals and departures occur on the same day. The trips may appear in any order - they are not necessarily sorted by time. The hour and minute values are both two digits, zero-padded, and are on a 24-hour clock (00:00 through 23:59).

After these **NA** lines, there are **NB** lines giving the departure and arrival times for the trips from B to A.

## Output

For each test case, output one line containing "Case #**x**: " followed by the number of trains that must start at A and the number of trains that must start at B.

## Limits

1 ≤ **N** ≤ 100

Small dataset

0 ≤ **NA**, **NB** ≤ 20

0 ≤ **T** ≤ 5

Large dataset

0 ≤ **NA**, **NB** ≤ 100

0 ≤ **T** ≤ 60

## Sample

<table>
  <tr>
    <td>
Input </td>
    <td>
Output </td>
  </tr>
  <tr>
    <td>2<br/>
5<br/>
3 2<br/>
09:00 12:00<br/>
10:00 13:00<br/>
11:00 12:30<br/>
12:02 15:00<br/>
09:00 10:30<br/>
2<br/>
2 0<br/>
09:00 09:01<br/>
12:00 12:02<br/>
</td>
    <td>Case #1: 2 2<br/>
Case #2: 2 0
</td>
  </tr>
</table>
