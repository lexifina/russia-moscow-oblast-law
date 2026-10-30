"""Independent letters-and-digits check of a corpus.d part against the Duma's text. Private.

The source is read again from the cached API page (sha256 must match the version's), and the law's HTML is read by
Python's html.parser (not parse.py's regular expressions). Every letter and digit of the source, in order, must equal
every letter and digit of the corpus units, in order (nothing dropped, added or moved).

    python -X utf8 verify.py corpus.d/20-zakony-01.json
"""
import hashlib, json, re, sys, unicodedata
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE.parent / 'russia-regions' / '.cache' / 'mosoblduma' / 'laws'


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        self.skip += tag in ('script', 'style')

    def handle_endtag(self, tag):
        self.skip -= tag in ('script', 'style') and self.skip > 0

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def alnum(s):
    return ''.join(c for c in unicodedata.normalize('NFC', s) if c.isalnum())


def main(part):
    c = json.loads(Path(part).read_text(encoding='utf-8'))
    bad = n = 0
    for a in c['acts']:
        for v in a['versions']:
            n += 1
            page = CACHE / f'p{int(v["source_url"].rsplit("=", 1)[1]):04d}.json'
            raw = page.read_bytes()
            assert hashlib.sha256(raw).hexdigest() == v['sha256'], a['slug']
            num = a['short'].split('№ ', 1)[1]
            def key(x):
                m = re.fullmatch(r'(\d+)/(\d{2}|\d{4})-ОЗ', x.replace(' ', ''))
                y = m and (m.group(2) if len(m.group(2)) == 4 else ('19' if int(m.group(2)) > 50 else '20') + m.group(2))
                return m and (int(m.group(1)), y)
            recs = [r for r in json.loads(raw)['data'] if key(r['number'] or '') == key(num)]
            assert len(recs) == 1, (a['slug'], len(recs))
            p = Text()
            p.feed(recs[0]['text'])
            p.close()
            src = alnum(''.join(p.out))
            ours = alnum(''.join(u['text'] for u in v['units'].values()))
            ok = src == ours
            bad += not ok
            if not ok:
                i = next((k for k in range(min(len(src), len(ours))) if src[k] != ours[k]), min(len(src), len(ours)))
                print('FAIL', a['slug'], len(ours), len(src), 'ours:', ours[i:i + 40], '| source:', src[i:i + 40])
    print(f'{part}: {n} versions, {bad} failing')
    return bad


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1]) else 0)
