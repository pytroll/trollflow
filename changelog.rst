Changelog
=========


v0.6.0 (2018-08-23)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.5.2 → 0.6.0. [Panu Lahtinen]
- Merge pull request #2 from pytroll/develop. [Panu Lahtinen]

  Add Python 3 support
- Merge pull request #1 from pytroll/feature-python3-support. [Panu
  Lahtinen]

  Python 3 compatibility
- Change print statements to functions, fix exceptions. [Panu Lahtinen]
- Remove mpop examples as there's no Python 3 support. [Panu Lahtinen]
- Use six to import queue, cast dict_items to tuple. [Panu Lahtinen]
- Delete potentially large internal variables to reduce memory use.
  [Panu Lahtinen]


v0.5.2 (2017-10-26)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.5.1 → 0.5.2. [Panu Lahtinen]
- Rename to more descriptive filename. [Panu Lahtinen]
- Update example to match current package structures. [Panu Lahtinen]
- Update readme. [Panu Lahtinen]


v0.5.1 (2017-08-15)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.5.0 → 0.5.1. [Panu Lahtinen]
- Fix PyYAML case as dependency in setup.cfg. [Martin Raspaud]


v0.5.0 (2017-04-04)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.4.0 → 0.5.0. [Panu Lahtinen]
- Fix restarting crashed workers/daemons. [Panu Lahtinen]
- Catch ValueError. [Panu Lahtinen]
- Add "flush_queue" kwarg. [Panu Lahtinen]

  When setting flush_queue=False, the queued items can be kept when
  restarting worker

- If previous worker died, release its lock. [Panu Lahtinen]

  NOTE: this need to be done so that all the downstream workers have
  finished working so that there won't be synchronisation issues

- Clarify log message. [Panu Lahtinen]
- Remove exception handling for MemoryError. [Panu Lahtinen]

  In this way the thread "watchdog" can restart the worker without losing
  all the existing items in the queues

- Find dead workers only when not shutting down. [Panu Lahtinen]
- Use also old output queues so possibly existing data are kept. [Panu
  Lahtinen]
- Recreate dead threads, reconnect queues and locks. [Panu Lahtinen]


v0.4.0 (2017-03-21)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.3.2 → 0.4.0. [Panu Lahtinen]
- Add optional forced garbage collection. [Panu Lahtinen]


v0.3.2 (2017-03-07)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.3.1 → 0.3.2. [Panu Lahtinen]
- Add missing import. [Panu Lahtinen]
- Use UTC timestamps in log files by default. [Panu Lahtinen]
- Catch MemoryError. [Panu Lahtinen]
- Fix finally/except misuse. [Panu Lahtinen]
- Make loop exit cleaner. [Panu Lahtinen]
- Catch all errors, not only KeyboardInterrupt. [Panu Lahtinen]
- Daemonize all worker threads. [Panu Lahtinen]


v0.3.1 (2017-02-28)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.3.0 → 0.3.1. [Panu Lahtinen]
- Make views lists so that also Python 3 should work. [Panu Lahtinen]


v0.3.0 (2017-02-28)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.2.0 → 0.3.0. [Panu Lahtinen]
- Merge branch 'master' into develop. [Panu Lahtinen]
- Merge branch 'release-0.2.0' [Panu Lahtinen]
- Merge branch 'release_0.1.0' [Panu Lahtinen]
- Remove tests dependencies. [Panu Lahtinen]
- Fix test requirement. [Panu Lahtinen]
- Change RLock to Lock, adjust tests. [Panu Lahtinen]
- Make import Python3 compatible. [Panu Lahtinen]
- Fix syntax by adding install group. [Panu Lahtinen]
- Move stremere init to setUp(), test stop() [Panu Lahtinen]
- Fix typos, add placeholders for testin start() and stop() [Panu
  Lahtinen]
- Add pyyaml to test requirements. [Panu Lahtinen]
- Add test_workflow_streamer, test WorkflowStreamer.__init__ [Panu
  Lahtinen]
- Add tests for workflow_component. [Panu Lahtinen]
- Remove unused import. [Panu Lahtinen]
- Adjust docstring, remove unused import. [Panu Lahtinen]
- Add tests for trollflow.utils. [Panu Lahtinen]
- Enable tests. [Panu Lahtinen]
- Remove unused function. [Panu Lahtinen]
- Make tests a package. [Panu Lahtinen]
- Add travis config. [Panu Lahtinen]
- Move lock acquire/release from trollflow_sat. [Panu Lahtinen]
- Remove redefinition of items at each run, use Rlock instead of Lock.
  [Panu Lahtinen]
- Remove unnecesary "content" dictionary. [Panu Lahtinen]
- Move locking from WorkflowComponent to WorkflowStreamer. [Panu
  Lahtinen]
- Adjust lock messages. [Panu Lahtinen]
- Handle workers without locking. [Panu Lahtinen]
- Fix lock name, fix typo in function name. [Panu Lahtinen]
- Catch ThreadError if releasing unlocked lock. [Panu Lahtinen]
- Create local lock at init time, set use_lock to False by default.
  [Panu Lahtinen]
- PEP8 and remove obsolete stuff. [Panu Lahtinen]
- Add locks. [Panu Lahtinen]
- Add missing file. [Panu Lahtinen]
- Remove obsolete files. [Panu Lahtinen]
- Add a methods to stop workers and get data from workers. [Panu
  Lahtinen]
- Add serial processing. [Panu Lahtinen]
- Rename create_workers() to create_threaded_workers() [Panu Lahtinen]
- Remove broken "serial" workflow generator, rename run() to wait()
  [Panu Lahtinen]
- Remove extra layer of threading. [Panu Lahtinen]
- Make sure all the queued items have been marked as done. [Panu
  Lahtinen]
- Apply task_done() after data is read from the input queue. [Panu
  Lahtinen]
- Add main, cleanup, pep8. [Panu Lahtinen]
- Remove unused import, fix config reader to use the argument. [Panu
  Lahtinen]
- Remove unused import. [Panu Lahtinen]
- Merge branch 'develop' of https://github.com/pytroll/trollflow into
  develop. [Panu Lahtinen]
- Add ordered load, restructure code, add serial processing. [Panu
  Lahtinen]


v0.2.0 (2016-11-22)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.1.0 → 0.2.0. [Panu Lahtinen]
- Fix order of functions and dict using them. [Panu Lahtinen]
- Add docstrings. [Panu Lahtinen]
- Clean main() to separate functions. [Panu Lahtinen]
- Fix style warnings, remove unused imports. [Panu Lahtinen]


v0.1.0 (2016-11-15)
-------------------
- Update changelog. [Panu Lahtinen]
- Bump version: 0.0.1 → 0.1.0. [Panu Lahtinen]
- Initial commit. [Panu Lahtinen]
- Remove test requirements for now. [Panu Lahtinen]
- Set execute bit. [Panu Lahtinen]
- Adjust requirements. [Panu Lahtinen]
- Adjust install requirements, add installable scripts. [Panu Lahtinen]
- Change directory name. [Panu Lahtinen]
- Convert from json to YAML. [Panu Lahtinen]
- Move WorkflowStreamer to own file. [Panu Lahtinen]
- Reorganize imports. [Panu Lahtinen]
- Reorganize imports, rewrap lines, delete obsolet files. [Panu
  Lahtinen]
- Move to bin, update from trollduction. [Panu Lahtinen]
- Remove generate_workflow.py from installed scripts, as it was moved to
  trollduction. [Panu Lahtinen]
- Change segment gatherer to use yaml config. [Panu Lahtinen]
- Add SegmentGatherer (.ini variant) [Panu Lahtinen]
- Fix logging from daemon threads. [Panu Lahtinen]
- Expose more arguments as config options. [Panu Lahtinen]
- Add logging and log config. [Panu Lahtinen]
- Add log config, add writer. [Panu Lahtinen]
- Add configuration for pansharpener, give better names for workflows.
  [Panu Lahtinen]
- Remove unnecessary error handling. [Panu Lahtinen]
- Add input and output queues to context, remove hard-coded items. [Panu
  Lahtinen]
- Move queue initial value to correct place. [Panu Lahtinen]
- Add all working trollduction plugins. [Panu Lahtinen]
- Work on workflowstreamer. [Martin Raspaud]
- Add first draft of trollduction flow. [Martin Raspaud]
- Test example runs with YAML. [Martin Raspaud]
- YAML example configs. [Panu Lahtinen]
- Fix import. [Panu Lahtinen]
- Change file modes to executable. [Panu Lahtinen]
- Fix import, add main(), pep8. [Panu Lahtinen]
- Separate versions for JSON and YAML config files. [Panu Lahtinen]
- Fix import, fix usage of reserved names, pep8. [Panu Lahtinen]
- Make examples a package. [Panu Lahtinen]
- Pep8. [Panu Lahtinen]
- Add example packages to install list. [Panu Lahtinen]
- Fix syntax error. [Panu Lahtinen]
- Add workflow_launcher.py to the list of installed scripts. [Panu
  Lahtinen]
- Move main() to bin/ [Panu Lahtinen]
- Move the main() to bin directory. [Panu Lahtinen]
- Restructure directory structure. [Panu Lahtinen]
- Add version file. [Panu Lahtinen]
- Modify to reflect the new directory structure. [Panu Lahtinen]
- Add gitignore. [Panu Lahtinen]
- Create setup for trollflow. [Panu Lahtinen]
- Remove java stuff. [Martin Raspaud]
- Removed empty module. [HelgeDMI]
- Removed an unnecessary module from the example workflows. [HelgeDMI]
- Now there is a component finder returning components in a search path.
  Furthermore, there is an initial version of a documenter module, which
  generates a visualisation of the dataflow in a workflow. The generated
  graph is currently incomplete. This is fixed in a next commit.
  [HelgeDMI]
- Added missing files for second example. [HelgeDMI]
- Initial commit. [HelgeDMI]


