import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from axiom.existence_is_span.span_quantifier import quantify

def test_quantify():
    assert quantify('abc') == 3
