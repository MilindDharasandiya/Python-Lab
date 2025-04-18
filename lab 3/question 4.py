def remove_substring(onestring, removestr):
    result = ''
    i = 0
    while i < len(onestring):
    
        match = True
        if i + len(removestr) <= len(onestring):
            for j in range(len(removestr)):
                if onestring[i + j] != removestr[j]:
                    match = False
                    break
        else:
            match = False

     
        if match:
            i += len(removestr)
        else:
            result += onestring[i]
            i += 1
    return result


onestring = "abcdef"
removestring = "cd"
finalstring = remove_substring(onestring, removestring)
print("Final String:", finalstring)
