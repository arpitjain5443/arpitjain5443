# Add Record
# Display Record
# Search by Roll no.
# Search By Name
# Exit

import pickle
import os

def add_record():
    try:
        if os.path.isfile("stud"):
            f = open("stud", "ab")
        else:
            f = open("stud","wb")
        # Roll no input
        while True:
            z = 0
            roll = input("Enter roll no (4 Digit):- ")
            if not roll.isdigit():
                print(" Roll no Has to be numeric ")
                input("Press enter to input again ")
                z = 1
                continue
            if not(int(roll)>=1000 and int(roll)<=9999):
                print("Roll no has to be 4 digits ")
                input("Press enter to input again ")
                z = 1
                continue
            if z!=1:
                break
            # Nmae input
        while True:
            z = 0
            name = input("Enter name ")
            if not name.isalpha():
                print("Name has to be alphabet ")
                input("Press enter to input again")
                z = 1
                continue
            if z != 1:
                break

        # Per input
        while True:
            z=0
            per =  input("Enter per ")
            if not per.isdigit():
                print("Per has to be numeric ")
                input("Press Enter to input again.. ")
                z = 1
                continue
            if not (float(per)>=0 and float(per)<=100):
                print("Per Has to be 100 or under 100 ")
                z=1
                continue
            if z!=1:
                break
        rec = [int(roll),name.upper(),float(per)]
        pickle.dump(rec,f)
        print("Record has been added in file ")
    except EOFError:
        f.close()

def std_display():
    try:
        f = open("stud","rb")
        print(" - "*20)
        print(" "*21,"Student Details")
        print(" - "*20)
        print("="*60)
        print("%-20s" % "Roll", "%-20s" % "Name", "%-20s" % "Per")
        print("=" * 60)
        while True:
            rec = pickle.load(f)
            print("%-20s" % rec[0], "%-20s" % rec[1], "%-20s" % rec[2])
    except EOFError:
        f.close()
        print("="*60)
    except IOError:
        print("Unable to open file")


def search_roll():
    try:
        z = 0
        tr = int(input("Enter roll no to search "))
        f = open("stud", "rb")
        # print("Roll","Name","Per")
        print( " - " * 20)
        print(" " * 23, "Student Details")
        print(" - " * 20)
        print("=" * 60)
        print("%-20s" % "Roll", "%-20s" % "Name", "%-20s" % "Per")
        print("=" * 60)
        while True:
            rec = pickle.load(f)
            if rec[0] == tr:
                z = 1
                # print(rec[0],rec[1],rec[2])
                print("%-20s" % rec[0], "%-20s" % rec[1], "%-20s" % rec[2])

    except EOFError:
        f.close()
        if z == 0:
            print("Record not found")
        print("=" * 60)
    except IOError:
        print("Unable to open the file")

def search_name():
    try:
        z = 0
        na = input("Enter Name to search ")
        na = na.upper()
        f = open("stud", "rb")
        print(" - " * 20)
        print(" " * 23, "Student Details")
        print(" - " * 20)
        print("=" * 60)

        print("%-20s" % "Roll", "%-20s" % "Name", "%-20s" % "Per")
        print("=" * 60)

        while True:
            rec = pickle.load(f)
            if rec[1].upper() == na.upper():
                z = 1
                print("%-20s" % rec[0], "%-20s" % rec[1], "%-20s" % rec[2])

    except EOFError:
        f.close()
        if z == 0:
            print("Record not found")
    except IOError:
        print("Unable to open the file")

def main():
    while True:
        m = """
        	   Main Menu
        	1. Add Record
        	2. Display Record
        	3. Search by roll no
        	4. Search by name
        	0. exit
        	"""
        os.system("cls")
        print(m, end='')
        ch=int(input("Enter your choice:- "))
        if ch==1:
            add_record()
        elif ch==2:
            std_display()
        elif ch==3:
            search_roll()
        elif ch==4:
            search_name()
        elif ch==0:
            break
        else:
            print("invalid choice")
        input("Press enter to cont.... ")

if __name__ == '__main__':
    main()

# Arpit Jain
# Date:- 05-02-2022
