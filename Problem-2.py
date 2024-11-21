# map str을 저장
input_str="""Stage 1
#####
#OoP#
#####
=====
Stage 2
  #######
###  O  ###
#    o    #
# Oo P oO #
###  o  ###
 #   O  # 
 ########
"""

#=====로 나눠 2 스테이지를 리스트에 저장
stages_str=input_str.split("=====\n")

# 스테이지를 포함한 str로 된 map을 넣으면 stage number와 변환하여 저장한 리스트 return
def parse_map(map_str):
    # 우선 줄로 나눈다.
    map_lines=map_str.split("\n")
    # 첫째줄은 stage num
    stage_num=int(map_lines[0].split(' ')[1])
    # 둘째줄부터 parse
    map_lines=map_lines[1:]
    # 변환 표
    parsing_dic={' ':0 ,'O':1,'o':2,'P':3,'#':4,'=':None}

    parse_map=[]
    for elems in map_lines:
        # split 하는 과정에서 생긴 빈 str는 제외
        if elems=='':
            continue
        line=[]
        for elem in elems:
            # parse 하여 append
            line.append(parsing_dic[elem])
        parse_map.append(line)
    
    return stage_num,parse_map

a,b=parse_map(stages_str[1])
print(a)
print(b)



# class stage:
#     def __init__(self,map_str):
#         self.map_str=map_str
#         map_lines=map_str.split("\n")
#         self.stage_num=int(map_lines[0].split(' ')[1])

