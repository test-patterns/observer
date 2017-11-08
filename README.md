# Observer Pattern
Sample problem featuring the observer pattern.

## Task 1 - Add a notification

Welcome to Pizza<sup>2</sup>! Our kitchen already sends notifications when a new pizza has just started cooking, and when a pizza is done, but we can't see when ingredients have been prepped. See for yourself by running the following command:

```
python observer -q 3
```

Add a new SMS notification to the sequence in main.py to send a notification when the pizza has been prepped.

### UML

![alt text](http://yuml.me/6ad6620c.png)
[edit](http://yuml.me/edit/6ad6620c)

### Previous output

```
SMS notification: The pizza just started cooking
SMS notification: The pizza is done
SMS notification: The pizza just started cooking
SMS notification: The pizza is done
SMS notification: The pizza just started cooking
SMS notification: The pizza is done
```

## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source observer -m unittest discover tests
coverage report -m
```

Increase this to 100%.
