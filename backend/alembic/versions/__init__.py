# backend/app/models/__init__.py

from sqlalchemy.orm import declarative_base

# 모든 모델이 공유할 Base 선언
Base = declarative_base()

from backend.app.models.keywords import Keyword
from backend.app.models.topics import Topic
from backend.app.models.trends import Trend
from backend.app.models.users import User

# __all__ 지정해서 외부에서 import할 때 깔끔하게 노출
__all__ = ["Base", "Keyword", "Topic", "Trend", "User"]