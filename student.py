class Student:
        
    #create a method to add a record roll must be unique
    def add(self,roll,dept,name,address,phone):
        #open the records file in read mode
        with open("students.csv","r") as f:
            #read the records
            records=f.read()
            #split the records into lines
            records=records.split(" \n")
            #iterate through the lines
            for record in records:
                #split the line into attributes
                record=record.split(",")
                #if the roll number matches return
                if record[0]==roll:
                    return False
        #open the records file in append mode
        with open("students.csv","a") as f:
            #write the record to the file
            f.write(roll+","+dept+","+name+","+address+","+phone+" \n")
        return True

    #create a method to search a record
    def search(self,roll):
        #open the records file in read mode
        with open("students.csv","r") as f:
            #read the records
            records=f.read()
            #split the records into lines
            records=records.split(" \n")
            #iterate through the lines
            for record in records:
                #split the line into attributes
                record=record.split(",")
                #if the roll number matches return the record
                if record[0]==roll:
                    return record
        #if the roll number is not found return None
            return False
    #create a method to edit a record
    def edit(self,roll,dept,name,address,phone):
        #open the records file in read mode
        with open("students.csv","r") as f:
            flag=False
            #read the records
            records=f.read()
            #split the records into lines
            records=records.split(" \n")
            #iterate through the lines
            for cipord in records:
                #split the line into attributes
                record=cipord.split(",")
                #if the roll number matches replace the record with the new record
                if record[0]==roll:
                    records[records.index(cipord)]=roll+","+dept+","+name+","+address+","+phone
                    flag=True
        #open the records file in write mode
        with open("students.csv","w") as f:
            #write the records to the file
            for record in records:
                f.write(record+" \n")
        return flag
    #create a method to delete a record
    def delete(self,roll):
        flag=False
        #open the records file in read mode
        with open("students.csv","r") as f:
            #read the records
            records=f.read()
            #split the records into lines
            records=records.split(" \n")
            #iterate through the lines
            for cipord in records:
                #split the line into attributes
                record=cipord.split(",")
                #if the roll number matches delete the record
                if record[0]==roll:

                    records.remove(cipord)
                    flag=True
        #open the records file in write mode
        with open("students.csv","w") as f:
            #write the records to the file
            for record in records:
                f.write(record+" \n")
        return flag
    #create a method to display all the records and display 5 at a time
    def display(self):
        #open the records file in read mode
        with open("students.csv","r") as f:
            #read the records
            records=f.read()
            #split the records into lines
            records=records.split(" \n")
            return records