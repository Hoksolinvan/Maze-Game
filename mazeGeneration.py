import random
from collections import defaultdict, Counter

class UnionFind:
    def __init__(self, elements):
        self.cur_dict = {}
        for element in elements:
            self.cur_dict[element] = element
    
    def find(self, x):
        result = self.cur_dict[x]
        if x == result:
            return result
        else:
            result = self.find(result)
            self.cur_dict[x] = result
            return self.cur_dict[x]
            
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.cur_dict[x] = min(x, y)
        self.cur_dict[y] = min(x, y)
        
    def getter(self):
        return self.cur_dict


class Cell:

    __slots__=('cell_number','right_wall','bottom_wall')
    def __init__(self, cell_number, right_wall=False, bottom_wall=False):
        self.cell_number = cell_number
        self.right_wall = right_wall
        self.bottom_wall = bottom_wall
    
    def __repr__(self):
        return f"{self.cell_number}, {self.right_wall}, {self.bottom_wall}"

    
    
    
    
    

def algorithm(m, n):
    all_rows = []
    
    # Step 1 & 2: create first row with unique set IDs
    temp = [Cell(i) for i in range(n)]
    next_id = n  # for assigning fresh IDs to cells that lost their set
    
    for i in range(m):
        
        # Part 3: right walls
        UF = UnionFind([x for x in range(n)])
        
        # initialize UF with current cell_numbers
        for x in range(n):
            UF.cur_dict[temp[x].cell_number] = temp[x].cell_number
        UF.cur_dict = {temp[x].cell_number: temp[x].cell_number for x in range(n)}
        
        for j in range(n - 1):
            if temp[j].cell_number == temp[j+1].cell_number:
                temp[j].right_wall = True
            else:
                if random.random() < 0.5:
                    temp[j].right_wall = True
                else:
                    UF.merge(temp[j].cell_number, temp[j+1].cell_number)
        
        # apply union results back to cells
        for x in range(n):
            temp[x].cell_number = UF.find(temp[x].cell_number)
        
        # Part 4: bottom walls
        temp_count = Counter(temp[x].cell_number for x in range(n))
        
        bottom = 0
        for j in range(n):
            if j - 1 >= 0 and temp[j].cell_number != temp[j-1].cell_number:
                bottom = 0
            
            if bottom == temp_count[temp[j].cell_number] - 1:
                temp[j].bottom_wall = False
                bottom = 0
                continue
            
            if random.random() < 0.5:
                temp[j].bottom_wall = True
                bottom += 1
            else:
                temp[j].bottom_wall = False
        
        # Part 5
        if i != m - 1:
            all_rows.append([Cell(temp[x].cell_number, temp[x].right_wall, temp[x].bottom_wall) for x in range(n)])
            
            # reset for next row: remove right walls, reassign sets for cells with bottom walls
            for x in range(n):
                temp[x].right_wall = False
                if temp[x].bottom_wall:
                    temp[x].cell_number = next_id  # fresh unique set
                    next_id += 1
                temp[x].bottom_wall = False
        
        else:
            # final row: all bottom walls, then remove right walls between different sets
            for x in range(n):
                temp[x].bottom_wall = True
            
            UF_final = UnionFind([temp[x].cell_number for x in range(n)])
            
            for x in range(n - 1):
                if UF_final.find(temp[x].cell_number) != UF_final.find(temp[x+1].cell_number):
                    temp[x].right_wall = False
                    UF_final.merge(temp[x].cell_number, temp[x+1].cell_number)
            
            all_rows.append([Cell(temp[x].cell_number, temp[x].right_wall, temp[x].bottom_wall) for x in range(n)])
    

    for i in range(m):
        all_rows[i][n-1].right_wall=True



    return all_rows
