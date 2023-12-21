def treeHight(tree):
    if tree == None:
        return 0
    else:
        leftHeight = treeHight(tree['L'])
        rightHeight = treeHight(tree['R'])
        
        #Tinggi pohon adalah maksimum dari tinggi anak kiri dan kanan ditambah satu
        
        height = max(leftHeight, rightHeight) + 1
        return height
    
def creatTree(tree,data):
    newNode = {'L' : None,'Data':data,'R' : None}  
    if tree == None:
        tree = newNode
    else:
        if data < tree['Data']:
            if tree['L'] == None:
                tree['L'] = newNode
            else:
                creatTree(tree['L'],data)
        else:
            if tree['R'] == None:
                tree['R'] = newNode
            else:
                creatTree(tree['R'],data)
    return tree
#=================== Main Function ===================#
tree = None
tree = creatTree(tree,5)
tree = creatTree(tree,9)
tree = creatTree(tree,4)
tree = creatTree(tree,7)
print(tree)
print("Jumlah Node : ",treeHight(tree))
