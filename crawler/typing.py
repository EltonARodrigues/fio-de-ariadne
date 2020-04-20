from datetime import date
from typing import Callable, Optional, Union


FieldValue = Optional[Union[Union[date, int], str]]
Cast = Callable[[str], Optional[Union[Union[str, date], int]]]
