# [Problem C. Fly Swatter](https://code.google.com/codejam/contest/32013/dashboard#s=p2)

This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the [Quick-Start Guide](https://code.google.com/codejam/resources/quickstart-guide#gcj) to get started.

<table>
  <tr>
    <td>Small input
5 points</td>
    <td>Solve C-small</td>
  </tr>
  <tr>
    <td>Large input
20 points</td>
    <td>Solve C-large</td>
  </tr>
</table>


## Problem

What are your chances of hitting a fly with a tennis racquet?

To start with, ignore the racquet's handle. Assume the racquet is a perfect ring, of outer radius **R** and thickness **t** (so the inner radius of the ring is **R**−**t**).

The ring is covered with horizontal and vertical strings. Each string is a cylinder of radius **r**. Each string is a chord of the ring (a straight line connecting two points of the circle). There is a gap of length **g** between neighbouring strings. The strings are symmetric with respect to the center of the racquet i.e. there is a pair of strings whose centers meet at the center of the ring.

The fly is a sphere of radius **f**. Assume that the racquet is moving in a straight line perpendicular to the plane of the ring. Assume also that the fly's center is inside the outer radius of the racquet and is equally likely to be anywhere within that radius. Any overlap between the fly and the racquet (the ring or a string) counts as a hit.

![img](https://github.com/xiaoyaoliu/CodeJam/blob/master/GoogleCodeJam/2008/Qualification_Round.C.Fly_Swatter/image_0.png)

## Input

One line containing an integer **N**, the number of test cases in the input file.

The next **N** lines will each contain the numbers **f**, **R**, **t**, **r** and **g** separated by exactly one space. Also the numbers will have at most 6 digits after the decimal point.

## Output

**N** lines, each of the form "Case #**k**: **P**", where **k** is the number of the test case and **P** is the probability of hitting the fly with a piece of the racquet.

Answers with a relative or absolute error of at most 10-6 will be considered correct.

## Limits

**f**, **R**, **t**, **r** and **g** will be positive and smaller or equal to 10000.

**t** < **R**

**f** < **R**

**r** < **R**

Small dataset

1 ≤ **N** ≤ 30

The total number of strings will be at most 60 (so at most 30 in each direction).

Large dataset

1 ≤ **N** ≤ 100

The total number of strings will be at most 2000 (so at most 1000 in each direction).

## Sample

<table>
  <tr>
    <td>
Input </td>
    <td>
Output </td>
  </tr>
  <tr>
    <td>5<br/>
0.25 1.0 0.1 0.01 0.5<br/>
0.25 1.0 0.1 0.01 0.9<br/>
0.00001 10000 0.00001 0.00001 1000<br/>
0.4 10000 0.00001 0.00001 700<br/>
1 100 1 1 10<br/>
</td>
    <td>Case #1: 1.000000<br/>
Case #2: 0.910015<br/>
Case #3: 0.000000<br/>
Case #4: 0.002371<br/>
Case #5: 0.573972<br/>
</td>
  </tr>
</table>
