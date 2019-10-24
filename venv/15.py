import os

def check(ll):
    # check if the list is sorted
    #return False
    if ll ==[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
        return True
    else:
        return False


def print_bord(ll):
    os.system("cls") # for windows you need to use "cls" instead of "clear"
    #print("15\t14\t13\t12\n11\t10\t9\t8\n7\t6\t5\t4\n3\t1\t2\t_")
    for i in range(len(ll)):
        if i % 4 ==0:
            print()
        if bord [i] !=0:
            print(bord[i], end="\t")
        else:
            print(" ", end="\t")
    print()

def check_move(move, bb):

    n=bb.index(move)
    n_0=bb.index(0)

    if bb[n] == bb[n_0-4] or bb[n] == bb[n_0-1] or bb[n] == bb[n_0+1] or bb[n] == bb[n_0+4] :
        bb[n], bb[n_0] = bb[n_0], bb[n]
        

        print(bb)




    #bb.index(move)=bb.index(0)-1 \



if __name__ == "__main__":
    print("You are playing the 15-th game")
    bord = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0]
    while not check(bord):
        print_bord(bord)
        while True:
            your_try = int(input("Enter numb 1-15 >>"))
            if check_move(your_try, bord):
                break
