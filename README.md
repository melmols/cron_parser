# cron_parser


### Cron parser class for translating cron syntax to human readable format. Functions available in the class are:

- cron_translate: which translate the cron syntax to a string definition in human readable format
- result_table: takes advantage of the output of cron_translate and parses the result into a nice table


### Examples

A demo called: demo_userinput is available. It imports the class cron_parser and takes the following arguments in user input format from the terminal:

- cron_exp: cron expression to translate
- job_name: the name of the job you wish to run

it will then output a table containing minute, hour, day and month information in regards to when the job will be run.

## Installation
  pip3 install -r python/requirements.txt
  
## Example usange

  python demo_userinput.py

### future work

- Create different demos with different user interaction and input.
-`Create better exceptions and error tests.
