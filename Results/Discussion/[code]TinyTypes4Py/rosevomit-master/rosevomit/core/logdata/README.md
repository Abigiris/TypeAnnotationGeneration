# logdata/ README

If enabled in the 'settings-data.ini' file, Rosevomit will generate messages as it runs. The messages are displayed in the following format:

````text
    <DATE> <TIME> <LOGGER NAME> @ <FILE>:<LINE> - <LEVEL> - <FUNCTION>:<MESSAGE>
````

where `<DATE>` is the date in 'YYYY-MM-DD' format, `<TIME>` is the time in 'HH:MM:SS,milliseconds' format, `<LOGGER NAME>` is the name of the logger that generated the message (which should be the `__name__` of the file where the logger was initialized), `<FILE>` and `<LINE>` is the file name and line number where the message was generated, `<LEVEL>` is the priority level that the message was generated at, `<FUNCTION>` is the name of the function that the message was generated inside, and `<MESSAGE>` is the actual message that was generated.

## Levels

Each message generated is given a "level" of significance. These levels are (in ascending order of significance) debug, info, warning, error, or critical.

| Value | Level | Meaning |
| --- | --- | --- |
| 50 | `CRITICAL` | A **critical** message is one containing information necessary for understanding all other messages. Startup and shutdown times, for instance, are considered critical messages. |
| 40 | `ERROR` | An **error** message is one that contains information about an error - something unexpected that has happened. An error may or may not end the program prematurely, but it certainly impairs functionality in some way. |
| 30 | `WARNING` | A **warning** message is a message containing information about an error that Rosevomit encountered but was able to handle through some sort of contingency procedure. |
| 20 | `INFO` | An **info** message contains information about the routine operation/activity of the program. While not directly related to an error, this level may be useful for determining the context of an error. |
| 10 | `DEBUG` | A **debug** message contains information about a low-importance program activities that will likely never be relevant except when tracking down a particularly stubborn bug. |
| 0 | `NOTSET` | This message's level has not been set. (This should never happen.) |

## Output files

When these messages are generated, they are placed in one or more files in this directory. All of these files end with the `.log` file extension to indicate their purpose, and should be able to be opened with most text editors. The possible output files are

````text
00-buffer.log
10-debug.log
20-info.log
30-warning.log
40-error.log
50-critical.log
````

The `debug`, `info`, `warning`, `error`, and `critical` files each contain all the messages that were generated at their respective levels or higher. This means that warning messages, for example, should be printed to `30-warning.log`, `20-info.log`, and `10-debug.log`.

Because of how Rosevomit's logging functionality is currently implemented, some messages are generated *before* Rosevomit is ready to log messages in the output files. Right now, these messages are *not* sorted by level and are instead dumped *en masse* into the `00-buffer.log` file.
