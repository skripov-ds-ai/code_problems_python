import pymystem3

s = input().strip()

def lemma_and_part_of_speech(s):
    myst = pymystem3.Mystem()
    a = myst.analyze(s)
    b = []

    for x in a:
        if 'analysis' in x:
            t = x['analysis'][0]['gr']
            t = t.replace('=', ',').split(',')
            #print(x)
            st = str(x['analysis'][0]['lex']).lower() + "|" + t[0]
            b.append(st)
    myst.close()
    return b


ans = lemma_and_part_of_speech(s)

print(' '.join(map(str, ans)))

# под|PR круглый|A прозрачный|A колпак|S
# из|PR неравномерно|ADV утолщающийся|A
# книзу|ADV стекло|S сиять|V торcионный|A весы|S
#

# под|PR круглым|A прозрачным|A колпаком|S
# из|PR неравномерно|ADV утолщающегося|V книзу|ADV стекла|S сияли|V торсионные|A часы|S
