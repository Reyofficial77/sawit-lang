import sys
import os

def jalanin_sawit(filepath):
    try:
        with open(filepath, 'r') as file:
            code = file.read()

        kamus = {
            "nyawit nih orang": "if",
            "67 nanggung rindu": "elif",
            "kebanyakan meratapi": "else",
            "tidak fantashh": "while",
            "19 jt": "for",
            "pria sawit": "in",
            "mati": "break",
            "pria etanol": "continue",
            "fomo": "pass",
            "pria 19 jt iq": "True",
            "pria solo": "False",
            "rakyat biasa": "None",
            "meta": "and",
            "aldis burger": "or",
            "cempaka putih": "not",
            "roti lembut": "is",
            "juicy luicy": "==",
            "riski febria": "!=",
            "ireng": "def",
            "balik": "return",
            "kelass": "class",
            "my": "self",
            "my gw": "__init__",
            "my in tain": "__main__",
            "ibu bapak lu sehat": "print",
            "aldis burger cempaka putih rotinya lembut juicy luicy riski febria bisa beli online": "input",
            "ga peduli": "str",
            "ga masalah": "int",
            "ga papa": "float",
            "tertawa tapi terluka": "list",
            "broken": "dict",
            "brutal": "len",
            "ea": "range",
            "angkat tangan": "sorted",
            "tau": "sum",
            "kegedean": "max",
            "kekecilan": "min",
            "tembok ratapan": "round",
            "minyak sawit": "import",
            "seleb": "from",
            "damn": "as",
            "bro": "with",
            "kebuka": "open",
            "tni amerika": "global",
            "tni inggris": "os.system('clear')",
            "coll i": "try",
            "coolmax": "except",
            "adalah pokoknya": "finally",
            "kulit lu warna apa bos": "raise"
        }

        for sawit in sorted(kamus.keys(), key=len, reverse=True):
            code = code.replace(sawit, kamus[sawit])

        custom_globals = {"__name__": "__main__", "os": os}
        exec(code, custom_globals)

    except FileNotFoundError:
        print(f"File {filepath} ga ketemu ngab!")
    except Exception as e:
        print(f"🔥 Waduh meledak kodenya:\n{e}")

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "now":
        print("💡 Pake command: nyawit now nama_file.sawit")
    else:
        jalanin_sawit(sys.argv[2])

