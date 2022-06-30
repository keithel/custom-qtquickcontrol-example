# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.3.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xcf\
[\
Controls]\x0d\x0aStyle\
=MyStyle\x0d\x0aFallba\
ckStyle=Material\
\x0d\x0a\x0d\x0a[Material]\x0d\x0a\
Variant=Dense\x0d\x0aA\
ccent=\x22#FF8300\x22\x0d\
\x0a# Theme=Light\x0d\x0a\
# Primary=<Color\
 like BlueGrey>\x0d\
\x0a\x0d\x0a[Default]\x0d\x0aFo\
nt\x5cFamily=Roboto\
 Condensed\x0d\x0aFont\
\x5cPixelSize=9\x0d\x0a\
\x00\x00\x0e\xb2\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: http://\
www.qt.io/licens\
ing/\x0d\x0a**\x0d\x0a** Thi\
s file is part o\
f the Qt Quick C\
ontrols 2 module\
 of the Qt Toolk\
it.\x0d\x0a**\x0d\x0a** $QT_\
BEGIN_LICENSE:LG\
PL3$\x0d\x0a** Commerc\
ial License Usag\
e\x0d\x0a** Licensees \
holding valid co\
mmercial Qt lice\
nses may use thi\
s file in\x0d\x0a** ac\
cordance with th\
e commercial lic\
ense agreement p\
rovided with the\
\x0d\x0a** Software or\
, alternatively,\
 in accordance w\
ith the terms co\
ntained in\x0d\x0a** a\
 written agreeme\
nt between you a\
nd The Qt Compan\
y. For licensing\
 terms\x0d\x0a** and c\
onditions see ht\
tp://www.qt.io/t\
erms-conditions.\
 For further\x0d\x0a**\
 information use\
 the contact for\
m at http://www.\
qt.io/contact-us\
.\x0d\x0a**\x0d\x0a** GNU Le\
sser General Pub\
lic License Usag\
e\x0d\x0a** Alternativ\
ely, this file m\
ay be used under\
 the terms of th\
e GNU Lesser\x0d\x0a**\
 General Public \
License version \
3 as published b\
y the Free Softw\
are\x0d\x0a** Foundati\
on and appearing\
 in the file LIC\
ENSE.LGPLv3 incl\
uded in the\x0d\x0a** \
packaging of thi\
s file. Please r\
eview the follow\
ing information \
to\x0d\x0a** ensure th\
e GNU Lesser Gen\
eral Public Lice\
nse version 3 re\
quirements\x0d\x0a** w\
ill be met: http\
s://www.gnu.org/\
licenses/lgpl.ht\
ml.\x0d\x0a**\x0d\x0a** GNU \
General Public L\
icense Usage\x0d\x0a**\
 Alternatively, \
this file may be\
 used under the \
terms of the GNU\
\x0d\x0a** General Pub\
lic License vers\
ion 2.0 or later\
 as published by\
 the Free\x0d\x0a** So\
ftware Foundatio\
n and appearing \
in the file LICE\
NSE.GPL included\
 in\x0d\x0a** the pack\
aging of this fi\
le. Please revie\
w the following \
information to\x0d\x0a\
** ensure the GN\
U General Public\
 License version\
 2.0 requirement\
s will be\x0d\x0a** me\
t: http://www.gn\
u.org/licenses/g\
pl-2.0.html.\x0d\x0a**\
\x0d\x0a** $QT_END_LIC\
ENSE$\x0d\x0a**\x0d\x0a*****\
****************\
****************\
****************\
****************\
*******/\x0d\x0a\x0d\x0aimpo\
rt QtQuick 2.12\x0d\
\x0aimport QtQuick.\
Controls 2.12\x0d\x0ai\
mport QtQuick.Co\
ntrols.Material \
2.12\x0d\x0aimport QtQ\
uick.Controls.Ma\
terial.impl 2.12\
\x0d\x0aimport QtQuick\
.Controls.impl 2\
.12\x0d\x0aimport QtQu\
ick.Templates 2.\
12 as T\x0d\x0a\x0d\x0aT.Tab\
Button {\x0d\x0a    id\
: control\x0d\x0a\x0d\x0a   \
 property color \
labelColor: !con\
trol.enabled ? c\
ontrol.Material.\
hintTextColor : \
control.down || \
control.checked \
? \x22white\x22 : \x22#76\
7676\x22\x0d\x0a    prope\
rty color gradie\
ntStartColor: do\
wn || checked ? \
Qt.lighter(\x22#323\
F48\x22, 1.7) : hov\
ered ? Qt.lighte\
r(\x22#E0E0E0\x22, 1.1\
) : \x22white\x22\x0d\x0a   \
 property color \
backgroundColor:\
 down || checked\
 ? \x22#323F48\x22 : h\
overed ? Qt.dark\
er(\x22#E0E0E0\x22, 1.\
1) : \x22#E0E0E0\x22\x0d\x0a\
    property boo\
l border: true\x0d\x0a\
\x0d\x0a    implicitWi\
dth: Math.max(im\
plicitBackground\
Width + leftInse\
t + rightInset, \
implicitContentW\
idth + leftPaddi\
ng + rightPaddin\
g)\x0d\x0a    implicit\
Height: Math.max\
(implicitBackgro\
undHeight + topI\
nset + bottomIns\
et, implicitCont\
entHeight + topP\
adding + bottomP\
adding)\x0d\x0a    pad\
ding: 12\x0d\x0a    sp\
acing: 6\x0d\x0a    ic\
on.width: 24\x0d\x0a  \
  icon.height: 2\
4\x0d\x0a    icon.colo\
r: !enabled ? Ma\
terial.hintTextC\
olor : down || c\
hecked ? \x22white\x22\
 : \x22#767676\x22\x0d\x0a\x0d\x0a\
    font {\x0d\x0a    \
    family: \x22Hel\
vetica\x22\x0d\x0a       \
 pixelSize: 20\x0d\x0a\
        bold: tr\
ue\x0d\x0a        capi\
talization: Font\
.MixedCase\x0d\x0a    \
}\x0d\x0a\x0d\x0a    content\
Item: IconLabel \
{\x0d\x0a        spaci\
ng: control.spac\
ing\x0d\x0a        mir\
rored: control.m\
irrored\x0d\x0a       \
 display: contro\
l.display\x0d\x0a     \
   icon: control\
.icon\x0d\x0a        t\
ext: control.tex\
t\x0d\x0a        font:\
 control.font\x0d\x0a \
       color: co\
ntrol.labelColor\
\x0d\x0a    }\x0d\x0a\x0d\x0a    b\
ackground: Recta\
ngle {\x0d\x0a        \
border.width: co\
ntrol.border ? 1\
 : 0\x0d\x0a        bo\
rder.color: \x22#C2\
C2C2\x22\x0d\x0a        i\
mplicitHeight: c\
ontrol.Material.\
touchTarget\x0d\x0a   \
     clip: true\x0d\
\x0a        color: \
backgroundColor\x0d\
\x0a\x0d\x0a        gradi\
ent: Gradient {\x0d\
\x0a            Gra\
dientStop {\x0d\x0a   \
             pos\
ition: 0\x0d\x0a      \
          color:\
 gradientStartCo\
lor\x0d\x0a           \
 }\x0d\x0a\x0d\x0a          \
  GradientStop {\
\x0d\x0a              \
  position: 1\x0d\x0a \
               c\
olor: background\
Color\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
}\x0d\x0a\x0d\x0a    }\x0d\x0a\x0d\x0a}\x0d\
\x0a\
\x00\x00\x06\xad\
i\
mport QtQuick 2.\
12\x0d\x0aimport QtQui\
ck.Controls.Mate\
rial 2.12\x0d\x0aimpor\
t QtQuick.Contro\
ls.Material.impl\
 2.12\x0d\x0aimport Qt\
Quick.Templates \
2.12 as T\x0d\x0a\x0d\x0aT.T\
abBar {\x0d\x0a    id:\
 control\x0d\x0a\x0d\x0a    \
property var ori\
entation: ListVi\
ew.Horizontal\x0d\x0a\x0d\
\x0a    implicitWid\
th: Math.max(imp\
licitBackgroundW\
idth + leftInset\
 + rightInset, c\
ontentWidth + le\
ftPadding + righ\
tPadding)\x0d\x0a    i\
mplicitHeight: M\
ath.max(implicit\
BackgroundHeight\
 + topInset + bo\
ttomInset, conte\
ntHeight + topPa\
dding + bottomPa\
dding)\x0d\x0a\x0d\x0a    co\
ntentItem: ListV\
iew {\x0d\x0a        m\
odel: control.co\
ntentModel\x0d\x0a    \
    currentIndex\
: control.curren\
tIndex\x0d\x0a        \
spacing: control\
.spacing\x0d\x0a      \
  orientation: c\
ontrol.orientati\
on\x0d\x0a        boun\
dsBehavior: Flic\
kable.StopAtBoun\
ds\x0d\x0a        flic\
kableDirection: \
Flickable.AutoFl\
ickIfNeeded\x0d\x0a   \
     snapMode: L\
istView.SnapToIt\
em\x0d\x0a        high\
lightMoveDuratio\
n: 250\x0d\x0a        \
highlightResizeD\
uration: 0\x0d\x0a    \
    highlightFol\
lowsCurrentItem:\
 true\x0d\x0a        h\
ighlightRangeMod\
e: ListView.Appl\
yRange\x0d\x0a        \
preferredHighlig\
htBegin: 48\x0d\x0a   \
     preferredHi\
ghlightEnd: widt\
h - 48\x0d\x0a\x0d\x0a      \
  highlight: Ite\
m {\x0d\x0a           \
 z: 2\x0d\x0a\x0d\x0a       \
     Rectangle {\
\x0d\x0a              \
  height: 2\x0d\x0a   \
             wid\
th: parent.width\
\x0d\x0a              \
  y: control.pos\
ition === T.TabB\
ar.Footer ? 0 : \
parent.height - \
height\x0d\x0a        \
        color: c\
ontrol.Material.\
accentColor\x0d\x0a   \
         }\x0d\x0a\x0d\x0a  \
      }\x0d\x0a\x0d\x0a    }\
\x0d\x0a\x0d\x0a    backgrou\
nd: Item {\x0d\x0a    \
    Rectangle {\x0d\
\x0a            anc\
hors.fill: paren\
t\x0d\x0a            c\
olor: \x22orange\x22\x0d\x0a\
            laye\
r.enabled: contr\
ol.Material.elev\
ation > 0\x0d\x0a\x0d\x0a   \
         layer.e\
ffect: Elevation\
Effect {\x0d\x0a      \
          elevat\
ion: control.Mat\
erial.elevation\x0d\
\x0a               \
 fullWidth: true\
\x0d\x0a            }\x0d\
\x0a\x0d\x0a        }\x0d\x0a\x0d\x0a\
    }\x0d\x0a\x0d\x0a}\x0d\x0a\
\x00\x00\x00\xae\
m\
odule MyStyle\x0d\x0a\x0d\
\x0aButton 6.0 Butt\
on.qml\x0d\x0aCombobox\
 6.0 Combobox.qm\
l\x0d\x0aLabel 6.0 Lab\
el.qml\x0d\x0aRoundBut\
ton 6.0 RoundBut\
ton.qml\x0d\x0aTabBar \
6.0 TabBar.qml\x0d\x0a\
TabButton 6.0 Ta\
bButton.qml\x0d\x0a\
\x00\x00\x08w\
\x00\
\x00\x1f\x99x\x9c\xd5\x18mo\xdb\xb8\xf9{\x81\xfe\x07\
\xd6(\x0e\xc9\xd6H\x8e{\xbdu\x06\xba\xa0M\x936\
@\x92\xa6\xad\xef\xee\xc30\x14\xb4D[\x5c%R\xa5\
(\xbf\xdcn\xff}\x0f_$R\x94\xec\xb8w\xd7\x0d\
\x13\x90X\xe2\xf3\xca\xe7\x9d\x8c\xff\xf4\x07>\x0f\x1f\x98\
?t\xce\xcb\xad\xa0\xcbL\xa2\xa3\xf3c4\x19\x9f\xfe\
\x05\xcd2\x82\xdeK\x80\x14%f[t-\xd3\xc8\xa2\
2\x89\x139E\x99\x94\xe54\x8e\xd7\xebu\xf4EF\
\x94\xc79M\x08\xab([\xc6-\xdfYF+\xb4\xa0\
9A\xf0[b!\x11_ i8\xbf\xafi\xf2Y\
\xb3\x13<\xaf\xd0\x04\x15<\xad\x01\xd3a\xcc8\xcf?\
S\x19\xb5\xec\x1e\xbf\x9f}zu\xf1\xe6\xea\xf6\xd3\xf5\
\xd5\xf9\xc5\xed\xc7\x8b\xe9\xf5\x9b\xbb\xeb\xa7\x8f\xadbE\
ADBq\x8e\xae\xb5&\x04\xfdX\xe1%\xd1@\xbb\
B*\x94\xf1<\x05\x1d\xd1\x0a\xe74E\x89#\x02\x81\
f\x07\x80T\xe0-\xaa\x81\x81t\xfa3\xcd\x07'\x09\
\x17)f\x09Ak*3\xad\xa9\xc7\xc32@x)\
\x08)\x08\x93\xa8\x14|ES\x92\xb6\xe8\x9a\xcdG\xbe\
\x90k,`\xb3\xe2\x09\xc2\xb9$\x82aIW$\xdf\
>\x01I\x83R\x00\xa7\xa8@\x16X\x9f2\xe0\xd7(\
\x84\xd6\x82JI\x98'sN\xe4\x9a\xc0\xca\x96\xd7\x08\
\xb34pe\x84.\xb9@\xad\xb3\x0cc\xc3\x8b)\x83\
\xb0\x94J\xcaY\x85\xc0\x5c}'k\xec\x13\x87e\xb8\
-j\x01:\x0a\xcd\x85\xb2\x05\x17\x05VPkCb\
\xd4N$R\x10\x84e\x9f\xadE8\xa9+\xe7\xed7\
\xb7?\xa2kRUD\xa07\x84\x11\x01\xf6\xbd\xab\xe7\
\xa0\xf8\x80\x7f_vm\xe8\xfc\xa6<9'J\x91\x14\
\xd5,\x05^\xce\x986\xd2\x9c\x1c#vX\xd6\x8a\x88\
Jm\xe9)\xc2\x10\xca\x0aVe\xc0s\xbe\xd5<.\
\xc1\xf6\xadW5\x9bK\x0e\xe2\x8c\x15\x94]qY\x12\
,\x94\xbd\xc1\xbf\x8aBkg\xc38Ra\xbcz\x0a\
\xa0$\xafS\xed\xdc6TJ\x9c|\xc6KE\xa8\xd5\
\xb5\xfb\x8a\xd0]N0\xa8%\xc8\x8a\x92\xb5\xe1\xc8\xf3\
\x9c\xaf\x8d\x08\xe7\x02\xc95\x1b\xd8C-H\xb0\xdf\xfb\
\xf7*\xc8\x97\x9a\x0a\x1dV&F\xd64\xcf\x95A\x0b\
bK@e\xfd\xb8du\xc4\xc52nr(\xce\x97\
e\x1ee\xb2\xc8\xbb\x1e\xfd\xd6\xae<\xc4\x87\x93h\x8c\
T\x0e` \xde\xe9\xcen\xa2~\x95;\xc1\x9b\xbe/\
5'\x85\xf4m|y\xc0f}76.\xd4\xacZ\
7\xee\xf2\x228\xf1\x048\x04\x8eT\x85\xf8\xe2\xf6u\
S\x86\x1f7\x80?\xee\x81\x1e\xf2\xf0\x01-J\x0e=\
\xe3\xbd4\xbdb\x12\x9d>\x0b\x17#\xd7@\xf6A\xa3\
\x1b\xe5kU\xa2\x0fC\x8b\x00\xe1>\xdc\xdd(3\x02\
 \xe0d\x94R\x116\xeb\xe1\xfcLY\xca\xd7\x96\xfe\
\xe1\x83\x19\xf0-\xe6\xfc\x15\xdf\xa0\x7f=|\x80\xe0\xa1\
\xe9T\xd7M\x90\xa5\x10\xf4\x12\xb0\xa5\x09\x95?\xd3T\
fS\x04\xcafQ\x817G\xcd\xfa+\x88\xaf\xa5P\
\x91\xaa1\xd0\x9fQN\x16\xf2\x0a\x1c)\xe1]7x\
\xfd\xf1\xa4\xe5\xa46\x03A\xe1\xa3\xdf\xe1T7HK\
`?\x8f\xbb\x1a\xbc%\x0a\xb6W\x05\x83\x02l$/\
\x1b\x15\xe6\x5cJ^\x0c\xeb\xe0\xe3;\x1d\x0c\x85\xfdv\
4W\xd0\x7f\x12,\xb98\x80\xca\xaa\xde\xa81E?\
\x98\x05O\x99v\xcd3\xc0\x14\xd2\xb5\xe1w\xf4\xc8z\
\x22*\xa8\x10\x5c@Z\xff\xfa+zD\x1b-\xba_\
\xd1\x8aVt\x0e\xf5\xe0\x0c\x8d\xd1\x14\xb9\xf5\xb55s\
\x05\x85\xc0)\xe6\x9b\xb9#\xf4\x1b\xcal\xe3\x9c\xe4d\
\xa5\x8b\xcb\x14- d\x81\xbc\x91Z\x0a\xd5#\xb4\xd0\
f)\xe3PT`\xe9\x0c\xa6\xb5\xa9\x96\x13\x22\x9f\xa1\
\xe7\xb0:\x09\x84\xcc\xdb\xa0h\xa5\x8c\xa4\xc0\x0ct\x12\
\xe0\xf9\x11\x90\xa8\x82\xbeP\x83M@\x0a\xc5\x8f\x04\xa4\
-*\x9a:\xbcR\xd0\x02\x8b\xed\x8cl \x9er.\
\x9a\x94Ia\x83K@\x02T\xc2\xea+I\x8a&\xbf\
\xd4\xb36\x89tM+\xf9\x13\x94\xdeH\xd5_c1\
\x87#\x81\xa5\xdb\xa8\xfa\xfa\xc0\xb5\x9d\x8f^\x0a\x81\xb7\
\x11\xad\xf4\xaf\xf3\x16\x07\x99\xc7\x00\xd7/\xaf\xb1\xc4\x7f\
\x0f\x89\xff\x01\x9akh\x1fr\xdc\x80\x14\xa1Sb\xd0\
\x1e\x0dqR\x0beF\xc8\x09\xb2A/^\xbcP\xde\
\x87\xb7\xb3`_\x89\xc93e\x03W\xe7`\xd4T#\
ch\x83A\x5c'\xdb)\x96A\xf0\xe6*\x80\x89\xa7\
\x90\xb7\x18(\xe5\x11\xaaX\xba`\x18b\xd6\xa7\xf4V\
\x0d\xee\xbf\xdb\xe2\xd7\x84\xf4\x14i\x0f_\x1501\xf8\
\xce\xdc86m\xc6x\xe1l\xf3\xca!\x99\xcc8A\
\xcdo\x80\xe9\x18o=\xf7\xfbU\xa6u9^a\x9a\
+\x9dm5:A\x99~9Fq\x93\x0b\xeaI\x94\
\xda\x8e\x171\xdb\xf4t\x1c\xb0\xb4\xa7o\x0b\xcd(\x93\
^\xa07\xec+^\x8b\x04\x02}\xf4E$\xd3\xf8\x8b\
<\x81\xb3\xc7?I\x22uC7\xdd\xa7\x8am\xfb\x89\
\xdb.6\x89\x1b\xbe\x80\x03\x16\xad\xe2T\xf0\xf2\xc4\x15\
\x90\x92-G\xa1\x90\x8f\xf4\x17%\xe8\xe9xs\xfa|\
\x84\xe2\x18\xbd\x83\x22\xa6\xcex\xdf\x8f7\x93\xef\x03\xc7\
y\xb14E\xb3Hi~II\x9e\xfa\xbe+\x9b\xf2\
\xf7\x83[\xeb\xd4\xe2\xd6hp\xee\xc0\xa6\xceM\xd0\xa0\
\xc3UY:\xf5\xac\xde-\xaf\x87\xf39\xd55nW\
\x1d\xf0\xe8\xfd%\xb59\x8f]J+\x18\x04tUr\
\x8cH\x18\xf4\x0d/\x87\x82k\xc9?&\x00\xcb\xf7a\
\x09\x82\xd3w,\xf7\xc2\x13&\x0a\xe6\xe0\x94\x95\xb5\xbc\
!2\xe3\xe9[\x08\x99\xca\xe1\x85\x10G\xa3\x8f\xc5&\
\xcb\x1a\xe4v\xc9\x8b\x02\xa8\xaa\x89|\xb5\xbd\xe10\x8d\
;L\xb3\xacvkA\x8eb\x01(\x0eQ}\xfd\xf7\
\xf2Bk\x05-\xee\xbc+'\xa8\x81\x83T$m\x19\
\x0e\x10\xda\xa6\xf3\xd6\x95\xbb\x01\xf1P\xd0$\xa4R\xfe\
\x12P\x98\x9a\xc0!\x09\x00+\xd2\xdf?\x9d\xc3\x02i\
\xbb\x95\xb6F-*.^\xb7}\xeb\xbc\xf3\xed'M\
\x9ba\xed\x8b\xdfh?\x80\xfa\x98-\xf3\x0eI0A\
\x9eN\xc6}X3\xdb\xf5\xb6;\xafa`b\x06\xec\
E!Ni\xed\xc5\x96\xed\xd2c7\x07x>~\xb4\
'\x7fZ9)\xfc\xe3KmF`\xd2\x99\x14\xbc\xea\
\x80\xb7DD\xfd\x5c\xb2\xc1\xf3\xddw\x03\xb2`\xb1\xbf\
\xa9\xd6d\x11F\x7fS\x09\xefd\x0c\x9aP\xfb\xd4\x0c\
[\xfb\x92S=[5\xce)\xbd\xa3-\xb4\x8b\x06w\
\x0eg\xbd\x1c\xe6\x97w\x8b\x05\x8c\x9e]\x0a;\x90X\
\xaa`\x12QO\x168\x07'\xea\xa0|\xc9\x93\xba\xb2\
\xa5\xec\xb4K\x10\xc7az\x0dX\xa3\xcbe_\x82|\
E\xdeyn?\x5c\xf6H\xddb15\x11\x8e\xcaZ\
\x949\x19\x0d\xc4\xbb\xf6\x0d-\xcb\xbec\x92\x9c\x96\xdd\
P\xec\xc3?\x1c\x14\xb0\xea\xd9\xec\xd7\xdc\x8d\xe2g\xfd\
\xb5h\xd3m\x1f\x9ew\x7f;O3\xaa\x1c\x12\x1f\x16\
#\x0b\x92U=vV\xef\x0d\xef],\xcc\x92\xec>\
\xd7\xedU\xd6EJ\xc0X\xfb\xbb\x7ft\xf0\xce\x19\x90\
^5\xceMH\xf4\x8f\x1f{#\xac\x0dJ\xa1\xe3#\
\x08\xc9N\x04\xd9\x0a\xb2X\x10u\x9d}\xd1\x1c\x84.\
\xf4B\x18X\xde9\xa9'\xaa\x85\xed+\xcd%/\xeb\
R\xcd?w\xea\xc5g\xbf\xdd;Ud\xcdH\xf9\xac\
\x1bOA,\x05\xa1\x90u\xce\xe7\x94\x1d\xf9\x03}\xb7\
\xd0?iy\x98+\x09'\x11\x86\xdd\x1b,\x96\x94\xc1\
\xbb9,\x9b\xcfco(R\xb5Y]P\xa9\x01\x90\
\x82q\xb4\x80\x19/=\x94\x86Kw,\xf3\x19v!\
\xad]eF\x0a2`o\xbd>\x80o\xca\xd4\xce\x06\
?@a\x1b\xf8\xee\xd6\xee\xc7\x8b\xee\xd4\xe0A\xb5e\
}\xf9\x1d\xc6\x08\xcc\xc1\xd0I\xd6\x9f\x168%\x9f(\
\xeb\x02o\xebbN\xc4KF\xed]^@\xabC\x04\
\x06o\x18\x16@\x9dQ\x05\x03\x83_\xfa\x9ag!8\
\x0c\xd1\xe3\xe8\xaf}\x90\xe4\xbd\xda\xaf\xb5\xc6\xea\x96?\
\x92\xdb\x12Lya>\xde\xd5\xea\x14\xc0d\x1f;\xad\
\x85\x8d\xf2\xc9$(^\x9d\xdc\xf9\xfa\x1dqu\xff \
\xb7\xbb\xf7\xf4{wt^\xcfi\xb2oG\xa7\xcf\xf6\
\xed\xa8\xf3A6T\xde\xe3\xe9*\x13\x94}6\xbe\xe6\
\xb5\xfcv\xce\x1e\xb0\x802\xcc`\x0c\xfc\xbf8{\xd7\
\x9e\xfe'\xce\xee\x9cO\x9bk\x90\xe1\xc1B\x8a:\x18\
\xf1\x86\x86\xe6\xf62\xb3\x8b\xaa\xafu\xbc\xb3\x9a\x9d\xe8\
o\xd4r \xcc\xbb\xd0\xd9}\xab\x124\xfe\x06z\x03\
]\xf2uk\x87q\xe8\xc8Yd\x0e\x96W\xee\xe6\xd0\
\x1eP\xa6(\x80\x846\xd8m\xc2{\xcf\x1d\xeai\x0e\
\x0a\xc1\x90e\x1b\xb8\x1dX\x86\x0e\x01]\xfc\xfd\x83\x7f\
\xb8\xdd\xafj\xf2\xea\xf1\x1a\xfd\xf3C\xb6\xaf_\xe0\xdf\
\x7f\x00B\x89\x9b{\
\x00\x00\x12\xc8\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: http://\
www.qt.io/licens\
ing/\x0d\x0a**\x0d\x0a** Thi\
s file is part o\
f the Qt Quick C\
ontrols 2 module\
 of the Qt Toolk\
it.\x0d\x0a**\x0d\x0a** $QT_\
BEGIN_LICENSE:LG\
PL3$\x0d\x0a** Commerc\
ial License Usag\
e\x0d\x0a** Licensees \
holding valid co\
mmercial Qt lice\
nses may use thi\
s file in\x0d\x0a** ac\
cordance with th\
e commercial lic\
ense agreement p\
rovided with the\
\x0d\x0a** Software or\
, alternatively,\
 in accordance w\
ith the terms co\
ntained in\x0d\x0a** a\
 written agreeme\
nt between you a\
nd The Qt Compan\
y. For licensing\
 terms\x0d\x0a** and c\
onditions see ht\
tp://www.qt.io/t\
erms-conditions.\
 For further\x0d\x0a**\
 information use\
 the contact for\
m at http://www.\
qt.io/contact-us\
.\x0d\x0a**\x0d\x0a** GNU Le\
sser General Pub\
lic License Usag\
e\x0d\x0a** Alternativ\
ely, this file m\
ay be used under\
 the terms of th\
e GNU Lesser\x0d\x0a**\
 General Public \
License version \
3 as published b\
y the Free Softw\
are\x0d\x0a** Foundati\
on and appearing\
 in the file LIC\
ENSE.LGPLv3 incl\
uded in the\x0d\x0a** \
packaging of thi\
s file. Please r\
eview the follow\
ing information \
to\x0d\x0a** ensure th\
e GNU Lesser Gen\
eral Public Lice\
nse version 3 re\
quirements\x0d\x0a** w\
ill be met: http\
s://www.gnu.org/\
licenses/lgpl.ht\
ml.\x0d\x0a**\x0d\x0a** GNU \
General Public L\
icense Usage\x0d\x0a**\
 Alternatively, \
this file may be\
 used under the \
terms of the GNU\
\x0d\x0a** General Pub\
lic License vers\
ion 2.0 or later\
 as published by\
 the Free\x0d\x0a** So\
ftware Foundatio\
n and appearing \
in the file LICE\
NSE.GPL included\
 in\x0d\x0a** the pack\
aging of this fi\
le. Please revie\
w the following \
information to\x0d\x0a\
** ensure the GN\
U General Public\
 License version\
 2.0 requirement\
s will be\x0d\x0a** me\
t: http://www.gn\
u.org/licenses/g\
pl-2.0.html.\x0d\x0a**\
\x0d\x0a** $QT_END_LIC\
ENSE$\x0d\x0a**\x0d\x0a*****\
****************\
****************\
****************\
****************\
*******/\x0d\x0a\x0d\x0aimpo\
rt QtQuick 2.12\x0d\
\x0aimport QtQuick.\
Controls 2.12\x0d\x0ai\
mport QtQuick.Co\
ntrols.Material \
2.12\x0d\x0aimport QtQ\
uick.Controls.Ma\
terial.impl 2.12\
\x0d\x0aimport QtQuick\
.Controls.impl 2\
.12\x0d\x0aimport QtQu\
ick.Templates 2.\
12 as T\x0d\x0a\x0d\x0aT.But\
ton {\x0d\x0a    id: c\
ontrol\x0d\x0a\x0d\x0a    im\
plicitWidth: Mat\
h.max(implicitBa\
ckgroundWidth + \
leftInset + righ\
tInset, implicit\
ContentWidth + l\
eftPadding + rig\
htPadding)\x0d\x0a    \
implicitHeight: \
Math.max(implici\
tBackgroundHeigh\
t + topInset + b\
ottomInset, impl\
icitContentHeigh\
t + topPadding +\
 bottomPadding)\x0d\
\x0a    topInset: 6\
\x0d\x0a    bottomInse\
t: 6\x0d\x0a    paddin\
g: 12\x0d\x0a    horiz\
ontalPadding: pa\
dding - 4\x0d\x0a    s\
pacing: 6\x0d\x0a    i\
con.width: 24\x0d\x0a \
   icon.height: \
24\x0d\x0a    icon.col\
or: !enabled ? M\
aterial.hintText\
Color : flat && \
highlighted ? Ma\
terial.accentCol\
or : highlighted\
 ? Material.prim\
aryHighlightedTe\
xtColor : Materi\
al.foreground\x0d\x0a \
   Material.elev\
ation: flat ? co\
ntrol.down || co\
ntrol.hovered ? \
2 : 0 : control.\
down ? 8 : 2\x0d\x0a  \
  Material.backg\
round: flat ? \x22t\
ransparent\x22 : un\
defined\x0d\x0a\x0d\x0a    f\
ont {\x0d\x0a        f\
amily: \x22Helvetic\
a\x22\x0d\x0a        pixe\
lSize: 50\x0d\x0a    }\
\x0d\x0a\x0d\x0a    contentI\
tem: IconLabel {\
\x0d\x0a        spacin\
g: control.spaci\
ng\x0d\x0a        mirr\
ored: control.mi\
rrored\x0d\x0a        \
display: control\
.display\x0d\x0a      \
  icon: control.\
icon\x0d\x0a        te\
xt: control.text\
\x0d\x0a        font: \
control.font\x0d\x0a  \
      color: !co\
ntrol.enabled ? \
control.Material\
.hintTextColor :\
 control.flat &&\
 control.highlig\
hted ? control.M\
aterial.accentCo\
lor : control.hi\
ghlighted ? cont\
rol.Material.pri\
maryHighlightedT\
extColor : contr\
ol.Material.fore\
ground\x0d\x0a    }\x0d\x0a\x0d\
\x0a    background:\
 Rectangle {\x0d\x0a  \
      implicitWi\
dth: 64\x0d\x0a       \
 implicitHeight:\
 control.Materia\
l.buttonHeight\x0d\x0a\
        radius: \
2\x0d\x0a        color\
: !control.enabl\
ed ? control.Mat\
erial.buttonDisa\
bledColor : cont\
rol.highlighted \
? control.Materi\
al.highlightedBu\
ttonColor : cont\
rol.Material.but\
tonColor\x0d\x0a      \
  // The layer i\
s disabled when \
the button color\
 is transparent \
so you can do\x0d\x0a \
       // Materi\
al.background: \x22\
transparent\x22 and\
 get a proper fl\
at button withou\
t needing\x0d\x0a     \
   // to set Mat\
erial.elevation \
as well\x0d\x0a       \
 layer.enabled: \
control.enabled \
&& control.Mater\
ial.buttonColor.\
a > 0\x0d\x0a\x0d\x0a       \
 PaddedRectangle\
 {\x0d\x0a            \
y: parent.height\
 - 4\x0d\x0a          \
  width: parent.\
width\x0d\x0a         \
   height: 4\x0d\x0a  \
          radius\
: 2\x0d\x0a           \
 topPadding: -2\x0d\
\x0a            cli\
p: true\x0d\x0a       \
     visible: co\
ntrol.checkable \
&& (!control.hig\
hlighted || cont\
rol.flat)\x0d\x0a     \
       color: co\
ntrol.checked &&\
 control.enabled\
 ? control.Mater\
ial.accentColor \
: control.Materi\
al.secondaryText\
Color\x0d\x0a        }\
\x0d\x0a\x0d\x0a        Ripp\
le {\x0d\x0a          \
  clipRadius: 2\x0d\
\x0a            wid\
th: parent.width\
\x0d\x0a            he\
ight: parent.hei\
ght\x0d\x0a           \
 pressed: contro\
l.pressed\x0d\x0a     \
       anchor: c\
ontrol\x0d\x0a        \
    active: cont\
rol.down || cont\
rol.visualFocus \
|| control.hover\
ed\x0d\x0a            \
color: control.f\
lat && control.h\
ighlighted ? con\
trol.Material.hi\
ghlightedRippleC\
olor : control.M\
aterial.rippleCo\
lor\x0d\x0a        }\x0d\x0a\
\x0d\x0a        layer.\
effect: Elevatio\
nEffect {\x0d\x0a     \
       elevation\
: control.Materi\
al.elevation\x0d\x0a  \
      }\x0d\x0a\x0d\x0a    }\
\x0d\x0a\x0d\x0a}\x0d\x0a\
\x00\x00\x0d\xfc\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: http://\
www.qt.io/licens\
ing/\x0d\x0a**\x0d\x0a** Thi\
s file is part o\
f the Qt Quick C\
ontrols 2 module\
 of the Qt Toolk\
it.\x0d\x0a**\x0d\x0a** $QT_\
BEGIN_LICENSE:LG\
PL3$\x0d\x0a** Commerc\
ial License Usag\
e\x0d\x0a** Licensees \
holding valid co\
mmercial Qt lice\
nses may use thi\
s file in\x0d\x0a** ac\
cordance with th\
e commercial lic\
ense agreement p\
rovided with the\
\x0d\x0a** Software or\
, alternatively,\
 in accordance w\
ith the terms co\
ntained in\x0d\x0a** a\
 written agreeme\
nt between you a\
nd The Qt Compan\
y. For licensing\
 terms\x0d\x0a** and c\
onditions see ht\
tp://www.qt.io/t\
erms-conditions.\
 For further\x0d\x0a**\
 information use\
 the contact for\
m at http://www.\
qt.io/contact-us\
.\x0d\x0a**\x0d\x0a** GNU Le\
sser General Pub\
lic License Usag\
e\x0d\x0a** Alternativ\
ely, this file m\
ay be used under\
 the terms of th\
e GNU Lesser\x0d\x0a**\
 General Public \
License version \
3 as published b\
y the Free Softw\
are\x0d\x0a** Foundati\
on and appearing\
 in the file LIC\
ENSE.LGPLv3 incl\
uded in the\x0d\x0a** \
packaging of thi\
s file. Please r\
eview the follow\
ing information \
to\x0d\x0a** ensure th\
e GNU Lesser Gen\
eral Public Lice\
nse version 3 re\
quirements\x0d\x0a** w\
ill be met: http\
s://www.gnu.org/\
licenses/lgpl.ht\
ml.\x0d\x0a**\x0d\x0a** GNU \
General Public L\
icense Usage\x0d\x0a**\
 Alternatively, \
this file may be\
 used under the \
terms of the GNU\
\x0d\x0a** General Pub\
lic License vers\
ion 2.0 or later\
 as published by\
 the Free\x0d\x0a** So\
ftware Foundatio\
n and appearing \
in the file LICE\
NSE.GPL included\
 in\x0d\x0a** the pack\
aging of this fi\
le. Please revie\
w the following \
information to\x0d\x0a\
** ensure the GN\
U General Public\
 License version\
 2.0 requirement\
s will be\x0d\x0a** me\
t: http://www.gn\
u.org/licenses/g\
pl-2.0.html.\x0d\x0a**\
\x0d\x0a** $QT_END_LIC\
ENSE$\x0d\x0a**\x0d\x0a*****\
****************\
****************\
****************\
****************\
*******/\x0d\x0a\x0d\x0aimpo\
rt QtQuick 2.12\x0d\
\x0aimport QtQuick.\
Controls 2.12\x0d\x0ai\
mport QtQuick.Co\
ntrols.impl 2.12\
\x0d\x0aimport QtQuick\
.Templates 2.12 \
as T\x0d\x0a\x0d\x0aT.RoundB\
utton {\x0d\x0a    id:\
 control\x0d\x0a\x0d\x0a    \
implicitWidth: M\
ath.max(implicit\
BackgroundWidth \
+ leftInset + ri\
ghtInset, implic\
itContentWidth +\
 leftPadding + r\
ightPadding)\x0d\x0a  \
  implicitHeight\
: Math.max(impli\
citBackgroundHei\
ght + topInset +\
 bottomInset, im\
plicitContentHei\
ght + topPadding\
 + bottomPadding\
)\x0d\x0a    padding: \
6\x0d\x0a    spacing: \
6\x0d\x0a    icon.widt\
h: 24\x0d\x0a    icon.\
height: 24\x0d\x0a    \
icon.color: cont\
rol.checked || c\
ontrol.highlight\
ed ? control.pal\
ette.brightText \
: control.flat &\
& !control.down \
? (control.visua\
lFocus ? control\
.palette.highlig\
ht : control.pal\
ette.windowText)\
 : control.palet\
te.buttonText\x0d\x0a\x0d\
\x0a    font {\x0d\x0a   \
     family: \x22He\
lvetica\x22\x0d\x0a      \
  pixelSize: 20\x0d\
\x0a    }\x0d\x0a\x0d\x0a    co\
ntentItem: IconL\
abel {\x0d\x0a        \
spacing: control\
.spacing\x0d\x0a      \
  mirrored: cont\
rol.mirrored\x0d\x0a  \
      display: c\
ontrol.display\x0d\x0a\
        icon: co\
ntrol.icon\x0d\x0a    \
    text: contro\
l.text\x0d\x0a        \
font: control.fo\
nt\x0d\x0a        colo\
r: control.check\
ed || control.hi\
ghlighted ? cont\
rol.palette.brig\
htText : control\
.flat && !contro\
l.down ? (contro\
l.visualFocus ? \
control.palette.\
highlight : cont\
rol.palette.wind\
owText) : contro\
l.palette.button\
Text\x0d\x0a    }\x0d\x0a\x0d\x0a \
   background: R\
ectangle {\x0d\x0a    \
    implicitWidt\
h: control.icon.\
width + 2\x0d\x0a     \
   implicitHeigh\
t: control.icon.\
height + 2\x0d\x0a    \
    radius: cont\
rol.radius\x0d\x0a    \
    opacity: ena\
bled ? 1 : 0.3\x0d\x0a\
        visible:\
 !control.flat |\
| control.down |\
| control.checke\
d || control.hig\
hlighted\x0d\x0a      \
  color: Color.b\
lend(control.che\
cked || control.\
highlighted ? co\
ntrol.palette.da\
rk : control.pal\
ette.button, con\
trol.palette.mid\
, control.down ?\
 0.5 : 0)\x0d\x0a     \
   border.color:\
 control.palette\
.highlight\x0d\x0a    \
    border.width\
: control.visual\
Focus ? 2 : 0\x0d\x0a \
   }\x0d\x0a\x0d\x0a}\x0d\x0a\
\x00\x00\x08#\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2017 The Qt C\
ompany Ltd.\x0d\x0a** \
Contact: http://\
www.qt.io/licens\
ing/\x0d\x0a**\x0d\x0a** Thi\
s file is part o\
f the Qt Quick C\
ontrols 2 module\
 of the Qt Toolk\
it.\x0d\x0a**\x0d\x0a** $QT_\
BEGIN_LICENSE:LG\
PL3$\x0d\x0a** Commerc\
ial License Usag\
e\x0d\x0a** Licensees \
holding valid co\
mmercial Qt lice\
nses may use thi\
s file in\x0d\x0a** ac\
cordance with th\
e commercial lic\
ense agreement p\
rovided with the\
\x0d\x0a** Software or\
, alternatively,\
 in accordance w\
ith the terms co\
ntained in\x0d\x0a** a\
 written agreeme\
nt between you a\
nd The Qt Compan\
y. For licensing\
 terms\x0d\x0a** and c\
onditions see ht\
tp://www.qt.io/t\
erms-conditions.\
 For further\x0d\x0a**\
 information use\
 the contact for\
m at http://www.\
qt.io/contact-us\
.\x0d\x0a**\x0d\x0a** GNU Le\
sser General Pub\
lic License Usag\
e\x0d\x0a** Alternativ\
ely, this file m\
ay be used under\
 the terms of th\
e GNU Lesser\x0d\x0a**\
 General Public \
License version \
3 as published b\
y the Free Softw\
are\x0d\x0a** Foundati\
on and appearing\
 in the file LIC\
ENSE.LGPLv3 incl\
uded in the\x0d\x0a** \
packaging of thi\
s file. Please r\
eview the follow\
ing information \
to\x0d\x0a** ensure th\
e GNU Lesser Gen\
eral Public Lice\
nse version 3 re\
quirements\x0d\x0a** w\
ill be met: http\
s://www.gnu.org/\
licenses/lgpl.ht\
ml.\x0d\x0a**\x0d\x0a** GNU \
General Public L\
icense Usage\x0d\x0a**\
 Alternatively, \
this file may be\
 used under the \
terms of the GNU\
\x0d\x0a** General Pub\
lic License vers\
ion 2.0 or later\
 as published by\
 the Free\x0d\x0a** So\
ftware Foundatio\
n and appearing \
in the file LICE\
NSE.GPL included\
 in\x0d\x0a** the pack\
aging of this fi\
le. Please revie\
w the following \
information to\x0d\x0a\
** ensure the GN\
U General Public\
 License version\
 2.0 requirement\
s will be\x0d\x0a** me\
t: http://www.gn\
u.org/licenses/g\
pl-2.0.html.\x0d\x0a**\
\x0d\x0a** $QT_END_LIC\
ENSE$\x0d\x0a**\x0d\x0a*****\
****************\
****************\
****************\
****************\
*******/\x0d\x0a\x0d\x0aimpo\
rt QtQuick 2.12\x0d\
\x0aimport QtQuick.\
Controls.Materia\
l 2.12\x0d\x0aimport Q\
tQuick.Templates\
 2.12 as T\x0d\x0a\x0d\x0aT.\
Label {\x0d\x0a    id:\
 control\x0d\x0a\x0d\x0a    \
color: enabled ?\
 Material.foregr\
ound : Material.\
hintTextColor\x0d\x0a \
   linkColor: Ma\
terial.accentCol\
or\x0d\x0a\x0d\x0a    font {\
\x0d\x0a        family\
: \x22Helvetica\x22\x0d\x0a \
       pixelSize\
: 20\x0d\x0a    }\x0d\x0a\x0d\x0a}\
\x0d\x0a\
"

qt_resource_name = b"\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x06\
\x07\xac\x02\xc3\
\x00s\
\x00t\x00y\x00l\x00e\x00s\
\x00\x07\
\x04\xea\xc0\x85\
\x00M\
\x00y\x00S\x00t\x00y\x00l\x00e\
\x00\x0d\
\x0f\xccp<\
\x00T\
\x00a\x00b\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\x00\x0a\
\x08\x8e\x1a\xfc\
\x00T\
\x00a\x00b\x00B\x00a\x00r\x00.\x00q\x00m\x00l\
\x00\x06\
\x07\x84+\x02\
\x00q\
\x00m\x00l\x00d\x00i\x00r\
\x00\x0c\
\x00'&\x5c\
\x00C\
\x00o\x00m\x00b\x00o\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x0a\
\x0bhq\x5c\
\x00B\
\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\x00\x0f\
\x03\xf1\x0c\xfc\
\x00R\
\x00o\x00u\x00n\x00d\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\x00\x09\
\x08\xbf\xf4\xdc\
\x00L\
\x00a\x00b\x00e\x00l\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x000\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x81\xb1t\xcc\xa3\
\x00\x00\x00B\x00\x02\x00\x00\x00\x07\x00\x00\x00\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xa2\x00\x01\x00\x00\x00\x01\x00\x00\x16\xec\
\x00\x00\x01\x81\xb1p\xf4\x04\
\x00\x00\x00\xda\x00\x00\x00\x00\x00\x01\x00\x0023\
\x00\x00\x01\x81\xb1e\xe0\x84\
\x00\x00\x00\x90\x00\x00\x00\x00\x00\x01\x00\x00\x16:\
\x00\x00\x01\x81\xb1\x8c\xbbU\
\x00\x00\x00v\x00\x00\x00\x00\x00\x01\x00\x00\x0f\x89\
\x00\x00\x01\x81\xb1f\xd4g\
\x00\x00\x00\xfe\x00\x00\x00\x00\x00\x01\x00\x00@3\
\x00\x00\x01\x81\xb1eD\xda\
\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x01\x00\x00\x1fg\
\x00\x00\x01\x81\xb1\x8f\xc2\x0d\
\x00\x00\x00V\x00\x00\x00\x00\x00\x01\x00\x00\x00\xd3\
\x00\x00\x01\x81\xb1i\xcb,\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
