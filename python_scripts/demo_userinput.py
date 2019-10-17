#this is a demo example for running cron_parser.py


#importing class cron_parser

from cron_parser import cron_parser_class

def test_with_input():
    ''' User interaction demo'''
    cp = cron_parser_class()

    cron_exp = input('Enter Cron expression: ')
    job_name = input('Enter job you wish to run: ')

    try:
        print ('The job: %s ' %job_name)
        print ('Will run as follows: ')
        print (cp.result_table(cron_exp))
    except Exception as e:
        print(e)
        cron_parser_class.usage()



if __name__ == "__main__":

    test_with_input()

