 #import "@preview/showybox:2.0.4": showybox

#let question(number, body) = context [
  #showybox(
    frame: (
      border-color: blue,
      title-color: blue,
      body-color: white,
    ),
    title-style: (
      color: white,
      weight: "bold",
      align: left,
      boxed-style: (
        radius: 4pt,
      ),
    ),
    title: [
      #smallcaps()[#text(size: 10pt, weight: "bold")[
          == Question #number
        ]]
    ],
  )[#body
    #v(1mm)
  ]
]
        #question("1",[ Assign and print the values 23.4, 45 and 678 to the variables `A, B, C`])
```python
A <- 23.4
B <- 45
C <- 678

cat(A, B, C)
```
=== Output
```txt
23.4 45 678
``` #question("2",[ Display the entire variables you have created on the screen])
```python
ls()
```
=== Output
```txt
[1] "A" "B" "C"
``` #question("3",[ Remove the variable `C` and display the list.])
```python
rm(C)
ls()
```
=== Output
```txt
[1] "A" "B"
``` #question("4",[ Create a comment "I am learning R"])
```python
# I am learning R
```
#question("5",[ Create strings firstname and lastname as "MyName" and "MySurname"])
```python
firstname <- "MyName"
lastname <- "MySurname"
```
#question("6",[ Create the variable that can hold a value `0` or `1`])
#question("7",[ Perform the operation as +, -, \* and / on variables `A, B, C` together.])
```python
C <- 678 # since it was deleted earlier
cat(A+B-C, "\n")
cat(A*B/C)
```
=== Output
```txt
-609.6 
1.553097
``` #question("8",[ Apply the following functions on some values `exp()`, `log()`, `log10()`, `log2()`, `pi`, `sqrt()`.])
```python
cat(exp(5), "\n")
cat(log(A), "\n")
cat(log10(B), "\n")
cat(log2(C), "\n")
cat(pi, "\n")
cat(sqrt(25))
```
=== Output
```txt
148.4132 
3.152736 
1.653213 
9.405141 
3.141593 
5
``` #question("9",[ Write the statements to solve the following expressions:
1. $23 + (4.5 \* 2.3) / 10$
2. $456/12 - log(90)$
3. $exp(5) + 12/(5^6)$
4. $sqrt(45)\*12/3$])
```python
cat(23 + (4.5 * 2.3) / 10, "\n")
cat(456/12 - log(90), "\n")
cat(exp(5) + 12/(5^6), "\n")
cat(sqrt(45)*12/3, "\n")
```
=== Output
```txt
24.035 
33.50019 
148.4139 
26.83282 

``` ```python

```
