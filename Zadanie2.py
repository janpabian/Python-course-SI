def bubble_sort(arr):
    indexes=[i for i in range(len(arr))]
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                indexes[j], indexes[j+1] = indexes[j+1], indexes[j]
            
    return arr,indexes


def znajdz_indeksy(lst,prog):
    posortowana_list,posortowane_indeksy=bubble_sort(lst)
    print(posortowane_indeksy)
    print(posortowana_list)
    wynik=[]
    for i in range(len(lst)):
        if posortowana_list[i]>prog:
            wynik.insert(0,posortowane_indeksy[i])
            if len(wynik)==3:
                break
    print(wynik)
znajdz_indeksy([9,1,1,1,0,0,0,8,10,11,14,9999999,99999999],2)