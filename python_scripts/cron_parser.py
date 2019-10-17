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
import sys

#for creating a nice result_table
import plotly.graph_objects as go

class cron_parser_class:

    @staticmethod
    def usage():
        '''Quick example for getting started'''
        print ('Example usage: ')
        print ('Enter Cron expresion: */15 0 1,15 * 1-5 ')
        print ('Enter job you wish to run: : /usr/bin/find')

        sys.exit(0)


    def cron_translate(self,cron_slices):
        '''Translates cron job into human redable'''

        raw_result = get_description(cron_slices)
        final_result = [x.strip() for x in raw_result.split(',')]

        return final_result

    def result_table(self,cron_slices):
        ''' Make a pretty nice output table of each cron slice'''
        result = self.cron_translate(cron_slices)

        minute = str(result[0])
        hour   = str(result[1])
        month  = str(result[2])
        day    = str(result[3])

        #Create a DataFrame
        #data = [['minute', minute],['hour', hour],['day of the month'], [month,'day', day]]

        #df = pd.DataFrame(set(data),columns=['Time','meaning'])

        #create pretty table

        fig = go.Figure(data=[go.Table(header=dict(values=['minute', 'hour','month','day']),
                 cells=dict(values=[[minute], [hour],[month],[day]]))
                     ])
        return fig.show()
