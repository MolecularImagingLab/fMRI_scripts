#!/usr/bin/env python

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
            args.filename, args.title, args.class1, args.levels1, args.class2, args.levels2, args.variable1, args.variable2, args.subjectnum,))
    
    #writes csv file
    #open file
    with open(args.filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=" ")
        #first row
        writer.writerow(["GroupDescriptorFile","1"])
        #second row
        writer.writerow(["Title", args.title])
        #Class rows
        if args.levels2 != "none":
            levels1 = (args.levels1).split(",")
            levels2 = (args.levels2).split(",")
            writer.writerow(["Class",str(levels1[0])+str(levels2[0])])
            writer.writerow(["Class",str(levels1[0])+str(levels2[1])])
            writer.writerow(["Class",str(levels1[1])+str(levels2[0])])
            writer.writerow(["Class",str(levels1[1])+str(levels2[1])])
        else:
            levels1 = (args.levels1).split(",")
            for factor in levels1:
                writer.writerow(["Class", factor])
        # Variables row
        if args.variable1 != "none":
            writer.writerow(["Variables", args.variable1])
        elif args.variable2 != "none":
            writer.writerow(["Variables", args.variable1, args.variable2])
        else:
            pass
        #Subjects data
        inputs=[[args.class1],[args.class2],[args.variable1],[args.variable2]]
        for subject in range(1,(args.subjectnum+1)):
            name = os.path.join("subject"+str(subject))
            gather = ["Input", name]
            for i in inputs:  
                if i != ["none"]:
                    datum = input(f"Input data for {name} in {i}:")
                    gather.append(datum)
            if args.class2 != "none":
                try:
                    writer.writerow(["Input", name, str(gather[2] + gather[3]), str(gather[4] + ""), str(gather[5] + "")])
                except:
                    writer.writerow(["Input", name, str(gather[2] + gather[3]), str(gather[4] + "")])
            else:
                writer.writerow(gather)
        #Notification                         
        PWD = str(os.getcwd())
        print(f"FSGD file sucessfully saved in {PWD}")
if __name__ == "__main__":
    # execute only if run as a script
    main()

