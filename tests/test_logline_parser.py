import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.logline_parser import parse_logline

def test_architecture_parsed():
    with open('docs/ARCHITECTURE.logline') as f:
        data = parse_logline(f.read())
    assert data[0]['type'] == 'architecture'


def test_dao_rule():
    with open('governance/dao_contract.logline') as f:
        data = parse_logline(f.read())
    dao = data[0]
    assert any(child.get('type') == 'rule' for child in dao.get('rules', []))
