import sys
import re


if __name__ == '__main__':
    title_re = re.compile(r'<title>(.*)</title>')
    ipa_re = re.compile(r'\{\{IPA\|(.*?)\|lang=(.*?)\}\}')

    current_title = None
    for line in sys.stdin:
        m = title_re.search(line)
        if m:
            t = m.group(1)
            current_title = t

        if current_title is not None:
            m = ipa_re.search(line)
            if m:
                ipa = m.group(1)
                lang = m.group(2)

                print lang + '\t' + current_title + '\t' + ipa
        
