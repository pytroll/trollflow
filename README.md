TrollFlow
=========


Trollflow is a small workflow execution framework inspired by the Modelling Workflow Engine MWE2 (http://www.eclipse.org/Xtext/documentation.html#MWE2).

It executes flows of loosely coupled software components. A component is created by subclassing workflow_component.AbstractWorkflowComponent and implementing at least an invoke() method.

The main scprit to invoke is `bin/flow_processor.py`. There are some workflow examples under the `examples/` directory.

Trollflow plugins for satellite image processing can be found in the Trollflow-sat package (https://github.com/pytroll/trollflow-sat).

TODO
----
  * documentation
  * clean obsolete files
  * simplify internal structure
