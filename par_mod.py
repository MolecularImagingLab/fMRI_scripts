#!/usr/bin/env python
#! /home/lauri/anaconda3/bin/python

#load libraries
import os, sys
import pandas as pd

def readin():
    '''read in the first argument as input
    and the second as output '''
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    return inputfile, outputfile

def read_data(inputfile):
    '''create a pandas df from input and give header names'''
    df = pd.read_csv(inputfile, delimiter=' ', names=['onset', 'type', 'duration', 'weight'])
    return df

def change_type(df, oldtype, newtype):
    ''' Use this function to change the event type, e.g. CS+ from 2 to 3 '''
    df.loc[df['type'] ==oldtype, 'type'] = newtype
    return df

def create_int_slope(df, event1, event2):
    ''' Loop over rows, create two rows for the selected event type,
    one of these rows is intercept, the other slope,
    slope will increase by one for each new trial of this event type '''

    # create an empty df
    new_df=pd.DataFrame(columns=df.columns)

    # set slope counter to 0
    slope_counter1 = 0
    slope_counter2 = 0

    # loop over rows in df
    for index, row in df.iterrows():

        # if row is of selected event type (CS and/or CS+)
        if row.type in (event1, 3):

            # increase slope counter
            slope_counter1 += 1

            if row.type == event1:

                # set up the first row
                first_row = row
                first_row.type = 1
                new_df = new_df.append(pd.Series(first_row))

                # set up the second row
                second_row = row
                second_row.type = 2
                second_row.weight = slope_counter1
                new_df = new_df.append(pd.Series(second_row))
            else:
                # set up the first row
                first_row = row
                first_row.type = 5
                new_df = new_df.append(pd.Series(first_row))

        elif row.type == event2:

            # increase slope counter
            slope_counter2 += 1

            # set up the first row
            first_row = row
            first_row.type = 3
            new_df = new_df.append(pd.Series(first_row))

            # set up the second row
            second_row = row
            second_row.type = 4
            second_row.weight = slope_counter2
            new_df = new_df.append(pd.Series(second_row))

        # otherwise just add the row
        else:

            new_df = new_df.append(pd.Series(row))

    new_df.round(decimals=0)
    return new_df

def write_output(new_df, outputfile):
    new_df.to_csv(outputfile, header=False, index=False, sep=" ")

def main():
    inputfile, outputfile =readin()
    print('using:')
    print(inputfile)
    print('saving as:')
    print(outputfile)

    df =read_data(inputfile)
    #change_type(df, 1, 3)
    new_df =create_int_slope(df, 1, 2)
    write_output(new_df, outputfile)

if __name__ == "__main__":
# execute only if run as a script
    main()
