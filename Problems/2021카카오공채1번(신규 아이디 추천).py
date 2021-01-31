import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    
    new_id = re.sub('[^0-9a-z-_.]','',new_id) # 2단계
    
    new_id = re.sub('[.]+','.',new_id) # 3단계
    
    new_id = new_id.strip('.') # 4단계
    
    if len(new_id) == 0: # 5단계
        new_id = 'a'
        
    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        new_id = new_id.strip('.')
        
    if len(new_id) <= 2: # 7단계
        last_word = new_id[-1]
        while len(new_id) < 3:
            new_id += last_word
            
    answer = new_id
    return answer
