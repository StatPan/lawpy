# Korean Law API Modules

This directory contains the Korean National Law Information Center Open API implementation.

## Architecture

The module structure follows the official [Korean Law Open API Guide](https://open.law.go.kr/LSO/openApi/guideList.do) to provide an intuitive and maintainable interface.

### Design Principles

1. **API Guide Alignment**: Module structure mirrors the official API guide (구분 → 분류 → 제공API)
2. **Modular Design**: Each category (구분) is a separate module for easy maintenance
3. **Unified Interface**: All modules share a common base class for consistency
4. **Flexible Usage**: Use individual modules or the integrated client based on needs

## Module Structure

```
lawpy/kr/
├── base.py                    # Common base class (HTTP client, exception handling)
├── law.py                     # Law (법령) - main text, articles, history, etc.
├── admin_rule.py              # Administrative Rules (행정규칙)
├── ordinance.py               # Autonomous Ordinances (자치법규)
├── precedent.py               # Precedents (판례)
├── constitutional_decision.py # Constitutional Court Decisions (헌재결정례)
├── interpretation.py          # Legal Interpretation Cases (법령해석례)
├── admin_review.py            # Administrative Review Cases (행정심판례)
├── committee/                 # Committee Decisions (위원회결정문 - 12 committees)
├── treaty.py                  # Treaties (조약)
├── annex_form.py              # Annexes and Forms (별표·서식)
├── school_public.py           # School Regulations, Public Agencies (학칙·공단·공공기관)
├── terminology.py             # Legal Terminology (법령용어)
├── mobile/                    # Mobile APIs (optimized for mobile)
├── customized.py              # Customized Services (맞춤형)
├── knowledge_base.py          # Legal Knowledge Base (법령정보지식베이스)
├── ministry_interpretation/   # Ministry Interpretations (중앙부처 1차 해석 - 26 ministries)
└── client.py                   # Integrated Client (all APIs in one)
```

## Category Mapping

| 구분 (Category) | Module | Description |
|----------------|--------|-------------|
| 법령 | `law.py` | Laws, decrees, ordinances with full text, articles, history |
| 행정규칙 | `admin_rule.py` | Administrative rules and regulations |
| 자치법규 | `ordinance.py` | Local government ordinances |
| 판례 | `precedent.py` | Court precedents |
| 헌재결정례 | `constitutional_decision.py` | Constitutional Court decisions |
| 법령해석례 | `interpretation.py` | Legal interpretation cases |
| 행정심판례 | `admin_review.py` | Administrative review cases |
| 위원회결정문 | `committee/` | Decisions from 12 committees |
| 조약 | `treaty.py` | International treaties |
| 별표·서식 | `annex_form.py` | Annexes and forms |
| 학칙·공단·공공기관 | `school_public.py` | School regulations, public agencies |
| 법령용어 | `terminology.py` | Legal terminology |
| 모바일 | `mobile/` | Mobile-optimized APIs |
| 맞춤형 | `customized.py` | Customized services |
| 법령정보지식베이스 | `knowledge_base.py` | Legal knowledge base (terms, relations, AI search) |
| 중앙부처 1차 해석 | `ministry_interpretation/` | First-level interpretations from 26 ministries |

## Usage

### Integrated Client (All APIs)

```python
from lawpy.kr import KoreanLawClient

client = KoreanLawClient(api_key="your_email_id")

# Law APIs
laws = client.search_laws("민법")
law_detail = client.get_law_detail(law_id="009682")
law_history = client.get_law_history(query="민법")
history_detail = client.get_law_history_detail(mst=9094)

# Precedent APIs (to be implemented)
precedents = client.search_precedents("민법")
```

### Individual Modules (Lightweight)

```python
from lawpy.kr.law import LawClient

client = LawClient(api_key="your_email_id")
laws = client.search_laws("민법")
```

## Module Details

### Law (law.py)

**Sub-categories**: 본문, 조항호목, 영문법령, 이력, 연계, 부가서비스

- `search_laws()` - Search laws (target=law)
- `get_law_detail()` - Get full text of a specific law
- `get_law_list()` - Get current law list by effective date
- `get_law_history()` - Get law amendment history list
- `get_law_history_detail()` - Get detailed amendment history text
- `get_law_articles()` - Get articles by item/hang/mok (to be implemented)
- `get_law_english()` - Get English version (to be implemented)
- `get_law_change_history()` - Get law change history (to be implemented)
- `get_law_delegated()` - Get delegated ordinances (to be implemented)
- `get_law_structure()` - Get law structure (to be implemented)
- `get_law_old_new()` - Get old/new law comparison (to be implemented)
- `get_law_3way_compare()` - Get 3-way comparison (to be implemented)
- `get_law_abbr()` - Get law abbreviations (to be implemented)
- `get_law_deleted_data()` - Get deleted data (to be implemented)
- `get_law_overview()` - Get overview (to be implemented)

### Committee (committee/)

**12 Committees**:

| Module | Committee |
|--------|-----------|
| `privacy_protection.py` | 개인정보보호위원회 (Personal Information Protection Commission) |
| `employment_insurance.py` | 고용보험심사위원회 (Employment Insurance Review Commission) |
| `fair_trade.py` | 공정거래위원회 (Fair Trade Commission) |
| `civil_rights.py` | 국민권익위원회 (Anti-Corruption & Civil Rights Commission) |
| `financial_services.py` | 금융위원회 (Financial Services Commission) |
| `labor_relations.py` | 노동위원회 (National Labor Relations Commission) |
| `broadcasting.py` | 방송미디어통신위원회 (Korea Communications Commission) |
| `industrial_accident.py` | 산업재해보상보험재심사위원회 (Industrial Accident Reconsideration Commission) |
| `land_expropriation.py` | 중앙토지수용위원회 (Central Land Expropriation Committee) |
| `environment_dispute.py` | 중앙환경분쟁조정위원회 (Central Environmental Dispute Mediation Commission) |
| `securities_futures.py` | 증권선물위원회 (Financial Supervisory Service) |
| `human_rights.py` | 국가인권위원회 (National Human Rights Commission) |

### Ministry Interpretation (ministry_interpretation/)

**26 Ministries**:

| Module | Ministry |
|--------|----------|
| `employment_labor.py` | 고용노동部 (Ministry of Employment and Labor) |
| `land_transport.py` | 국토교통部 (Ministry of Land, Infrastructure and Transport) |
| `economy_finance.py` | 재정경제部 (Ministry of Economy and Finance) |
| `maritime_fisheries.py` | 해양수산部 (Ministry of Oceans and Fisheries) |
| `interior_safety.py` | 행정안전部 (Ministry of the Interior and Safety) |
| `environment_energy.py` | 기후에너지환경部 (Ministry of Environment) |
| `customs.py` | 관세청 (Korea Customs Service) |
| `national_tax.py` | 국세청 (National Tax Service) |
| `education.py` | 교육部 (Ministry of Education) |
| `science_ict.py` | 과학기술정보통신部 (Ministry of Science and ICT) |
| `veterans_affairs.py` | 국가보훈部 (Ministry of Patriots and Veterans Affairs) |
| `defense.py` | 국방部 (Ministry of National Defense) |
| `agriculture_food.py` | 농림축산식품部 (Ministry of Agriculture, Food and Rural Affairs) |
| `culture_tourism.py` | 문화체육관광部 (Ministry of Culture, Sports and Tourism) |
| `justice.py` | 법무部 (Ministry of Justice) |
| `health_welfare.py` | 보건복지部 (Ministry of Health and Welfare) |
| `industry_trade.py` | 산업통상자원部 (Ministry of Trade, Industry and Energy) |
| `gender_equality.py` | 성평등가족部 (Ministry of Gender Equality and Family) |
| `foreign_affairs.py` | 외교部 (Ministry of Foreign Affairs) |
| `sme_startups.py` | 중소벤처기업部 (Ministry of SMEs and Startups) |
| `unification.py` | 통일部 (Ministry of Unification) |
| `government_legislation.py` | 법제처 (Ministry of Government Legislation) |
| `food_drug_safety.py` | 식품의약품안전처 (Ministry of Food and Drug Safety) |
| `personnel_management.py` | 인사혁신처 (Ministry of Personnel Management) |
| `meteorology.py` | 기상청 (Korea Meteorological Administration) |
| `heritage.py` | 국가유산청 (Heritage Administration) |

## Implementation Status

| Category | Module | Status |
|----------|--------|--------|
| 법령 | `law.py` | ✅ Partial (search, detail, list, history) |
| 행정규칙 | `admin_rule.py` | ⏳ Not started |
| 자치법규 | `ordinance.py` | ⏳ Not started |
| 판례 | `precedent.py` | ⏳ Not started |
| 헌재결정례 | `constitutional_decision.py` | ⏳ Not started |
| 법령해석례 | `interpretation.py` | ⏳ Not started |
| 행정심판례 | `admin_review.py` | ⏳ Not started |
| 위원회결정문 | `committee/` | ⏳ Not started |
| 조약 | `treaty.py` | ⏳ Not started |
| 별표·서식 | `annex_form.py` | ⏳ Not started |
| 학칙·공단·공공기관 | `school_public.py` | ⏳ Not started |
| 법령용어 | `terminology.py` | ⏳ Not started |
| 모바일 | `mobile/` | ⏳ Not started |
| 맞춤형 | `customized.py` | ⏳ Not started |
| 법령정보지식베이스 | `knowledge_base.py` | ⏳ Not started |
| 중앙부처 1차 해석 | `ministry_interpretation/` | ⏳ Not started |

## API Key

API key is your email ID registered with the [Korean National Law Information Center](https://open.law.go.kr/).

```bash
export LAWPY_API_KEY=your_email_id
```

Or pass it directly:

```python
from lawpy.kr import KoreanLawClient
client = KoreanLawClient(api_key="your_email_id")
```

## References

- [Korean Law Open API Guide](https://open.law.go.kr/LSO/openApi/guideList.do)
- [API Application](https://open.law.go.kr/LSO/openApi/cuAskList.do)
