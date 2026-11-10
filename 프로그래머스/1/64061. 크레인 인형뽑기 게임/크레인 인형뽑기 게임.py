def solution(board, moves):
    # 필요한 변수
    # board -> 인형이 들어있는 크레인 크기(N x N), 각 칸에 0 <= 정수 <= 100 (정수는 각기 다른 인형의 모양)
    # moves -> moves의 원소 = 몇 번째 칸에서 옮길 지 / 1<= moves.length(옮기는 횟수) <= 1000
    #       -> 인형의 종류 예시 = 1,2,3,4,5.... (0은 인형이 없다는 의미)
    # result -> 터뜨려진 인형을 담을 바구니 자료구조
    #        -> 중복 X
    #        -> 중복 허용이 안되기 때문에 해시? / 배열 X / 
    
    # 설계
    # 1. result 배열로 초기화
    # 2. 이중 순회를 사용해서 board 원소에 접근해서 result에 담아준다.
    #   2-1. moves 외부 순회 iterator i
    #           moved_doll = moves[i] 초기화 
    #           > board 내부 순회
    #               board[i][j] == moved_doll가
    #               - result에서 pop
    #               - answer += 2 ✔︎ 연속으로 파괴된 2개의 인형 모두 카운트
    # 3. result set()함수를 사용해 중복값 제거
    #    -> 잘못된 설계. 중복값이 아니라 연속된 값이면 제거 -> 문제를 정확하게 읽어야 함 (문제의 요구사항부터 정리 필요)
    # 4. answer에 result의 길이를 할당해주고 반환

    answer = 0
    # result 배열 초기화
    result = []
    # 이중 순회 (for moves > for board)를 통해 result에 push
    # moves 외부 순회
    for moved_doll in moves:
        # moves의 1 = board의 0번째 칸이므로 -1
        j = moved_doll-1
        # board 내부 순회(열은 moves의 원소로 할당되있는 고정값)
        for i in range(len(board)):
            board_doll = board[i][j]
             # 각 칸의 인형이 존재한다면(어떤 종류라도) = (board_doll !=0) result에 append
            if board_doll != 0:
                # board에서 꺼냈으면 해당 원소 0으로 치환
                board[i][j] = 0
                # 연속으로 같은 종류의 인형이 append되면 모두 제거
                if result and result[-1] == board_doll:
                    result.pop()
                    # 제거한 수만큼 answer는 +2
                    answer+=2
                else:
                    result.append(board_doll)
                # ★인형을 뽑았으면 다음 차례 진행. break가 없다면 모든 칸의 인형을 뽑게 되는 문제 발생.
                break 
    return answer