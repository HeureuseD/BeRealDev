from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from backend.app.database import Base

class Trend(Base):
    __tablename__ = "trends"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(255), nullable=True)          # 데이터 수집 출처 (Google News, Naver 등)
    title = Column(String(500), nullable=False)         # 기사/문서 제목
    url = Column(String(1000), nullable=True)           # 원본 링크
    content = Column(Text, nullable=True)               # 본문 텍스트
    collected_at = Column(DateTime, default=datetime.utcnow)  # 데이터 수집 시간

    def __repr__(self):
        return f"<Trend(title='{self.title}', source='{self.source}')>"
