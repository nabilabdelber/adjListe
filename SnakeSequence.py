
from csv import reader
import codecs

def getMaxSequence(matrix):

        rows = len(matrix)
        cols = len(matrix[0])
        maxLenth =1
        maxRow = 0
        maxCol = 0

        #//create result matrix
            
        result = [[1 for x in range(cols)] for y in range(rows)] 

        for  i  in range(0,rows): 
            for j  in range(0,cols): 
                if(i!=0 or j!=0):
                    #//check from left
                    if(i>0 and abs(matrix[i][j]-matrix[i-1][j])==1):
                        result[i][j] = max(result[i][j],  result[i-1][j]+1)
                        if(maxLenth<result[i][j]):
                            maxLenth = result[i][j]
                            maxRow = i
                            maxCol = j

                    #//check from top
                    if(j>0 and abs(matrix[i][j]-matrix[i][j-1])==1):
                        result[i][j] = max(result[i][j], result[i][j-1]+1)
                        if(maxLenth<result[i][j]):
                            maxLenth = result[i][j]
                            maxRow = i
                            maxCol = j
    

        #//Now we will check the max entry in the result[][].
        sequence = printPath(matrix, result, maxLenth, maxRow, maxCol)
        return sequence, maxLenth
    

def printPath(matrix, result, maxLength, maxRow, maxCol):
        sequence = []
        while(maxLength>=1):

            sequence.append(matrix[maxRow][maxCol])
            if(maxRow>0 and abs(result[maxRow-1][maxCol]-result[maxRow][maxCol])==1 and abs(matrix[maxRow-1][maxCol]-matrix[maxRow][maxCol])==1):
                maxRow = maxRow - 1
            elif(maxCol>0 and abs(result[maxRow][maxCol-1]-result[maxRow][maxCol])==1 and abs(matrix[maxRow][maxCol-1]-matrix[maxRow][maxCol])==1):
                maxCol= maxCol - 1
            
            maxLength -= 1
        
        return sequence
        
     

matrixfile = []
with open('matrix_adj.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        int_list = [int(i) for i in row]
        matrixfile.append(int_list)

sequence, maxLenth = getMaxSequence(matrixfile)

sequence2 = []
for k in range(len(sequence)):
    sequence2.append(sequence[len(sequence)-k-1])

print("Longueur de la sequance : " , maxLenth)     
print(sequence2)


with codecs.open('matrix_adj_result.txt', 'w', "utf-8") as write_obj:
    write_obj.write("Longueur de la séquance : " + str(maxLenth) + "\n")     
    write_obj.write("Séquance : " + ", ".join(str(x) for x in sequence2))