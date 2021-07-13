import sys
import parsedf

import quantstats as qs

if __name__ == "__main__":

    # Ingest baseline.csv and strategy.csv
    qs_baseline_csv = sys.argv[1] #required: .csv
    qs_strat_csv = sys.argv[2] #required: .csv
    qs_strat_name = sys.argv[3] #required: string
    qs_base_name = sys.argv[4] #required: string

    # Define 'date' or 'timestamp' for parse_df timedate
    date = 'date'
    filename_output = qs_strat_name + 'vs' + qs_base_name + '.html'

    qs_base_strat = parsedf.parse_df(qs_baseline_csv, date)
    qs_strat = parsedf.parse_df(qs_strat_csv, date)

    #extend pandas functionality with metrics, etc.
    qs.reports.html(qs_base_strat['pct_change'], qs_strat['pct_change'], output=filename_output)
    # report
    qs.reports.full(qs_base_strat['pct_change'], qs_strat['pct_change'])
