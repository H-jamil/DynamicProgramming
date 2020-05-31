def permutation(input_list, partial, used):
    if len(partial)== len(input_list):
        print(partial)
    else:
         for i in range(0, len(input_list)):
             if not used[i] and not (input_list[i] ==input_list[i - 1] and not used[i - 1]):
                 used[i] = True
                 partial.append(input_list[i])
                 permutation(input_list, partial,used)
                 used[i] = False
                 partial.pop(len(partial) - 1)
def main():
    IN=[1,4,1]
    USED=[]
    for i in range(len(IN)):
        USED.append(False)
    permutation(IN,[],USED)

if __name__ == '__main__':
    main()
