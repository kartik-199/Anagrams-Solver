import enchant
import math
def main():
    given = input('Enter a string of letters: ')
    list = combo_gen(6, given)
    master_list = []
    compressed_list = []
    for element in list:
        master_list.append(element)
    for i in range(0,len(given)):
        word = ''
        for j in range(0,len(given)):
                if(i==j):
                    continue
                else:
                    word += given[j]
        list = combo_gen(5, word)
        for element in list:
            master_list.append(element)
    for i in range(0,len(given)):
        for j in range(0,len(given)):
            word = ''
            for k in range(0,len(given)):
                if(k!=j and k!=i):
                    word+=given[k]
        list = combo_gen(4, word)
        for element in list:
            master_list.append(element)
    for i in range(0,len(given)):
        for j in range(0,len(given)):
            for k in range(0,len(given)):
                word = ''
                for l in range(0, len(given)):
                    if(l!=j and l!=i and l!=k):
                        word+=given[l]
        list = combo_gen(3, word)
        for element in list:
            master_list.append(element)
    for element in master_list:
        if element not in compressed_list:
            compressed_list.append(element)
    print("Solutions:\n"+", ".join(compressed_list))


def combo_gen(letters, string):
    l_bound = 0
    u_bound = 0
    for i in range(1,letters+1):
        l_bound += i*math.pow(10,letters-i)
    for i in range(letters, 0, -1):
        u_bound += i*math.pow(10,i-1)
    index_combos = []
    string_combos = []
    count = 0
    d = enchant.Dict("en_US")
    for indices in range(int(l_bound),int(u_bound)+2):
        indices_arr = int_to_arr(indices)
        if is_unique(indices_arr) and bound(indices_arr,letters+1) and exclude(indices_arr,0):
            index_combos.append(indices_arr)
            count+=1
    for indices_arr in index_combos:
        word_test = ''
        for index in indices_arr:
            word_test += string[index-1]
        if d.check(word_test):
            string_combos.append(word_test)
    return string_combos


def int_to_arr(val):
    return_arr = list()
    while(val!=0):
        return_arr.append(val%10)
        val = int(val/10)
    return return_arr


def is_unique(indices_arr):
    for i in range(1,len(indices_arr)):
        for j in range(0,i):
            if indices_arr[j] == indices_arr[i]:
                return False
    return True


def bound(indices_arr, bound):
    for i in indices_arr:
        if(i>bound-1):
            return False
    return True


def exclude(indices_arr, element):
    for i in indices_arr:
        if(i==element):
            return False
    return True


if __name__ == "__main__":
    main()