import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import greet

def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Bonjour, Alice!\n"

