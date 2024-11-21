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

    def print_stage_map(self):
        print()
        for line in self.map_data:
            for elem in line:
                print(self.reverse_parsing_dic[elem],end='')
            print()


def main():
    #=====로 나눠 2 스테이지를 리스트에 저장
    stages_str=input_str.split("=====\n")

    st2=stage(stages_str[1])
    print(f'Stage {st2.stage_num}')
    st2.print_stage_map()

    while True:
        print()
        orders=list(input('SOKOBAN>'))
        if orders[0]=='q'or orders[0]=='Q':
            print('Bye~')
            break
        for elem in orders:
            move(st2,elem)  


def move(stage,order):
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    order_dic={'W':0,'w':0,'S':1,'s':1,'A':2,'a':2,'D':3,'d':3}

    directions={0:'위로',1:'아래로',2:'왼쪽으로',3:'오른쪽으로'}
    # 지원하지 않는 명령
    if order not in order_dic:
        stage.print_stage_map()
        print()
        print(f"{order.upper()}: (경고!) 지원하지 않는 명령입니다!")

    #index에 맞게 1씩 빼준다
    else:
        r,c=stage.p_location[0]-1,stage.p_location[1]-1

        # order 에 맞게 이동한 위치는 nr,nc
        nr,nc=r+dxs[order_dic[order]],c+dys[order_dic[order]]

        if stage.map_data[nr][nc]==0:
            #움직일 수 있을 때
            stage.map_data[nr][nc]=3
            stage.map_data[r][c]=0
            stage.p_location=(nr+1,nc+1)
            stage.print_stage_map()
            print()
            print(f'{order.upper()}: {directions[order_dic[order]]} 이동합니다.')

        else:
            stage.print_stage_map()
            print()
            print(f'{order.upper()}: (경고!) 해당 명령을 수행할 수 없습니다!')
            #cant move
                
    

if __name__=="__main__":
    main()
