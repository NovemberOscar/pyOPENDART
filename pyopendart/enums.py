from enum import Enum as BaseEnum


class Enum(BaseEnum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value


class Market(Enum):
    KOSPI = "Y"
    KOSDAQ = "K"
    KONEX = "N"
    ETC = "E"

    def __missing__(self, key):
        return None


class ReportType(Enum):
    Q1 = 11013  # 1분기보고서
    SEMI_ANNUAL = 11012  # 반기보고서
    Q3 = 11014  # 3분기보고서
    ANNUAL = 11011  # 사업보고서


class FinancialStatementDivision(Enum):
    FINANCIAL_STATEMENT = "OFS"
    CONSOLIDATED_FINANCIAL_STATEMENT = "CFS"


class SortBy(Enum):
    DATE = "date"
    CORP_NAME = "crp"
    REPORT_NAME = "rpt"


class DisclosureType(Enum):
    A = "정기공시"
    B = "주요사항보고"
    C = "발행공시"
    D = "지분공시"
    E = "기타공시"
    F = "외부감사관련"
    G = "펀드공시"
    H = "자산유동화"
    I = "거래소공시"
    J = "공정위공시"


class DisclosureTypeDetail(Enum):
    A001 = "사업보고서"
    A002 = "반기보고서"
    A003 = "분기보고서"
    A004 = "등록법인결산서류(자본시장법이전)"
    A005 = "소액공모법인결산서류"
    B001 = "주요사항보고서"
    B002 = "주요경영사항신고(자본시장법 이전)"
    B003 = "최대주주등과의거래신고(자본시장법 이전)"
    C001 = "증권신고(지분증권)"
    C002 = "증권신고(채무증권)"
    C003 = "증권신고(파생결합증권)"
    C004 = "증권신고(합병등)"
    C005 = "증권신고(기타)"
    C006 = "소액공모(지분증권)"
    C007 = "소액공모(채무증권)"
    C008 = "소액공모(파생결합증권)"
    C009 = "소액공모(합병등)"
    C010 = "소액공모(기타)"
    C011 = "호가중개시스템을통한소액매출"
    D001 = "주식등의대량보유상황보고서"
    D002 = "임원ㆍ주요주주특정증권등소유상황보고서"
    D003 = "의결권대리행사권유"
    D004 = "공개매수"
    E001 = "자기주식취득/처분"
    E002 = "신탁계약체결/해지"
    E003 = "합병등종료보고서"
    E004 = "주식매수선택권부여에관한신고"
    E005 = "사외이사에관한신고"
    E006 = "주주총회소집공고"
    E007 = "시장조성/안정조작"
    E008 = "합병등신고서(자본시장법 이전)"
    E009 = "금융위등록/취소(자본시장법 이전)"
    F001 = "감사보고서"
    F002 = "연결감사보고서"
    F003 = "결합감사보고서"
    F004 = "회계법인사업보고서"
    F005 = "감사전재무제표미제출신고서"
    G001 = "증권신고(집합투자증권-신탁형)"
    G002 = "증권신고(집합투자증권-회사형)"
    G003 = "증권신고(집합투자증권-합병)"
    H001 = "자산유동화계획/양도등록"
    H002 = "사업/반기/분기보고서"
    H003 = "증권신고(유동화증권등)"
    H004 = "채권유동화계획/양도등록"
    H005 = "수시보고"
    H006 = "주요사항보고서"
    I001 = "수시공시"
    I002 = "공정공시"
    I003 = "시장조치/안내"
    I004 = "지분공시"
    I005 = "증권투자회사"
    I006 = "채권공시"
    J001 = "대규모내부거래관련"
    J002 = "대규모내부거래관련(구)"
    J004 = "기업집단현황공시"
    J005 = "비상장회사중요사항공시"
    J006 = "기타공정위공시"


class FinancialStatementTypeDetail(Enum):
    BS1 = "재무상태표 | 연결 | 유동/비유동법"
    BS2 = "재무상태표 | 개별 | 유동/비유동법"
    BS3 = "재무상태표 | 연결 | 유동성배열법"
    BS4 = "재무상태표 | 개별 | 유동성배열법"
    IS1 = "별개의 손익계산서 | 연결 | 기능별분류"
    IS2 = "별개의 손익계산서 | 개별 | 기능별분류"
    IS3 = "별개의 손익계산서 | 연결 | 성격별분류"
    IS4 = "별개의 손익계산서 | 개별 | 성격별분류"
    CIS1 = "포괄손익계산서 | 연결 | 세후"
    CIS2 = "포괄손익계산서 | 개별 | 세후"
    CIS3 = "포괄손익계산서 | 연결 | 세전"
    CIS4 = "포괄손익계산서 | 개별 | 세전"
    DCIS1 = "단일 포괄손익계산서 | 연결 | 기능별분류 | 세후포괄손익"
    DCIS2 = "단일 포괄손익계산서 | 개별 | 기능별분류 | 세후포괄손익"
    DCIS3 = "단일 포괄손익계산서 | 연결 | 기능별분류 | 세전"
    DCIS4 = "단일 포괄손익계산서 | 개별 | 기능별분류 | 세전"
    DCIS5 = "단일 포괄손익계산서 | 연결 | 성격별분류 | 세후포괄손익"
    DCIS6 = "단일 포괄손익계산서 | 개별 | 성격별분류 | 세후포괄손익"
    DCIS7 = "단일 포괄손익계산서 | 연결 | 성격별분류 | 세전"
    DCIS8 = "단일 포괄손익계산서 | 개별 | 성격별분류 | 세전"
    CF1 = "현금흐름표 | 연결 | 직접법"
    CF2 = "현금흐름표 | 개별 | 직접법"
    CF3 = "현금흐름표 | 연결 | 간접법"
    CF4 = "현금흐름표 | 개별 | 간접법"
    SCE1 = "자본변동표 | 연결"
    SCE2 = "자본변동표 | 개별"


class RenameMode(Enum):
    ENG = 1
    KOR = 2
