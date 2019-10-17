#References:
## https://github.com/bradymholt/cron-expression-descriptor
## https://gitlab.com/doctormo/python-crontab
#License: MIT,
#Author: Melmols

## 17/10/2019
## Description:
#parsers a cron string and expands each fields to show the times at
#which it will run

#libs

#cron translator to human readable
from cron_descriptor import get_description, ExpressionDescriptor

class cron_parser:
    def usage():
          print 'Example usage: '
          print 'python %s */15 0 1,15 * 1-5 /usr/bin/find' % sys.argv[0]

          sys.exit(0)

    def cron_translate(cron_slice):
        '''Translates cron job into human redable'''

        raw_result = get_description(cron_slice)
        final_result = [x.strip() for x in raw_result.split(',')]

        return final_result

def start_test_input():
    ''' User interaction demo'''

    cron_exp = raw_input('Enter Cron Expression: ')
    job_name = raw_input('Enter job you wish to run: ')

    try:
        print ('The job: %s will run: ' %job_name)
        print (cron_translate(cron_exp))
    except Exception as e: print(e)



if __name__ == "__main__":

    start_test_input()
