# Problem-2
## input_str을 통해 map data 관리하기
우선 input_str에 string 저장  
스테이지 구분자로 나눠 스테이지 2개를 stages_str 리스트에 저장

## map 정보 parse 하기
parse_map이라는 함수는 stages_str 리스트에서 스테이지 값 하나를 받음  
parse_map은 우선 받은 string을 줄 별로 나눠, 첫째줄에서는 스테이지 number를 가져옴.  
그리고 나머지 줄들, 즉 map string들은 parsing dictionary를 통해 변환함.  
결국 stage number와 parsed map 리스트를 return 한다.

## stage 클래스 만들기
### stage 클래스 attribute 
stage 클래스의 속성에는 stage_num, map_data와 map_data를 기반으로  
find_attributes 함수를 통해 찾은 width,height,holes,balls,p_location이 있다.
find_attributes 함수는 map_data를 돌며 각각의 속성의 값을 찾는다.

### stage 클래스 생성자
stage 클래스는 string으로 된 stage 정보를 받는다.  
생성자는 이 string을 parse 하여 map_data를 만들고, find_attributes 함수를 통해  
클래스의 속성을 설정한다.

### stage print 메서드
print_stage 메서드는 이 클래스의 속성들을 print한다.  
현재 스테이지에는 map_data로 parse되어 있기 때문에, 다시 parse 하여 string형태의   
맵으로 만들어야 한다. 그렇게 하기 위해 reverse_parse_dic을 만들어 map_data를 다시 parse 하도록 했다.


