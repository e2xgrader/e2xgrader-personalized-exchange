(activate_exchange)=

# Activating the Exchange

There are two versions of the exchange.

## Basic Exchange

In the basic exchange each student gets a custom submit and feedback directory. No hashing of the submissions is performed and no html version of each notebook is created.

To activate the basic exchange in nbgrader, add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

# ... Other config

from e2xgrader_personalized_exchange.config import activate_exchange

activate_exchange(c)

# Set the root of the exchange

c.Exchange.root = "<path_to_your_exchange_directory>"
```

## Exam Exchange

The exam exchange extends the basic exchange by hashing student submissions and creating a HTML version of each notebook in the assignment directory. A cell containing the hashcode, timestamp and a custom submit message is added to the HTML. The following files are created during submit:

```
<assignment>/
├── <username>_info.txt
├── <notebook>_hashcode.html
├── SHA1SUM.txt
└── <notebook>.ipynb
```

* `<username>_info.txt`: Contains the username, hashcode and timestamp of the submission.
* `<notebook>_hashcode.html`: Generated for each notebook in the assignment. Contains a cell containing the hashcode, timestamp and a custom submit message at the top.
* `SHA1SUM.txt`: Stores SHA1-hash values for each file of the assignment (excluding generated files).
* `<notebook>.ipynb`: The notebook file for each notebook in the assignment.

To activate the exam exchange in nbgrader, add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

# ... Other config

from e2xgrader_personalized_exchange.config import activate_exam_exchange

activate_exam_exchange(c)

# Set the root of the exchange

c.Exchange.root = "<path_to_your_exchange_directory>"
```