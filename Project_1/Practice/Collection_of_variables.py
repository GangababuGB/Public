with open('Collection of variables Task.txt', 'r') as f:
    file = f.read()
print(file)

class COV():
    def __init__(self, prg1, prg2, prg3, prg4, prg5, prg6): #constructor
        self.ip1 = prg1
        self.ip2 = prg2
        self.ip3 = prg3
        self.ip4 = prg4
        self.ip5 = prg5
        self.ip6 = prg6

    def select_Program(self):
        print("Welcome to Collection of variables :)")
        print("Available Execution ranges between 1 to 7:")
        print("1. Execute 1st program: Sort_by_keys")
        print("2. Execute 2nd program: Remove duplicates from a list")
        print("3. Execute 3rd program: Finding longer than n from the list of words")
        print("4. Execute 4th program: Removing specified words from the List")
        print("5. Execute 5th program: Move all zero digits to end")
        print("6. Execute 6th program: Remove the K'th element from a given list")
        print("7. To terminate from the COV Program")


    # Task -1 Sorting by keys#
    def Sort_keys(self):
        self.ip1.sort(key = lambda x : x[1])  # Sorting by Second index from the input list.
        print(self.ip1) #calling parameters of constructor
    # Task 2
    def Remove_Dup_module(self):
        Dup_module = lambda x : list(set(x))
        print("Original_list : "+ str(self.ip2))
        Dup_result = Dup_module(self.ip2)
        print("Resulted_list : "+ str(Dup_result) + " duplicates removed")
    # Task 3
    def nth_element (self):
        print("Original_list : " + str(self.ip3))
        n = int(input("Enter n'th element:"))
        print("Chosen Element:",n)
        filter_list = [x for x in self.ip3 if len(x) > n]
        print("Filtered_list : "+ str(filter_list))
    # Task 4 #Slicing
    def slicing(self):
        print(self.ip4[1:4])

    # Task 5
    def stable_sort(self):
        print("Original_list : "+ str(self.ip5))
        task5 = sorted(self.ip5, key=lambda x: x==0) # stable sort
        print("updated_list :  "+ str(task5) + " Zero's Moved to end")

    # Task 6
    def remove_kth(self):
        print("Original_list : " + str(self.ip6))
        k = int(input("Enter K'th element:"))
        print("Selected index: ",k)
        del self.ip6[k]
        print("resulted_list : "+ str(self.ip6))

def main():
    ip1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    ip2 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 8, 8, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    ip3 = ['one', 'bird', 'two', 'birds', 'road', 'RoadmapIT', 'temp', 'temperature', 'fun', 'funnier', 'apple',
           'today', 'i', 'saw', 'a', 'monkey', 'eating', 'fruit', 'at', 'temple']
    ip4 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    ip5 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    ip6 = [1, 1, 2, 3, 4, 4, 5, 1]
    cov1 = COV(ip1, ip2, ip3, ip4, ip5, ip6)
    cov1.select_Program()
    while True:
        option_no = int(input("Which program would you like to to execute: "))
        if option_no == 1:
            cov1.Sort_keys()
        elif option_no == 2:
            cov1.Remove_Dup_module()
        elif option_no == 3:
            cov1.nth_element()
        elif option_no == 4:
            cov1.slicing()
        elif option_no == 5:
            cov1.stable_sort()
        elif option_no == 6:
            cov1.remove_kth()
        elif option_no == 7:
            break
        else:
            print("Invalid Please enter range between 1 to 7")


if __name__ == '__main__':
    main()
