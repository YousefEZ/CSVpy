# User made module.
# Contains all the required functions.
# To use, we simply use the import function.
# import BackEnd


def CSVReader(File): #Function that reads a csv file, and returns the records. 
	
	'''
	
	$ Argument 1, File: File Path to the .csv file

	Sample Argument: 'Desktop/Python/Tables.csv'


	Pass through a csv file,
	which is split into a 2d array,
	and returns it.


	===========================================================
	# First Name #    Surname    #   Nationality  #    Age    #
	# ========== # ============= # ============== # ========= #
	#   Ahmed    #    Mohammed   #    Egyptian    #     17    #
	#    Amr     #      Hamza    #    Egyptian    #     15    #
	===========================================================



	Sample .csv File would be:
	--------------------------

	First Name,Surname,Nationality,Age
	Ahmed,Mohammed,Egyptian,17
	Amr,Hamza,Egyptian,15

	---------------------------



	Sample return would be:
	=========================

	[['First Name','Surname','Nationality','Age'],
	 ['Ahmed', 'Mohammed', 'Egyptian', '17'],
	 ['Amr', 'Hamza', 'Egyptian', '15']]
	
	=========================

	'''

	#Part 1, open the file, splits, and stores the records into a list.

	f = open(File,'r') #Reads the file that is passed through.
	Reader = " " #Variable that will hold what is read from the file (line by line).
	Lines = [] #Variable that will split the file into lines.

	while Reader != "": #To check whether the reader has reached EOF.
		Reader = f.readline() #Grabs the next line.
		if Reader != "": #To make sure hasn't reached EOF.
			Lines.append(Reader) #Inserts the line into the list.
	f.close() # Closes the file.


	#Part 2, Splits the records by fields, and stores it into a 2D list.

	Records = []

	for Record in range(len(Lines)): #Loops over the number of lines (Records) available.
		CurrentRecord = Lines[Record] #Grabs the next line.
		Field = 0 #Variable that indexes the field on the record. Starts at 0.
		SplitFrom = 0 #Variable that will Separate values. Used to mark the from character position.
		SplitTo = 0 #Variable that will Separate values. Used to mark the to character position.

		EOL = False 
		Records.append([])
		while not EOL: #Whilst the End of Line hasn't been reached.
			SplitTo = SplitTo + 1 #Moves to the next character to split.
			if CurrentRecord[SplitTo-1:SplitTo] == ",": #Checks if the character is ','.
				Records[Record].append(CurrentRecord[SplitFrom : SplitTo - 1]) #Stores the field from the last ','.
				Field = Field + 1 #Moves to the next field in the line.
				SplitFrom = SplitTo #To start the next field from after the Split.

			if CurrentRecord[SplitTo-1:SplitTo+1] == "\n" or CurrentRecord[SplitTo-1:SplitTo+1] == "": #Checks if we have reached EOL
				Records[Record].append(CurrentRecord[SplitFrom : SplitTo - 1]) #Stores the last field.
				EOL = True #Reached EOL, so we need to increase the counter by 1, to move onto next record.

	return Records #Returns the 2d array containing the records and field.


def CSVBuilder(File, Data):


	'''

	$ Argument 1, File : Builds the .csv file under the specified filepath.
	$ Argument 2, Data : 2D Array from which the data is retrieved from.

	Builds a .csv file using the data is retrieved from the given 2D Array.


	'''
	

	FileData = ""
	for i in Data:
		FileData = FileData + i[0] + ","
		for x in range(1, len(i)-1):
			FileData = FileData + i[x] + ","
		FileData = FileData + i[len(i)-1] + "\n"
	
	CSVFile = open(File,'w')
	CSVFile.write(FileData)
	CSVFile.close()



def Count(Data):
	
	'''
	$ Argument 1, Data : 2D Array containing all the records and fields

	Counts the number of records

	Sample Data:
	[['First Name','Surname','Nationality','Age'],
	 ['Ahmed', 'Mohammed', 'Egyptian', '17'],
	 ['Amr', 'Hamza', 'Egyptian', '15']]

	Sample Return:
	3

	'''
	return len(Data)


def SimilarCheck(Data, StartIndex, Index, Form = 'LIST'):
	'''

	$ Argument 1, Data : 2D Array containing all the records and fields.
	$ Argument 2, StartIndex : Decides from which record to start.
	$ Argument 3, Index : The index in the 2D Array to compare the fields to.
	$ Argument 4, Form : Dictionary or List

	Stores, and counts how many of the records are related
	by having the same value in the field.

	Theoretical Sample Return:
	{'Egyptian': 5, 'Kuwaiti': 7, 'Jordanian': 1, 'British': 4, 'Lebanese': 2, 'Nigerian': 1, 'Korean': 1, 
	'Pakistani': 1, 'Polish': 2, 'Japanese': 1, 'Canadian': 1, 'Italin': 1, 
	'Turkish': 1, 'Danish': 1, 'Ethiopian': 1, 'Indian': 2}

	However sent to another Function Dict2List to convert into a 2D List.
	'''
	


	Dict = {}
	for i in range (StartIndex, len(Data)):
		if Data[i][Index] in Dict:
			Dict[Data[i][Index]] = Dict[Data[i][Index]] + 1
		else:
			Dict[Data[i][Index]] = 1

	if Form.upper() == "LIST":
		return Dict2List(Dict)
	elif Form.upper() in "DICTIONARY":
		return Dict




def Dict2List(Dictionary):

	'''
	$ Argument 1, Dictionary : Dictionary containing the data

	Converts a Dictionary into a 2 Dimensional Array

	Theoretical Sample Input:
	-------------------------

	{'Egyptian': 5, 'Kuwaiti': 7, 'Jordanian': 1, 'British': 4, 'Lebanese': 2, 'Nigerian': 1, 'Korean': 1, 
	'Pakistani': 1, 'Polish': 2, 'Japanese': 1, 'Canadian': 1, 'Italin': 1, 
	'Turkish': 1, 'Danish': 1, 'Ethiopian': 1, 'Indian': 2}


	Theoretical Sample Return:
	--------------------------
	[['Egyptian', 5], ['Kuwaiti', 7], ['Jordanian', 1], ['British', 4], ['Lebanese', 2], ['Nigerian', 1], 
	['Korean', 1], ['Pakistani', 1], ['Polish', 2], ['Japanese', 1], ['Canadian', 1], ['Italin', 1], 
	['Turkish', 1], ['Danish', 1], ['Ethiopian', 1], ['Indian', 2]]

	'''

	List = [['' for i in range (2)] for x in range (len(Dictionary))]
	increment = 0 
	for key,val in Dictionary.items():
		List[increment][0] = key
		List[increment][1] = val
		increment = increment + 1

	return List


def RangeCheck(Data, StartIndex, Index, From, To):
	'''
	$ Argument 1, Data :  The 2D Array to retrieve the data from
	$ Argument 2, StartIndex : Decides which Record to start on
	$ Argument 3, Index : Checks the range on which Index
	$ Argument 4, From : Starting Range
	$ Argument 5, To :  End Range

	Checks whether the stated index values are within the stated range, and stores 
	the array in 2 arrays depending on whether the condition is met or not

	Sample Input:
	------------

	Where Data = 
	[['First Name','Surname','Nationality','Age', 'Option 1', 'Option 2', 'Option 3'],
	 ['Ahmed', 'MOHAMMED', 'Egyptian', '17', 'Chemistry', 'None', 'None'],
	 ['Amr', 'HAMZA', 'Egyptian', '15','Physics','Biology','Computer Science']]

	$ RangeCheck (Data, 1, 3, 16, 18)
	
	Sample Return:
	-------------
	[['Ahmed', 'MOHAMMED', 'Egyptian', '17', 'Chemistry', 'None', 'None']]

	'''
	InRange = []
	OutRange = []
	for i in range (StartIndex, len(Data)):
		NewData = Data[i]
		if int(Data[i][Index]) >= From and int(Data[i][Index]) <= To:
			InRange.append(NewData)
		else:
			OutRange.append(NewData)

	return InRange, OutRange


def FieldCheck(Data, Criteria, Indices):


	'''
	
	$ Argument 1, Data : The 2D Array from which we retrieve the data from.
	$ Argument 2, Crtieria : Search Criteria to match with the fields
	$ Argument 3, Indices : To search across which fields in the 2D Array.

	This will allow the user to search which records contains a certain value.

	Sample Input:
	------------
	Data = [["Aly","IBRAHIM","Egyptian","17","History","None","None"],
	["Bader","AL BAHRANI","Kuwaiti","18","History","English Literature","Geography"]]


	FieldCheck(Data, '17', [3])


	Sample Return:
	--------------
	[["Aly","IBRAHIM","Egyptian","17","History","None","None"]]

	
	'''


	MatchedRecords = []
	for Record in Data:
		LineCheck = False
		for Index in Indices:	
			if Record[Index] == Criteria and not LineCheck: 
				MatchedRecords.append(Record)
				LineCheck = True
	
	return MatchedRecords


def RecordFilter(Data, ReqIndex):

	'''
	$ Argument 1, Data : 2D Array which the Data is retrieved from.
	$ Argument 2, ReqIndex : List of indices that reference the wanted fields.

	This allows for the user to cut the 2D Array records into only wanted fields.

	Sample Input:
	-------------

	Data = [["Aly","IBRAHIM","Egyptian","17","History","None","None"],
["Bader","AL BAHRANI","Kuwaiti","18","History","English Literature","Geography"]]

	RecordFilter(Data, [2,3])


	Sample Return:
	--------------

	[["Egyptian","17], ["Kuwaiti", "18"]]

	'''

	NewData = [['' for x in range(len(ReqIndex))] for i in range (len(Data))]
	for i in range (len(Data)):
		for x in range (len(ReqIndex)):
			NewData[i][x] = Data[i][ReqIndex[x]]
	
	return NewData


def Sort(Data, order = 'ASCENDING'):
	'''
	$ Argument 1, Data : 2D Array from which we can retrieve the data from.
	$ Argument 2, order : option to order the list in ASCENDING or DESCENDING order.

	This allows the user to sort the 2D Array in ASCENDING or DESCENDING order based
	on the value.

	Sample Input:
	-------------
	Data = [["Aly","IBRAHIM"],
	["Dana","AL SANE"],
	["Bader","AL BAHRANI"]]

	Sort (Data, order = "ASCENDING")

	Sample Return:
	--------------
	[["Aly", "IBRAHIM"],
	["Bader", "AL BAHRANI"],
	["Dana", "AL SANE"]
	'''
	if order.upper() == "ASCENDING":
		Run = False 
		while not Run: #Loop to ensure that everything is sorted in the correct manner
			Run = True #If the list is sorted correctly, the list will break, as otherwise Run will switch to False on L10
			for counter in range(len(Data)-1): #Comparing all the elements in the list/array
				if Data[counter] > Data[counter + 1]: #To check whether the previous element is larger or smaller.
					temp = Data[counter] #Stores it into a temporary variable to switch.
					Data[counter] = Data[counter + 1]#Switches the previous element with the next element.From smallest -> largest)
					Data[counter + 1] = temp #Switches the next element with the previous element. (From Smallest to Largest)
					Run = False #To not break the loop as more sorting may be required.
	elif order.upper() == "DESCENDING":
		Run = False 
		while not Run: #Loop to ensure that everything is sorted in the correct manner
			Run = True #If the list is sorted correctly, the list will break, as otherwise Run will switch to False on L10
			for counter in range(len(Data)-1): #Comparing all the elements in the list/array
				if Data[counter] < Data[counter + 1]: #To check whether the previous element is larger or smaller.
					temp = Data[counter] #Stores it into a temporary variable to switch.
					Data[counter] = Data[counter + 1]#Switches the previous element with the next element.From Largest -> smallest)
					Data[counter + 1] = temp #Switches the next element with the previous element. (From Largest to smallest)
					Run = False #To not break the loop as more sorting may be required.
	else:
		raise SyntaxError ('order must be "DESCENDING" or "ASCENDING"')

	return Data


def RemoveRecords(Data, Records):
	'''
	$ Argument 1, Data: 2D Array from which we can retrieve the Data from.
	$ Argument 2, Records: 2D Array which the user wants to remove from the Data Array.

	This allows the user to remove specifically matching Records.

	Sample Input:
	------------
	Data = [["Aly","IBRAHIM"],
	["Dana","AL SANE"],
	["Bader","AL BAHRANI"]]

	Records = ["Bader","AL BAHRANI"]]

	RemoveRecords(Data, Records)

	Sample Return:
	--------------
	[["Aly","IBRAHIM"],
	["Dana","AL SANE"]]
	
	'''

	NewData = []
	for i in Data:
		Check = False
		for Record in Records:
			if i == Record:
				Check = True
				break
		if not Check:
			NewData.append(i)
	
	return NewData

def MergeFields(Data, Order = "LR"):


	'''

	$ Argument 1, Data : 2D Array, from which the Data is retrieved from.
	$ Argument 2, Order: "LR"/"RL" Left -> Right or Right -> Left
	
	Merges all the fields of the record together

	Sample Input:
	-------------

	Data = [['Ahmed','MOHAMMED'],
	['Amr', 'HAMZA']]

	Merge_Fields(Data, Order = "RL")



	Sample Return:
	--------------
	[['MOHAMMED Ahmed'],
	['HAMZA Amr']] 

	'''


	if Order == "LR":
		step = 1
	elif Order == "RL":
		step = -1


	MergedRecords = []
	for i in Data:
		string = i[0]
		for x in range (1,len(i),step):
			string = string + " " + i[x]
		MergedRecords.append(string)

	return MergedRecords


def UniqueField(Data, index):
	'''
	$ Argument 1, Data : 2D Array from which the data is retrieved from.
	$ Argument 2, Index : to indicate which field to search in.

	Finds all the various values that have been belong to a certain field

	Sample Input:
	-------------
	Data = 	[['Ahmed', 'Mohammed', 'Egyptian', '17'],
	 ['Amr', 'Hamza', 'Egyptian', '15']]
	
	UniqueField(Data, 2)

	Sample Return:
	--------------
	['Egyptian']
	'''
	
	UniqueRecords = [Data[0][index]]
	for i in range (1,len(Data)):
		Unique = True
		for x in range (len(UniqueRecords)):
			if UniqueRecords[x] == Data[i][index]:
				Unique = False
		if Unique:
			UniqueRecords.append(Data[i][index])
	
	return UniqueRecords