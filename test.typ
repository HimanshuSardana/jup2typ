
        #let question(number, body) = [
            #smallcaps()[Question #number]
            #body
        ]
        #question("1",": Write a program to find the complement of an image")
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

                    ```
                    ```python
print("Hello world")
```

                    === Output
                    ```txt
                    Hello world

                    ```
                    ```python

```
