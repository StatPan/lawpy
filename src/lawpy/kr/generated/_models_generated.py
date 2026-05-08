"""Auto-generated Pydantic models from specs/kr/*.json + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit by hand.
"""

# ruff: noqa: E501

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class AcrList(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 결정문 목록 조회.

    Source: specs/kr/acrListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    acr_id: str | None = Field(None, alias="acr id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    제목: str | None = Field(None, alias="제목")
    민원표시명: str | None = Field(None, alias="민원표시명")
    의안번호: str | None = Field(None, alias="의안번호")
    회의종류: str | None = Field(None, alias="회의종류")
    결정구분: str | None = Field(None, alias="결정구분")
    의결일: str | None = Field(None, alias="의결일")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class AcrDetail(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 결정문 본문 조회.

    Source: specs/kr/acrInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    회의종류: str | None = Field(None, alias="회의종류")
    결정구분: str | None = Field(None, alias="결정구분")
    의안번호: str | None = Field(None, alias="의안번호")
    민원표시: str | None = Field(None, alias="민원표시")
    제목: str | None = Field(None, alias="제목")
    신청인: str | None = Field(None, alias="신청인")
    대리인: str | None = Field(None, alias="대리인")
    피신청인: str | None = Field(None, alias="피신청인")
    관계기관: str | None = Field(None, alias="관계기관")
    의결일: str | None = Field(None, alias="의결일")
    주문: str | None = Field(None, alias="주문")
    이유: str | None = Field(None, alias="이유")
    별지: str | None = Field(None, alias="별지")
    의결문: str | None = Field(None, alias="의결문")
    의결일자: str | None = Field(None, alias="의결일자")
    위원정보: str | None = Field(None, alias="위원정보")
    결정요지: str | None = Field(None, alias="결정요지")

class AcrspecialdeccList(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccAcrListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    decc_id: str | None = Field(None, alias="decc id")
    특별행정심판재결례_일련번호: str | None = Field(None, alias="특별행정심판재결례 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    처분일자: str | None = Field(None, alias="처분일자")
    의결일자: str | None = Field(None, alias="의결일자")
    처분청: str | None = Field(None, alias="처분청")
    재결청: str | None = Field(None, alias="재결청")
    재결구분명: str | None = Field(None, alias="재결구분명")
    재결구분코드: str | None = Field(None, alias="재결구분코드")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    행정심판재결례_상세링크: str | None = Field(None, alias="행정심판재결례 상세링크")

class AcrspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccAcrInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class AdapspecialdeccList(BaseModel):
    """[GENERATED] Response model for 인사혁신처 소청심사위원회 특별행정심판재결례 목록 조회.

    Source: specs/kr/specialDeccAdapListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    decc_id: str | None = Field(None, alias="decc id")
    특별행정심판재결례_일련번호: str | None = Field(None, alias="특별행정심판재결례 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    처분일자: str | None = Field(None, alias="처분일자")
    의결일자: str | None = Field(None, alias="의결일자")
    처분청: str | None = Field(None, alias="처분청")
    재결청: str | None = Field(None, alias="재결청")
    재결구분명: str | None = Field(None, alias="재결구분명")
    재결구분코드: str | None = Field(None, alias="재결구분코드")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    행정심판재결례_상세링크: str | None = Field(None, alias="행정심판재결례 상세링크")

class AdapspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 인사혁신처 소청심사위원회 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccAdapInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class AdmbylList(BaseModel):
    """[GENERATED] Response model for 행정규칙 별표ㆍ서식 목록 조회.

    Source: specs/kr/admrulBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    admrulbyl_id: str | None = Field(None, alias="admrulbyl id")
    별표일련번호: str | None = Field(None, alias="별표일련번호")
    관련행정규칙_일련번호: str | None = Field(None, alias="관련행정규칙 일련번호")
    별표명: str | None = Field(None, alias="별표명")
    관련행정규칙명: str | None = Field(None, alias="관련행정규칙명")
    별표번호: str | None = Field(None, alias="별표번호")
    별표종류: str | None = Field(None, alias="별표종류")
    소관부처명: str | None = Field(None, alias="소관부처명")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    관련법령id: str | None = Field(None, alias="관련법령ID")
    행정규칙종류: str | None = Field(None, alias="행정규칙종류")
    별표서식파일링크: str | None = Field(None, alias="별표서식파일링크")
    별표행정규칙_상세링크: str | None = Field(None, alias="별표행정규칙 상세링크")

class AdmrulList(BaseModel):
    """[GENERATED] Response model for 행정규칙 목록 조회.

    Source: specs/kr/admrulListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    admrul_id: str | None = Field(None, alias="admrul id")
    행정규칙_일련번호: str | None = Field(None, alias="행정규칙 일련번호")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    행정규칙종류: str | None = Field(None, alias="행정규칙종류")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    소관부처명: str | None = Field(None, alias="소관부처명")
    현행연혁구분: str | None = Field(None, alias="현행연혁구분")
    제개정_구분코드: str | None = Field(None, alias="제개정 구분코드")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    행정규칙_상세링크: str | None = Field(None, alias="행정규칙 상세링크")
    시행일자: str | None = Field(None, alias="시행일자")
    생성일자: str | None = Field(None, alias="생성일자")

class AdmrulDetail(BaseModel):
    """[GENERATED] Response model for 행정규칙 본문 조회.

    Source: specs/kr/admrulInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    행정규칙_일련번호: str | None = Field(None, alias="행정규칙 일련번호")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    행정규칙종류: str | None = Field(None, alias="행정규칙종류")
    행정규칙종류코드: str | None = Field(None, alias="행정규칙종류코드")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    제개정_구분코드: str | None = Field(None, alias="제개정 구분코드")
    조문형식여부: str | None = Field(None, alias="조문형식여부")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    소관부처명: str | None = Field(None, alias="소관부처명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    상위부처명: str | None = Field(None, alias="상위부처명")
    담당부서기관코드: str | None = Field(None, alias="담당부서기관코드")
    담당부서기관명: str | None = Field(None, alias="담당부서기관명")
    담당자명: str | None = Field(None, alias="담당자명")
    전화번호: str | None = Field(None, alias="전화번호")
    현행여부: str | None = Field(None, alias="현행여부")
    시행일자: str | None = Field(None, alias="시행일자")
    생성일자: str | None = Field(None, alias="생성일자")
    조문내용: str | None = Field(None, alias="조문내용")
    부칙: str | None = Field(None, alias="부칙")
    부칙공포일자: str | None = Field(None, alias="부칙공포일자")
    부칙공포번호: str | None = Field(None, alias="부칙공포번호")
    부칙내용: str | None = Field(None, alias="부칙내용")
    별표: str | None = Field(None, alias="별표")
    별표번호: str | None = Field(None, alias="별표번호")
    별표가지번호: str | None = Field(None, alias="별표가지번호")
    별표구분: str | None = Field(None, alias="별표구분")
    별표제목: str | None = Field(None, alias="별표제목")
    별표서식파일링크: str | None = Field(None, alias="별표서식파일링크")
    별표서식pdf파일링크: str | None = Field(None, alias="별표서식PDF파일링크")
    별표내용: str | None = Field(None, alias="별표내용")
    첨부파일: str | None = Field(None, alias="첨부파일")
    첨부파일명: str | None = Field(None, alias="첨부파일명")
    첨부파일링크: str | None = Field(None, alias="첨부파일링크")

class AdmruloldandnewList(BaseModel):
    """[GENERATED] Response model for 행정규칙 신구법 비교 목록 조회.

    Source: specs/kr/admrulOldAndNewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    resultcode: str | None = Field(None, alias="resultCode")
    resultmsg: str | None = Field(None, alias="resultMsg")
    oldandnew_id: str | None = Field(None, alias="oldAndNew id")
    신구법_일련번호: str | None = Field(None, alias="신구법 일련번호")
    현행연혁구분: str | None = Field(None, alias="현행연혁구분")
    신구법명: str | None = Field(None, alias="신구법명")
    신구법id: str | None = Field(None, alias="신구법ID")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    신구법_상세링크: str | None = Field(None, alias="신구법 상세링크")

class AdmruloldandnewDetail(BaseModel):
    """[GENERATED] Response model for 행정규칙 신구법 비교 본문 조회.

    Source: specs/kr/admrulOldAndNewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    구조문_기본정보: str | None = Field(None, alias="구조문_ 기본정보")
    행정규칙일련번호: str | None = Field(None, alias="행정규칙일련번호")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    시행일자: str | None = Field(None, alias="시행일자")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    현행여부: str | None = Field(None, alias="현행여부")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    행정규칙종류: str | None = Field(None, alias="행정규칙종류")
    신조문_기본정보: str | None = Field(None, alias="신조문_ 기본정보")
    구조문목록: str | None = Field(None, alias="구조문목록")
    조문: str | None = Field(None, alias="조문")
    신조문목록: str | None = Field(None, alias="신조문목록")
    신구법_존재여부: str | None = Field(None, alias="신구법 존재여부")

class AirltlsList(BaseModel):
    """[GENERATED] Response model for 지능형 법령검색 시스템 연관법령 API 조회.

    Source: specs/kr/aiRltLsGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    법령조문id: str | None = Field(None, alias="법령조문ID")
    법령id: str | None = Field(None, alias="법령ID")
    법령명: str | None = Field(None, alias="법령명")
    시행일자: str | None = Field(None, alias="시행일자")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    조문번호: str | None = Field(None, alias="조문번호")
    조문가지번호: str | None = Field(None, alias="조문가지번호")
    조문제목: str | None = Field(None, alias="조문제목")
    행정규칙조문_id: str | None = Field(None, alias="행정규칙조문 ID")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")

class AisearchList(BaseModel):
    """[GENERATED] Response model for 지능형 법령검색 시스템 검색 API 조회.

    Source: specs/kr/aiSearchGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    법령조문id: str | None = Field(None, alias="법령조문ID")
    법령id: str | None = Field(None, alias="법령ID")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    법령명: str | None = Field(None, alias="법령명")
    시행일자: str | None = Field(None, alias="시행일자")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령종류명: str | None = Field(None, alias="법령종류명")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    법령편장절관코드: str | None = Field(None, alias="법령편장절관코드")
    조문일련번호: str | None = Field(None, alias="조문일련번호")
    조문번호: str | None = Field(None, alias="조문번호")
    조문가지번호: str | None = Field(None, alias="조문가지번호")
    조문제목: str | None = Field(None, alias="조문제목")
    조문내용: str | None = Field(None, alias="조문내용")
    법령별표서식_id: str | None = Field(None, alias="법령별표서식 ID")
    별표서식_일련번호: str | None = Field(None, alias="별표서식 일련번호")
    별표서식번호: str | None = Field(None, alias="별표서식번호")
    별표서식_가지번호: str | None = Field(None, alias="별표서식 가지번호")
    별표서식제목: str | None = Field(None, alias="별표서식제목")
    별표서식_구분코드: str | None = Field(None, alias="별표서식 구분코드")
    별표서식_구분명: str | None = Field(None, alias="별표서식 구분명")
    행정규칙조문_id: str | None = Field(None, alias="행정규칙조문 ID")
    행정규칙_일련번호: str | None = Field(None, alias="행정규칙 일련번호")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    발령기관명: str | None = Field(None, alias="발령기관명")
    행정규칙_종류명: str | None = Field(None, alias="행정규칙 종류명")
    행정규칙_별표서식id: str | None = Field(None, alias="행정규칙 별표서식ID")

class BaipvcsList(BaseModel):
    """[GENERATED] Response model for 감사원 사전컨설팅 의견서 목록 조회.

    Source: specs/kr/baiPvcsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    baipvcs_id: str | None = Field(None, alias="baiPvcs id")
    감사원사전컨설팅_의견서일련번호: str | None = Field(None, alias="감사원사전컨설팅 의견서일련번호")
    의견서명: str | None = Field(None, alias="의견서명")
    회신일자: str | None = Field(None, alias="회신일자")
    신청기관명: str | None = Field(None, alias="신청기관명")
    접수번호: str | None = Field(None, alias="접수번호")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    감사원_사전컨설팅_의견서_상세링크: str | None = Field(None, alias="감사원 사전컨설팅 의견서 상세링크")

class BaipvcsDetail(BaseModel):
    """[GENERATED] Response model for 감사원 사전컨설팅 의견서 본문 조회.

    Source: specs/kr/baiPvcsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class CouseadmrulList(BaseModel):
    """[GENERATED] Response model for 맞춤형 행정규칙 조문 목록 조회.

    Source: specs/kr/custAdmrulJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    vcode: str | None = Field(None, alias="vcode")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    행정규칙_일련번호: str | None = Field(None, alias="행정규칙 일련번호")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    행정규칙구분명: str | None = Field(None, alias="행정규칙구분명")
    소관부처명: str | None = Field(None, alias="소관부처명")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    담당부서기관코드: str | None = Field(None, alias="담당부서기관코드")
    담당부서기관명: str | None = Field(None, alias="담당부서기관명")
    담당자명: str | None = Field(None, alias="담당자명")
    전화번호: str | None = Field(None, alias="전화번호")
    조문단위_조문키: str | None = Field(None, alias="조문단위 조문키")
    조문번호: str | None = Field(None, alias="조문번호")
    조문가지번호: str | None = Field(None, alias="조문가지번호")
    조문상세링크: str | None = Field(None, alias="조문상세링크")

class CouselsList(BaseModel):
    """[GENERATED] Response model for 맞춤형 법령 조문 목록 조회.

    Source: specs/kr/custLsJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    vcode: str | None = Field(None, alias="vcode")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    법령_법령키: str | None = Field(None, alias="법령 법령키")
    법령id: str | None = Field(None, alias="법령ID")
    법령명한글: str | None = Field(None, alias="법령명한글")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    조문번호: str | None = Field(None, alias="조문번호")
    조문가지번호: str | None = Field(None, alias="조문가지번호")
    조문제목: str | None = Field(None, alias="조문제목")
    조문시행일자: str | None = Field(None, alias="조문시행일자")
    조문제개정유형: str | None = Field(None, alias="조문제개정유형")
    조문제개정일자문자열: str | None = Field(None, alias="조문제개정일자문자열")
    조문상세링크: str | None = Field(None, alias="조문상세링크")

class CouseordinList(BaseModel):
    """[GENERATED] Response model for 맞춤형 자치법규 조문 목록 조회.

    Source: specs/kr/custOrdinJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    vcode: str | None = Field(None, alias="vcode")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    자치법규일련번호: str | None = Field(None, alias="자치법규일련번호")
    자치법규명: str | None = Field(None, alias="자치법규명")
    자치법규id: str | None = Field(None, alias="자치법규ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    자치법규종류: str | None = Field(None, alias="자치법규종류")
    지자체기관명: str | None = Field(None, alias="지자체기관명")
    시행일자: str | None = Field(None, alias="시행일자")
    자치법규분야명: str | None = Field(None, alias="자치법규분야명")
    조문단위_조문키: str | None = Field(None, alias="조문단위 조문키")
    조문번호: str | None = Field(None, alias="조문번호")
    조문가지번호: str | None = Field(None, alias="조문가지번호")
    조문제목: str | None = Field(None, alias="조문제목")
    조문내용: str | None = Field(None, alias="조문내용")

class DapacgmexpcList(BaseModel):
    """[GENERATED] Response model for 방위사업청 법령해석 목록.

    Source: specs/kr/cgmExpcDapaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class DapacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 방위사업청 법령해석 본문.

    Source: specs/kr/cgmExpcDapaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class DeccList(BaseModel):
    """[GENERATED] Response model for 행정심판례 목록 조회.

    Source: specs/kr/deccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    decc_id: str | None = Field(None, alias="decc id")
    행정심판재결례일련번호: str | None = Field(None, alias="행정심판재결례일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    처분일자: str | None = Field(None, alias="처분일자")
    의결일자: str | None = Field(None, alias="의결일자")
    처분청: str | None = Field(None, alias="처분청")
    재결청: str | None = Field(None, alias="재결청")
    재결구분명: str | None = Field(None, alias="재결구분명")
    재결구분코드: str | None = Field(None, alias="재결구분코드")
    행정심판례_상세링크: str | None = Field(None, alias="행정심판례 상세링크")

class DeccDetail(BaseModel):
    """[GENERATED] Response model for 행정심판례 본문 조회.

    Source: specs/kr/deccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    행정심판례일련번호: str | None = Field(None, alias="행정심판례일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    주문: str | None = Field(None, alias="주문")

class DetcList(BaseModel):
    """[GENERATED] Response model for 헌재결정례 목록 조회.

    Source: specs/kr/detcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    detc_id: str | None = Field(None, alias="detc id")
    헌재결정례일련번호: str | None = Field(None, alias="헌재결정례일련번호")
    종국일자: str | None = Field(None, alias="종국일자")
    사건번호: str | None = Field(None, alias="사건번호")
    사건명: str | None = Field(None, alias="사건명")
    헌재결정례_상세링크: str | None = Field(None, alias="헌재결정례 상세링크")

class DetcDetail(BaseModel):
    """[GENERATED] Response model for 헌재결정례 본문 조회.

    Source: specs/kr/detcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    id: str | None = Field(None, alias="ID")
    lm: str | None = Field(None, alias="LM")

class DlytrmList(BaseModel):
    """[GENERATED] Response model for 일상용어 조회.

    Source: specs/kr/dlytrmGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    section: str | None = Field(None, alias="section")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    일상용어_id: str | None = Field(None, alias="일상용어 id")
    일상용어명: str | None = Field(None, alias="일상용어명")
    출처: str | None = Field(None, alias="출처")
    용어간관계_링크: str | None = Field(None, alias="용어간관계 링크")

class DlytrmrltDetail(BaseModel):
    """[GENERATED] Response model for 일상용어-법령용어 연계 조회.

    Source: specs/kr/dlytrmRltGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    일상용어명: str | None = Field(None, alias="일상용어명")
    출처: str | None = Field(None, alias="출처")
    연계용어_id: str | None = Field(None, alias="연계용어 id")
    법령용어명: str | None = Field(None, alias="법령용어명")
    비고: str | None = Field(None, alias="비고")
    용어관계코드: str | None = Field(None, alias="용어관계코드")
    용어관계: str | None = Field(None, alias="용어관계")
    용어간관계_링크: str | None = Field(None, alias="용어간관계 링크")
    조문간관계_링크: str | None = Field(None, alias="조문간관계 링크")

class EccList(BaseModel):
    """[GENERATED] Response model for 중앙환경분쟁조정위원회 결정문 목록 조회.

    Source: specs/kr/eccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    ecc_id: str | None = Field(None, alias="ecc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    의결번호: str | None = Field(None, alias="의결번호")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class EccDetail(BaseModel):
    """[GENERATED] Response model for 중앙환경분쟁조정위원회 결정문 본문 조회.

    Source: specs/kr/eccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    의결번호: str | None = Field(None, alias="의결번호")
    사건명: str | None = Field(None, alias="사건명")
    사건의개요: str | None = Field(None, alias="사건의개요")
    신청인: str | None = Field(None, alias="신청인")
    피신청인: str | None = Field(None, alias="피신청인")
    분쟁의경과: str | None = Field(None, alias="분쟁의경과")
    당사자주장: str | None = Field(None, alias="당사자주장")
    사실조사결과: str | None = Field(None, alias="사실조사결과")
    평가의견: str | None = Field(None, alias="평가의견")
    주문: str | None = Field(None, alias="주문")
    이유: str | None = Field(None, alias="이유")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class EflawList(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 목록 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    law_id: str | None = Field(None, alias="law id")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    현행연혁코드: str | None = Field(None, alias="현행연혁코드")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령약칭명: str | None = Field(None, alias="법령약칭명")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    공동부령구분: str | None = Field(None, alias="공동부령구분")
    시행일자: str | None = Field(None, alias="시행일자")
    자법타법여부: str | None = Field(None, alias="자법타법여부")
    법령상세링크: str | None = Field(None, alias="법령상세링크")

class EflawDetail(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 본문 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    언어: str | None = Field(None, alias="언어")
    법종구분: str | None = Field(None, alias="법종구분")
    법종구분코드: str | None = Field(None, alias="법종구분코드")
    법령명_한글: str | None = Field(None, alias="법령명_한글")
    법령명_한자: str | None = Field(None, alias="법령명_한자")
    법령명약칭: str | None = Field(None, alias="법령명약칭")
    편장절관: str | None = Field(None, alias="편장절관")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처: str | None = Field(None, alias="소관부처")
    전화번호: str | None = Field(None, alias="전화번호")
    시행일자: str | None = Field(None, alias="시행일자")
    제개정구분: str | None = Field(None, alias="제개정구분")
    조문시행일자문자열: str | None = Field(None, alias="조문시행일자문자열")
    별표시행일자문자열: str | None = Field(None, alias="별표시행일자문자열")
    별표편집여부: str | None = Field(None, alias="별표편집여부")
    공포법령여부: str | None = Field(None, alias="공포법령여부")
    소관부처명: str | None = Field(None, alias="소관부처명")
    부서명: str | None = Field(None, alias="부서명")
    부서연락처: str | None = Field(None, alias="부서연락처")
    공동부령구분: str | None = Field(None, alias="공동부령구분")
    구분코드: str | None = Field(None, alias="구분코드")
    조문번호: str | None = Field(None, alias="조문번호")
    조문가지번호: str | None = Field(None, alias="조문가지번호")
    조문여부: str | None = Field(None, alias="조문여부")
    조문제목: str | None = Field(None, alias="조문제목")
    조문시행일자: str | None = Field(None, alias="조문시행일자")
    조문제개정유형: str | None = Field(None, alias="조문제개정유형")
    조문이동이전: str | None = Field(None, alias="조문이동이전")
    조문이동이후: str | None = Field(None, alias="조문이동이후")
    조문변경여부: str | None = Field(None, alias="조문변경여부")
    조문내용: str | None = Field(None, alias="조문내용")
    항번호: str | None = Field(None, alias="항번호")
    항제개정유형: str | None = Field(None, alias="항제개정유형")
    항제개정일자문자열: str | None = Field(None, alias="항제개정일자문자열")
    항내용: str | None = Field(None, alias="항내용")
    호번호: str | None = Field(None, alias="호번호")
    호내용: str | None = Field(None, alias="호내용")
    목번호: str | None = Field(None, alias="목번호")
    목내용: str | None = Field(None, alias="목내용")
    조문참고자료: str | None = Field(None, alias="조문참고자료")
    부칙공포일자: str | None = Field(None, alias="부칙공포일자")
    부칙공포번호: str | None = Field(None, alias="부칙공포번호")
    부칙내용: str | None = Field(None, alias="부칙내용")
    별표번호: str | None = Field(None, alias="별표번호")
    별표가지번호: str | None = Field(None, alias="별표가지번호")
    별표구분: str | None = Field(None, alias="별표구분")
    별표제목: str | None = Field(None, alias="별표제목")
    별표제목_문자열: str | None = Field(None, alias="별표제목 문자열")
    별표시행일자: str | None = Field(None, alias="별표시행일자")
    별표서식_파일링크: str | None = Field(None, alias="별표서식 파일링크")
    별표hwp_파일명: str | None = Field(None, alias="별표HWP 파일명")
    별표서식_pdf파일링크: str | None = Field(None, alias="별표서식 PDF파일링크")
    별표pdf_파일명: str | None = Field(None, alias="별표PDF 파일명")
    별표서식_이미지파일링크: str | None = Field(None, alias="별표서식 이미지파일링크")
    별표이미지_파일명: str | None = Field(None, alias="별표이미지 파일명")
    별표내용: str | None = Field(None, alias="별표내용")
    개정문내용: str | None = Field(None, alias="개정문내용")
    제개정이유내용: str | None = Field(None, alias="제개정이유내용")

class EflawjosubList(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 본문 조항호목 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    법령키: str | None = Field(None, alias="법령키")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    언어: str | None = Field(None, alias="언어")
    법종구분: str | None = Field(None, alias="법종구분")
    법종구분_코드: str | None = Field(None, alias="법종구분 코드")
    법령명_한글: str | None = Field(None, alias="법령명_한글")
    법령명_한자: str | None = Field(None, alias="법령명_한자")
    법령명_영어: str | None = Field(None, alias="법령명_영어")
    편장절관: str | None = Field(None, alias="편장절관")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처: str | None = Field(None, alias="소관부처")
    전화번호: str | None = Field(None, alias="전화번호")
    시행일자: str | None = Field(None, alias="시행일자")
    제개정구분: str | None = Field(None, alias="제개정구분")
    제안구분: str | None = Field(None, alias="제안구분")
    의결구분: str | None = Field(None, alias="의결구분")
    적용시작일자: str | None = Field(None, alias="적용시작일자")
    적용종료일자: str | None = Field(None, alias="적용종료일자")
    이전법령명: str | None = Field(None, alias="이전법령명")
    조문시행일자문자열: str | None = Field(None, alias="조문시행일자문자열")
    별표시행일자문자열: str | None = Field(None, alias="별표시행일자문자열")
    별표편집여부: str | None = Field(None, alias="별표편집여부")
    공포법령여부: str | None = Field(None, alias="공포법령여부")
    조문번호: str | None = Field(None, alias="조문번호")
    조문여부: str | None = Field(None, alias="조문여부")
    조문제목: str | None = Field(None, alias="조문제목")
    조문시행일자: str | None = Field(None, alias="조문시행일자")
    조문이동이전: str | None = Field(None, alias="조문이동이전")
    조문이동이후: str | None = Field(None, alias="조문이동이후")
    조문변경여부: str | None = Field(None, alias="조문변경여부")
    조문내용: str | None = Field(None, alias="조문내용")
    항번호: str | None = Field(None, alias="항번호")
    항내용: str | None = Field(None, alias="항내용")
    호번호: str | None = Field(None, alias="호번호")
    호내용: str | None = Field(None, alias="호내용")
    목번호: str | None = Field(None, alias="목번호")
    목내용: str | None = Field(None, alias="목내용")

class EiacList(BaseModel):
    """[GENERATED] Response model for 고용보험심사위원회 결정문 목록 조회.

    Source: specs/kr/eiacListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    eiac_id: str | None = Field(None, alias="eiac id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    의결일자: str | None = Field(None, alias="의결일자")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class EiacDetail(BaseModel):
    """[GENERATED] Response model for 고용보험심사위원회 결정문 본문 조회.

    Source: specs/kr/eiacInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건의분류: str | None = Field(None, alias="사건의분류")
    의결서종류: str | None = Field(None, alias="의결서종류")
    개요: str | None = Field(None, alias="개요")
    사건번호: str | None = Field(None, alias="사건번호")
    사건명: str | None = Field(None, alias="사건명")
    청구인: str | None = Field(None, alias="청구인")
    대리인: str | None = Field(None, alias="대리인")
    피청구인: str | None = Field(None, alias="피청구인")
    이해관계인: str | None = Field(None, alias="이해관계인")
    심사결정심사관: str | None = Field(None, alias="심사결정심사관")
    주문: str | None = Field(None, alias="주문")
    청구취지: str | None = Field(None, alias="청구취지")
    이유: str | None = Field(None, alias="이유")
    의결일자: str | None = Field(None, alias="의결일자")
    기관명: str | None = Field(None, alias="기관명")
    별지: str | None = Field(None, alias="별지")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class ElawList(BaseModel):
    """[GENERATED] Response model for 영문 법령 목록 조회.

    Source: specs/kr/lsEngListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    law_id: str | None = Field(None, alias="law id")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    현행연혁코드: str | None = Field(None, alias="현행연혁코드")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령명영문: str | None = Field(None, alias="법령명영문")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    자법타법여부: str | None = Field(None, alias="자법타법여부")
    법령상세링크: str | None = Field(None, alias="법령상세링크")

class ElawDetail(BaseModel):
    """[GENERATED] Response model for 영문 법령 본문 조회.

    Source: specs/kr/lsEngInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class ExpcList(BaseModel):
    """[GENERATED] Response model for 법령해석례 목록 조회.

    Source: specs/kr/expcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    expc_id: str | None = Field(None, alias="expc id")
    법령해석례일련번호: str | None = Field(None, alias="법령해석례일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    회신기관코드: str | None = Field(None, alias="회신기관코드")
    회신기관명: str | None = Field(None, alias="회신기관명")
    회신일자: str | None = Field(None, alias="회신일자")
    법령해석례_상세링크: str | None = Field(None, alias="법령해석례 상세링크")

class ExpcDetail(BaseModel):
    """[GENERATED] Response model for 법령해석례 본문 조회.

    Source: specs/kr/expcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    id: str | None = Field(None, alias="ID")
    lm: str | None = Field(None, alias="LM")

class FscList(BaseModel):
    """[GENERATED] Response model for 금융위원회 결정문 목록 조회.

    Source: specs/kr/fscListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    fsc_id: str | None = Field(None, alias="fsc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    안건명: str | None = Field(None, alias="안건명")
    의결번호: str | None = Field(None, alias="의결번호")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class FscDetail(BaseModel):
    """[GENERATED] Response model for 금융위원회 결정문 본문 조회.

    Source: specs/kr/fscInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    의결번호: str | None = Field(None, alias="의결번호")
    안건명: str | None = Field(None, alias="안건명")
    조치대상자의인적사항: str | None = Field(None, alias="조치대상자의인적사항")
    조치대상: str | None = Field(None, alias="조치대상")
    조치내용: str | None = Field(None, alias="조치내용")
    조치이유: str | None = Field(None, alias="조치이유")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class FtcList(BaseModel):
    """[GENERATED] Response model for 공정거래위원회 결정문 목록 조회.

    Source: specs/kr/ftcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    ftc_id: str | None = Field(None, alias="ftc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    문서유형: str | None = Field(None, alias="문서유형")
    회의종류: str | None = Field(None, alias="회의종류")
    결정번호: str | None = Field(None, alias="결정번호")
    결정일자: str | None = Field(None, alias="결정일자")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class FtcDetail(BaseModel):
    """[GENERATED] Response model for 공정거래위원회 결정문 본문 조회.

    Source: specs/kr/ftcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    문서유형: str | None = Field(None, alias="문서유형")
    사건번호: str | None = Field(None, alias="사건번호")
    사건명: str | None = Field(None, alias="사건명")
    피심정보명: str | None = Field(None, alias="피심정보명")
    피심정보내용: str | None = Field(None, alias="피심정보내용")
    의결서종류: str | None = Field(None, alias="의결서종류")
    시정권고참조법률: str | None = Field(None, alias="시정권고참조법률")
    시정권고사항: str | None = Field(None, alias="시정권고사항")
    시정권고이유: str | None = Field(None, alias="시정권고이유")
    법위반내용: str | None = Field(None, alias="법위반내용")
    적용법조: str | None = Field(None, alias="적용법조")
    법령의적용: str | None = Field(None, alias="법령의적용")
    시정기한: str | None = Field(None, alias="시정기한")
    수락여부통지기간: str | None = Field(None, alias="수락여부통지기간")
    수락여부통지기한: str | None = Field(None, alias="수락여부통지기한")
    수락거부시의조치: str | None = Field(None, alias="수락거부시의조치")
    수락거부시조치방침: str | None = Field(None, alias="수락거부시조치방침")
    별지: str | None = Field(None, alias="별지")
    결정요지: str | None = Field(None, alias="결정요지")

class IaciacList(BaseModel):
    """[GENERATED] Response model for 산업재해보상보험재심사위원회 결정문 목록 조회.

    Source: specs/kr/iaciacListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    iaciac_id: str | None = Field(None, alias="iaciac id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건: str | None = Field(None, alias="사건")
    사건번호: str | None = Field(None, alias="사건번호")
    의결일자: str | None = Field(None, alias="의결일자")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class IaciacDetail(BaseModel):
    """[GENERATED] Response model for 산업재해보상보험재심사위원회 결정문 본문 조회.

    Source: specs/kr/iaciacInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건대분류: str | None = Field(None, alias="사건대분류")
    사건중분류: str | None = Field(None, alias="사건중분류")
    사건소분류: str | None = Field(None, alias="사건소분류")
    쟁점: str | None = Field(None, alias="쟁점")
    사건번호: str | None = Field(None, alias="사건번호")
    의결일자: str | None = Field(None, alias="의결일자")
    사건: str | None = Field(None, alias="사건")
    청구인: str | None = Field(None, alias="청구인")
    재해근로자: str | None = Field(None, alias="재해근로자")
    재해자: str | None = Field(None, alias="재해자")
    피재근로자: str | None = Field(None, alias="피재근로자")
    진폐근로자: str | None = Field(None, alias="진폐근로자")
    수진자: str | None = Field(None, alias="수진자")
    원처분기관: str | None = Field(None, alias="원처분기관")
    주문: str | None = Field(None, alias="주문")
    청구취지: str | None = Field(None, alias="청구취지")
    이유: str | None = Field(None, alias="이유")
    별지: str | None = Field(None, alias="별지")
    문서제공구분: str | None = Field(None, alias="문서제공구분")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class JorltlstrmDetail(BaseModel):
    """[GENERATED] Response model for 조문-법령용어 연계 조회.

    Source: specs/kr/joRltLstrmGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    법령조문_id: str | None = Field(None, alias="법령조문 id")
    법령명: str | None = Field(None, alias="법령명")
    조번호: str | None = Field(None, alias="조번호")
    조가지번호: str | None = Field(None, alias="조가지번호")
    조문내용: str | None = Field(None, alias="조문내용")
    연계용어_id: str | None = Field(None, alias="연계용어 id")
    법령용어명: str | None = Field(None, alias="법령용어명")
    비고: str | None = Field(None, alias="비고")
    용어구분코드: str | None = Field(None, alias="용어구분코드")
    용어구분: str | None = Field(None, alias="용어구분")
    용어간관계_링크: str | None = Field(None, alias="용어간관계 링크")
    용어연계_조문링크: str | None = Field(None, alias="용어연계 조문링크")

class KccList(BaseModel):
    """[GENERATED] Response model for 방송미디어통신위원회 결정문 목록 조회.

    Source: specs/kr/kccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    kcc_id: str | None = Field(None, alias="kcc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    의결일자: str | None = Field(None, alias="의결일자")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class KccDetail(BaseModel):
    """[GENERATED] Response model for 방송미디어통신위원회 결정문 본문 조회.

    Source: specs/kr/kccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    의결서유형: str | None = Field(None, alias="의결서유형")
    안건번호: str | None = Field(None, alias="안건번호")
    사건번호: str | None = Field(None, alias="사건번호")
    안건명: str | None = Field(None, alias="안건명")
    사건명: str | None = Field(None, alias="사건명")
    피심인: str | None = Field(None, alias="피심인")
    피심의인: str | None = Field(None, alias="피심의인")
    청구인: str | None = Field(None, alias="청구인")
    참고인: str | None = Field(None, alias="참고인")
    원심결정: str | None = Field(None, alias="원심결정")
    의결일자: str | None = Field(None, alias="의결일자")
    주문: str | None = Field(None, alias="주문")
    이유: str | None = Field(None, alias="이유")
    별지: str | None = Field(None, alias="별지")
    문서제공구분: str | None = Field(None, alias="문서제공구분")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class KcgcgmexpcList(BaseModel):
    """[GENERATED] Response model for 해양경찰청 법령해석 목록.

    Source: specs/kr/cgmExpcKcgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KcgcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 해양경찰청 법령해석 본문.

    Source: specs/kr/cgmExpcKcgInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KcscgmexpcList(BaseModel):
    """[GENERATED] Response model for 관세청 법령해석 목록 조회.

    Source: specs/kr/cgmExpcKcsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KcscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 관세청 법령해석 본문 조회.

    Source: specs/kr/cgmExpcKcsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    업무분야: str | None = Field(None, alias="업무분야")
    안건명: str | None = Field(None, alias="안건명")
    해석일자: str | None = Field(None, alias="해석일자")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    관리기관코드: str | None = Field(None, alias="관리기관코드")
    등록일시: str | None = Field(None, alias="등록일시")
    질의요지: str | None = Field(None, alias="질의요지")
    회답: str | None = Field(None, alias="회답")
    이유: str | None = Field(None, alias="이유")
    관련법령: str | None = Field(None, alias="관련법령")
    관세법령정보포털원문링크: str | None = Field(None, alias="관세법령정보포털원문링크")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")

class KdcacgmexpcList(BaseModel):
    """[GENERATED] Response model for 질병관리청 법령해석 목록.

    Source: specs/kr/cgmExpcKdcaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KdcacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 질병관리청 법령해석 본문.

    Source: specs/kr/cgmExpcKdcaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KfscgmexpcList(BaseModel):
    """[GENERATED] Response model for 산림청 법령해석 목록.

    Source: specs/kr/cgmExpcKfsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KfscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 산림청 법령해석 본문.

    Source: specs/kr/cgmExpcKfsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KhscgmexpcList(BaseModel):
    """[GENERATED] Response model for 국가유산청 법령해석 목록.

    Source: specs/kr/cgmExpcKhsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KhscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국가유산청 법령해석 본문.

    Source: specs/kr/cgmExpcKhsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KipocgmexpcList(BaseModel):
    """[GENERATED] Response model for 지식재산처 법령해석 목록.

    Source: specs/kr/cgmExpcKipoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KipocgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 지식재산처 법령해석 본문.

    Source: specs/kr/cgmExpcKipoInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KmacgmexpcList(BaseModel):
    """[GENERATED] Response model for 기상청 법령해석 목록.

    Source: specs/kr/cgmExpcKmaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KmacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 기상청 법령해석 본문.

    Source: specs/kr/cgmExpcKmaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KmstspecialdeccList(BaseModel):
    """[GENERATED] Response model for 해양안전심판원 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccKmstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    decc_id: str | None = Field(None, alias="decc id")
    특별행정심판재결례_일련번호: str | None = Field(None, alias="특별행정심판재결례 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    재결번호: str | None = Field(None, alias="재결번호")
    처분일자: str | None = Field(None, alias="처분일자")
    의결일자: str | None = Field(None, alias="의결일자")
    처분청: str | None = Field(None, alias="처분청")
    재결청: str | None = Field(None, alias="재결청")
    재결구분명: str | None = Field(None, alias="재결구분명")
    재결구분코드: str | None = Field(None, alias="재결구분코드")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    행정심판재결례_상세링크: str | None = Field(None, alias="행정심판재결례 상세링크")

class KmstspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 해양안전심판원 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccKmstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class KostatcgmexpcList(BaseModel):
    """[GENERATED] Response model for 국가데이터처 법령해석 목록.

    Source: specs/kr/cgmExpcKostatListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class KostatcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국가데이터처 법령해석 본문.

    Source: specs/kr/cgmExpcKostatInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class LawList(BaseModel):
    """[GENERATED] Response model for 법령 목록 조회.

    Source: specs/kr/mobLsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    law_id: str | None = Field(None, alias="law id")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    현행연혁코드: str | None = Field(None, alias="현행연혁코드")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령약칭명: str | None = Field(None, alias="법령약칭명")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처명: str | None = Field(None, alias="소관부처명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    법령구분명: str | None = Field(None, alias="법령구분명")
    공동부령구분: str | None = Field(None, alias="공동부령구분")
    시행일자: str | None = Field(None, alias="시행일자")
    자법타법여부: str | None = Field(None, alias="자법타법여부")
    법령상세링크: str | None = Field(None, alias="법령상세링크")

class LawDetail(BaseModel):
    """[GENERATED] Response model for 법령 본문 조회.

    Source: specs/kr/mobLsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class LawjosubList(BaseModel):
    """[GENERATED] Response model for 현행법령(공포일) 본문 조항호목 조회.

    Source: specs/kr/lsNwJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    법령키: str | None = Field(None, alias="법령키")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    언어: str | None = Field(None, alias="언어")
    법령명_한글: str | None = Field(None, alias="법령명_한글")
    법령명_한자: str | None = Field(None, alias="법령명_한자")
    법종구분코드: str | None = Field(None, alias="법종구분코드")
    법종구분명: str | None = Field(None, alias="법종구분명")
    제명변경여부: str | None = Field(None, alias="제명변경여부")
    한글법령여부: str | None = Field(None, alias="한글법령여부")
    편장절관: str | None = Field(None, alias="편장절관")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처: str | None = Field(None, alias="소관부처")
    전화번호: str | None = Field(None, alias="전화번호")
    시행일자: str | None = Field(None, alias="시행일자")
    제개정구분: str | None = Field(None, alias="제개정구분")
    제안구분: str | None = Field(None, alias="제안구분")
    의결구분: str | None = Field(None, alias="의결구분")
    이전법령명: str | None = Field(None, alias="이전법령명")
    조문별_시행일자: str | None = Field(None, alias="조문별 시행일자")
    조문시행일자문자열: str | None = Field(None, alias="조문시행일자문자열")
    별표시행일자문자열: str | None = Field(None, alias="별표시행일자문자열")
    별표편집여부: str | None = Field(None, alias="별표편집여부")
    공포법령여부: str | None = Field(None, alias="공포법령여부")
    시행일기준_편집여부: str | None = Field(None, alias="시행일기준 편집여부")
    조문번호: str | None = Field(None, alias="조문번호")
    조문여부: str | None = Field(None, alias="조문여부")
    조문제목: str | None = Field(None, alias="조문제목")
    조문시행일자: str | None = Field(None, alias="조문시행일자")
    조문이동이전: str | None = Field(None, alias="조문이동이전")
    조문이동이후: str | None = Field(None, alias="조문이동이후")
    조문변경여부: str | None = Field(None, alias="조문변경여부")
    조문내용: str | None = Field(None, alias="조문내용")
    항번호: str | None = Field(None, alias="항번호")
    항내용: str | None = Field(None, alias="항내용")
    호번호: str | None = Field(None, alias="호번호")
    호내용: str | None = Field(None, alias="호내용")
    목번호: str | None = Field(None, alias="목번호")
    목내용: str | None = Field(None, alias="목내용")

class LicbylList(BaseModel):
    """[GENERATED] Response model for 법령 별표ㆍ서식 목록 조회.

    Source: specs/kr/lsBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    licbyl_id: str | None = Field(None, alias="licbyl id")
    별표일련번호: str | None = Field(None, alias="별표일련번호")
    관련법령일련번호: str | None = Field(None, alias="관련법령일련번호")
    관련법령id: str | None = Field(None, alias="관련법령ID")
    별표명: str | None = Field(None, alias="별표명")
    관련법령명: str | None = Field(None, alias="관련법령명")
    별표번호: str | None = Field(None, alias="별표번호")
    별표종류: str | None = Field(None, alias="별표종류")
    소관부처명: str | None = Field(None, alias="소관부처명")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    법령종류: str | None = Field(None, alias="법령종류")
    별표서식_파일링크: str | None = Field(None, alias="별표서식 파일링크")
    별표서식_pdf파일링크: str | None = Field(None, alias="별표서식 PDF파일링크")
    별표법령_상세링크: str | None = Field(None, alias="별표법령 상세링크")

class LnklsList(BaseModel):
    """[GENERATED] Response model for 법령 기준 자치법규 연계 관련 목록 조회.

    Source: specs/kr/lsOrdinConListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    law_id: str | None = Field(None, alias="law id")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령id: str | None = Field(None, alias="법령ID")
    자치법규_일련번호: str | None = Field(None, alias="자치법규 일련번호")
    자치법규명: str | None = Field(None, alias="자치법규명")
    자치법규id: str | None = Field(None, alias="자치법규ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    자치법규종류: str | None = Field(None, alias="자치법규종류")
    시행일자: str | None = Field(None, alias="시행일자")

class LnkordList(BaseModel):
    """[GENERATED] Response model for 자치법규 기준 법령 연계 관련 목록 조회.

    Source: specs/kr/ordinLsConListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    law_id: str | None = Field(None, alias="law id")
    자치법규_일련번호: str | None = Field(None, alias="자치법규 일련번호")
    자치법규명: str | None = Field(None, alias="자치법규명")
    자치법규id: str | None = Field(None, alias="자치법규ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    자치법규종류: str | None = Field(None, alias="자치법규종류")
    시행일자: str | None = Field(None, alias="시행일자")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령id: str | None = Field(None, alias="법령ID")

class LsabrvList(BaseModel):
    """[GENERATED] Response model for 법률명 약칭 조회.

    Source: specs/kr/lsAbrvListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    totalcnt: str | None = Field(None, alias="totalCnt")
    law_id: str | None = Field(None, alias="law id")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    현행연혁코드: str | None = Field(None, alias="현행연혁코드")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령약칭명: str | None = Field(None, alias="법령약칭명")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처명: str | None = Field(None, alias="소관부처명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    등록일: str | None = Field(None, alias="등록일")
    자법타법여부: str | None = Field(None, alias="자법타법여부")
    법령상세링크: str | None = Field(None, alias="법령상세링크")

class LshistoryList(BaseModel):
    """[GENERATED] Response model for 법령 연혁 목록 조회.

    Source: specs/kr/lsHstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class LshistoryDetail(BaseModel):
    """[GENERATED] Response model for 법령 연혁 본문 조회.

    Source: specs/kr/lsHstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class LshstinfList(BaseModel):
    """[GENERATED] Response model for 법령 변경이력 목록 조회.

    Source: specs/kr/lsChgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    law_id: str | None = Field(None, alias="law id")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    현행연혁코드: str | None = Field(None, alias="현행연혁코드")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    자법타법여부: str | None = Field(None, alias="자법타법여부")
    법령상세링크: str | None = Field(None, alias="법령상세링크")

class LsjohstinfList(BaseModel):
    """[GENERATED] Response model for 조문별 변경 이력 목록 조회.

    Source: specs/kr/lsJoChgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    법령id: str | None = Field(None, alias="법령ID")
    법령명한글: str | None = Field(None, alias="법령명한글")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처명: str | None = Field(None, alias="소관부처명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    조문번호: str | None = Field(None, alias="조문번호")
    변경사유: str | None = Field(None, alias="변경사유")
    조문링크: str | None = Field(None, alias="조문링크")
    조문변경일: str | None = Field(None, alias="조문변경일")

class LsrltList(BaseModel):
    """[GENERATED] Response model for 관련법령 조회.

    Source: specs/kr/lsRltGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    기준법령id: str | None = Field(None, alias="기준법령ID")
    기준법령명: str | None = Field(None, alias="기준법령명")
    기준법령_상세링크: str | None = Field(None, alias="기준법령 상세링크")
    관련법령_id: str | None = Field(None, alias="관련법령 id")
    관련법령id: str | None = Field(None, alias="관련법령ID")
    관련법령명: str | None = Field(None, alias="관련법령명")
    법령간관계_코드: str | None = Field(None, alias="법령간관계 코드")
    법령간관계: str | None = Field(None, alias="법령간관계")
    관련법령_상세링크: str | None = Field(None, alias="관련법령 상세링크")
    관련법령_조회링크: str | None = Field(None, alias="관련법령 조회링크")

class LsstmdList(BaseModel):
    """[GENERATED] Response model for 법령 체계도 목록 조회.

    Source: specs/kr/lsStmdListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    resultcode: str | None = Field(None, alias="resultCode")
    resultmsg: str | None = Field(None, alias="resultMsg")
    law_id: str | None = Field(None, alias="law id")
    법령_일련번호: str | None = Field(None, alias="법령 일련번호")
    법령명: str | None = Field(None, alias="법령명")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    본문_상세링크: str | None = Field(None, alias="본문 상세링크")

class LsstmdDetail(BaseModel):
    """[GENERATED] Response model for 법령 체계도 본문 조회.

    Source: specs/kr/lsStmdInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    기본정보: str | None = Field(None, alias="기본정보")
    법령id: str | None = Field(None, alias="법령ID")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    법종구분: str | None = Field(None, alias="법종구분")
    법령명: str | None = Field(None, alias="법령명")
    시행일자: str | None = Field(None, alias="시행일자")
    제개정구분: str | None = Field(None, alias="제개정구분")
    상하위법: str | None = Field(None, alias="상하위법")
    법률: str | None = Field(None, alias="법률")
    시행령: str | None = Field(None, alias="시행령")
    시행규칙: str | None = Field(None, alias="시행규칙")
    본문_상세링크: str | None = Field(None, alias="본문 상세링크")

class LstrmList(BaseModel):
    """[GENERATED] Response model for 법령 용어 목록 조회.

    Source: specs/kr/lsTrmListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    lstrm_id: str | None = Field(None, alias="lstrm id")
    법령용어id: str | None = Field(None, alias="법령용어ID")
    법령용어명: str | None = Field(None, alias="법령용어명")
    법령용어상세검색: str | None = Field(None, alias="법령용어상세검색")
    사전구분코드: str | None = Field(None, alias="사전구분코드")
    법령용어_상세링크: str | None = Field(None, alias="법령용어 상세링크")
    법령종류코드: str | None = Field(None, alias="법령종류코드")

class LstrmDetail(BaseModel):
    """[GENERATED] Response model for 법령 용어 본문 조회.

    Source: specs/kr/lsTrmInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    법령용어_일련번호: str | None = Field(None, alias="법령용어 일련번호")
    법령용어명_한글: str | None = Field(None, alias="법령용어명_한글")
    법령용어명_한자: str | None = Field(None, alias="법령용어명_한자")
    법령용어코드: str | None = Field(None, alias="법령용어코드")
    법령용어코드명: str | None = Field(None, alias="법령용어코드명")
    출처: str | None = Field(None, alias="출처")
    법령용어정의: str | None = Field(None, alias="법령용어정의")

class LstrmaiList(BaseModel):
    """[GENERATED] Response model for 법령용어 조회.

    Source: specs/kr/lstrmAIGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    section: str | None = Field(None, alias="section")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    법령용어_id: str | None = Field(None, alias="법령용어 id")
    법령용어명: str | None = Field(None, alias="법령용어명")
    동음이의어_존재여부: str | None = Field(None, alias="동음이의어 존재여부")
    비고: str | None = Field(None, alias="비고")
    용어간관계_링크: str | None = Field(None, alias="용어간관계 링크")
    조문간관계_링크: str | None = Field(None, alias="조문간관계 링크")

class LstrmrltDetail(BaseModel):
    """[GENERATED] Response model for 법령용어-일상용어 연계 조회.

    Source: specs/kr/lstrmRltGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    법령용어_id: str | None = Field(None, alias="법령용어 id")
    법령용어명: str | None = Field(None, alias="법령용어명")
    비고: str | None = Field(None, alias="비고")
    연계용어_id: str | None = Field(None, alias="연계용어 id")
    일상용어명: str | None = Field(None, alias="일상용어명")
    용어관계코드: str | None = Field(None, alias="용어관계코드")
    용어관계: str | None = Field(None, alias="용어관계")
    일상용어_조회링크: str | None = Field(None, alias="일상용어 조회링크")
    용어간관계_링크: str | None = Field(None, alias="용어간관계 링크")

class LstrmrltjoDetail(BaseModel):
    """[GENERATED] Response model for 법령용어-조문 연계 조회.

    Source: specs/kr/lstrmRltJoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    검색결과개수: str | None = Field(None, alias="검색결과개수")
    법령용어_id: str | None = Field(None, alias="법령용어 id")
    법령용어명: str | None = Field(None, alias="법령용어명")
    비고: str | None = Field(None, alias="비고")
    용어간관계_링크: str | None = Field(None, alias="용어간관계 링크")
    연계법령_id: str | None = Field(None, alias="연계법령 id")
    법령명: str | None = Field(None, alias="법령명")
    조번호: str | None = Field(None, alias="조번호")
    조가지번호: str | None = Field(None, alias="조가지번호")
    조문내용: str | None = Field(None, alias="조문내용")
    용어구분코드: str | None = Field(None, alias="용어구분코드")
    용어구분: str | None = Field(None, alias="용어구분")
    조문연계_용어링크: str | None = Field(None, alias="조문연계 용어링크")

class MafracgmexpcList(BaseModel):
    """[GENERATED] Response model for 농림축산식품부 법령해석 목록.

    Source: specs/kr/cgmExpcMafraListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MafracgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 농림축산식품부 법령해석 본문.

    Source: specs/kr/cgmExpcMafraInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class McstcgmexpcList(BaseModel):
    """[GENERATED] Response model for 문화체육관광부 법령해석 목록.

    Source: specs/kr/cgmExpcMcstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class McstcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 문화체육관광부 법령해석 본문.

    Source: specs/kr/cgmExpcMcstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MecgmexpcList(BaseModel):
    """[GENERATED] Response model for 기후에너지환경부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMeListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MecgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 기후에너지환경부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMeInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MfdscgmexpcList(BaseModel):
    """[GENERATED] Response model for 식품의약품안전처 법령해석 목록.

    Source: specs/kr/cgmExpcMfdsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MfdscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 식품의약품안전처 법령해석 본문.

    Source: specs/kr/cgmExpcMfdsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MmacgmexpcList(BaseModel):
    """[GENERATED] Response model for 병무청 법령해석 목록.

    Source: specs/kr/cgmExpcMmaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MmacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 병무청 법령해석 본문.

    Source: specs/kr/cgmExpcMmaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MndcgmexpcList(BaseModel):
    """[GENERATED] Response model for 국방부 법령해석 목록.

    Source: specs/kr/cgmExpcMndListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MndcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국방부 법령해석 본문.

    Source: specs/kr/cgmExpcMndInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MoecgmexpcList(BaseModel):
    """[GENERATED] Response model for 교육부 법령해석 목록.

    Source: specs/kr/cgmExpcMoeListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MoecgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 교육부 법령해석 본문.

    Source: specs/kr/cgmExpcMoeInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MoefcgmexpcList(BaseModel):
    """[GENERATED] Response model for 재정경제부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMoefListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MoelcgmexpcList(BaseModel):
    """[GENERATED] Response model for 고용노동부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMoelListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MoelcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 고용노동부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMoelInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MofcgmexpcList(BaseModel):
    """[GENERATED] Response model for 해양수산부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMofListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MofcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 해양수산부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMofInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MofacgmexpcList(BaseModel):
    """[GENERATED] Response model for 외교부 법령해석 목록.

    Source: specs/kr/cgmExpcMofaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MofacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 외교부 법령해석 본문.

    Source: specs/kr/cgmExpcMofaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MogefcgmexpcList(BaseModel):
    """[GENERATED] Response model for 성평등가족부 법령해석 목록.

    Source: specs/kr/cgmExpcMogefListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MogefcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 성평등가족부 법령해석 본문.

    Source: specs/kr/cgmExpcMogefInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MohwcgmexpcList(BaseModel):
    """[GENERATED] Response model for 보건복지부 법령해석 목록.

    Source: specs/kr/cgmExpcMohwListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MohwcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 보건복지부 법령해석 본문.

    Source: specs/kr/cgmExpcMohwInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MoiscgmexpcList(BaseModel):
    """[GENERATED] Response model for 행정안전부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMoisListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MoiscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 행정안전부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMoisInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MojcgmexpcList(BaseModel):
    """[GENERATED] Response model for 법무부 법령해석 목록.

    Source: specs/kr/cgmExpcMojListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MojcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 법무부 법령해석 본문.

    Source: specs/kr/cgmExpcMojInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MolegcgmexpcList(BaseModel):
    """[GENERATED] Response model for 법제처 법령해석 목록.

    Source: specs/kr/cgmExpcMolegListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MolegcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 법제처 법령해석 본문.

    Source: specs/kr/cgmExpcMolegInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MolitcgmexpcList(BaseModel):
    """[GENERATED] Response model for 국토교통부 법령해석 목록 조회.

    Source: specs/kr/cgmExpcMolitListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MolitcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국토교통부 법령해석 본문 조회.

    Source: specs/kr/cgmExpcMolitInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MotiecgmexpcList(BaseModel):
    """[GENERATED] Response model for 산업통상부 법령해석 목록.

    Source: specs/kr/cgmExpcMotieListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MotiecgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 산업통상부 법령해석 본문.

    Source: specs/kr/cgmExpcMotieInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MoucgmexpcList(BaseModel):
    """[GENERATED] Response model for 통일부 법령해석 목록.

    Source: specs/kr/cgmExpcMouListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MoucgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 통일부 법령해석 본문.

    Source: specs/kr/cgmExpcMouInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MpmcgmexpcList(BaseModel):
    """[GENERATED] Response model for 인사혁신처 법령해석 목록.

    Source: specs/kr/cgmExpcMpmListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MpmcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 인사혁신처 법령해석 본문.

    Source: specs/kr/cgmExpcMpmInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MpvacgmexpcList(BaseModel):
    """[GENERATED] Response model for 국가보훈부 법령해석 목록.

    Source: specs/kr/cgmExpcMpvaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MpvacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 국가보훈부 법령해석 본문.

    Source: specs/kr/cgmExpcMpvaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MsitcgmexpcList(BaseModel):
    """[GENERATED] Response model for 과학기술정보통신부 법령해석 목록.

    Source: specs/kr/cgmExpcMsitListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MsitcgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 과학기술정보통신부 법령해석 본문.

    Source: specs/kr/cgmExpcMsitInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class MsscgmexpcList(BaseModel):
    """[GENERATED] Response model for 중소벤처기업부 법령해석 목록.

    Source: specs/kr/cgmExpcMssListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class MsscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 중소벤처기업부 법령해석 본문.

    Source: specs/kr/cgmExpcMssInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class NaacccgmexpcList(BaseModel):
    """[GENERATED] Response model for 행정중심복합도시건설청 법령해석 목록.

    Source: specs/kr/cgmExpcNaaccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class NaacccgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 행정중심복합도시건설청 법령해석 본문.

    Source: specs/kr/cgmExpcNaaccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class NfacgmexpcList(BaseModel):
    """[GENERATED] Response model for 소방청 법령해석 목록.

    Source: specs/kr/cgmExpcNfaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class NfacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 소방청 법령해석 본문.

    Source: specs/kr/cgmExpcNfaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class NhrckList(BaseModel):
    """[GENERATED] Response model for 국가인권위원회 결정문 목록 조회.

    Source: specs/kr/nhrckListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    nhrck_id: str | None = Field(None, alias="nhrck id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    의결일자: str | None = Field(None, alias="의결일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class NhrckDetail(BaseModel):
    """[GENERATED] Response model for 국가인권위원회 결정문 본문 조회.

    Source: specs/kr/nhrckInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    위원회명: str | None = Field(None, alias="위원회명")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    의결일자: str | None = Field(None, alias="의결일자")
    주문: str | None = Field(None, alias="주문")
    이유: str | None = Field(None, alias="이유")
    위원정보: str | None = Field(None, alias="위원정보")
    별지: str | None = Field(None, alias="별지")
    결정요지: str | None = Field(None, alias="결정요지")
    판단요지: str | None = Field(None, alias="판단요지")
    주문요지: str | None = Field(None, alias="주문요지")
    분류명: str | None = Field(None, alias="분류명")
    결정유형: str | None = Field(None, alias="결정유형")
    신청인: str | None = Field(None, alias="신청인")
    피신청인: str | None = Field(None, alias="피신청인")
    피해자: str | None = Field(None, alias="피해자")
    피조사자: str | None = Field(None, alias="피조사자")
    원본다운로드_url: str | None = Field(None, alias="원본다운로드 URL")
    바로보기_url: str | None = Field(None, alias="바로보기 URL")
    결정례전문: str | None = Field(None, alias="결정례전문")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")

class NlrcList(BaseModel):
    """[GENERATED] Response model for 노동위원회 결정문 목록 조회.

    Source: specs/kr/nlrcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    nlrc_id: str | None = Field(None, alias="nlrc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    제목: str | None = Field(None, alias="제목")
    사건번호: str | None = Field(None, alias="사건번호")
    등록일: str | None = Field(None, alias="등록일")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class NlrcDetail(BaseModel):
    """[GENERATED] Response model for 노동위원회 결정문 본문 조회.

    Source: specs/kr/nlrcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    사건번호: str | None = Field(None, alias="사건번호")
    자료구분: str | None = Field(None, alias="자료구분")
    담당부서: str | None = Field(None, alias="담당부서")
    등록일: str | None = Field(None, alias="등록일")
    제목: str | None = Field(None, alias="제목")
    내용: str | None = Field(None, alias="내용")
    판정사항: str | None = Field(None, alias="판정사항")
    판정요지: str | None = Field(None, alias="판정요지")
    판정결과: str | None = Field(None, alias="판정결과")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class NpacgmexpcList(BaseModel):
    """[GENERATED] Response model for 경찰청 법령해석 목록.

    Source: specs/kr/cgmExpcNpaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class NpacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 경찰청 법령해석 본문.

    Source: specs/kr/cgmExpcNpaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class NtscgmexpcList(BaseModel):
    """[GENERATED] Response model for 국세청 법령해석 목록 조회.

    Source: specs/kr/cgmExpcNtsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class OcltList(BaseModel):
    """[GENERATED] Response model for 중앙토지수용위원회 결정문 목록 조회.

    Source: specs/kr/ocltListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    oclt_id: str | None = Field(None, alias="oclt id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    제목: str | None = Field(None, alias="제목")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class OcltDetail(BaseModel):
    """[GENERATED] Response model for 중앙토지수용위원회 결정문 본문 조회.

    Source: specs/kr/ocltInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    제목: str | None = Field(None, alias="제목")
    관련법리: str | None = Field(None, alias="관련법리")
    관련규정: str | None = Field(None, alias="관련규정")
    판단: str | None = Field(None, alias="판단")
    근거: str | None = Field(None, alias="근거")
    주해: str | None = Field(None, alias="주해")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class OkacgmexpcList(BaseModel):
    """[GENERATED] Response model for 재외동포청 법령해석 목록.

    Source: specs/kr/cgmExpcOkaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class OkacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 재외동포청 법령해석 본문.

    Source: specs/kr/cgmExpcOkaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class OldandnewList(BaseModel):
    """[GENERATED] Response model for 신구법 목록 조회.

    Source: specs/kr/oldAndNewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    resultcode: str | None = Field(None, alias="resultCode")
    resultmsg: str | None = Field(None, alias="resultMsg")
    oldandnew_id: str | None = Field(None, alias="oldAndNew id")
    신구법_일련번호: str | None = Field(None, alias="신구법 일련번호")
    현행연혁구분: str | None = Field(None, alias="현행연혁구분")
    신구법명: str | None = Field(None, alias="신구법명")
    신구법id: str | None = Field(None, alias="신구법ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    신구법_상세링크: str | None = Field(None, alias="신구법 상세링크")

class OldandnewDetail(BaseModel):
    """[GENERATED] Response model for 신구법 본문 조회.

    Source: specs/kr/oldAndNewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    구조문_기본정보: str | None = Field(None, alias="구조문_ 기본정보")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    법령id: str | None = Field(None, alias="법령ID")
    시행일자: str | None = Field(None, alias="시행일자")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    현행여부: str | None = Field(None, alias="현행여부")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    법령명: str | None = Field(None, alias="법령명")
    법종구분: str | None = Field(None, alias="법종구분")
    신조문_기본정보: str | None = Field(None, alias="신조문_ 기본정보")
    구조문목록: str | None = Field(None, alias="구조문목록")
    조문: str | None = Field(None, alias="조문")
    신조문목록: str | None = Field(None, alias="신조문목록")
    신구법_존재여부: str | None = Field(None, alias="신구법 존재여부")

class OneviewList(BaseModel):
    """[GENERATED] Response model for 한눈보기 목록 조회.

    Source: specs/kr/oneViewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    법령_id: str | None = Field(None, alias="법령 id")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    법령명: str | None = Field(None, alias="법령명")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    시행일자: str | None = Field(None, alias="시행일자")
    제공건수: str | None = Field(None, alias="제공건수")
    제공일자: str | None = Field(None, alias="제공일자")

class OneviewDetail(BaseModel):
    """[GENERATED] Response model for 한눈보기 본문 조회.

    Source: specs/kr/oneViewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    패턴일련번호: str | None = Field(None, alias="패턴일련번호")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    법령명: str | None = Field(None, alias="법령명")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    조문시행일자: str | None = Field(None, alias="조문시행일자")
    최초제공일자: str | None = Field(None, alias="최초제공일자")
    조번호: str | None = Field(None, alias="조번호")
    조제목: str | None = Field(None, alias="조제목")
    콘텐츠제목: str | None = Field(None, alias="콘텐츠제목")
    링크텍스트: str | None = Field(None, alias="링크텍스트")
    링크url: str | None = Field(None, alias="링크URL")

class OrdinList(BaseModel):
    """[GENERATED] Response model for 자치법규 목록 조회.

    Source: specs/kr/ordinListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    자치법규명: str | None = Field(None, alias="자치법규명")
    자치법규일련번호: str | None = Field(None, alias="자치법규일련번호")
    자치법규종류: str | None = Field(None, alias="자치법규종류")

class OrdinDetail(BaseModel):
    """[GENERATED] Response model for 자치법규 본문 조회.

    Source: specs/kr/ordinInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class OrdinbylList(BaseModel):
    """[GENERATED] Response model for 자치법규 별표ㆍ서식 목록 조회.

    Source: specs/kr/ordinBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    ordinbyl_id: str | None = Field(None, alias="ordinbyl id")
    별표일련번호: str | None = Field(None, alias="별표일련번호")
    관련자치법규일련번호: str | None = Field(None, alias="관련자치법규일련번호")
    별표명: str | None = Field(None, alias="별표명")
    관련자치법규명: str | None = Field(None, alias="관련자치법규명")
    별표번호: str | None = Field(None, alias="별표번호")
    별표종류: str | None = Field(None, alias="별표종류")
    지자체기관명: str | None = Field(None, alias="지자체기관명")
    전체기관명: str | None = Field(None, alias="전체기관명")
    자치법규시행일자: str | None = Field(None, alias="자치법규시행일자")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    별표서식파일링크: str | None = Field(None, alias="별표서식파일링크")
    별표자치법규상세링크: str | None = Field(None, alias="별표자치법규상세링크")

class PpcList(BaseModel):
    """[GENERATED] Response model for 개인정보보호위원회 결정문 목록 조회.

    Source: specs/kr/ppcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    ppc_id: str | None = Field(None, alias="ppc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    안건명: str | None = Field(None, alias="안건명")
    의안번호: str | None = Field(None, alias="의안번호")
    회의종류: str | None = Field(None, alias="회의종류")
    결정구분: str | None = Field(None, alias="결정구분")
    의결일: str | None = Field(None, alias="의결일")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class PpcDetail(BaseModel):
    """[GENERATED] Response model for 개인정보보호위원회 결정문 본문 조회.

    Source: specs/kr/ppcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    결정: str | None = Field(None, alias="결정")
    회의종류: str | None = Field(None, alias="회의종류")
    안건번호: str | None = Field(None, alias="안건번호")
    안건명: str | None = Field(None, alias="안건명")
    신청인: str | None = Field(None, alias="신청인")
    의결연월일: str | None = Field(None, alias="의결연월일")
    주문: str | None = Field(None, alias="주문")
    이유: str | None = Field(None, alias="이유")
    배경: str | None = Field(None, alias="배경")
    이의제기방법및기간: str | None = Field(None, alias="이의제기방법및기간")
    주요내용: str | None = Field(None, alias="주요내용")
    의결일자: str | None = Field(None, alias="의결일자")
    위원서명: str | None = Field(None, alias="위원서명")
    별지: str | None = Field(None, alias="별지")
    결정요지: str | None = Field(None, alias="결정요지")

class PpscgmexpcList(BaseModel):
    """[GENERATED] Response model for 조달청 법령해석 목록.

    Source: specs/kr/cgmExpcPpsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class PpscgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 조달청 법령해석 본문.

    Source: specs/kr/cgmExpcPpsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class PrecList(BaseModel):
    """[GENERATED] Response model for 판례 목록 조회.

    Source: specs/kr/precListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    공포번호: str | None = Field(None, alias="공포번호")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    prec_id: str | None = Field(None, alias="prec id")
    판례일련번호: str | None = Field(None, alias="판례일련번호")
    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    선고일자: str | None = Field(None, alias="선고일자")
    법원명: str | None = Field(None, alias="법원명")
    법원종류코드: str | None = Field(None, alias="법원종류코드")
    사건종류명: str | None = Field(None, alias="사건종류명")
    사건종류코드: str | None = Field(None, alias="사건종류코드")
    판결유형: str | None = Field(None, alias="판결유형")
    선고: str | None = Field(None, alias="선고")
    데이터출처명: str | None = Field(None, alias="데이터출처명")
    판례상세링크: str | None = Field(None, alias="판례상세링크")

class PrecDetail(BaseModel):
    """[GENERATED] Response model for 판례 본문 조회.

    Source: specs/kr/precInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class RdacgmexpcList(BaseModel):
    """[GENERATED] Response model for 농촌진흥청 법령해석 목록.

    Source: specs/kr/cgmExpcRdaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    id: str | None = Field(None, alias="id")
    법령해석일련번호: str | None = Field(None, alias="법령해석일련번호")
    안건명: str | None = Field(None, alias="안건명")
    안건번호: str | None = Field(None, alias="안건번호")
    질의기관코드: str | None = Field(None, alias="질의기관코드")
    질의기관명: str | None = Field(None, alias="질의기관명")
    해석기관코드: str | None = Field(None, alias="해석기관코드")
    해석기관명: str | None = Field(None, alias="해석기관명")
    해석일자: str | None = Field(None, alias="해석일자")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    법령해석_상세링크: str | None = Field(None, alias="법령해석 상세링크")

class RdacgmexpcDetail(BaseModel):
    """[GENERATED] Response model for 농촌진흥청 법령해석 본문.

    Source: specs/kr/cgmExpcRdaInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec

class SchoolList(BaseModel):
    """[GENERATED] Response model for 학칙ㆍ공단ㆍ공공기관 목록 조회.

    Source: specs/kr/schlPubRulListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    resultcode: str | None = Field(None, alias="resultCode")
    resultmsg: str | None = Field(None, alias="resultMsg")
    admrul_id: str | None = Field(None, alias="admrul id")
    행정규칙_일련번호: str | None = Field(None, alias="행정규칙 일련번호")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    행정규칙종류: str | None = Field(None, alias="행정규칙종류")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    소관부처명: str | None = Field(None, alias="소관부처명")
    현행연혁구분: str | None = Field(None, alias="현행연혁구분")
    제개정_구분코드: str | None = Field(None, alias="제개정 구분코드")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    법령분류코드: str | None = Field(None, alias="법령분류코드")
    법령분류명: str | None = Field(None, alias="법령분류명")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    행정규칙_상세링크: str | None = Field(None, alias="행정규칙 상세링크")
    시행일자: str | None = Field(None, alias="시행일자")
    생성일자: str | None = Field(None, alias="생성일자")

class SchoolDetail(BaseModel):
    """[GENERATED] Response model for 학칙ㆍ공단ㆍ공공기관 본문 조회.

    Source: specs/kr/schlPubRulInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    행정규칙_일련번호: str | None = Field(None, alias="행정규칙 일련번호")
    행정규칙명: str | None = Field(None, alias="행정규칙명")
    행정규칙종류: str | None = Field(None, alias="행정규칙종류")
    행정규칙종류코드: str | None = Field(None, alias="행정규칙종류코드")
    발령일자: str | None = Field(None, alias="발령일자")
    발령번호: str | None = Field(None, alias="발령번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    제개정_구분코드: str | None = Field(None, alias="제개정 구분코드")
    조문형식여부: str | None = Field(None, alias="조문형식여부")
    행정규칙id: str | None = Field(None, alias="행정규칙ID")
    소관부처명: str | None = Field(None, alias="소관부처명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    담당부서기관코드: str | None = Field(None, alias="담당부서기관코드")
    담당부서기관명: str | None = Field(None, alias="담당부서기관명")
    담당자명: str | None = Field(None, alias="담당자명")
    전화번호: str | None = Field(None, alias="전화번호")
    현행여부: str | None = Field(None, alias="현행여부")
    생성일자: str | None = Field(None, alias="생성일자")
    조문내용: str | None = Field(None, alias="조문내용")
    부칙공포일자: str | None = Field(None, alias="부칙공포일자")
    부칙공포번호: str | None = Field(None, alias="부칙공포번호")
    부칙내용: str | None = Field(None, alias="부칙내용")
    별표단위_별표키: str | None = Field(None, alias="별표단위 별표키")
    별표번호: str | None = Field(None, alias="별표번호")
    별표가지번호: str | None = Field(None, alias="별표가지번호")
    별표구분: str | None = Field(None, alias="별표구분")
    별표제목: str | None = Field(None, alias="별표제목")
    별표서식_파일링크: str | None = Field(None, alias="별표서식 파일링크")
    개정문내용: str | None = Field(None, alias="개정문내용")
    제개정이유내용: str | None = Field(None, alias="제개정이유내용")

class SfcList(BaseModel):
    """[GENERATED] Response model for 증권선물위원회 결정문 목록 조회.

    Source: specs/kr/sfcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    기관명: str | None = Field(None, alias="기관명")
    sfc_id: str | None = Field(None, alias="sfc id")
    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    안건명: str | None = Field(None, alias="안건명")
    의결번호: str | None = Field(None, alias="의결번호")
    결정문_상세링크: str | None = Field(None, alias="결정문 상세링크")

class SfcDetail(BaseModel):
    """[GENERATED] Response model for 증권선물위원회 결정문 본문 조회.

    Source: specs/kr/sfcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    결정문_일련번호: str | None = Field(None, alias="결정문 일련번호")
    기관명: str | None = Field(None, alias="기관명")
    의결번호: str | None = Field(None, alias="의결번호")
    안건명: str | None = Field(None, alias="안건명")
    조치대상자의인적사항: str | None = Field(None, alias="조치대상자의인적사항")
    조치대상: str | None = Field(None, alias="조치대상")
    조치내용: str | None = Field(None, alias="조치내용")
    조치이유: str | None = Field(None, alias="조치이유")
    각주번호: str | None = Field(None, alias="각주번호")
    각주내용: str | None = Field(None, alias="각주내용")

class ThdcmpList(BaseModel):
    """[GENERATED] Response model for 3단 비교 목록 조회.

    Source: specs/kr/thdCmpListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    numofrows: str | None = Field(None, alias="numOfRows")
    resultcode: str | None = Field(None, alias="resultCode")
    resultmsg: str | None = Field(None, alias="resultMsg")
    thdcmp_id: str | None = Field(None, alias="thdCmp id")
    삼단비교_일련번호: str | None = Field(None, alias="삼단비교 일련번호")
    법령명_한글: str | None = Field(None, alias="법령명 한글")
    법령id: str | None = Field(None, alias="법령ID")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    제개정구분명: str | None = Field(None, alias="제개정구분명")
    소관부처코드: str | None = Field(None, alias="소관부처코드")
    소관부처명: str | None = Field(None, alias="소관부처명")
    법령구분명: str | None = Field(None, alias="법령구분명")
    시행일자: str | None = Field(None, alias="시행일자")
    인용조문_삼단비교상세링크: str | None = Field(None, alias="인용조문_삼단비교상세링크")
    위임조문_삼단비교상세링크: str | None = Field(None, alias="위임조문_삼단비교상세링크")

class ThdcmpDetail(BaseModel):
    """[GENERATED] Response model for 3단 비교 본문 조회.

    Source: specs/kr/thdCmpInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    기본정보: str | None = Field(None, alias="기본정보")
    법령id: str | None = Field(None, alias="법령ID")
    법령일련번호: str | None = Field(None, alias="법령일련번호")
    공포일자: str | None = Field(None, alias="공포일자")
    공포번호: str | None = Field(None, alias="공포번호")
    법종구분: str | None = Field(None, alias="법종구분")
    법령명: str | None = Field(None, alias="법령명")
    시행일자: str | None = Field(None, alias="시행일자")
    제개정구분: str | None = Field(None, alias="제개정구분")
    삼단비교_존재여부: str | None = Field(None, alias="삼단비교 존재여부")
    기준법_법령명: str | None = Field(None, alias="기준법 법령명")
    기준법령목록: str | None = Field(None, alias="기준법령목록")
    위임3비교_상세링크: str | None = Field(None, alias="위임3비교 상세링크")
    위임조문_삼단비교: str | None = Field(None, alias="위임조문 삼단비교")
    법률조문: str | None = Field(None, alias="법률조문")
    조번호: str | None = Field(None, alias="조번호")
    조가지번호: str | None = Field(None, alias="조가지번호")
    조제목: str | None = Field(None, alias="조제목")
    조내용: str | None = Field(None, alias="조내용")
    시행령조문: str | None = Field(None, alias="시행령조문")
    시행규칙_조문목록: str | None = Field(None, alias="시행규칙 조문목록")
    시행규칙조문: str | None = Field(None, alias="시행규칙조문")

class TrtyList(BaseModel):
    """[GENERATED] Response model for 조약 목록 조회.

    Source: specs/kr/trtyListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    trty_id: str | None = Field(None, alias="trty id")
    조약일련번호: str | None = Field(None, alias="조약일련번호")
    조약명: str | None = Field(None, alias="조약명")
    조약구분코드: str | None = Field(None, alias="조약구분코드")
    조약구분명: str | None = Field(None, alias="조약구분명")
    발효일자: str | None = Field(None, alias="발효일자")
    서명일자: str | None = Field(None, alias="서명일자")
    관보게제일자: str | None = Field(None, alias="관보게제일자")
    조약번호: str | None = Field(None, alias="조약번호")
    국가번호: str | None = Field(None, alias="국가번호")
    조약상세링크: str | None = Field(None, alias="조약상세링크")

class TrtyDetail(BaseModel):
    """[GENERATED] Response model for 조약 본문 조회.

    Source: specs/kr/trtyInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    조약일련번호: str | None = Field(None, alias="조약일련번호")
    조약명_한글: str | None = Field(None, alias="조약명_한글")
    조약명_영문: str | None = Field(None, alias="조약명_영문")
    조약구분코드: str | None = Field(None, alias="조약구분코드")
    대통령재가일자: str | None = Field(None, alias="대통령재가일자")
    발효일자: str | None = Field(None, alias="발효일자")
    조약번호: str | None = Field(None, alias="조약번호")
    관보게재일자: str | None = Field(None, alias="관보게재일자")
    국무회의심의일자: str | None = Field(None, alias="국무회의심의일자")
    국무회의심의회차: str | None = Field(None, alias="국무회의심의회차")
    국회비준동의여부: str | None = Field(None, alias="국회비준동의여부")
    국회비준동의일자: str | None = Field(None, alias="국회비준동의일자")
    서명일자: str | None = Field(None, alias="서명일자")
    서명장소: str | None = Field(None, alias="서명장소")
    비고: str | None = Field(None, alias="비고")
    추가정보: str | None = Field(None, alias="추가정보")
    체결대상국가: str | None = Field(None, alias="체결대상국가")
    체결대상국가한글: str | None = Field(None, alias="체결대상국가한글")
    우리측국내절차완료통보: str | None = Field(None, alias="우리측국내절차완료통보")
    상대국측국내절차완료통보: str | None = Field(None, alias="상대국측국내절차완료통보")
    양자조약분야코드: str | None = Field(None, alias="양자조약분야코드")
    양자조약분야명: str | None = Field(None, alias="양자조약분야명")
    제2외국어종류: str | None = Field(None, alias="제2외국어종류")
    국가코드: str | None = Field(None, alias="국가코드")
    조약내용: str | None = Field(None, alias="조약내용")
    체결일자: str | None = Field(None, alias="체결일자")
    체결장소: str | None = Field(None, alias="체결장소")
    기탁처: str | None = Field(None, alias="기탁처")
    다자조약분야코드: str | None = Field(None, alias="다자조약분야코드")
    다자조약분야명: str | None = Field(None, alias="다자조약분야명")
    수락서기탁일자: str | None = Field(None, alias="수락서기탁일자")
    국내발효일자: str | None = Field(None, alias="국내발효일자")
    id: str | None = Field(None, alias="ID")

class TtspecialdeccList(BaseModel):
    """[GENERATED] Response model for 조세심판원 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccTtListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    target: str | None = Field(None, alias="target")
    키워드: str | None = Field(None, alias="키워드")
    section: str | None = Field(None, alias="section")
    totalcnt: str | None = Field(None, alias="totalCnt")
    page: str | None = Field(None, alias="page")
    decc_id: str | None = Field(None, alias="decc id")
    특별행정심판재결례_일련번호: str | None = Field(None, alias="특별행정심판재결례 일련번호")
    사건명: str | None = Field(None, alias="사건명")
    청구번호: str | None = Field(None, alias="청구번호")
    처분일자: str | None = Field(None, alias="처분일자")
    의결일자: str | None = Field(None, alias="의결일자")
    처분청: str | None = Field(None, alias="처분청")
    재결청: str | None = Field(None, alias="재결청")
    재결구분명: str | None = Field(None, alias="재결구분명")
    재결구분코드: str | None = Field(None, alias="재결구분코드")
    데이터기준일시: str | None = Field(None, alias="데이터기준일시")
    행정심판재결례_상세링크: str | None = Field(None, alias="행정심판재결례 상세링크")

class TtspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 조세심판원 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccTtInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {"populate_by_name": True}

    pass  # no response fields in spec




def _normalize_to_list(v: Any) -> list[Any]:
    if v is None:
        return []
    if isinstance(v, dict):
        return [v]
    return v


class LsdelegatedDepartmentInfo(BaseModel):
    content: str | None = None
    소관부처코드: str | None = None


class LsdelegatedLawInfo(BaseModel):
    법령ID: str | None = None
    법령일련번호: str | None = None
    소관부처: LsdelegatedDepartmentInfo | None = None
    법령명: str | None = None
    시행일자: str | None = None
    공포번호: str | None = None
    전화번호: str | None = None
    공포일자: str | None = None


class LsdelegatedArticleInfo(BaseModel):
    조문번호: str | None = None
    조문제목: str | None = None
    조문가지번호: str | None = None


class LsdelegatedAdminRuleArticle(BaseModel):
    위임행정규칙제목: str | None = None
    라인텍스트: str | None = None
    위임행정규칙일련번호: str | None = None
    조항호목: str | None = None
    링크텍스트: str | None = None


class LsdelegatedLawRuleArticle(BaseModel):
    라인텍스트: str | None = None
    위임법령조문번호: str | None = None
    조항호목: str | None = None
    링크텍스트: str | None = None
    위임법령조문제목: str | None = None


class LsdelegatedDelegateInfo(BaseModel):
    위임구분: str | None = None
    위임법령제목: str | None = None
    위임법령일련번호: str | None = None
    위임행정규칙조문정보: list[LsdelegatedAdminRuleArticle] = []
    위임법령조문정보: list[LsdelegatedLawRuleArticle] = []

    _normalize_admin = field_validator("위임행정규칙조문정보", mode="before")(_normalize_to_list)
    _normalize_law = field_validator("위임법령조문정보", mode="before")(_normalize_to_list)


class LsdelegatedDelegateArticle(BaseModel):
    위임정보: list[LsdelegatedDelegateInfo] = []
    조정보: LsdelegatedArticleInfo | None = None

    _normalize_delegate = field_validator("위임정보", mode="before")(_normalize_to_list)


class LsdelegatedDetail(BaseModel):
    법령정보: LsdelegatedLawInfo | None = None
    위임조문정보: list[LsdelegatedDelegateArticle] = []


class DrlawList(BaseModel):
    """Response model for 법령-자치법규 연계현황 조회 (drlaw, XML-only).

    Source: specs/kr/lsOrdinConGuide.json + live API response analysis
    """
    model_config = {"populate_by_name": True}

    법령일련번호: str | None = None
    법령ID: str | None = None
    법령공포일자: str | None = None
    법령공포번호: str | None = None
    법령명한글: str | None = None
    조문일련번호: str | None = None
    조문번호: str | None = None
    조문가지번호: str | None = None
    조문제목: str | None = None
    조문개정표시포함여부: str | None = None
    조문공포일자: str | None = None
    조문시행일자: str | None = None
    조문변경여부: str | None = None
    전체건수: str | None = None
    서울특별시: str | None = None
    부산광역시: str | None = None
    대구광역시: str | None = None
    인천광역시: str | None = None
    광주광역시: str | None = None
    대전광역시: str | None = None
    세종특별자치시: str | None = None
    울산광역시: str | None = None
    경기도: str | None = None
    강원도: str | None = None
    충청북도: str | None = None
    충청남도: str | None = None
    전라북도: str | None = None
    전라남도: str | None = None
    경상북도: str | None = None
    경상남도: str | None = None
    제주특별자치도: str | None = None
    교육청: str | None = None
    위임규제여부: str | None = None
    소관부처명: str | None = None
    소관부처코드: str | None = None
    법령시행일자: str | None = None
