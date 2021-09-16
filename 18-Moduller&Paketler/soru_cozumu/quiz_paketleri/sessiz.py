"""
verilen stringin içindeki sessiz harfleri alan bir modul


"""


def sessiz_harfler(kel):
    sessizler = set()
    sesliler = "aeiouıöü"

    try:
        for harf in kel:
            if not harf in sesliler and harf.isalpha():
                sessizler.add(harf)
    except:
        pass
    finally:
        return sessizler



