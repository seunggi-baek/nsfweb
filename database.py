import atexit
import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='1111',
                             db='nsf',
                             charset='utf8')

def execute_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        if query.lower().startswith('select'):
            # SELECT 쿼리의 경우 결과를 반환
            return cursor.fetchall()
        else:
            # 그 외 쿼리는 커밋 수행
            connection.commit()

# 쿼리 실행 예시
# 결과 = execute_query("SELECT * FROM your_table")

# 애플리케이션 종료 시 연결 닫기
def close_connection():
    connection.close()

# 애플리케이션 종료 전에 close_connection() 호출
# atexit에 연결 닫기 함수 등록
atexit.register(close_connection)
