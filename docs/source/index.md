# e2xgrader-personalized-exchange

The e2xgrader personalized exchange provides an nbgrader exchange for personalized submissions.
The exchange is based on the original nbgrader file-based exchange and extends it with the following features:

* Personalized `inbound` and `feedback` directories for each student, to prevent students from accessing each other`s submissions and feedback (Activated by default).
* Personalized `outbound` directory for each student, to provide personalized verisons of an assignment. If activate, each student gets their own version of the assignment (Deactivated by default).
* Custom submit behavior in exam mode. In exam mode the submissions are hashed and a HTML version of each notebook is produced on submit, including the hashcode and timestamp and a custom submit message.

```{toctree}
:maxdepth: 2

getting_started/installation
getting_started/activate_exchange
configuration/configuration_options
```