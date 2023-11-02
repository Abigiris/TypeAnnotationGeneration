# LOGS-DEVNOTES

As of this moment (2019-10-13) the logging functionality within Rosevomit is... functional, but awkwardly implemented and probably shows just how little I know about Python. This README file exists to help document my thoughts and intentions about the logging functionality now, while it's still fresh in my head, in order for me to come back and improve everything later.

## Context

Since Rosevomit exists so I can learn Python, my goals for Rosevomit's logging functionality are ambitious - I want to be able to capture everything that happens when Rosevomit runs. This doesn't mean that I **will** log everything, but it does mean that I want to know that I can put a logging function anywhere in Rosevomit's code and know that the record it generates will be captured.

Because of how Rosevomit's logging functionality is currently implemented, some messages are generated *before* Rosevomit is ready to log messages in the output files. Right now, these messages are *not* sorted by level and are instead dumped *en masse* into the `00-buffer.log` file.

Unlike most code I've written up to this point, my implementation of the logging functionality relies on the execution of code within an `__init__` file. Specifically, Rosevomit's "root logger" that all other logs are passed to is created in the core module's `__init__` file.

## Operational details

*Copy-pasted from [Python's official documentation](https://docs.python.org/3/library/logging.html#logging-levels).*

Python's `logging` modules has four basic classes of objects.

- **Loggers** expose the interface that application code directly uses, and generate *records*.
- **Handlers** send the log records (created by loggers) to the appropriate destination.
- **Filters** provide a finer grained facility for determining which log records to output.
- **Formatters** specify the layout of log records in the final output.

Note that Loggers should NEVER be instantiated directly, but always through the module-level function `logging.getLogger(name)`. Multiple calls to `getLogger()` with the same name will always return a reference to the same Logger object.

The `name` is potentially a period-separated hierarchical value, like `foo.bar.baz` (though it could also be just plain `foo`, for example). Loggers that are further down in the hierarchical list are children of loggers higher up in the list. For example, given a logger with a name of `foo`, loggers with names of `foo.bar`, `foo.bar.baz`, and `foo.bam` are all descendants of `foo`. The logger name hierarchy is analogous to the Python package hierarchy, and identical to it if you organise your loggers on a per-module basis using the recommended construction `logging.getLogger(__name__)`. That’s because in a module, `__name__` is the module’s name in the Python package namespace.

## Logging levels

*Copy-pasted from [Python's official documentation](https://docs.python.org/3/library/logging.html).*

The numeric values of logging levels are given in the following table. These are primarily of interest if you want to define your own levels, and need them to have specific values relative to the predefined levels. If you define a level with the same numeric value, it overwrites the predefined value; the predefined name is lost.

| Value | Level |
| --- | --- |
| 50 | `CRITICAL` |
| 40 | `ERROR` |
| 30 | `WARNING` |
| 20 | `INFO` |
| 10 | `DEBUG` |
| 0 | `NOTSET` |
