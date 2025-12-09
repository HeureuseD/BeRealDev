from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from backend.app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    # 유저 인증 관련
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)

    # 사용자 구분 (admin, 일반 사용자 등)
    role = Column(String(50), default="user")

    # 계정 상태
    is_active = Column(Boolean, default=True)

    # 생성/수정 시간
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(email='{self.email}', role='{self.role}')>"
