# e2xgrader-personalized-exchange

The e2xgrader personalized exchange provides an nbgrader exchange for personalized submissions. The exchange is based on the original nbgrader file-based exchange and extends it with the following features:

* **Personalized `inbound` and `feedback` directories** for each student, to prevent students from accessing each other's submissions and feedback (Activated by default).
* **Personalized `outbound` directory** for each student, to provide personalized versions of an assignment. If activated, each student gets their own version of the assignment (Deactivated by default).
* **Custom submit behavior in exam mode**. In exam mode the submissions are hashed and a HTML version of each notebook is produced on submit, including the hashcode and timestamp and a custom submit message.

## Installation

The e2xgrader personalized exchange can be installed from source via:

```bash
pip install git+https://github.com/e2xgrader/e2xgrader-personalized-exchange
```

## Quick Start

### Basic Exchange

In the basic exchange each student gets a custom submit and feedback directory. No hashing of the submissions is performed and no html version of each notebook is created.

To activate the basic exchange in nbgrader, add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

from e2xgrader_personalized_exchange.config import activate_exchange

activate_exchange(c)

# Set the root of the exchange
c.Exchange.root = "<path_to_your_exchange_directory>"
```

### Exam Exchange

The exam exchange extends the basic exchange by hashing student submissions and creating a HTML version of each notebook in the assignment directory. A cell containing the hashcode, timestamp and a custom submit message is added to the HTML.

To activate the exam exchange in nbgrader, add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

from e2xgrader_personalized_exchange.config import activate_exam_exchange

activate_exam_exchange(c)

# Set the root of the exchange
c.Exchange.root = "<path_to_your_exchange_directory>"
```

## Configuration

### Personalized Outbound

The `outbound` directory is the directory where students fetch their assignments from. If the personalized outbound is activated, students will fetch from a personalized directory. This is useful if you want to create personalized versions of an assignment for each student.

To activate the personalized outbound add the following to your `nbgrader_config.py`:

```python
c.Exchange.personalized_outbound = True
```

### Customizing the HTML Submission Exporter

If you use the exam exchange, the HTML exporter for the notebooks can be configured:

```python
c.HTMLSubmissionExporter.exam_submitted_message = "Your exam was successfully submitted!"
c.HTMLSubmissionExporter.verify_exam_message = "Verify your exam below!"
c.HTMLSubmissionExporter.your_hashcode_message = "This is your hashcode:"
```

## Documentation

For more detailed documentation, see the [full documentation](docs/source/index.md).
