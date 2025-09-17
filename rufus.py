
from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
   # YOUR CODE HERE


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)