#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds user to database
        Return: User Object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Finds a user by arbitrary keyword arguments.
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            User: The first user found matching the arguments.
        Raises:
            NoResultFound: If no user is found.
            InvalidRequestError: If invalid arguments are provided.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("No user found with the provided filter.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid filter arguments provided.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user based on user ID
        """
        user = self.find_user_by(id=user_id)
        VALID_KEYS = ['id', 'email', 'hashed_password', 'session_id',
                      'reset_token']
        for k, v in kwargs.items():
            if k not in VALID_KEYS:
                raise ValueError
            setattr(user, k, v)
        self._session.commit()
