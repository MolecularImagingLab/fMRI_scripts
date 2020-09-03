#!/usr/bin/env python
# coding: utf-8

# In[11]:


def main():
    #load libraries
    import argparse
    import csv
    import os
    
    #load parser
    parser = argparse.ArgumentParser()
    #--file, --title, --class1, --levels1 --class2, --levels2, --variable1 --variable2 --subjectnum
    parser.add_argument("-f", "--file", dest = "filename", default = "fsgd.csv", type= str, help="File name.")
    parser.add_argument("-t", "--title", dest = "title", default = "FSGD", type= str, help="Title of FSGD file.")
    parser.add_argument("-c1", "--class1",dest ="class1", required = True, type= str, help="Class 1 name.")
    parser.add_argument("-l1", "--levels1",dest = "levels1", required = True, type= str, help="Specify levels for class 1. E.g. M,F")
    parser.add_argument("-c2", "--class2",dest = "class2", default = "none", type= str, help="Class 2 name.")
    parser.add_argument("-l2", "--levels2",dest = "levels2", default = "none", type= str, help="Specify levels for class 2. E.g. M,F")
    parser.add_argument("-v1", "--variable1",dest = "variable1", default = "none", type= str, help="Variable 1 name.")
    parser.add_argument("-v2", "--variable2",dest = "variable2", default = "none", type= str, help="Variable 2 name.")
    parser.add_argument("-s", "--subjectnum",dest = "subjectnum", required = True, type= int, help="Enter the number of subjects.")
    #load arguments
    args = parser.parse_args()
    #print parsed arguments
    print( "filename {} title {} class1 {} levels1 {} class2 {} levels2 {} variable1 {} variable2 {} subjectnum {}".format(
            args.filename,
            args.title,
            args.class1,
            args.levels1,
            args.class2,
            args.levels2,
            args.variable1,
            args.variable2,
            args.subjectnum,
            ))
    
    #writes csv file
    #open file
    with open(args.filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=" ")
        #first row
        writer.writerow(["GroupDescriptorFile","1"])
        #second row
        writer.writerow(["Title", args.title])
        #Class 1 rows
        levels1 = (args.levels1).split(",")
        if len(levels1) == 1:
            writer.writerow(["Class", levels1])
        else:
            for factor in levels1:
                writer.writerow(["Class", factor])
        #Class 2 rows
        if args.levels2 != "none":
            levels2 = (args.levels2).split(",")
            for factor in levels2:
                writer.writerow(["Class", factor])
        else:
            pass
        writer.writerow(["Variables", args.variable1, args.variable2])
        #Subjects data
        for subject in range(1,(args.subjectnum+1)):
            name = os.path.join("subject"+str(subject))
            if args.levels2 != "none": 
                input1= input(f"Input data for {name} in {args.class1}:")
                input2= input(f"Input data for {name} in {args.class2}:")
                input3= input(f"Input data for {name} in {args.variable1}:")
                input4= input(f"Input data for {name} in {args.variable2}:")
                writer.writerow(["Input", name, input1, input2, input3, input4])
            else:
                input1= input(f"Input data for {name} in {args.class1}:")
                input3= input(f"Input data for {name} in {args.variable1}:")
                input4= input(f"Input data for {name} in {args.variable2}:")
                writer.writerow(["Input", name, input1, input3, input4])
        PWD = str(os.getcwd())
        print(f"FSGD file sucessfully saved in {PWD}")
if __name__ == "__main__":
    # execute only if run as a script
    main()

