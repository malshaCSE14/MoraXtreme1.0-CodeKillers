import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

base = raw_input()
baseURL =[]
for n in base:
    baseURL.append(hex(ord(n)))

T = input()
targetURLs =[]
for t in range(0,T):
    tgt = raw_input()
    targetURL = []
    for c in tgt:
        targetURL.append(hex(ord(c)))
    targetURLs.append(targetURL)

for eachTargetURL in targetURLs:
    newBaseURL = []
    newTargetURL = []
    if len(eachTargetURL)<len(baseURL):
        multiplies = len(baseURL)//len(eachTargetURL)
        newTargetURL +=multiplies * baseURL
        newTargetURL +=baseURL[0:len(baseURL) % len(eachTargetURL)]
        newBaseURL = baseURL

    elif len(eachTargetURL)>len(baseURL):
        multiplies = len(eachTargetURL) // len(baseURL)
        newBaseURL += multiplies * baseURL
        newBaseURL += baseURL[0:len(eachTargetURL) % len(baseURL)]
        newTargetURL = eachTargetURL
    else:
        newBaseURL = baseURL
        newTargetURL = eachTargetURL
    resultingURL =[]
    print newBaseURL
    for c in range(0,len(newTargetURL)):
        chra = "0x{:02x}".format((int(newTargetURL[c], 16) ^ int(newBaseURL[c], 16)))
        resultingURL.append(chra)
    #print resultingURL
    eightBytes = ''
    for i in resultingURL[-8:]:
        eightBytes+=i[-2:]
    number = int(eightBytes,16)
    base62 = int2base(number,62)
    print base+'/'+base62






