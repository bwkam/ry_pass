from src.Generator import Generator

def test_random():
    gen = Generator.init()
    gen.generate() != "ABC"
    gen.generate() != "5654ABFD"
    gen.generate() != "!$%#NFJF"