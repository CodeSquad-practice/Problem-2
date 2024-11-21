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

class stage:
    # 변환 표
    parsing_dic={' ':0 ,'O':1,'o':2,'P':3,'#':4,'=':None}
    reverse_parsing_dic={0:' ' ,1:'O',2:'o',3:'P',4:'#',None:'='}

    def __init__(self,map_str):
        self.stage_num,self.map_data=self.parse_map(map_str)
        self.width,self.height,self.holes,self.balls,self.p_location=self.find_attributes()
    
    
    def parse_map(self,map_str):
        # 우선 줄로 나눈다.
        map_lines=map_str.split("\n")
        # 첫째줄은 stage num
        stage_num=int(map_lines[0].split(' ')[1])
        # 둘째줄부터 parse
        map_lines=map_lines[1:]
        
        parsed_map=[]
        for elems in map_lines:
            # split 하는 과정에서 생긴 빈 str는 제외
            if elems=='':
                continue
            line=[]
            for elem in elems:
                # parse 하여 append
                line.append(self.parsing_dic[elem])
            parsed_map.append(line)
        
        return stage_num,parsed_map

    def find_attributes(self):
        width=0
        height=len(self.map_data)
        holes=0
        balls=0

        row=0
        for line in self.map_data:
            row+=1
            col=0
            for elem in line:
                col+=1
                if elem==1:
                    holes+=1
                elif elem==2:
                    balls+=1
                elif elem==3:
                    p_location=(row,col)
                width=max(width,col)

        return width,height,holes,balls,p_location
    
    def print_stage(self):
        print("Stage",self.stage_num)
        print()
        # 다시 parse 해서 print
        for line in self.map_data:
            for elem in line:
                print(self.reverse_parsing_dic[elem],end='')
            print()
        print()
        print("가로크기:",self.width)
        print("세로크기:",self.height)
        print("구멍의 수:",self.holes)
        print("공의 수:",self.balls)
        print(f"플레이어 위치: {self.p_location[0]}행 {self.p_location[1]}열")

def main():
    #=====로 나눠 2 스테이지를 리스트에 저장
    stages_str=input_str.split("=====\n")
   
    st1=stage(stages_str[0])
    st1.print_stage()
    st2=stage(stages_str[1])
    st2.print_stage()

if __name__=="__main__":
    main()

