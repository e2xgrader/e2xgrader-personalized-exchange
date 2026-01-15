(configuration_options)=

# Configuration Options

## Personalized Outbound

The `outbound` directory is the directory where students fetch their assignments from. If the personalized outbound is activated, students will fetch from a personalized directory. This is useful if you want to create personalized versions of an assignment for each student.

Students will fetch from `<exchange_directory>/<course_id>/outbound/<assignment_id>/<student_id>/`.

To create personalized versions of an assignment, you will need to create a directory for each student under the release version of an assignment.

Instead of having your notebooks under `release/<assignment_id>/MyNotebook.ipynb` you will need to create a directory for each student as `release/<assignment_id>/<student_id>/MyNotebook.ipynb`. These notebooks can be personalized for each student.

To activate the personalized outbound add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

# ... Other config

from e2xgrader_personalized_exchange.config import activate_exchange

activate_exchange(c)

c.Exchange.personalized_outbound = True
```

## Customizing the HTML Submission Exporter

If you use the exam exchange, the HTML exporter for the notebooks can be configured.

## Customizing the Hashcode Cell

Below you see an example of a hashcode cell:


```{image} ../images/hashcode_cell.png
:align: center
:alt: true
:class: screenshot shadow
```

The hashcode cell has three messages that can be customized:

### Messages

There are three messages in the hashcode cell that can be customized:

* The first message is the `exam_submitted_message`. The default message is `We have received your exam!`.
* The second message is the `your_hashcode_message`. The default message is `Your hashcode:`.
* The last message is the `verify_exam_message`. The default message is `Verify your exam below and then close the browser and shut down your computer`.

To modify these messages add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

# ... Other config

c.HTMLSubmissionExporter.exam_submitted_message = "Your exam was successfully submitted!"
c.HTMLSubmissionExporter.verify_exam_message = "Verify your exam below!"
c.HTMLSubmissionExporter.your_hashcode_message = "This is your hashcode:"
```

### Using Your Own Template for the Hashcode Cell

You can use a custom template for the hashcode cell. Make sure that the template is in the default template paths. To change the template add the following to your `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

# ... Other config

c.HTMLSubmissionExporter.hashcode_cell_template_name = "mytemplate.html"
```

### Using Your Own HTMLSubmissionExporter

You can also use your own custom exporter for generating the HTML version of the notebook. Make sure it inherits from either `e2xgrader_core.exporters.E2xGraderExporter` or directly from `e2xgrader_personalized_exchange.exporters.HTMLSubmissionExporter`. You can set the class in the `nbgrader_config.py`:

```python
# nbgrader_config.py

c = get_config()

# ... Other config

c.ExchangeSubmit.submission_exporter_class = MyExporterClass
```



