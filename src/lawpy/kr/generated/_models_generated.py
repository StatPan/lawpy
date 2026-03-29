"""Auto-generated Pydantic models from specs/kr/*.json + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit by hand.
"""

# ruff: noqa: E501

from pydantic import BaseModel


class AcrList(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 결정문 목록 조회.

    Source: specs/kr/acrListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 기관명
    acr_id: str | None = None  # acr id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    제목: str | None = None  # 제목: 제목
    민원표시명: str | None = None  # 민원표시명: 민원표시명
    의안번호: str | None = None  # 의안번호: 의안번호
    회의종류: str | None = None  # 회의종류: 회의종류
    결정구분: str | None = None  # 결정구분: 결정구분
    의결일: str | None = None  # 의결일: 의결일
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class AcrDetail(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 결정문 본문 조회.

    Source: specs/kr/acrInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    기관명: str | None = None  # 기관명: 기관명
    회의종류: str | None = None  # 회의종류: 회의종류
    결정구분: str | None = None  # 결정구분: 결정구분
    의안번호: str | None = None  # 의안번호: 의안번호
    민원표시: str | None = None  # 민원표시: 민원표시
    제목: str | None = None  # 제목: 제목
    신청인: str | None = None  # 신청인: 신청인
    대리인: str | None = None  # 대리인: 대리인
    피신청인: str | None = None  # 피신청인: 피신청인
    관계기관: str | None = None  # 관계기관: 관계기관
    의결일: str | None = None  # 의결일: 의결일
    주문: str | None = None  # 주문: 주문
    이유: str | None = None  # 이유: 이유
    별지: str | None = None  # 별지: 별지
    의결문: str | None = None  # 의결문: 의결문
    의결일자: str | None = None  # 의결일자: 의결일자
    위원정보: str | None = None  # 위원정보: 위원정보
    결정요지: str | None = None  # 결정요지: 결정요지

class AcrspecialdeccList(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccAcrListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(EvtNm:재결례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    decc_id: str | None = None  # decc id: 검색결과번호
    특별행정심판재결례_일련번호: str | None = None  # 특별행정심판재결례 일련번호: 특별행정심판재결례일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    처분일자: str | None = None  # 처분일자: 처분일자
    의결일자: str | None = None  # 의결일자: 의결일자
    처분청: str | None = None  # 처분청: 처분청
    재결청: str | None = None  # 재결청: 재결청
    재결구분명: str | None = None  # 재결구분명: 재결구분명
    재결구분코드: str | None = None  # 재결구분코드: 재결구분코드
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    행정심판재결례_상세링크: str | None = None  # 행정심판재결례 상세링크: 행정심판재결례상세링크

class AcrspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccAcrInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AdapspecialdeccList(BaseModel):
    """[GENERATED] Response model for 인사혁신처 소청심사위원회 특별행정심판재결례 목록 조회.

    Source: specs/kr/specialDeccAdapListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(EvtNm:재결례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    decc_id: str | None = None  # decc id: 검색결과번호
    특별행정심판재결례_일련번호: str | None = None  # 특별행정심판재결례 일련번호: 특별행정심판재결례일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    처분일자: str | None = None  # 처분일자: 처분일자
    의결일자: str | None = None  # 의결일자: 의결일자
    처분청: str | None = None  # 처분청: 처분청
    재결청: str | None = None  # 재결청: 재결청
    재결구분명: str | None = None  # 재결구분명: 재결구분명
    재결구분코드: str | None = None  # 재결구분코드: 재결구분코드
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    행정심판재결례_상세링크: str | None = None  # 행정심판재결례 상세링크: 행정심판재결례상세링크

class AdapspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 인사혁신처 소청심사위원회 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccAdapInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AdmbylList(BaseModel):
    """[GENERATED] Response model for 행정규칙 별표ㆍ서식 목록 조회.

    Source: specs/kr/mobAdmrulBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AdmrulList(BaseModel):
    """[GENERATED] Response model for 행정규칙 목록 조회.

    Source: specs/kr/admrulListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    admrul_id: str | None = None  # admrul id: 결과 번호
    행정규칙_일련번호: str | None = None  # 행정규칙 일련번호: 행정규칙일련번호
    행정규칙명: str | None = None  # 행정규칙명: 행정규칙명
    행정규칙종류: str | None = None  # 행정규칙종류: 행정규칙종류
    발령일자: str | None = None  # 발령일자: 발령일자
    발령번호: str | None = None  # 발령번호: 발령번호
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    현행연혁구분: str | None = None  # 현행연혁구분: 현행연혁구분
    제개정_구분코드: str | None = None  # 제개정 구분코드: 제개정구분코드
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    행정규칙id: str | None = None  # 행정규칙ID: 행정규칙
    행정규칙_상세링크: str | None = None  # 행정규칙 상세링크: 행정규칙상세링크
    시행일자: str | None = None  # 시행일자: 시행일자
    생성일자: str | None = None  # 생성일자: 생성일자

class AdmrulDetail(BaseModel):
    """[GENERATED] Response model for 행정규칙 본문 조회.

    Source: specs/kr/mobAdmrulInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AdmruloldandnewList(BaseModel):
    """[GENERATED] Response model for 행정규칙 신구법 비교 목록 조회.

    Source: specs/kr/admrulOldAndNewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    numofrows: str | None = None  # numOfRows: 페이지 당 출력 결과 수
    resultcode: str | None = None  # resultCode: 조회 여부(성공 : 00 / 실패 : 01)
    resultmsg: str | None = None  # resultMsg: 조회 여부(성공 : success / 실패 : fail)
    oldandnew_id: str | None = None  # oldAndNew id: 검색 결과 순번
    신구법_일련번호: str | None = None  # 신구법 일련번호: 신구법 일련번호
    현행연혁구분: str | None = None  # 현행연혁구분: 현행연혁코드
    신구법명: str | None = None  # 신구법명: 신구법명
    신구법id: str | None = None  # 신구법ID: 신구법ID
    발령일자: str | None = None  # 발령일자: 발령일자
    발령번호: str | None = None  # 발령번호: 발령번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    신구법_상세링크: str | None = None  # 신구법 상세링크: 신구법 상세링크

class AdmruloldandnewDetail(BaseModel):
    """[GENERATED] Response model for 행정규칙 신구법 비교 본문 조회.

    Source: specs/kr/admrulOldAndNewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    구조문_기본정보: str | None = None  # 구조문_ 기본정보: 구조문_기본정보
    행정규칙일련번호: str | None = None  # 행정규칙일련번호: 행정규칙일련번호
    행정규칙id: str | None = None  # 행정규칙ID: 행정규칙ID
    시행일자: str | None = None  # 시행일자: 시행일자
    발령일자: str | None = None  # 발령일자: 발령일자
    발령번호: str | None = None  # 발령번호: 발령번호
    현행여부: str | None = None  # 현행여부: 현행여부
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    행정규칙명: str | None = None  # 행정규칙명: 행정규칙명
    행정규칙종류: str | None = None  # 행정규칙종류: 행정규칙종류
    신조문_기본정보: str | None = None  # 신조문_ 기본정보: 구조문과 동일한 기본 정보 들어가 있음.
    구조문목록: str | None = None  # 구조문목록: 구조문목록
    조문: str | None = None  # 조문: 조문
    신조문목록: str | None = None  # 신조문목록: 신조문목록
    신구법_존재여부: str | None = None  # 신구법 존재여부: 신구법이 존재하지 않을 경우 N이 조회.

class BaipvcsList(BaseModel):
    """[GENERATED] Response model for 감사원 사전컨설팅 의견서 목록 조회.

    Source: specs/kr/baiPvcsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(PvcsNm:의견서명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    baipvcs_id: str | None = None  # baiPvcs id: 검색결과번호
    감사원사전컨설팅_의견서일련번호: str | None = None  # 감사원사전컨설팅 의견서일련번호: 감사원사전컨설팅의견서일련번호
    의견서명: str | None = None  # 의견서명: 의견서명
    회신일자: str | None = None  # 회신일자: 회신일자
    신청기관명: str | None = None  # 신청기관명: 신청기관명
    접수번호: str | None = None  # 접수번호: 접수번호
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    감사원_사전컨설팅_의견서_상세링크: str | None = None  # 감사원 사전컨설팅 의견서 상세링크: 감사원 사전컨설팅 의견서상세링크

class BaipvcsDetail(BaseModel):
    """[GENERATED] Response model for 감사원 사전컨설팅 의견서 본문 조회.

    Source: specs/kr/baiPvcsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class CouseadmrulList(BaseModel):
    """[GENERATED] Response model for 맞춤형 행정규칙 조문 목록 조회.

    Source: specs/kr/custAdmrulJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    vcode: str | None = None  # vcode: 분류코드
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    행정규칙_일련번호: str | None = None  # 행정규칙 일련번호: 행정규칙일련번호
    행정규칙명: str | None = None  # 행정규칙명: 행정규칙명
    행정규칙id: str | None = None  # 행정규칙ID: 행정규칙ID
    발령일자: str | None = None  # 발령일자: 발령일자
    발령번호: str | None = None  # 발령번호: 발령번호
    행정규칙구분명: str | None = None  # 행정규칙구분명: 행정규칙구분명
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    담당부서기관코드: str | None = None  # 담당부서기관코드: 담당부서기관코드
    담당부서기관명: str | None = None  # 담당부서기관명: 담당부서기관명
    담당자명: str | None = None  # 담당자명: 담당자명
    전화번호: str | None = None  # 전화번호: 전화번호
    조문단위_조문키: str | None = None  # 조문단위 조문키: 조문단위 조문키
    조문번호: str | None = None  # 조문번호: 조문번호
    조문가지번호: str | None = None  # 조문가지번호: 조문가지번호
    조문상세링크: str | None = None  # 조문상세링크: 조문상세링크

class CouselsList(BaseModel):
    """[GENERATED] Response model for 맞춤형 법령 조문 목록 조회.

    Source: specs/kr/custLsJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    vcode: str | None = None  # vcode: 분류코드
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 페이지당 결과 수
    page: str | None = None  # page: 페이지당 결과 수
    법령_법령키: str | None = None  # 법령 법령키: 법령 법령키
    법령id: str | None = None  # 법령ID: 법령ID
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    조문번호: str | None = None  # 조문번호: 조문번호
    조문가지번호: str | None = None  # 조문가지번호: 조문가지번호
    조문제목: str | None = None  # 조문제목: 조문제목
    조문시행일자: str | None = None  # 조문시행일자: 조문시행일자
    조문제개정유형: str | None = None  # 조문제개정유형: 조문제개정유형
    조문제개정일자문자열: str | None = None  # 조문제개정일자문자열: 조문제개정일자문자열
    조문상세링크: str | None = None  # 조문상세링크: 조문상세링크

class CouseordinList(BaseModel):
    """[GENERATED] Response model for 맞춤형 자치법규 조문 목록 조회.

    Source: specs/kr/custOrdinJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    vcode: str | None = None  # vcode: 분류코드
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    자치법규일련번호: str | None = None  # 자치법규일련번호: 자치법규일련번호
    자치법규명: str | None = None  # 자치법규명: 자치법규명
    자치법규id: str | None = None  # 자치법규ID: 자치법규ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    자치법규종류: str | None = None  # 자치법규종류: 자치법규종류
    지자체기관명: str | None = None  # 지자체기관명: 지자체기관명
    시행일자: str | None = None  # 시행일자: 시행일자
    자치법규분야명: str | None = None  # 자치법규분야명: 자치법규분야명
    조문단위_조문키: str | None = None  # 조문단위 조문키: 조문단위 조문키
    조문번호: str | None = None  # 조문번호: 조문번호
    조문가지번호: str | None = None  # 조문가지번호: 조문가지번호
    조문제목: str | None = None  # 조문제목: 조문제목
    조문내용: str | None = None  # 조문내용: 조문내용

class DapacgmexpcList(BaseModel):
    """[GENERATED] Response model for 방위사업청 법령해석 목록.

    Source: specs/kr/cgmExpcDapaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class DapacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 방위사업청 법령해석 본문.

    Source: specs/kr/cgmExpcDapaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class DeccList(BaseModel):
    """[GENERATED] Response model for 행정심판례 목록 조회.

    Source: specs/kr/mobDeccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(EvtNm:재결례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    decc_id: str | None = None  # decc id: 검색결과번호
    행정심판재결례일련번호: str | None = None  # 행정심판재결례일련번호: 행정심판재결례일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    처분일자: str | None = None  # 처분일자: 처분일자
    처분청: str | None = None  # 처분청: 처분청
    재결청: str | None = None  # 재결청: 재결청
    재결구분명: str | None = None  # 재결구분명: 재결구분명
    재결구분코드: str | None = None  # 재결구분코드: 재결구분코드
    행정심판례_상세링크: str | None = None  # 행정심판례 상세링크: 행정심판례상세링크

class DeccDetail(BaseModel):
    """[GENERATED] Response model for 행정심판례 본문 조회.

    Source: specs/kr/mobDeccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class DetcList(BaseModel):
    """[GENERATED] Response model for 헌재결정례 목록 조회.

    Source: specs/kr/mobDetcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(EvtNm:헌재결정례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    detc_id: str | None = None  # detc id: 검색결과번호
    헌재결정례일련번호: str | None = None  # 헌재결정례일련번호: 헌재결정례일련번호
    종국일자: str | None = None  # 종국일자: 종국일자
    사건번호: str | None = None  # 사건번호: 사건번호
    사건명: str | None = None  # 사건명: 사건명
    헌재결정례_상세링크: str | None = None  # 헌재결정례 상세링크: 헌재결정례상세링크

class DetcDetail(BaseModel):
    """[GENERATED] Response model for 헌재결정례 본문 조회.

    Source: specs/kr/mobDetcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EccList(BaseModel):
    """[GENERATED] Response model for 중앙환경분쟁조정위원회 결정문 목록 조회.

    Source: specs/kr/eccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    ecc_id: str | None = None  # ecc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    사건명: str | None = None  # 사건명: 사건명
    의결번호: str | None = None  # 의결번호: 의결번호
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class EccDetail(BaseModel):
    """[GENERATED] Response model for 중앙환경분쟁조정위원회 결정문 본문 조회.

    Source: specs/kr/eccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    의결번호: str | None = None  # 의결번호: 의결번호
    사건명: str | None = None  # 사건명: 사건명
    사건의개요: str | None = None  # 사건의개요: 사건의 개요
    신청인: str | None = None  # 신청인: 신청인
    피신청인: str | None = None  # 피신청인: 피신청인
    분쟁의경과: str | None = None  # 분쟁의경과: 분쟁의 경과
    당사자주장: str | None = None  # 당사자주장: 당사자 주장
    사실조사결과: str | None = None  # 사실조사결과: 사실조사 결과
    평가의견: str | None = None  # 평가의견: 평가의견
    주문: str | None = None  # 주문: 주문
    이유: str | None = None  # 이유: 이유
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class EflawList(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 목록 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    law_id: str | None = None  # law id: 결과 번호
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    현행연혁코드: str | None = None  # 현행연혁코드: 현행연혁코드
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령약칭명: str | None = None  # 법령약칭명: 법령약칭명
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처명
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    공동부령구분: str | None = None  # 공동부령구분: 공동부령구분
    시행일자: str | None = None  # 시행일자: 시행일자
    자법타법여부: str | None = None  # 자법타법여부: 자법타법여부
    법령상세링크: str | None = None  # 법령상세링크: 법령상세링크

class EflawDetail(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 본문 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    언어: str | None = None  # 언어: 언어종류
    법종구분: str | None = None  # 법종구분: 법종류의 구분
    법종구분코드: str | None = None  # 법종구분코드: 법종구분코드
    법령명_한글: str | None = None  # 법령명_한글: 한글법령명
    법령명_한자: str | None = None  # 법령명_한자: 법령명_한자
    법령명약칭: str | None = None  # 법령명약칭: 법령명약칭
    편장절관: str | None = None  # 편장절관: 편장절관 일련번호
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    소관부처: str | None = None  # 소관부처: 소관부처명
    전화번호: str | None = None  # 전화번호: 전화번호
    시행일자: str | None = None  # 시행일자: 시행일자
    제개정구분: str | None = None  # 제개정구분: 제개정구분
    조문시행일자문자열: str | None = None  # 조문시행일자문자열: 조문시행일자문자열
    별표시행일자문자열: str | None = None  # 별표시행일자문자열: 별표시행일자문자열
    별표편집여부: str | None = None  # 별표편집여부: 별표편집여부
    공포법령여부: str | None = None  # 공포법령여부: 공포법령여부
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    부서명: str | None = None  # 부서명: 연락부서명
    부서연락처: str | None = None  # 부서연락처: 연락부서 전화번호
    공동부령구분: str | None = None  # 공동부령구분: 공동부령의 구분
    구분코드: str | None = None  # 구분코드: 구분코드(공동부령구분 구분코드)
    조문번호: str | None = None  # 조문번호: 조문번호
    조문가지번호: str | None = None  # 조문가지번호: 조문가지번호
    조문여부: str | None = None  # 조문여부: 조문여부
    조문제목: str | None = None  # 조문제목: 조문제목
    조문시행일자: str | None = None  # 조문시행일자: 조문시행일자
    조문제개정유형: str | None = None  # 조문제개정유형: 조문제개정유형
    조문이동이전: str | None = None  # 조문이동이전: 조문이동이전
    조문이동이후: str | None = None  # 조문이동이후: 조문이동이후
    조문변경여부: str | None = None  # 조문변경여부: 조문변경여부 (Y값이 있으면 해당 조문내에 변경 내용 있음 )
    조문내용: str | None = None  # 조문내용: 조문내용
    항번호: str | None = None  # 항번호: 항번호
    항제개정유형: str | None = None  # 항제개정유형: 항제개정유형
    항제개정일자문자열: str | None = None  # 항제개정일자문자열: 항제개정일자문자열
    항내용: str | None = None  # 항내용: 항내용
    호번호: str | None = None  # 호번호: 호번호
    호내용: str | None = None  # 호내용: 호내용
    목번호: str | None = None  # 목번호: 목번호
    목내용: str | None = None  # 목내용: 목내용
    조문참고자료: str | None = None  # 조문참고자료: 조문참고자료
    부칙공포일자: str | None = None  # 부칙공포일자: 부칙공포일자
    부칙공포번호: str | None = None  # 부칙공포번호: 부칙공포번호
    부칙내용: str | None = None  # 부칙내용: 부칙내용
    별표번호: str | None = None  # 별표번호: 별표번호
    별표가지번호: str | None = None  # 별표가지번호: 별표가지번호
    별표구분: str | None = None  # 별표구분: 별표구분
    별표제목: str | None = None  # 별표제목: 별표제목
    별표제목_문자열: str | None = None  # 별표제목 문자열: 별표제목문자열
    별표시행일자: str | None = None  # 별표시행일자: 별표시행일자
    별표서식_파일링크: str | None = None  # 별표서식 파일링크: 별표서식파일링크
    별표hwp_파일명: str | None = None  # 별표HWP 파일명: 별표 HWP 파일명
    별표서식_pdf파일링크: str | None = None  # 별표서식 PDF파일링크: 별표서식PDF파일링크
    별표pdf_파일명: str | None = None  # 별표PDF 파일명: 별표 PDF 파일명
    별표이미지_파일명: str | None = None  # 별표이미지 파일명: 별표 이미지 파일명
    별표내용: str | None = None  # 별표내용: 별표내용
    개정문내용: str | None = None  # 개정문내용: 개정문내용
    제개정이유내용: str | None = None  # 제개정이유내용: 제개정이유내용

class EflawjosubList(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 본문 조항호목 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    법령키: str | None = None  # 법령키: 법령키
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    언어: str | None = None  # 언어: 언어
    법종구분: str | None = None  # 법종구분: 법종구분
    법종구분_코드: str | None = None  # 법종구분 코드: 법종구분 코드
    법령명_한글: str | None = None  # 법령명_한글: 법령명을 한글로 제공
    법령명_한자: str | None = None  # 법령명_한자: 법령명을 한자로 제공
    법령명_영어: str | None = None  # 법령명_영어: 법령명을 영어로 제공
    편장절관: str | None = None  # 편장절관: 편장절관
    소관부처코드: str | None = None  # 소관부처코드: 소관부처 코드
    소관부처: str | None = None  # 소관부처: 소관부처명
    전화번호: str | None = None  # 전화번호: 전화번호
    시행일자: str | None = None  # 시행일자: 시행일자
    제개정구분: str | None = None  # 제개정구분: 제개정구분명
    제안구분: str | None = None  # 제안구분: 제안구분
    의결구분: str | None = None  # 의결구분: 의결구분
    적용시작일자: str | None = None  # 적용시작일자: 적용시작일자
    적용종료일자: str | None = None  # 적용종료일자: 적용종료일자
    이전법령명: str | None = None  # 이전법령명: 이전법령명
    조문시행일자문자열: str | None = None  # 조문시행일자문자열: 조문시행일자문자열
    별표시행일자문자열: str | None = None  # 별표시행일자문자열: 별표시행일자문자열
    별표편집여부: str | None = None  # 별표편집여부: 별표편집여부
    공포법령여부: str | None = None  # 공포법령여부: 공포법령여부 (Y값이 있으면 해당 법령은 공포법령임)
    조문번호: str | None = None  # 조문번호: 조문번호
    조문여부: str | None = None  # 조문여부: 조문여부
    조문제목: str | None = None  # 조문제목: 조문제목
    조문시행일자: str | None = None  # 조문시행일자: 조문시행일자
    조문이동이전: str | None = None  # 조문이동이전: 조문이동이전번호
    조문이동이후: str | None = None  # 조문이동이후: 조문이동이후번호
    조문변경여부: str | None = None  # 조문변경여부: 조문변경여부 (Y값이 있으면 해당 조문내에 변경 내용 있음 )
    조문내용: str | None = None  # 조문내용: 조문내용
    항번호: str | None = None  # 항번호: 항번호
    항내용: str | None = None  # 항내용: 항내용
    호번호: str | None = None  # 호번호: 호번호
    호내용: str | None = None  # 호내용: 호내용
    목번호: str | None = None  # 목번호: 목번호
    목내용: str | None = None  # 목내용: 목내용

class EiacList(BaseModel):
    """[GENERATED] Response model for 고용보험심사위원회 결정문 목록 조회.

    Source: specs/kr/eiacListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    eiac_id: str | None = None  # eiac id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    의결일자: str | None = None  # 의결일자: 의결일자
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class EiacDetail(BaseModel):
    """[GENERATED] Response model for 고용보험심사위원회 결정문 본문 조회.

    Source: specs/kr/eiacInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    사건의분류: str | None = None  # 사건의분류: 사건의 분류
    의결서종류: str | None = None  # 의결서종류: 의결서 종류
    개요: str | None = None  # 개요: 개요
    사건번호: str | None = None  # 사건번호: 사건번호
    사건명: str | None = None  # 사건명: 사건명
    청구인: str | None = None  # 청구인: 청구인
    대리인: str | None = None  # 대리인: 대리인
    피청구인: str | None = None  # 피청구인: 피청구인
    이해관계인: str | None = None  # 이해관계인: 이해관계인
    심사결정심사관: str | None = None  # 심사결정심사관: 심사결정심사관
    주문: str | None = None  # 주문: 주문
    청구취지: str | None = None  # 청구취지: 청구취지
    이유: str | None = None  # 이유: 이유
    의결일자: str | None = None  # 의결일자: 의결일자
    기관명: str | None = None  # 기관명: 기관명
    별지: str | None = None  # 별지: 별지
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class ElawList(BaseModel):
    """[GENERATED] Response model for 영문 법령 목록 조회.

    Source: specs/kr/lsEngListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    law_id: str | None = None  # law id: 결과 번호
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    현행연혁코드: str | None = None  # 현행연혁코드: 현행연혁코드
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령명영문: str | None = None  # 법령명영문: 법령명영문
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    자법타법여부: str | None = None  # 자법타법여부: 자법타법여부
    법령상세링크: str | None = None  # 법령상세링크: 법령상세링크

class ElawDetail(BaseModel):
    """[GENERATED] Response model for 영문 법령 본문 조회.

    Source: specs/kr/lsEngInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class ExpcList(BaseModel):
    """[GENERATED] Response model for 법령해석례 목록 조회.

    Source: specs/kr/mobExpcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    expc_id: str | None = None  # expc id: 검색결과번호
    법령해석례일련번호: str | None = None  # 법령해석례일련번호: 법령해석례일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    회신기관코드: str | None = None  # 회신기관코드: 회신기관코드
    회신기관명: str | None = None  # 회신기관명: 회신기관명
    회신일자: str | None = None  # 회신일자: 회신일자
    법령해석례_상세링크: str | None = None  # 법령해석례 상세링크: 법령해석례상세링크

class ExpcDetail(BaseModel):
    """[GENERATED] Response model for 법령해석례 본문 조회.

    Source: specs/kr/mobExpcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class FscList(BaseModel):
    """[GENERATED] Response model for 금융위원회 결정문 목록 조회.

    Source: specs/kr/fscListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    fsc_id: str | None = None  # fsc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    안건명: str | None = None  # 안건명: 안건명
    의결번호: str | None = None  # 의결번호: 의결번호
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class FscDetail(BaseModel):
    """[GENERATED] Response model for 금융위원회 결정문 본문 조회.

    Source: specs/kr/fscInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    기관명: str | None = None  # 기관명: 기관명
    의결번호: str | None = None  # 의결번호: 의결번호
    안건명: str | None = None  # 안건명: 안건명
    조치대상자의인적사항: str | None = None  # 조치대상자의인적사항: 조치대상자의 인적사항
    조치대상: str | None = None  # 조치대상: 조치대상
    조치내용: str | None = None  # 조치내용: 조치내용
    조치이유: str | None = None  # 조치이유: 조치이유
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class FtcList(BaseModel):
    """[GENERATED] Response model for 공정거래위원회 결정문 목록 조회.

    Source: specs/kr/ftcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    ftc_id: str | None = None  # ftc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    문서유형: str | None = None  # 문서유형: 문서유형
    회의종류: str | None = None  # 회의종류: 회의종류
    결정번호: str | None = None  # 결정번호: 결정번호
    결정일자: str | None = None  # 결정일자: 결정일자
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class FtcDetail(BaseModel):
    """[GENERATED] Response model for 공정거래위원회 결정문 본문 조회.

    Source: specs/kr/ftcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    문서유형: str | None = None  # 문서유형: 출력 형태 : 의결서 / 시정권고서
    사건번호: str | None = None  # 사건번호: 사건번호
    사건명: str | None = None  # 사건명: 사건명
    피심정보명: str | None = None  # 피심정보명: 피심정보명
    피심정보내용: str | None = None  # 피심정보내용: 피심정보내용
    의결서종류: str | None = None  # 의결서종류: 의결서종류
    시정권고참조법률: str | None = None  # 시정권고참조법률: 시정권고참조법률
    시정권고사항: str | None = None  # 시정권고사항: 시정권고사항
    시정권고이유: str | None = None  # 시정권고이유: 시정권고이유
    법위반내용: str | None = None  # 법위반내용: 법위반내용
    적용법조: str | None = None  # 적용법조: 적용법조
    법령의적용: str | None = None  # 법령의적용: 법령의적용
    시정기한: str | None = None  # 시정기한: 시정기한
    수락여부통지기간: str | None = None  # 수락여부통지기간: 수락여부통지기간
    수락여부통지기한: str | None = None  # 수락여부통지기한: 수락여부통지기한
    수락거부시의조치: str | None = None  # 수락거부시의조치: 수락거부시의조치
    수락거부시조치방침: str | None = None  # 수락거부시조치방침: 수락거부시조치방침
    별지: str | None = None  # 별지: 별지
    결정요지: str | None = None  # 결정요지: 결정요지

class IaciacList(BaseModel):
    """[GENERATED] Response model for 산업재해보상보험재심사위원회 결정문 목록 조회.

    Source: specs/kr/iaciacListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    iaciac_id: str | None = None  # iaciac id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    사건: str | None = None  # 사건: 시건
    사건번호: str | None = None  # 사건번호: 사건번호
    의결일자: str | None = None  # 의결일자: 의결일자
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class IaciacDetail(BaseModel):
    """[GENERATED] Response model for 산업재해보상보험재심사위원회 결정문 본문 조회.

    Source: specs/kr/iaciacInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    사건대분류: str | None = None  # 사건대분류: 사건 대분류
    사건중분류: str | None = None  # 사건중분류: 사건 중분류
    사건소분류: str | None = None  # 사건소분류: 사건 소분류
    쟁점: str | None = None  # 쟁점: 쟁점
    사건번호: str | None = None  # 사건번호: 사건번호
    의결일자: str | None = None  # 의결일자: 의결일자
    사건: str | None = None  # 사건: 사건
    청구인: str | None = None  # 청구인: 청구인
    재해근로자: str | None = None  # 재해근로자: 재해근로자
    재해자: str | None = None  # 재해자: 재해자
    피재근로자: str | None = None  # 피재근로자: 피재근로자/피재자성명/피재자/피재자(망인)
    진폐근로자: str | None = None  # 진폐근로자: 진폐근로자
    수진자: str | None = None  # 수진자: 수진자
    원처분기관: str | None = None  # 원처분기관: 원처분기관
    주문: str | None = None  # 주문: 주문
    청구취지: str | None = None  # 청구취지: 청구취지
    이유: str | None = None  # 이유: 이유
    별지: str | None = None  # 별지: 별지
    문서제공구분: str | None = None  # 문서제공구분: 문서제공구분(데이터 개방|이유하단 이미지개방)
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class KccList(BaseModel):
    """[GENERATED] Response model for 방송미디어통신위원회 결정문 목록 조회.

    Source: specs/kr/kccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    kcc_id: str | None = None  # kcc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    의결일자: str | None = None  # 의결일자: 의결일자
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class KccDetail(BaseModel):
    """[GENERATED] Response model for 방송미디어통신위원회 결정문 본문 조회.

    Source: specs/kr/kccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    기관명: str | None = None  # 기관명: 기관명
    의결서유형: str | None = None  # 의결서유형: 의결서 유형
    안건번호: str | None = None  # 안건번호: 안건번호
    사건번호: str | None = None  # 사건번호: 사건번호
    안건명: str | None = None  # 안건명: 안건명
    사건명: str | None = None  # 사건명: 사건명
    피심인: str | None = None  # 피심인: 피심인
    피심의인: str | None = None  # 피심의인: 피심의인
    청구인: str | None = None  # 청구인: 청구인
    참고인: str | None = None  # 참고인: 참고인
    원심결정: str | None = None  # 원심결정: 원심결정
    의결일자: str | None = None  # 의결일자: 의결일자
    주문: str | None = None  # 주문: 주문
    이유: str | None = None  # 이유: 이유
    별지: str | None = None  # 별지: 별지
    문서제공구분: str | None = None  # 문서제공구분: 문서제공구분(데이터 개방|이유하단 이미지개방)
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class KcgcgmexpcList(BaseModel):
    """[GENERATED] Response model for 해양경찰청 법령해석 목록.

    Source: specs/kr/cgmExpcKcgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KcgcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 해양경찰청 법령해석 본문.

    Source: specs/kr/cgmExpcKcgInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KcscgmexpcList(BaseModel):
    """[GENERATED] Response model for 관세청 법령해석 목록 조회.

    Source: specs/kr/cgmExpcKcsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KcscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 관세청 법령해석 본문 조회.

    Source: specs/kr/cgmExpcKcsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    업무분야: str | None = None  # 업무분야: 업무분야
    안건명: str | None = None  # 안건명: 안건명
    해석일자: str | None = None  # 해석일자: 해석일자
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    관리기관코드: str | None = None  # 관리기관코드: 관리기관코드
    등록일시: str | None = None  # 등록일시: 등록일시
    질의요지: str | None = None  # 질의요지: 질의요지
    회답: str | None = None  # 회답: 회답
    이유: str | None = None  # 이유: 이유
    관련법령: str | None = None  # 관련법령: 관련법령
    관세법령정보포털원문링크: str | None = None  # 관세법령정보포털원문링크: 관세법령정보포털원문링크
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시

class KdcacgmexpcList(BaseModel):
    """[GENERATED] Response model for 질병관리청 법령해석 목록.

    Source: specs/kr/cgmExpcKdcaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KdcacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 질병관리청 법령해석 본문.

    Source: specs/kr/cgmExpcKdcaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KfscgmexpcList(BaseModel):
    """[GENERATED] Response model for 산림청 법령해석 목록.

    Source: specs/kr/cgmExpcKfsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KfscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 산림청 법령해석 본문.

    Source: specs/kr/cgmExpcKfsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KhscgmexpcList(BaseModel):
    """[GENERATED] Response model for 국가유산청 법령해석 목록.

    Source: specs/kr/cgmExpcKhsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KhscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국가유산청 법령해석 본문.

    Source: specs/kr/cgmExpcKhsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KipocgmexpcList(BaseModel):
    """[GENERATED] Response model for 지식재산처 법령해석 목록.

    Source: specs/kr/cgmExpcKipoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KipocgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 지식재산처 법령해석 본문.

    Source: specs/kr/cgmExpcKipoInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KmacgmexpcList(BaseModel):
    """[GENERATED] Response model for 기상청 법령해석 목록.

    Source: specs/kr/cgmExpcKmaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KmacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 기상청 법령해석 본문.

    Source: specs/kr/cgmExpcKmaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KmstspecialdeccList(BaseModel):
    """[GENERATED] Response model for 해양안전심판원 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccKmstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(EvtNm:재결례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    decc_id: str | None = None  # decc id: 검색결과번호
    특별행정심판재결례_일련번호: str | None = None  # 특별행정심판재결례 일련번호: 특별행정심판재결례일련번호
    사건명: str | None = None  # 사건명: 사건명
    재결번호: str | None = None  # 재결번호: 재결번호
    처분일자: str | None = None  # 처분일자: 처분일자
    의결일자: str | None = None  # 의결일자: 의결일자
    처분청: str | None = None  # 처분청: 처분청
    재결청: str | None = None  # 재결청: 재결청
    재결구분명: str | None = None  # 재결구분명: 재결구분명
    재결구분코드: str | None = None  # 재결구분코드: 재결구분코드
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    행정심판재결례_상세링크: str | None = None  # 행정심판재결례 상세링크: 행정심판재결례상세링크

class KmstspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 해양안전심판원 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccKmstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KostatcgmexpcList(BaseModel):
    """[GENERATED] Response model for 국가데이터처 법령해석 목록.

    Source: specs/kr/cgmExpcKostatListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class KostatcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국가데이터처 법령해석 본문.

    Source: specs/kr/cgmExpcKostatInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LawList(BaseModel):
    """[GENERATED] Response model for 법령 목록 조회.

    Source: specs/kr/mobLsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    law_id: str | None = None  # law id: 결과 번호
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    현행연혁코드: str | None = None  # 현행연혁코드: 현행연혁코드
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령약칭명: str | None = None  # 법령약칭명: 법령약칭명
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    공동부령구분: str | None = None  # 공동부령구분: 공동부령구분
    시행일자: str | None = None  # 시행일자: 시행일자
    자법타법여부: str | None = None  # 자법타법여부: 자법타법여부
    법령상세링크: str | None = None  # 법령상세링크: 법령상세링크

class LawDetail(BaseModel):
    """[GENERATED] Response model for 법령 본문 조회.

    Source: specs/kr/mobLsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LawjosubList(BaseModel):
    """[GENERATED] Response model for 현행법령(공포일) 본문 조항호목 조회.

    Source: specs/kr/lsNwJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    법령키: str | None = None  # 법령키: 법령키
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    언어: str | None = None  # 언어: 언어 구분
    법령명_한글: str | None = None  # 법령명_한글: 법령명을 한글로 제공
    법령명_한자: str | None = None  # 법령명_한자: 법령명을 한자로 제공
    법종구분코드: str | None = None  # 법종구분코드: 법종구분코드
    법종구분명: str | None = None  # 법종구분명: 법종구분명
    제명변경여부: str | None = None  # 제명변경여부: 제명변경여부 (Y값이 있으면 해당 법령은 제명 변경임)
    한글법령여부: str | None = None  # 한글법령여부: 한글법령여부 (Y값이 있으면 해당 법령은 한글법령)
    편장절관: str | None = None  # 편장절관: 편장절관
    소관부처코드: str | None = None  # 소관부처코드: 소관부처 코드
    소관부처: str | None = None  # 소관부처: 소관부처명
    전화번호: str | None = None  # 전화번호: 전화번호
    시행일자: str | None = None  # 시행일자: 시행일자
    제개정구분: str | None = None  # 제개정구분: 제개정구분명
    제안구분: str | None = None  # 제안구분: 제안구분
    의결구분: str | None = None  # 의결구분: 의결구분
    이전법령명: str | None = None  # 이전법령명: 이전법령명
    조문별_시행일자: str | None = None  # 조문별 시행일자: 조문별시행일자
    조문시행일자문자열: str | None = None  # 조문시행일자문자열: 조문시행일자문자열
    별표시행일자문자열: str | None = None  # 별표시행일자문자열: 별표시행일자문자열
    별표편집여부: str | None = None  # 별표편집여부: 별표편집여부
    공포법령여부: str | None = None  # 공포법령여부: 공포법령여부 (Y값이 있으면 해당 법령은 공포법령임)
    시행일기준_편집여부: str | None = None  # 시행일기준 편집여부: 시행일기준편집여부 (Y값이 있으면 해당 법령은 시행일 기준 편집됨)
    조문번호: str | None = None  # 조문번호: 조문번호
    조문여부: str | None = None  # 조문여부: 조문여부
    조문제목: str | None = None  # 조문제목: 조문제목
    조문시행일자: str | None = None  # 조문시행일자: 조문시행일자
    조문이동이전: str | None = None  # 조문이동이전: 조문이동이전번호
    조문이동이후: str | None = None  # 조문이동이후: 조문이동이후번호
    조문변경여부: str | None = None  # 조문변경여부: 조문변경여부 (Y값이 있으면 해당 조문내에 변경 내용 있음 )
    조문내용: str | None = None  # 조문내용: 조문내용
    항번호: str | None = None  # 항번호: 항번호
    항내용: str | None = None  # 항내용: 항내용
    호번호: str | None = None  # 호번호: 호번호
    호내용: str | None = None  # 호내용: 호내용
    목번호: str | None = None  # 목번호: 목번호
    목내용: str | None = None  # 목내용: 목내용

class LicbylList(BaseModel):
    """[GENERATED] Response model for 법령 별표ㆍ서식 목록 조회.

    Source: specs/kr/mobLsBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LnklsList(BaseModel):
    """[GENERATED] Response model for 법령 기준 자치법규 연계 관련 목록 조회.

    Source: specs/kr/lsOrdinConListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    law_id: str | None = None  # law id: 결과 번호
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령id: str | None = None  # 법령ID: 법령ID
    자치법규_일련번호: str | None = None  # 자치법규 일련번호: 자치법규 일련번호
    자치법규명: str | None = None  # 자치법규명: 자치법규명
    자치법규id: str | None = None  # 자치법규ID: 자치법규ID
    공포일자: str | None = None  # 공포일자: 자치법규 공포일자
    공포번호: str | None = None  # 공포번호: 자치법규 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    자치법규종류: str | None = None  # 자치법규종류: 자치법규종류
    시행일자: str | None = None  # 시행일자: 자치법규 시행일자

class LnkordList(BaseModel):
    """[GENERATED] Response model for 자치법규 기준 법령 연계 관련 목록 조회.

    Source: specs/kr/ordinLsConListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    law_id: str | None = None  # law id: 결과 번호
    자치법규_일련번호: str | None = None  # 자치법규 일련번호: 자치법규 일련번호
    자치법규명: str | None = None  # 자치법규명: 자치법규명
    자치법규id: str | None = None  # 자치법규ID: 자치법규ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    자치법규종류: str | None = None  # 자치법규종류: 자치법규종류
    시행일자: str | None = None  # 시행일자: 시행일자
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령id: str | None = None  # 법령ID: 법령ID

class LsabrvList(BaseModel):
    """[GENERATED] Response model for 법률명 약칭 조회.

    Source: specs/kr/lsAbrvListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    totalcnt: str | None = None  # totalCnt: 검색건수
    law_id: str | None = None  # law id: 결과 번호
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    현행연혁코드: str | None = None  # 현행연혁코드: 현행연혁코드
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령약칭명: str | None = None  # 법령약칭명: 법령약칭명
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    등록일: str | None = None  # 등록일: 등록일
    자법타법여부: str | None = None  # 자법타법여부: 자법타법여부
    법령상세링크: str | None = None  # 법령상세링크: 법령상세링크

class LshistoryList(BaseModel):
    """[GENERATED] Response model for 법령 연혁 목록 조회.

    Source: specs/kr/lsHstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LshistoryDetail(BaseModel):
    """[GENERATED] Response model for 법령 연혁 본문 조회.

    Source: specs/kr/lsHstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LshstinfList(BaseModel):
    """[GENERATED] Response model for 법령 변경이력 목록 조회.

    Source: specs/kr/lsChgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 현재 페이지번호
    law_id: str | None = None  # law id: 검색 결과 순번
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    현행연혁코드: str | None = None  # 현행연혁코드: 현행연혁코드
    법령명한글: str | None = None  # 법령명한글: 법령명한글
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    자법타법여부: str | None = None  # 자법타법여부: 자법타법여부
    법령상세링크: str | None = None  # 법령상세링크: 법령상세링크

class LsjohstinfList(BaseModel):
    """[GENERATED] Response model for 조문별 변경 이력 목록 조회.

    Source: specs/kr/lsJoChgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    법령id: str | None = None  # 법령ID: 법령ID
    법령명한글: str | None = None  # 법령명한글: 법령명(한글)
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    조문번호: str | None = None  # 조문번호: 조문번호
    변경사유: str | None = None  # 변경사유: 변경사유
    조문링크: str | None = None  # 조문링크: 변경사유
    조문변경일: str | None = None  # 조문변경일: 조문변경일

class LsstmdList(BaseModel):
    """[GENERATED] Response model for 법령 체계도 목록 조회.

    Source: specs/kr/lsStmdListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    numofrows: str | None = None  # numOfRows: 페이지 당 출력 결과 수
    resultcode: str | None = None  # resultCode: 조회 여부(성공 : 00 / 실패 : 01)
    resultmsg: str | None = None  # resultMsg: 조회 여부(성공 : success / 실패 : fail)
    law_id: str | None = None  # law id: 검색 결과 순번
    법령_일련번호: str | None = None  # 법령 일련번호: 법령 일련번호
    법령명: str | None = None  # 법령명: 법령명
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    본문_상세링크: str | None = None  # 본문 상세링크: 본문 상세링크

class LsstmdDetail(BaseModel):
    """[GENERATED] Response model for 법령 체계도 본문 조회.

    Source: specs/kr/lsStmdInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    기본정보: str | None = None  # 기본정보: 기본정보
    법령id: str | None = None  # 법령ID: 법령ID
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    법종구분: str | None = None  # 법종구분: 법종구분
    법령명: str | None = None  # 법령명: 법령
    시행일자: str | None = None  # 시행일자: 시행일자
    제개정구분: str | None = None  # 제개정구분: 제개정구분
    상하위법: str | None = None  # 상하위법: 상하위법
    법률: str | None = None  # 법률: 법률
    시행령: str | None = None  # 시행령: 시행령
    시행규칙: str | None = None  # 시행규칙: 시행규칙
    본문_상세링크: str | None = None  # 본문 상세링크: 본문 상세링크

class LstrmList(BaseModel):
    """[GENERATED] Response model for 법령 용어 목록 조회.

    Source: specs/kr/mobLsTrmListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색건수
    page: str | None = None  # page: 결과페이지번호
    lstrm_id: str | None = None  # lstrm id: 결과 번호
    법령용어id: str | None = None  # 법령용어ID: 법령용어ID
    법령용어명: str | None = None  # 법령용어명: 법령용어명
    법령용어상세검색: str | None = None  # 법령용어상세검색: 법령용어상세검색
    사전구분코드: str | None = None  # 사전구분코드: 사전구분코드(법령용어사전 : 011401, 법령정의사전 : 011402, 법령한영사전 : 011403)
    법령용어상세링크: str | None = None  # 법령용어상세링크: 법령용어상세링크
    법령종류코드: str | None = None  # 법령종류코드: 법령 종류 코드(법령 : 010101, 행정규칙 : 010102)

class LstrmDetail(BaseModel):
    """[GENERATED] Response model for 법령 용어 본문 조회.

    Source: specs/kr/lsTrmInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    법령용어_일련번호: str | None = None  # 법령용어 일련번호: 법령용어 일련번호
    법령용어명_한글: str | None = None  # 법령용어명_한글: 법령용어명 한글
    법령용어명_한자: str | None = None  # 법령용어명_한자: 법령용어명한자
    법령용어코드: str | None = None  # 법령용어코드: 법령용어코드
    법령용어코드명: str | None = None  # 법령용어코드명: 법령용어코드명
    출처: str | None = None  # 출처: 출처
    법령용어정의: str | None = None  # 법령용어정의: 법령용어정의

class MafracgmexpcList(BaseModel):
    """[GENERATED] Response model for 농림축산식품부 법령해석 목록.

    Source: specs/kr/cgmExpcMafraListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MafracgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 농림축산식품부 법령해석 본문.

    Source: specs/kr/cgmExpcMafraInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class McstcgmexpcList(BaseModel):
    """[GENERATED] Response model for 문화체육관광부 법령해석 목록.

    Source: specs/kr/cgmExpcMcstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class McstcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 문화체육관광부 법령해석 본문.

    Source: specs/kr/cgmExpcMcstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MecgmexpcList(BaseModel):
    """[GENERATED] Response model for 기후에너지환경부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMeListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MecgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 기후에너지환경부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMeInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MfdscgmexpcList(BaseModel):
    """[GENERATED] Response model for 식품의약품안전처 법령해석 목록.

    Source: specs/kr/cgmExpcMfdsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MfdscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 식품의약품안전처 법령해석 본문.

    Source: specs/kr/cgmExpcMfdsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MmacgmexpcList(BaseModel):
    """[GENERATED] Response model for 병무청 법령해석 목록.

    Source: specs/kr/cgmExpcMmaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MmacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 병무청 법령해석 본문.

    Source: specs/kr/cgmExpcMmaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MndcgmexpcList(BaseModel):
    """[GENERATED] Response model for 국방부 법령해석 목록.

    Source: specs/kr/cgmExpcMndListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MndcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국방부 법령해석 본문.

    Source: specs/kr/cgmExpcMndInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoecgmexpcList(BaseModel):
    """[GENERATED] Response model for 교육부 법령해석 목록.

    Source: specs/kr/cgmExpcMoeListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MoecgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 교육부 법령해석 본문.

    Source: specs/kr/cgmExpcMoeInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoefcgmexpcList(BaseModel):
    """[GENERATED] Response model for 재정경제부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMoefListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoelcgmexpcList(BaseModel):
    """[GENERATED] Response model for 고용노동부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMoelListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoelcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 고용노동부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMoelInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MofcgmexpcList(BaseModel):
    """[GENERATED] Response model for 해양수산부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMofListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MofcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 해양수산부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMofInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MofacgmexpcList(BaseModel):
    """[GENERATED] Response model for 외교부 법령해석 목록.

    Source: specs/kr/cgmExpcMofaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MofacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 외교부 법령해석 본문.

    Source: specs/kr/cgmExpcMofaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MogefcgmexpcList(BaseModel):
    """[GENERATED] Response model for 성평등가족부 법령해석 목록.

    Source: specs/kr/cgmExpcMogefListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MogefcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 성평등가족부 법령해석 본문.

    Source: specs/kr/cgmExpcMogefInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MohwcgmexpcList(BaseModel):
    """[GENERATED] Response model for 보건복지부 법령해석 목록.

    Source: specs/kr/cgmExpcMohwListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MohwcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 보건복지부 법령해석 본문.

    Source: specs/kr/cgmExpcMohwInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoiscgmexpcList(BaseModel):
    """[GENERATED] Response model for 행정안전부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMoisListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoiscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 행정안전부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMoisInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MojcgmexpcList(BaseModel):
    """[GENERATED] Response model for 법무부 법령해석 목록.

    Source: specs/kr/cgmExpcMojListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MojcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 법무부 법령해석 본문.

    Source: specs/kr/cgmExpcMojInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MolegcgmexpcList(BaseModel):
    """[GENERATED] Response model for 법제처 법령해석 목록.

    Source: specs/kr/cgmExpcMolegListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MolegcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 법제처 법령해석 본문.

    Source: specs/kr/cgmExpcMolegInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MolitcgmexpcList(BaseModel):
    """[GENERATED] Response model for 국토교통부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMolitListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MolitcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국토교통부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMolitInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MotiecgmexpcList(BaseModel):
    """[GENERATED] Response model for 산업통상부 법령해석 목록.

    Source: specs/kr/cgmExpcMotieListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MotiecgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 산업통상부 법령해석 본문.

    Source: specs/kr/cgmExpcMotieInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MoucgmexpcList(BaseModel):
    """[GENERATED] Response model for 통일부 법령해석 목록.

    Source: specs/kr/cgmExpcMouListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MoucgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 통일부 법령해석 본문.

    Source: specs/kr/cgmExpcMouInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MpmcgmexpcList(BaseModel):
    """[GENERATED] Response model for 인사혁신처 법령해석 목록.

    Source: specs/kr/cgmExpcMpmListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MpmcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 인사혁신처 법령해석 본문.

    Source: specs/kr/cgmExpcMpmInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MpvacgmexpcList(BaseModel):
    """[GENERATED] Response model for 국가보훈부 법령해석 목록.

    Source: specs/kr/cgmExpcMpvaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MpvacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국가보훈부 법령해석 본문.

    Source: specs/kr/cgmExpcMpvaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MsitcgmexpcList(BaseModel):
    """[GENERATED] Response model for 과학기술정보통신부 법령해석 목록.

    Source: specs/kr/cgmExpcMsitListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MsitcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 과학기술정보통신부 법령해석 본문.

    Source: specs/kr/cgmExpcMsitInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MsscgmexpcList(BaseModel):
    """[GENERATED] Response model for 중소벤처기업부 법령해석 목록.

    Source: specs/kr/cgmExpcMssListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class MsscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 중소벤처기업부 법령해석 본문.

    Source: specs/kr/cgmExpcMssInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NaacccgmexpcList(BaseModel):
    """[GENERATED] Response model for 행정중심복합도시건설청 법령해석 목록.

    Source: specs/kr/cgmExpcNaaccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class NaacccgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 행정중심복합도시건설청 법령해석 본문.

    Source: specs/kr/cgmExpcNaaccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NfacgmexpcList(BaseModel):
    """[GENERATED] Response model for 소방청 법령해석 목록.

    Source: specs/kr/cgmExpcNfaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class NfacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 소방청 법령해석 본문.

    Source: specs/kr/cgmExpcNfaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NhrckList(BaseModel):
    """[GENERATED] Response model for 국가인권위원회 결정문 목록 조회.

    Source: specs/kr/nhrckListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    nhrck_id: str | None = None  # nhrck id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    의결일자: str | None = None  # 의결일자: 의결일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class NhrckDetail(BaseModel):
    """[GENERATED] Response model for 국가인권위원회 결정문 본문 조회.

    Source: specs/kr/nhrckInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문일련번호
    기관명: str | None = None  # 기관명: 기관명
    위원회명: str | None = None  # 위원회명: 위원회명
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    의결일자: str | None = None  # 의결일자: 의결일자
    주문: str | None = None  # 주문: 주문
    이유: str | None = None  # 이유: 이유
    위원정보: str | None = None  # 위원정보: 위원정보
    별지: str | None = None  # 별지: 별지
    결정요지: str | None = None  # 결정요지: 결정요지
    판단요지: str | None = None  # 판단요지: 판단요지
    주문요지: str | None = None  # 주문요지: 주문요지
    분류명: str | None = None  # 분류명: 분류명
    결정유형: str | None = None  # 결정유형: 결정유형
    신청인: str | None = None  # 신청인: 신청인
    피신청인: str | None = None  # 피신청인: 피신청인
    피해자: str | None = None  # 피해자: 피해자
    피조사자: str | None = None  # 피조사자: 피조사자
    원본다운로드_url: str | None = None  # 원본다운로드 URL: 원본다운로드URL
    바로보기_url: str | None = None  # 바로보기 URL: 바로보기URL
    결정례전문: str | None = None  # 결정례전문: 결정례전문
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시

class NlrcList(BaseModel):
    """[GENERATED] Response model for 노동위원회 결정문 목록 조회.

    Source: specs/kr/nlrcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    nlrc_id: str | None = None  # nlrc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    제목: str | None = None  # 제목: 제목
    사건번호: str | None = None  # 사건번호: 사건번호
    등록일: str | None = None  # 등록일: 등록일
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class NlrcDetail(BaseModel):
    """[GENERATED] Response model for 노동위원회 결정문 본문 조회.

    Source: specs/kr/nlrcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    기관명: str | None = None  # 기관명: 기관명
    사건번호: str | None = None  # 사건번호: 사건번호
    자료구분: str | None = None  # 자료구분: 자료구분
    담당부서: str | None = None  # 담당부서: 담당부서
    등록일: str | None = None  # 등록일: 등록일
    제목: str | None = None  # 제목: 제목
    내용: str | None = None  # 내용: 내용
    판정사항: str | None = None  # 판정사항: 판정사항
    판정요지: str | None = None  # 판정요지: 판정요지
    판정결과: str | None = None  # 판정결과: 판정결과
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class NpacgmexpcList(BaseModel):
    """[GENERATED] Response model for 경찰청 법령해석 목록.

    Source: specs/kr/cgmExpcNpaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class NpacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 경찰청 법령해석 본문.

    Source: specs/kr/cgmExpcNpaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NtscgmexpcList(BaseModel):
    """[GENERATED] Response model for 국세청 법령해석 목록 조회.

    Source: specs/kr/cgmExpcNtsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OcltList(BaseModel):
    """[GENERATED] Response model for 중앙토지수용위원회 결정문 목록 조회.

    Source: specs/kr/ocltListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    oclt_id: str | None = None  # oclt id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    제목: str | None = None  # 제목: 제목
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class OcltDetail(BaseModel):
    """[GENERATED] Response model for 중앙토지수용위원회 결정문 본문 조회.

    Source: specs/kr/ocltInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    제목: str | None = None  # 제목: 제목
    관련법리: str | None = None  # 관련법리: 관련 법리
    관련규정: str | None = None  # 관련규정: 관련 규정
    판단: str | None = None  # 판단: 판단
    근거: str | None = None  # 근거: 근거
    주해: str | None = None  # 주해: 주해
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class OkacgmexpcList(BaseModel):
    """[GENERATED] Response model for 재외동포청 법령해석 목록.

    Source: specs/kr/cgmExpcOkaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class OkacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 재외동포청 법령해석 본문.

    Source: specs/kr/cgmExpcOkaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OldandnewList(BaseModel):
    """[GENERATED] Response model for 신구법 목록 조회.

    Source: specs/kr/oldAndNewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    numofrows: str | None = None  # numOfRows: 페이지 당 출력 결과 수
    resultcode: str | None = None  # resultCode: 조회 여부(성공 : 00 / 실패 : 01)
    resultmsg: str | None = None  # resultMsg: 조회 여부(성공 : success / 실패 : fail)
    oldandnew_id: str | None = None  # oldAndNew id: 검색 결과 순번
    신구법_일련번호: str | None = None  # 신구법 일련번호: 신구법 일련번호
    현행연혁구분: str | None = None  # 현행연혁구분: 현행연혁코드
    신구법명: str | None = None  # 신구법명: 신구법명
    신구법id: str | None = None  # 신구법ID: 신구법ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    신구법_상세링크: str | None = None  # 신구법 상세링크: 신구법 상세링크

class OldandnewDetail(BaseModel):
    """[GENERATED] Response model for 신구법 본문 조회.

    Source: specs/kr/oldAndNewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    구조문_기본정보: str | None = None  # 구조문_ 기본정보: 구조문_기본정보
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    법령id: str | None = None  # 법령ID: 법령ID
    시행일자: str | None = None  # 시행일자: 시행일자
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    현행여부: str | None = None  # 현행여부: 현행여부
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    법령명: str | None = None  # 법령명: 법령
    법종구분: str | None = None  # 법종구분: 법종구분
    신조문_기본정보: str | None = None  # 신조문_ 기본정보: 구조문과 동일한 기본 정보 들어가 있음.
    구조문목록: str | None = None  # 구조문목록: 구조문목록
    조문: str | None = None  # 조문: 조문
    신조문목록: str | None = None  # 신조문목록: 신조문목록
    신구법_존재여부: str | None = None  # 신구법 존재여부: 신구법이 존재하지 않을 경우 N이 조회.

class OneviewList(BaseModel):
    """[GENERATED] Response model for 한눈보기 목록 조회.

    Source: specs/kr/oneViewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    법령_id: str | None = None  # 법령 id: 검색결과번호
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    법령명: str | None = None  # 법령명: 법령명
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    시행일자: str | None = None  # 시행일자: 시행일자
    제공건수: str | None = None  # 제공건수: 제공건수
    제공일자: str | None = None  # 제공일자: 제공일자

class OneviewDetail(BaseModel):
    """[GENERATED] Response model for 한눈보기 본문 조회.

    Source: specs/kr/oneViewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    패턴일련번호: str | None = None  # 패턴일련번호: 패턴일련번호
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    법령명: str | None = None  # 법령명: 법령명
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    조문시행일자: str | None = None  # 조문시행일자: 조문시행일자
    최초제공일자: str | None = None  # 최초제공일자: 최초제공일자
    조번호: str | None = None  # 조번호: 조번호
    조제목: str | None = None  # 조제목: 조제목
    콘텐츠제목: str | None = None  # 콘텐츠제목: 콘텐츠제목
    링크텍스트: str | None = None  # 링크텍스트: 링크텍스트
    링크url: str | None = None  # 링크URL: 링크URL

class OrdinList(BaseModel):
    """[GENERATED] Response model for 자치법규 목록 조회.

    Source: specs/kr/mobOrdinListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(ordinNm:자치법규명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    law_id: str | None = None  # law id: 검색결과번호
    자치법규일련번호: str | None = None  # 자치법규일련번호: 자치법규일련번호
    자치법규명: str | None = None  # 자치법규명: 자치법규명
    자치법규id: str | None = None  # 자치법규ID: 자치법규ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    지자체기관명: str | None = None  # 지자체기관명: 지자체기관명
    자치법규종류: str | None = None  # 자치법규종류: 자치법규종류
    시행일자: str | None = None  # 시행일자: 시행일자
    자치법규_상세링크: str | None = None  # 자치법규 상세링크: 자치법규상세링크
    자치법규분야명: str | None = None  # 자치법규분야명: 자치법규분야명
    참조데이터구분: str | None = None  # 참조데이터구분: 참조데이터구분

class OrdinDetail(BaseModel):
    """[GENERATED] Response model for 자치법규 본문 조회.

    Source: specs/kr/mobOrdinInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OrdinbylList(BaseModel):
    """[GENERATED] Response model for 자치법규 별표ㆍ서식 목록 조회.

    Source: specs/kr/mobOrdinBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class PpcList(BaseModel):
    """[GENERATED] Response model for 개인정보보호위원회 결정문 목록 조회.

    Source: specs/kr/ppcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    ppc_id: str | None = None  # ppc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    안건명: str | None = None  # 안건명: 안건명
    의안번호: str | None = None  # 의안번호: 의안번호
    회의종류: str | None = None  # 회의종류: 회의종류
    결정구분: str | None = None  # 결정구분: 결정구분
    의결일: str | None = None  # 의결일: 의결일
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class PpcDetail(BaseModel):
    """[GENERATED] Response model for 개인정보보호위원회 결정문 본문 조회.

    Source: specs/kr/ppcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    기관명: str | None = None  # 기관명: 기관명
    결정: str | None = None  # 결정: 결정
    회의종류: str | None = None  # 회의종류: 회의종류
    안건번호: str | None = None  # 안건번호: 안건번호
    안건명: str | None = None  # 안건명: 안건명
    신청인: str | None = None  # 신청인: 신청인
    의결연월일: str | None = None  # 의결연월일: 의결연월일
    주문: str | None = None  # 주문: 주문
    이유: str | None = None  # 이유: 이유
    배경: str | None = None  # 배경: 배경
    이의제기방법및기간: str | None = None  # 이의제기방법및기간: 이의제기방법및기간
    주요내용: str | None = None  # 주요내용: 주요내용
    의결일자: str | None = None  # 의결일자: 의결일자
    위원서명: str | None = None  # 위원서명: 위원서명
    별지: str | None = None  # 별지: 별지
    결정요지: str | None = None  # 결정요지: 결정요지

class PpscgmexpcList(BaseModel):
    """[GENERATED] Response model for 조달청 법령해석 목록.

    Source: specs/kr/cgmExpcPpsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class PpscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 조달청 법령해석 본문.

    Source: specs/kr/cgmExpcPpsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class PrecList(BaseModel):
    """[GENERATED] Response model for 판례 목록 조회.

    Source: specs/kr/mobPrecListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 검색어
    section: str | None = None  # section: 검색범위(EvtNm:판례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    prec_id: str | None = None  # prec id: 검색결과번호
    판례일련번호: str | None = None  # 판례일련번호: 판례일련번호
    사건명: str | None = None  # 사건명: 사건명
    사건번호: str | None = None  # 사건번호: 사건번호
    선고일자: str | None = None  # 선고일자: 선고일자
    법원명: str | None = None  # 법원명: 법원명
    법원종류코드: str | None = None  # 법원종류코드: 법원종류코드(대법원:400201, 하위법원:400202)
    사건종류명: str | None = None  # 사건종류명: 사건종류명
    사건종류코드: str | None = None  # 사건종류코드: 사건종류코드
    판결유형: str | None = None  # 판결유형: 판결유형
    선고: str | None = None  # 선고: 선고
    데이터출처명: str | None = None  # 데이터출처명: 데이터출처명
    판례상세링크: str | None = None  # 판례상세링크: 판례상세링크

class PrecDetail(BaseModel):
    """[GENERATED] Response model for 판례 본문 조회.

    Source: specs/kr/mobPrecInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class RdacgmexpcList(BaseModel):
    """[GENERATED] Response model for 농촌진흥청 법령해석 목록.

    Source: specs/kr/cgmExpcRdaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(lawNm:법령해석명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    id: str | None = None  # id: 검색결과번호
    법령해석일련번호: str | None = None  # 법령해석일련번호: 법령해석일련번호
    안건명: str | None = None  # 안건명: 안건명
    안건번호: str | None = None  # 안건번호: 안건번호
    질의기관코드: str | None = None  # 질의기관코드: 질의기관코드
    질의기관명: str | None = None  # 질의기관명: 질의기관명
    해석기관코드: str | None = None  # 해석기관코드: 해석기관코드
    해석기관명: str | None = None  # 해석기관명: 해석기관명
    해석일자: str | None = None  # 해석일자: 해석일자
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    법령해석_상세링크: str | None = None  # 법령해석 상세링크: 법령해석 상세링크

class RdacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 농촌진흥청 법령해석 본문.

    Source: specs/kr/cgmExpcRdaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class SchoolList(BaseModel):
    """[GENERATED] Response model for 학칙ㆍ공단ㆍ공공기관 목록 조회.

    Source: specs/kr/schlPubRulListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    numofrows: str | None = None  # numOfRows: 페이지 당 출력 결과 수
    resultcode: str | None = None  # resultCode: 조회 여부(성공 : 00 / 실패 : 01)
    resultmsg: str | None = None  # resultMsg: 조회 여부(성공 : success / 실패 : fail)
    admrul_id: str | None = None  # admrul id: 검색 결과 순번
    행정규칙_일련번호: str | None = None  # 행정규칙 일련번호: 학칙공단 일련번호
    행정규칙명: str | None = None  # 행정규칙명: 학칙공단명
    행정규칙종류: str | None = None  # 행정규칙종류: 학칙공단 종류
    발령일자: str | None = None  # 발령일자: 발령일자
    발령번호: str | None = None  # 발령번호: 발령번호
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    현행연혁구분: str | None = None  # 현행연혁구분: 현행연혁구분
    제개정_구분코드: str | None = None  # 제개정 구분코드: 제개정구분코드
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    법령분류코드: str | None = None  # 법령분류코드: 법령분류코드
    법령분류명: str | None = None  # 법령분류명: 법령분류명
    행정규칙id: str | None = None  # 행정규칙ID: 학칙공단ID
    행정규칙_상세링크: str | None = None  # 행정규칙 상세링크: 학칙공단 상세링크
    시행일자: str | None = None  # 시행일자: 시행일자
    생성일자: str | None = None  # 생성일자: 생성일자

class SchoolDetail(BaseModel):
    """[GENERATED] Response model for 학칙ㆍ공단ㆍ공공기관 본문 조회.

    Source: specs/kr/schlPubRulInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    행정규칙_일련번호: str | None = None  # 행정규칙 일련번호: 학칙공단 일련번호
    행정규칙명: str | None = None  # 행정규칙명: 학칙공단명
    행정규칙종류: str | None = None  # 행정규칙종류: 학칙공단 종류
    행정규칙종류코드: str | None = None  # 행정규칙종류코드: 학칙공단 종류코드
    발령일자: str | None = None  # 발령일자: 발령일자
    발령번호: str | None = None  # 발령번호: 발령번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    제개정_구분코드: str | None = None  # 제개정 구분코드: 제개정구분코드
    조문형식여부: str | None = None  # 조문형식여부: 조문형식여부
    행정규칙id: str | None = None  # 행정규칙ID: 학칙공단ID
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    담당부서기관코드: str | None = None  # 담당부서기관코드: 담당부서기관코드
    담당부서기관명: str | None = None  # 담당부서기관명: 담당부서기관명
    담당자명: str | None = None  # 담당자명: 담당자명
    전화번호: str | None = None  # 전화번호: 전화번호
    현행여부: str | None = None  # 현행여부: 현행여부
    생성일자: str | None = None  # 생성일자: 생성일자
    조문내용: str | None = None  # 조문내용: 조문내용
    부칙공포일자: str | None = None  # 부칙공포일자: 부칙 공포일자
    부칙공포번호: str | None = None  # 부칙공포번호: 부칙 공포번호
    부칙내용: str | None = None  # 부칙내용: 부칙내용
    별표단위_별표키: str | None = None  # 별표단위 별표키: 별표단위 별표키
    별표번호: str | None = None  # 별표번호: 별표번호
    별표가지번호: str | None = None  # 별표가지번호: 별표가지번호
    별표구분: str | None = None  # 별표구분: 별표구분
    별표제목: str | None = None  # 별표제목: 별표제목
    별표서식_파일링크: str | None = None  # 별표서식 파일링크: 별표서식 파일링크
    개정문내용: str | None = None  # 개정문내용: 개정문내용
    제개정이유내용: str | None = None  # 제개정이유내용: 제개정이유내용

class SfcList(BaseModel):
    """[GENERATED] Response model for 증권선물위원회 결정문 목록 조회.

    Source: specs/kr/sfcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    기관명: str | None = None  # 기관명: 위원회명
    sfc_id: str | None = None  # sfc id: 검색 결과 순번
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    안건명: str | None = None  # 안건명: 안건명
    의결번호: str | None = None  # 의결번호: 의결번호
    결정문_상세링크: str | None = None  # 결정문 상세링크: 결정문 상세링크

class SfcDetail(BaseModel):
    """[GENERATED] Response model for 증권선물위원회 결정문 본문 조회.

    Source: specs/kr/sfcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    결정문_일련번호: str | None = None  # 결정문 일련번호: 결정문 일련번호
    기관명: str | None = None  # 기관명: 기관명
    의결번호: str | None = None  # 의결번호: 의결번호
    안건명: str | None = None  # 안건명: 안건명
    조치대상자의인적사항: str | None = None  # 조치대상자의인적사항: 조치대상자의 인적사항
    조치대상: str | None = None  # 조치대상: 조치대상
    조치내용: str | None = None  # 조치내용: 조치내용
    조치이유: str | None = None  # 조치이유: 조치이유
    각주번호: str | None = None  # 각주번호: 각주번호
    각주내용: str | None = None  # 각주내용: 각주내용

class ThdcmpList(BaseModel):
    """[GENERATED] Response model for 3단 비교 목록 조회.

    Source: specs/kr/thdCmpListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색서비스 대상
    키워드: str | None = None  # 키워드: 검색 단어
    section: str | None = None  # section: 검색범위
    totalcnt: str | None = None  # totalCnt: 검색 건수
    page: str | None = None  # page: 현재 페이지번호
    numofrows: str | None = None  # numOfRows: 페이지 당 출력 결과 수
    resultcode: str | None = None  # resultCode: 조회 여부(성공 : 00 / 실패 : 01)
    resultmsg: str | None = None  # resultMsg: 조회 여부(성공 : success / 실패 : fail)
    thdcmp_id: str | None = None  # thdCmp id: 검색결과 순번
    삼단비교_일련번호: str | None = None  # 삼단비교 일련번호: 삼단비교 일련번호
    법령명_한글: str | None = None  # 법령명 한글: 법령명 한글
    법령id: str | None = None  # 법령ID: 법령ID
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    제개정구분명: str | None = None  # 제개정구분명: 제개정구분명
    소관부처코드: str | None = None  # 소관부처코드: 소관부처코드
    소관부처명: str | None = None  # 소관부처명: 소관부처명
    법령구분명: str | None = None  # 법령구분명: 법령구분명
    시행일자: str | None = None  # 시행일자: 시행일자
    인용조문_삼단비교상세링크: str | None = None  # 인용조문_삼단비교상세링크: 인용조문_삼단비교 상세링크
    위임조문_삼단비교상세링크: str | None = None  # 위임조문_삼단비교상세링크: 위임조문_삼단비교 상세링크

class ThdcmpDetail(BaseModel):
    """[GENERATED] Response model for 3단 비교 본문 조회.

    Source: specs/kr/thdCmpInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    기본정보: str | None = None  # 기본정보: 위임 삼단비교 기본정보
    법령id: str | None = None  # 법령ID: 법령 ID
    법령일련번호: str | None = None  # 법령일련번호: 법령일련번호
    공포일자: str | None = None  # 공포일자: 공포일자
    공포번호: str | None = None  # 공포번호: 공포번호
    법종구분: str | None = None  # 법종구분: 법종 구분
    법령명: str | None = None  # 법령명: 법령 명
    시행일자: str | None = None  # 시행일자: 시행일자
    제개정구분: str | None = None  # 제개정구분: 제개정구분
    삼단비교_존재여부: str | None = None  # 삼단비교 존재여부: 삼단비교 존재하지 않으면 N이 조회.
    기준법_법령명: str | None = None  # 기준법 법령명: 기준법 법령명
    기준법령목록: str | None = None  # 기준법령목록: 기준 법령 목록
    위임3비교_상세링크: str | None = None  # 위임3비교 상세링크: 위임조문 3비교 목록 상세링크
    위임조문_삼단비교: str | None = None  # 위임조문 삼단비교: 위임조문 삼단비교
    법률조문: str | None = None  # 법률조문: 법률조문
    조번호: str | None = None  # 조번호: 조번호
    조가지번호: str | None = None  # 조가지번호: 조가지번호
    조제목: str | None = None  # 조제목: 조제목
    조내용: str | None = None  # 조내용: 조내용
    시행령조문: str | None = None  # 시행령조문: 하위 시행령조문
    시행규칙_조문목록: str | None = None  # 시행규칙 조문목록: 시행규칙조문목록
    시행규칙조문: str | None = None  # 시행규칙조문: 하위 시행규칙조문

class TrtyList(BaseModel):
    """[GENERATED] Response model for 조약 목록 조회.

    Source: specs/kr/mobTrtyListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(TrtyNm:조약명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    trty_id: str | None = None  # trty id: 검색결과번호
    조약일련번호: str | None = None  # 조약일련번호: 조약일련번호
    조약명: str | None = None  # 조약명: 조약명
    조약구분코드: str | None = None  # 조약구분코드: 조약구분코드
    조약구분명: str | None = None  # 조약구분명: 조약구분명
    발효일자: str | None = None  # 발효일자: 발효일자
    서명일자: str | None = None  # 서명일자: 서명일자
    관보게재일자: str | None = None  # 관보게재일자: 관보게재일자
    조약번호: str | None = None  # 조약번호: 조약번호
    조약상세링크: str | None = None  # 조약상세링크: 조약상세링크

class TrtyDetail(BaseModel):
    """[GENERATED] Response model for 조약 본문 조회.

    Source: specs/kr/mobTrtyInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class TtspecialdeccList(BaseModel):
    """[GENERATED] Response model for 조세심판원 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccTtListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    target: str | None = None  # target: 검색 대상
    키워드: str | None = None  # 키워드: 키워드
    section: str | None = None  # section: 검색범위(EvtNm:재결례명/bdyText:본문)
    totalcnt: str | None = None  # totalCnt: 검색결과갯수
    page: str | None = None  # page: 출력페이지
    decc_id: str | None = None  # decc id: 검색결과번호
    특별행정심판재결례_일련번호: str | None = None  # 특별행정심판재결례 일련번호: 특별행정심판재결례일련번호
    사건명: str | None = None  # 사건명: 사건명
    청구번호: str | None = None  # 청구번호: 청구번호
    처분일자: str | None = None  # 처분일자: 처분일자
    의결일자: str | None = None  # 의결일자: 의결일자
    처분청: str | None = None  # 처분청: 처분청
    재결청: str | None = None  # 재결청: 재결청
    재결구분명: str | None = None  # 재결구분명: 재결구분명
    재결구분코드: str | None = None  # 재결구분코드: 재결구분코드
    데이터기준일시: str | None = None  # 데이터기준일시: 데이터기준일시
    행정심판재결례_상세링크: str | None = None  # 행정심판재결례 상세링크: 행정심판재결례상세링크

class TtspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 조세심판원 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccTtInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

