#PDF MultiPurpose Tool
#Authors: Hassan Magdi
#Date: 10/3/2022 


import PyPDF2

#extract a page 
def extract_page():
    n = int(input("Please Enter the Number of the Page You Want: "))
    n -= 1                                                              #page indexing starts at 0
    file = open(input("Enter File Name: ")+".pdf" , "rb")
    file_reader = PyPDF2.PdfFileReader(file)
    needed_page = file_reader.getPage(n)
    file_writer = PyPDF2.PdfFileWriter()
    file_writer.addPage(needed_page)
    output = open(f"output-{n + 1}.pdf" , "wb")
    file_writer.write(output)
    output.close()

#merge pages

def merge():
    file1 = open(input("Please Enter the Name of the First File: ")+".pdf" , "rb")
    file2 = open(input("Please Enter the Name of the Second File: ")+".pdf" , "rb")
    merged_name = input("What Do You Want to call the New File: ")
    file1_reader = PyPDF2.PdfFileReader(file1)
    file2_reader = PyPDF2.PdfFileReader(file2)
    merged_file = open(merged_name + ".pdf" , "wb")
    file_merger = PyPDF2.PdfFileMerger()
    file_merger.merge(0 , file1_reader)
    file_merger.merge(file1_reader.getNumPages()  , file2_reader)
    file_merger.write(merged_file)
    merged_file.close()
    
#split pdf 

def split(n):                                   #n --> number of splits 
    start = 0
    file = open(input("Enter File Name: ") , "rb")
    file_reader = PyPDF2.PdfFileReader(file)
    num_of_pages = file_reader.getNumPages()
    
    if num_of_pages % n == 0:
        split_size = num_of_pages / n
    else:
        split_size = num_of_pages // n

    
    for i in range(1 , n+1):
        file_writer = PyPDF2.PdfFileWriter()
        split = open(f"part {i}.pdf" , "wb")
        
        if i == n:
            split_size += (num_of_pages % n)
        
        for j in range(start , start + split_size):
            page = file_reader.getPage(j)
            file_writer.addPage(page)
            file_writer.write(split)
        split.close() 
        start += split_size   
        










 




    



    
