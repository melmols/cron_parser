# pseudo code


- cron_parser:

1) a Main class of the project

2) uses cron_descriptor to translate to human readable format in string

3) create a function that uses cron_descriptor and parse the string in a way that separates the definition of minute,hour,day and month

4) create a table function, that will get the list from the cron_descriptor function, and by calling at their respective index add it to the table.

5) output: a table that describes the time definition at when the cron job will run by minute, hour,day and month

- test_cases:

call the class using an input test where the string for the cron job is inputed by the user on the terminal

benefits: no need for opt,argv or sys play
