"""Auto-generated Pydantic models from specs/kr/*.json + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit by hand.
"""

from pydantic import BaseModel


class AcrList(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 결정문 목록 조회.

    Source: specs/kr/acrListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AcrDetail(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 결정문 본문 조회.

    Source: specs/kr/acrInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AcrspecialdeccList(BaseModel):
    """[GENERATED] Response model for 국민권익위원회 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccAcrListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    샘플_url: str | None = None  # 샘플 URL: 
    1_행정규칙_별표서식_목록_xml_조회: str | None = None  # 1. 행정규칙 별표서식 목록 XML 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_admbyl_type_xml_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=admbyl&type=XML&mobileYn=Y: 
    2_행정규칙_별표서식_목록_html_조회: str | None = None  # 2. 행정규칙 별표서식 목록 HTML 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_admbyl_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=admbyl&type=HTML&mobileYn=Y: 
    3_행정규칙_별표서식_목록_json_조회: str | None = None  # 3. 행정규칙 별표서식 목록 JSON 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_admbyl_type_json_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=admbyl&type=JSON&mobileYn=Y: 
    4_농림축산식품부_행정규칙_별표서식_목록_조회: str | None = None  # 4. 농림축산식품부 행정규칙 별표서식 목록 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_admbyl_type_xml_org_1543000_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=admbyl&type=XML&org=1543000&mobileYn=Y: 

class AdmrulList(BaseModel):
    """[GENERATED] Response model for 행정규칙 목록 조회.

    Source: specs/kr/admrulListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AdmrulDetail(BaseModel):
    """[GENERATED] Response model for 행정규칙 본문 조회.

    Source: specs/kr/mobAdmrulInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_행정규칙_html_상세조회: str | None = None  # 1. 행정규칙 HTML 상세조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_admrul_id_62505_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=admrul&ID=62505&type=HTML&mobileYn=Y: 

class AdmruloldandnewList(BaseModel):
    """[GENERATED] Response model for 행정규칙 신구법 비교 목록 조회.

    Source: specs/kr/admrulOldAndNewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class AdmruloldandnewDetail(BaseModel):
    """[GENERATED] Response model for 행정규칙 신구법 비교 본문 조회.

    Source: specs/kr/admrulOldAndNewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class BaipvcsList(BaseModel):
    """[GENERATED] Response model for 감사원 사전컨설팅 의견서 목록 조회.

    Source: specs/kr/baiPvcsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class CouselsList(BaseModel):
    """[GENERATED] Response model for 맞춤형 법령 조문 목록 조회.

    Source: specs/kr/custLsJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class CouseordinList(BaseModel):
    """[GENERATED] Response model for 맞춤형 자치법규 조문 목록 조회.

    Source: specs/kr/custOrdinJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class DapacgmexpcList(BaseModel):
    """[GENERATED] Response model for 방위사업청 법령해석 목록.

    Source: specs/kr/cgmExpcDapaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class DeccDetail(BaseModel):
    """[GENERATED] Response model for 행정심판례 본문 조회.

    Source: specs/kr/mobDeccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_행정심판례_일련번호가_2782인_행정심판례_html_조회: str | None = None  # 1. 행정심판례 일련번호가 2782인 행정심판례 HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_decc_id_2782_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=decc&ID=2782&type=HTML&mobileYn=Y: 
    2_산림기술자_자격취소처분_취소청구_등_행정심판례_조회: str | None = None  # 2. 산림기술자 자격취소처분 취소청구 등 행정심판례 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_decc_id_222883_lm_산림기술자_자격취소처분_취소청구_등_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=decc&ID=222883&LM=산림기술자 자격취소처분 취소청구 등&type=HTML&mobileYn=Y: 

class DetcList(BaseModel):
    """[GENERATED] Response model for 헌재결정례 목록 조회.

    Source: specs/kr/mobDetcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class DetcDetail(BaseModel):
    """[GENERATED] Response model for 헌재결정례 본문 조회.

    Source: specs/kr/mobDetcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_헌재결정례_일련번호가_58386인_헌재결정례_html_조회: str | None = None  # 1. 헌재결정례 일련번호가 58386인 헌재결정례 HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_detc_id_58386_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=detc&ID=58386&type=HTML&mobileYn=Y: 
    2_산림기술자_자격취소처분_취소청구_등_헌재결정례_조회: str | None = None  # 2. 산림기술자 자격취소처분 취소청구 등 헌재결정례 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_detc_id_127830_lm_자동차관리법제26조등위헌확인등_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=detc&ID=127830&&LM=자동차관리법제26조등위헌확인등&type=HTML&mobileYn=Y: 

class EccList(BaseModel):
    """[GENERATED] Response model for 중앙환경분쟁조정위원회 결정문 목록 조회.

    Source: specs/kr/eccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EccDetail(BaseModel):
    """[GENERATED] Response model for 중앙환경분쟁조정위원회 결정문 본문 조회.

    Source: specs/kr/eccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EflawList(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 목록 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EflawDetail(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 본문 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EflawjosubList(BaseModel):
    """[GENERATED] Response model for 현행법령(시행일) 본문 조항호목 조회 (국가법령정보센터 기준).

    Source: specs/kr/lsEfYdJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EiacList(BaseModel):
    """[GENERATED] Response model for 고용보험심사위원회 결정문 목록 조회.

    Source: specs/kr/eiacListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class EiacDetail(BaseModel):
    """[GENERATED] Response model for 고용보험심사위원회 결정문 본문 조회.

    Source: specs/kr/eiacInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class ElawList(BaseModel):
    """[GENERATED] Response model for 영문 법령 목록 조회.

    Source: specs/kr/lsEngListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class ElawDetail(BaseModel):
    """[GENERATED] Response model for 영문 법령 본문 조회.

    Source: specs/kr/lsEngInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_표준시에_관한_법률_id_html_조회: str | None = None  # 1. 표준시에 관한 법률 ID HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_elaw_id_000744_type_html: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=elaw&ID=000744&type=HTML: 
    2_상호저축은행법_시행령_seq_xml_조회: str | None = None  # 2. 상호저축은행법 시행령 seq XML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_elaw_mst_127280_type_xml: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=elaw&MST=127280&type=XML: 
    3_상호저축은행법_시행령_seq_json_조회: str | None = None  # 3. 상호저축은행법 시행령 seq JSON 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_elaw_mst_127280_type_json: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=elaw&MST=127280&type=JSON: 

class ExpcList(BaseModel):
    """[GENERATED] Response model for 법령해석례 목록 조회.

    Source: specs/kr/mobExpcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class ExpcDetail(BaseModel):
    """[GENERATED] Response model for 법령해석례 본문 조회.

    Source: specs/kr/mobExpcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_법령해석례일련번호가_281909인_해석례_html_조회: str | None = None  # 1. 법령해석례일련번호가 281909인 해석례 HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_expc_id_334617_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=expc&ID=334617&type=HTML&mobileYn=Y: 
    2_여성가족부_건강가정기본법_제35조_제2항_관련_법령해석례_조회: str | None = None  # 2. 여성가족부 - 건강가정기본법 제35조 제2항 관련 법령해석례 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_expc_id_315191_lm_여성가족부_건강가정기본법_제35조_제2항_관련_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=expc&ID=315191&LM=여성가족부 - 건강가정기본법 제35조 제2항 관련&type=HTML&mobileYn=Y: 

class FscList(BaseModel):
    """[GENERATED] Response model for 금융위원회 결정문 목록 조회.

    Source: specs/kr/fscListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class FscDetail(BaseModel):
    """[GENERATED] Response model for 금융위원회 결정문 본문 조회.

    Source: specs/kr/fscInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class FtcList(BaseModel):
    """[GENERATED] Response model for 공정거래위원회 결정문 목록 조회.

    Source: specs/kr/ftcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class FtcDetail(BaseModel):
    """[GENERATED] Response model for 공정거래위원회 결정문 본문 조회.

    Source: specs/kr/ftcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class IaciacList(BaseModel):
    """[GENERATED] Response model for 산업재해보상보험재심사위원회 결정문 목록 조회.

    Source: specs/kr/iaciacListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class IaciacDetail(BaseModel):
    """[GENERATED] Response model for 산업재해보상보험재심사위원회 결정문 본문 조회.

    Source: specs/kr/iaciacInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KccList(BaseModel):
    """[GENERATED] Response model for 방송미디어통신위원회 결정문 목록 조회.

    Source: specs/kr/kccListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KccDetail(BaseModel):
    """[GENERATED] Response model for 방송미디어통신위원회 결정문 본문 조회.

    Source: specs/kr/kccInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class KcgcgmexpcList(BaseModel):
    """[GENERATED] Response model for 해양경찰청 법령해석 목록.

    Source: specs/kr/cgmExpcKcgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class KdcacgmexpcList(BaseModel):
    """[GENERATED] Response model for 질병관리청 법령해석 목록.

    Source: specs/kr/cgmExpcKdcaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class LawDetail(BaseModel):
    """[GENERATED] Response model for 법령 본문 조회.

    Source: specs/kr/mobLsInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_자동차관리법_id_html_조회: str | None = None  # 1. 자동차관리법 ID HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_law_id_1747_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=law&ID=1747&type=HTML&mobileYn=Y: 
    2_자동차관리법_법령_seq_html조회: str | None = None  # 2. 자동차관리법 법령 seq HTML조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_law_mst_91689_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=law&MST=91689&type=HTML&mobileYn=Y: 

class LawjosubList(BaseModel):
    """[GENERATED] Response model for 현행법령(공포일) 본문 조항호목 조회.

    Source: specs/kr/lsNwJoListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LicbylList(BaseModel):
    """[GENERATED] Response model for 법령 별표ㆍ서식 목록 조회.

    Source: specs/kr/mobLsBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_법령_별표서식_목록_xml_검색: str | None = None  # 1. 법령 별표서식 목록 XML 검색: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_licbyl_type_xml_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=licbyl&type=XML&mobileYn=Y: 
    2_법령_별표서식_목록_html_검색: str | None = None  # 2. 법령 별표서식 목록 HTML 검색: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_licbyl_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=licbyl&type=HTML&mobileYn=Y: 
    3_법령_별표서식_목록_json_검색: str | None = None  # 3. 법령 별표서식 목록 JSON 검색: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_licbyl_type_json_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=licbyl&type=JSON&mobileYn=Y: 
    4_경찰청_법령_별표서식_목록_검색: str | None = None  # 4. 경찰청 법령 별표서식 목록 검색: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_licbyl_type_xml_org_1320000_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=licbyl&type=XML&org=1320000&mobileYn=Y: 

class LnklsList(BaseModel):
    """[GENERATED] Response model for 법령 기준 자치법규 연계 관련 목록 조회.

    Source: specs/kr/lsOrdinConListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LnkordList(BaseModel):
    """[GENERATED] Response model for 자치법규 기준 법령 연계 관련 목록 조회.

    Source: specs/kr/ordinLsConListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LsabrvList(BaseModel):
    """[GENERATED] Response model for 법률명 약칭 조회.

    Source: specs/kr/lsAbrvListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LshistoryList(BaseModel):
    """[GENERATED] Response model for 법령 연혁 목록 조회.

    Source: specs/kr/lsHstListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_자동차관리법_법령연혁_html_조회: str | None = None  # 1. 자동차관리법 법령연혁 HTML 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_lshistory_type_html_query_자동차관리법: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=lsHistory&type=HTML&query=자동차관리법: 
    2_소관부처별_행정안전부_1741000_법령연혁_html조회: str | None = None  # 2. 소관부처별(행정안전부 : 1741000) 법령연혁 HTML조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_lshistory_type_html_org_1741000: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=lsHistory&type=HTML&org=1741000: 

class LshistoryDetail(BaseModel):
    """[GENERATED] Response model for 법령 연혁 본문 조회.

    Source: specs/kr/lsHstInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_법령연혁_html_상세조회: str | None = None  # 1. 법령연혁 HTML 상세조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_lshistory_mst_9094_type_html: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=lsHistory&MST=9094&type=HTML: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_lshistory_mst_166500_type_html: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=lsHistory&MST=166500&type=HTML: 

class LshstinfList(BaseModel):
    """[GENERATED] Response model for 법령 변경이력 목록 조회.

    Source: specs/kr/lsChgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LsjohstinfList(BaseModel):
    """[GENERATED] Response model for 조문별 변경 이력 목록 조회.

    Source: specs/kr/lsJoChgListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LsstmdList(BaseModel):
    """[GENERATED] Response model for 법령 체계도 목록 조회.

    Source: specs/kr/lsStmdListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LsstmdDetail(BaseModel):
    """[GENERATED] Response model for 법령 체계도 본문 조회.

    Source: specs/kr/lsStmdInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LstrmList(BaseModel):
    """[GENERATED] Response model for 법령 용어 목록 조회.

    Source: specs/kr/mobLsTrmListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class LstrmDetail(BaseModel):
    """[GENERATED] Response model for 법령 용어 본문 조회.

    Source: specs/kr/lsTrmInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class MafracgmexpcList(BaseModel):
    """[GENERATED] Response model for 농림축산식품부 법령해석 목록.

    Source: specs/kr/cgmExpcMafraListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class NhrckDetail(BaseModel):
    """[GENERATED] Response model for 국가인권위원회 결정문 본문 조회.

    Source: specs/kr/nhrckInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NlrcList(BaseModel):
    """[GENERATED] Response model for 노동위원회 결정문 목록 조회.

    Source: specs/kr/nlrcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NlrcDetail(BaseModel):
    """[GENERATED] Response model for 노동위원회 결정문 본문 조회.

    Source: specs/kr/nlrcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class NpacgmexpcList(BaseModel):
    """[GENERATED] Response model for 경찰청 법령해석 목록.

    Source: specs/kr/cgmExpcNpaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class OcltDetail(BaseModel):
    """[GENERATED] Response model for 중앙토지수용위원회 결정문 본문 조회.

    Source: specs/kr/ocltInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OkacgmexpcList(BaseModel):
    """[GENERATED] Response model for 재외동포청 법령해석 목록.

    Source: specs/kr/cgmExpcOkaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class OldandnewDetail(BaseModel):
    """[GENERATED] Response model for 신구법 본문 조회.

    Source: specs/kr/oldAndNewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OneviewList(BaseModel):
    """[GENERATED] Response model for 한눈보기 목록 조회.

    Source: specs/kr/oneViewListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OneviewDetail(BaseModel):
    """[GENERATED] Response model for 한눈보기 본문 조회.

    Source: specs/kr/oneViewInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OrdinList(BaseModel):
    """[GENERATED] Response model for 자치법규 목록 조회.

    Source: specs/kr/mobOrdinListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class OrdinDetail(BaseModel):
    """[GENERATED] Response model for 자치법규 본문 조회.

    Source: specs/kr/mobOrdinInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_자치법규_id_html_조회: str | None = None  # 1. 자치법규 ID HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_ordin_id_2047729_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=ordin&ID=2047729&type=HTML&mobileYn=Y: 
    2_자치법규_mst_html_조회: str | None = None  # 2. 자치법규 MST HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_ordin_type_html_mobileyn_y_mst_1062134: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=ordin&type=HTML&mobileYn=Y&MST=1062134: 

class OrdinbylList(BaseModel):
    """[GENERATED] Response model for 자치법규 별표ㆍ서식 목록 조회.

    Source: specs/kr/mobOrdinBylListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_자치법규_별표서식_목록_xml_조회: str | None = None  # 1. 자치법규 별표서식 목록 XML 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_ordinbyl_mobileyn_y_type_xml: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=ordinbyl&mobileYn=Y&type=XML: 
    2_자치법규_별표서식_목록_html_조회: str | None = None  # 2. 자치법규 별표서식 목록 HTML 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_ordinbyl_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=ordinbyl&type=HTML&mobileYn=Y: 
    3_자치법규_별표서식_목록_json_조회: str | None = None  # 3. 자치법규 별표서식 목록 JSON 조회: 
    http_www_law_go_kr_drf_lawsearch_do_oc_test_target_ordinbyl_type_json_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawSearch.do?OC=test&target=ordinbyl&type=JSON&mobileYn=Y: 

class PpcList(BaseModel):
    """[GENERATED] Response model for 개인정보보호위원회 결정문 목록 조회.

    Source: specs/kr/ppcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class PpcDetail(BaseModel):
    """[GENERATED] Response model for 개인정보보호위원회 결정문 본문 조회.

    Source: specs/kr/ppcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class PpscgmexpcList(BaseModel):
    """[GENERATED] Response model for 조달청 법령해석 목록.

    Source: specs/kr/cgmExpcPpsListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class PrecDetail(BaseModel):
    """[GENERATED] Response model for 판례 본문 조회.

    Source: specs/kr/mobPrecInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_판례일련번호가_96538인_판례_html_조회: str | None = None  # 1. 판례일련번호가 96538인 판례 HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_prec_id_228547_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=prec&ID=228547&type=HTML&mobileYn=Y: 

class RdacgmexpcList(BaseModel):
    """[GENERATED] Response model for 농촌진흥청 법령해석 목록.

    Source: specs/kr/cgmExpcRdaListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

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
    pass  # no response fields in spec

class SchoolDetail(BaseModel):
    """[GENERATED] Response model for 학칙ㆍ공단ㆍ공공기관 본문 조회.

    Source: specs/kr/schlPubRulInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class SfcList(BaseModel):
    """[GENERATED] Response model for 증권선물위원회 결정문 목록 조회.

    Source: specs/kr/sfcListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class SfcDetail(BaseModel):
    """[GENERATED] Response model for 증권선물위원회 결정문 본문 조회.

    Source: specs/kr/sfcInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class ThdcmpList(BaseModel):
    """[GENERATED] Response model for 3단 비교 목록 조회.

    Source: specs/kr/thdCmpListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class ThdcmpDetail(BaseModel):
    """[GENERATED] Response model for 3단 비교 본문 조회.

    Source: specs/kr/thdCmpInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class TrtyList(BaseModel):
    """[GENERATED] Response model for 조약 목록 조회.

    Source: specs/kr/mobTrtyListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class TrtyDetail(BaseModel):
    """[GENERATED] Response model for 조약 본문 조회.

    Source: specs/kr/mobTrtyInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    샘플_url: str | None = None  # 샘플 URL: 
    1_조약_html_조회: str | None = None  # 1. 조약 HTML 조회: 
    http_www_law_go_kr_drf_lawservice_do_oc_test_target_trty_id_983_type_html_mobileyn_y: str | None = None  # http://www.law.go.kr/DRF/lawService.do?OC=test&target=trty&ID=983&type=HTML&mobileYn=Y: 

class TtspecialdeccList(BaseModel):
    """[GENERATED] Response model for 조세심판원 특별행정심판례 목록 조회.

    Source: specs/kr/specialDeccTtListGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

class TtspecialdeccDetail(BaseModel):
    """[GENERATED] Response model for 조세심판원 특별행정심판례 본문 조회.

    Source: specs/kr/specialDeccTtInfoGuide.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    pass  # no response fields in spec

