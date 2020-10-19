
# From Baidu ba-dls-deepspeech - https://github.com/baidu-research/ba-dls-deepspeech
# Character map list


char_map_str = """
<SPACE> 0
a 1
b 2
c 3
d 4
e 5
f 6
g 7
h 8
i 9
j 10
k 11
l 12
m 13
n 14
o 15
p 16
q 17
r 18
s 19
t 20
u 21
v 22
w 23
x 24
y 25
z 26
' 27
A 28
B 29
C 30
D 31
E 32
F 33
G 34
H 35
I 36
J 37
K 38
L 39
M 40
N 41
O 42
P 43
Q 44
R 45
S 46
T 47
U 48
V 49
W 50
X 51
Y 52
Z 53
| 54
{ 55
& 66
~ 67
! 68
( 69
^ 70
% 71
# 72
@ 73
/ 74
* 75
< 76
: 77
. 78
, 79
0 80
1 81
2 82
3 83
4 84
5 85
6 86
7 87
8 88
9 89
? 90
$ 91
- 92
"""

char_map = {}
index_map = {}

for line in char_map_str.strip().split('\n'):
    ch, index = line.split()
    char_map[ch] = int(index)
    index_map[int(index)] = ch

index_map[0] = ' '

