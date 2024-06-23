import csv

res_nt = 0
res_a = 0
tot_nt=0
tot_a=0
same_nt = 0
same_a = 0

results = []
with open("x12.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader: # each row is a list
        results.append(row)
        
lines = len(results)
for i in range(lines//3):
    row1 = results[i] # normal
    row2 = results[i + lines//3] #non-tour
    row3 = results[i + 2 * lines//3] #adaptive
    #print(i)
    #print(row1)
    
    for idx, (c1, c2) in enumerate(zip(reversed(row1), reversed(row2))):
        try: 
            val = int(c1)
            val = int(c2)
        except:
            same_nt += 1
            res_nt += 1
            tot_nt += idx
            break
        
        if c1 != c2:
            res_nt += idx/max(len(row1), len(row2))
            tot_nt += idx
            break
            
    for idx, (c1, c2) in enumerate(zip(reversed(row1), reversed(row3))):
        try: 
            val = int(c1)
            val = int(c2)
        except:
            same_a += 1
            res_a += 1
            tot_a += idx
            break
         
        if c1 != c2:
            #print(f"c1:{c1}, c2:{c2}, idx:{idx}")
            tot_a += idx
            res_a += idx/max(len(row1), len(row3))
            break
    
print(f"Same nt: {same_nt}")      
print(f"Same adaptive: {same_a}")     
print(f"Average deviation non-tournament: {res_nt/(lines//3)}")
print(f"Average deviation adaptive: {res_a/(lines//3)}")
print(f"Average deviation adaptive total: {tot_a/(lines//3)}")
print(f"Average deviation non-tournament total: {tot_nt/(lines//3)}")


            
    
