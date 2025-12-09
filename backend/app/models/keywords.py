from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.database import Base


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True)

    # 외래키 설정
    trend_id = Column(Integer, ForeignKey("trends.id", ondelete="CASCADE"))
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="SET NULL"), nullable=True)

    # 키워드 본문
    keyword = Column(String(255), nullable=False)

    # NLP confidence score ex) 0.92
    confidence = Column(Float, nullable=True)

    # 관계 매핑
    trend = relationship("Trend", backref="keywords")
    topic = relationship("Topic", backref="keywords")

    def __repr__(self):
        return f"<Keyword(keyword='{self.keyword}', trend_id={self.trend_id}, confidence={self.confidence})>"
