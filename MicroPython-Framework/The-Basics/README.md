# MicroPython Code Basics

## 1. Hello World:

```python
print("Hello, MicroPython!")
```

## 2. Variables and Data Types:

```python
# Integer
x = 10
# Float
y = 3.14
# String
name = "MicroPython"
# Boolean
is_enabled = True
```

## 3. Control Structures:

```python
# If statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
elif temperature < 10:
    print("It's cold outside!")
else:
    print("The weather is pleasant.")

# For loop
for i in range(5):
    print("Count:", i)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

## 4. GPIO Control:

```python
import machine
import time

# Configure GPIO pin
led_pin = machine.Pin(2, machine.Pin.OUT)

# Toggle LED
while True:
    led_pin.value(not led_pin.value())
    time.sleep(1)
```

## 5. File Operations:

```python
# Write to a file
with open("data.txt", "w") as file:
    file.write("Hello from MicroPython!")

# Read from a file
with open("data.txt", "r") as file:
    content = file.read()
    print("File content:", content)
```
