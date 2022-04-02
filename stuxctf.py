#!/usr/bin/env python3
import math
# (g * a % p) = 5391134870836286926502927177235397878411936185993201788264267119607541691346129888688129092480323386027363105050175216827235981718273698163253326217194256
# (g * b % p) = 8119698214121315840983160573926585899545739988184539364875648433942693876598202641778630681381620186065767618767847683402001454975104342325572663405591876
# (g * c) = 6091917800833598741530924081762225477418277010142022622731688158297759621329407070985497917078988781448889947074350694220209769840915705739528359582454617
p=9975298661930085086019708402870402191114171745913160469454315876556947370642799226714405016920875594030192024506376929926694545081888689821796050434591251
g=7
a=330
b=450
gc=6091917800833598741530924081762225477418277010142022622731688158297759621329407070985497917078988781448889947074350694220209769840915705739528359582454617

gca = (gc**a) % p
gcab = (gca**b) % p

print(str(gcab)[:128])