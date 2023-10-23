from main import *

def test_scifi_name():
    assert scifi_name("David Yin","Matthews","Austin") == "Yivid Aumat"
    assert scifi_name("Claire Hoverman", "Casis", "Austin") == "Hoire Aucas"