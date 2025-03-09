def get_num_words(str):
    nw = len(str.split())
    return nw

def get_num_char(str):
    str = str.lower()
    dict = {}
    for l in str:
        if l in dict:
            dict[l] = dict[l] + 1
        else:
            dict[l] = 1
    #char = {c for c in str}
    #dict = {c:str.count(c) for c in char}
    return dict

def sort_dict(dict):
    def sort_on(dict):
        return dict["num"]
    
    list_dict_to_sort=[]
    for c in dict:    
        list_dict_to_sort.append({"char": c, "num": dict[c]}) 
        
    list_dict_to_sort.sort(key=sort_on, reverse=True)
    return list_dict_to_sort