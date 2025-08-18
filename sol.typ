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
        #question("1",[ Write a program to find the complement of an image])
```python
import cv2

img = cv2.imread("./gray.jpeg")
print(img)

complement = 255 - img

# cv2.imwrite("complement.jpg", complement)

```
=== Output
```txt
[[[149 149 149]
  [152 152 152]
  [156 156 156]
  ...
  [ 74  74  74]
  [ 74  74  74]
  [ 74  74  74]]

 [[157 157 157]
  [159 159 159]
  [161 161 161]
  ...
  [ 74  74  74]
  [ 74  74  74]
  [ 74  74  74]]

 [[165 165 165]
  [167 167 167]
  [168 168 168]
  ...
  [ 74  74  74]
  [ 74  74  74]
  [ 74  74  74]]

 ...

 [[192 192 192]
  [192 192 192]
  [192 192 192]
  ...
  [190 190 190]
  [188 188 188]
  [187 187 187]]

 [[192 192 192]
  [192 192 192]
  [192 192 192]
  ...
  [190 190 190]
  [188 188 188]
  [187 187 187]]

 [[192 192 192]
  [192 192 192]
  [192 192 192]
  ...
  [190 190 190]
  [188 188 188]
  [187 187 187]]]

``` #question("2",[ Convert image to grayscale using
(a) Mean Threshold
(b) User-defined threshold])
```python
import cv2
import numpy as np

img = cv2.imread("./gray.jpeg", cv2.IMREAD_GRAYSCALE)
# gray_img = cv2.threshold(img, np.mean(img), 255)

```
#question("3",[ Find the output of `3+4` and the following program
```python
print("Hello World")
```])
```python
print("Hello world")
```
=== Output
```txt
Hello world

``` ```python

```
```python

```
