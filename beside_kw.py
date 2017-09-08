def find_kw(corpus, windows_num, seg_kw):   #find_kw(test, 2, "拌")
    seg_text = corpus.split(seg_kw)
    inside = []
    
    for content in seg_text:
        if seg_text.index(content) == 0:
            inside.append(content[-windows_num:])
        elif seg_text.index(content) == (len(seg_text)-1):
            inside.append(content[:windows_num])
        else:
            front_end = str(content[:windows_num]) + " " + str(content[-windows_num:])
            inside.append(front_end)
    join_inside = seg_kw.join(inside)
    return(join_inside)
