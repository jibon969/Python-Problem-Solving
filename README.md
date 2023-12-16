<img src="img/problem-solving.png" id='header'>

<h1 align="center">Python Problem Solving </h1>

<div align="center">
<!-- Gmail Account -->
<a href="mailto:jayed.swe@gmail.com">
<img src='https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="tel:+8801987132107">
<img
src='https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white'
alt='Jayed Hossain Jibon'
/>
<a href="#" target="_blank">
<img
src='https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="https://www.facebook.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white'
alt='Jayed Hossain Jibon'
/>

<a href="https://www.linkedin.com/in/jibon969/" target="_blank">
<img
src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="https://github.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
</div>

<hr/>

<div align="center">
        <a href="https://www.programiz.com/python-programming/examples" target="_blank">Programiz
        </a>
        |
        <a href="https://pynative.com/python-basic-exercise-for-beginners/" target="_blank">PYnative</a>
        |
        <a href="https://www.geeksforgeeks.org/python-programming-examples/" target="_blank">Geeksforgeeks</a>
        |
        <a href="https://www.w3resource.com/python-exercises/" target="_blank">w3resource</a>
        |
        <a href="https://www.hackerrank.com/" target="_blank">HackerRank</a>
        |
        <a href="https://leetcode.com/" target="_blank">LeetCode</a>
</div>
<hr/>

##### 01. Print Hello world!
<details>
<summary style="cursor:pointer">Solution</summary>

```js
print("Hello World!")
```
</details>

##### 02. Add Two Numbers
```
Input: num1 = 5, num2 = 10
Output: 15
Explanation: 5 + 10 = 15

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
num1 = 5;
num2 = 10;
sum = num1 + num2;
print(sum) // Output: 15
```
</details>

##### 03. Square Root
```
Input: num1 = 5, num2 = 10
Output: 15

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
user_input = int(input("Enter your number : "))
output = user_input ** 0.5
print(output)
```
</details>

##### 04. Area of triangle
```
formula : area = 0.5 * base * height.

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)
```
</details>

##### 05. Quadratic Equation
```
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
```
</details>

##### 06. Swap Variable
```
input  : a = 5
         b = 6
output : a = 6
         b = 5
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
a = 5
b = 6
c = a + b
a = c - a
b = c - b
print(a)
print(b)
# or
a, b = b, a 
print(a)
print(b)
```
</details>

##### 07. Generate a Random Number
```
output : Random number 
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
import random
x = random.randint(1, 100)
print(x)
```
</details>


##### 08. Positive Negative or
```
input  : 10
output : Positive
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
number = 10
if number > 0:
    print("Positive")
elif number < 0:
        print("Negative")
elif number == 0:
     print("0")
```
</details>

##### 08. Positive Negative or
```
input  : 10
output : Positive
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
number = 10
if number > 0:
        print("Positive")
elif number < 0:
         print("Negative")
elif number == 0:
         print("0")
```
</details>


##### 09. Even or odd Number
```
input  : 10
output : Even number
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
number = 10
if number % 2 == 0:
    print("Even number")
else:
     print("Odd number")
```
</details>


##### 10. Check Leap Year
```
input  : 2024
output : Leap Year
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
year = int(input("Enter your your : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not leap year ")
```
</details>


##### 11. Find the Largest Among Three Numbers
```
input  : a = 5
         b = 6
         c = 10
output : C is large number
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
a =  int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))
if a > b:
    print("A is largest number")
elif b > c:
    print("B is largest number ")
elif a < c:
    print("C is largest number")
```
</details>


##### 12. Check Prime Number
```
input  : 13
output : Its Prime 
Definition :
A prime number can be defined as a natural number greater than 1
whose only factors are 1 and the number itself.
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
is_prime = int(input("Enter your number : "))
for i in range(2, is_prime):
    if is_prime % i == 0:
        print("Not a prime number ")
        break
else:
    print("Its Prime")
```
</details>


##### 13. Prime numbers within an interval
```
input  : 900, 1000
output : Its Prime 
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
```
</details>


---
**[⬆ Back to Top](#header)**
