TrollFlow
=========


Trollflow is a small workflow execution framework inspired by the Modelling Workflow Engine MWE2 (http://www.eclipse.org/Xtext/documentation.html#MWE2).

It executes flows of loosely coupled software components. A component is created by subclassing workflow_component.AbstractWorkflowComponent and implementing at least an invoke() method. Each component is holdong slots to to exchange data and information with its environment.

Worklflows are currently just json files. Examples for workflows can be found under /test



Trollflow is currently under development. The easiest way to try and run it is adding trollflow to your virtual environment.

With virtualenvwrapper: add2virtualenv /path/to/trollflow
And run it: python workflow/workflow_launcher.py /path/to/workflow.json



TODO
----

  * create a setup.py
  * include tests
  * better documentation
