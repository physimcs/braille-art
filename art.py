input_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⢶⢒⣚⣛⡛⠓⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣛⣲⠶⠤⣤⡤⠖⠋⠉⣀⡤⠖⠋⠉⠉⠉⠉⠙⠶⡀⠙⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⢽⡆⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣹⣿⣿⣿⣟⡾⠁⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠂⠙⠦⠼⠛⠋⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⢿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡟⠀⠀⢠⣄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣀⣀⣀⠀⠀⠀⣀⣀⣠⠶⠛⠁⠀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⣰⠿⠀⠀⣰⣾⠇⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⣼⢁⣤⣦⡀⠀⠀
⠀⠀⣰⠃⠀⠀⠐⠿⢿⣄⣀⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠶⠒⠒⠒⠲⠤⣄⣸⡿⠋⢛⣿⣷⠀⠀
⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠈⠙⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠴⠚⠉⠁⠀⠀
⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀
⣇⠀⠀⠀⠀⠀⠋⠉⠉⠉⠓⠦⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀
⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀
⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠋⠉
⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠧⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣋⣀⣀⡤
⠀⠀⠀⠀⠀⠀⠙⠒⠦⣄⣀⡀⠀⠀⠀⠀⢠⣿⡛⠒⠲⠦⠤⠤⠤⠤⠤⠶⠒⠒⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

import csv

# Initializing our glyph dot dictionary
braille_values = {}
dot_braille_values = {}

# Reading our glyph_storage file and storing it as a dictionary
"""with open('glyph_storage.csv', newline='', encoding='utf-8') as csvfile:
   reader = csv.reader(csvfile)

   # For each column,
   for column in reader:
      # Unpack values from the two columns
      numbers, glyph = column
      # Store glyph as key and dots as value
      braille_values[glyph] = numbers
      # Opposite for dot_braille_values
      dot_braille_values[numbers] = glyph
"""

def unglyph(glyph_string):
    number_list = []

    for glyph in glyph_string:
         # In case of it being a new line
         if glyph == '\n':
            number_list.append('\n')
         # Otherwise just match and append
         else:
            numbers = braille_values.get(glyph, 'undefined')
            if numbers == 'undefined':
               print(f"Glyph '{glyph}' caused an undefined value.")
            number_list.append(numbers)
         
    return number_list

def print_braille(number_list):
   printable = ""

   for number in number_list:
      if number == '\n':
         printable += '\n'
      else:
         glyph = dot_braille_values.get(number, '')
         printable += str(glyph)

   return printable

stupid_braille = """
2800
⠀
Braille Pattern Blank
2801
⠁
Braille Pattern Dots-1
2802
⠂
Braille Pattern Dots-2
2803
⠃
Braille Pattern Dots-12
2804
⠄
Braille Pattern Dots-3
2805
⠅
Braille Pattern Dots-13
2806
⠆
Braille Pattern Dots-23
2807
⠇
Braille Pattern Dots-123
2808
⠈
Braille Pattern Dots-4
2809
⠉
Braille Pattern Dots-14
280A
⠊
Braille Pattern Dots-24
280B
⠋
Braille Pattern Dots-124
280C
⠌
Braille Pattern Dots-34
280D
⠍
Braille Pattern Dots-134
280E
⠎
Braille Pattern Dots-234
280F
⠏
Braille Pattern Dots-1234
2810
⠐
Braille Pattern Dots-5
2811
⠑
Braille Pattern Dots-15
2812
⠒
Braille Pattern Dots-25
2813
⠓
Braille Pattern Dots-125
2814
⠔
Braille Pattern Dots-35
2815
⠕
Braille Pattern Dots-135
2816
⠖
Braille Pattern Dots-235
2817
⠗
Braille Pattern Dots-1235
2818
⠘
Braille Pattern Dots-45
2819
⠙
Braille Pattern Dots-145
281A
⠚
Braille Pattern Dots-245
281B
⠛
Braille Pattern Dots-1245
281C
⠜
Braille Pattern Dots-345
281D
⠝
Braille Pattern Dots-1345
281E
⠞
Braille Pattern Dots-2345
281F
⠟
Braille Pattern Dots-12345
2820
⠠
Braille Pattern Dots-6
2821
⠡
Braille Pattern Dots-16
2822
⠢
Braille Pattern Dots-26
2823
⠣
Braille Pattern Dots-126
2824
⠤
Braille Pattern Dots-36
2825
⠥
Braille Pattern Dots-136
2826
⠦
Braille Pattern Dots-236
2827
⠧
Braille Pattern Dots-1236
2828
⠨
Braille Pattern Dots-46
2829
⠩
Braille Pattern Dots-146
282A
⠪
Braille Pattern Dots-246
282B
⠫
Braille Pattern Dots-1246
282C
⠬
Braille Pattern Dots-346
282D
⠭
Braille Pattern Dots-1346
282E
⠮
Braille Pattern Dots-2346
282F
⠯
Braille Pattern Dots-12346
2830
⠰
Braille Pattern Dots-56
2831
⠱
Braille Pattern Dots-156
2832
⠲
Braille Pattern Dots-256
2833
⠳
Braille Pattern Dots-1256
2834
⠴
Braille Pattern Dots-356
2835
⠵
Braille Pattern Dots-1356
2836
⠶
Braille Pattern Dots-2356
2837
⠷
Braille Pattern Dots-12356
2838
⠸
Braille Pattern Dots-456
2839
⠹
Braille Pattern Dots-1456
283A
⠺
Braille Pattern Dots-2456
283B
⠻
Braille Pattern Dots-12456
283C
⠼
Braille Pattern Dots-3456
283D
⠽
Braille Pattern Dots-13456
283E
⠾
Braille Pattern Dots-23456
283F
⠿
Braille Pattern Dots-123456
2840
⡀
Braille Pattern Dots-7
2841
⡁
Braille Pattern Dots-17
2842
⡂
Braille Pattern Dots-27
2843
⡃
Braille Pattern Dots-127
2844
⡄
Braille Pattern Dots-37
2845
⡅
Braille Pattern Dots-137
2846
⡆
Braille Pattern Dots-237
2847
⡇
Braille Pattern Dots-1237
2848
⡈
Braille Pattern Dots-47
2849
⡉
Braille Pattern Dots-147
284A
⡊
Braille Pattern Dots-247
284B
⡋
Braille Pattern Dots-1247
284C
⡌
Braille Pattern Dots-347
284D
⡍
Braille Pattern Dots-1347
284E
⡎
Braille Pattern Dots-2347
284F
⡏
Braille Pattern Dots-12347
2850
⡐
Braille Pattern Dots-57
2851
⡑
Braille Pattern Dots-157
2852
⡒
Braille Pattern Dots-257
2853
⡓
Braille Pattern Dots-1257
2854
⡔
Braille Pattern Dots-357
2855
⡕
Braille Pattern Dots-1357
2856
⡖
Braille Pattern Dots-2357
2857
⡗
Braille Pattern Dots-12357
2858
⡘
Braille Pattern Dots-457
2859
⡙
Braille Pattern Dots-1457
285A
⡚
Braille Pattern Dots-2457
285B
⡛
Braille Pattern Dots-12457
285C
⡜
Braille Pattern Dots-3457
285D
⡝
Braille Pattern Dots-13457
285E
⡞
Braille Pattern Dots-23457
285F
⡟
Braille Pattern Dots-123457
2860
⡠
Braille Pattern Dots-67
2861
⡡
Braille Pattern Dots-167
2862
⡢
Braille Pattern Dots-267
2863
⡣
Braille Pattern Dots-1267
2864
⡤
Braille Pattern Dots-367
2865
⡥
Braille Pattern Dots-1367
2866
⡦
Braille Pattern Dots-2367
2867
⡧
Braille Pattern Dots-12367
2868
⡨
Braille Pattern Dots-467
2869
⡩
Braille Pattern Dots-1467
286A
⡪
Braille Pattern Dots-2467
286B
⡫
Braille Pattern Dots-12467
286C
⡬
Braille Pattern Dots-3467
286D
⡭
Braille Pattern Dots-13467
286E
⡮
Braille Pattern Dots-23467
286F
⡯
Braille Pattern Dots-123467
2870
⡰
Braille Pattern Dots-567
2871
⡱
Braille Pattern Dots-1567
2872
⡲
Braille Pattern Dots-2567
2873
⡳
Braille Pattern Dots-12567
2874
⡴
Braille Pattern Dots-3567
2875
⡵
Braille Pattern Dots-13567
2876
⡶
Braille Pattern Dots-23567
2877
⡷
Braille Pattern Dots-123567
2878
⡸
Braille Pattern Dots-4567
2879
⡹
Braille Pattern Dots-14567
287A
⡺
Braille Pattern Dots-24567
287B
⡻
Braille Pattern Dots-124567
287C
⡼
Braille Pattern Dots-34567
287D
⡽
Braille Pattern Dots-134567
287E
⡾
Braille Pattern Dots-234567
287F
⡿
Braille Pattern Dots-1234567
2880
⢀
Braille Pattern Dots-8
2881
⢁
Braille Pattern Dots-18
2882
⢂
Braille Pattern Dots-28
2883
⢃
Braille Pattern Dots-128
2884
⢄
Braille Pattern Dots-38
2885
⢅
Braille Pattern Dots-138
2886
⢆
Braille Pattern Dots-238
2887
⢇
Braille Pattern Dots-1238
2888
⢈
Braille Pattern Dots-48
2889
⢉
Braille Pattern Dots-148
288A
⢊
Braille Pattern Dots-248
288B
⢋
Braille Pattern Dots-1248
288C
⢌
Braille Pattern Dots-348
288D
⢍
Braille Pattern Dots-1348
288E
⢎
Braille Pattern Dots-2348
288F
⢏
Braille Pattern Dots-12348
2890
⢐
Braille Pattern Dots-58
2891
⢑
Braille Pattern Dots-158
2892
⢒
Braille Pattern Dots-258
2893
⢓
Braille Pattern Dots-1258
2894
⢔
Braille Pattern Dots-358
2895
⢕
Braille Pattern Dots-1358
2896
⢖
Braille Pattern Dots-2358
2897
⢗
Braille Pattern Dots-12358
2898
⢘
Braille Pattern Dots-458
2899
⢙
Braille Pattern Dots-1458
289A
⢚
Braille Pattern Dots-2458
289B
⢛
Braille Pattern Dots-12458
289C
⢜
Braille Pattern Dots-3458
289D
⢝
Braille Pattern Dots-13458
289E
⢞
Braille Pattern Dots-23458
289F
⢟
Braille Pattern Dots-123458
28A0
⢠
Braille Pattern Dots-68
28A1
⢡
Braille Pattern Dots-168
28A2
⢢
Braille Pattern Dots-268
28A3
⢣
Braille Pattern Dots-1268
28A4
⢤
Braille Pattern Dots-368
28A5
⢥
Braille Pattern Dots-1368
28A6
⢦
Braille Pattern Dots-2368
28A7
⢧
Braille Pattern Dots-12368
28A8
⢨
Braille Pattern Dots-468
28A9
⢩
Braille Pattern Dots-1468
28AA
⢪
Braille Pattern Dots-2468
28AB
⢫
Braille Pattern Dots-12468
28AC
⢬
Braille Pattern Dots-3468
28AD
⢭
Braille Pattern Dots-13468
28AE
⢮
Braille Pattern Dots-23468
28AF
⢯
Braille Pattern Dots-123468
28B0
⢰
Braille Pattern Dots-568
28B1
⢱
Braille Pattern Dots-1568
28B2
⢲
Braille Pattern Dots-2568
28B3
⢳
Braille Pattern Dots-12568
28B4
⢴
Braille Pattern Dots-3568
28B5
⢵
Braille Pattern Dots-13568
28B6
⢶
Braille Pattern Dots-23568
28B7
⢷
Braille Pattern Dots-123568
28B8
⢸
Braille Pattern Dots-4568
28B9
⢹
Braille Pattern Dots-14568
28BA
⢺
Braille Pattern Dots-24568
28BB
⢻
Braille Pattern Dots-124568
28BC
⢼
Braille Pattern Dots-34568
28BD
⢽
Braille Pattern Dots-134568
28BE
⢾
Braille Pattern Dots-234568
28BF
⢿
Braille Pattern Dots-1234568
28C0
⣀
Braille Pattern Dots-78
28C1
⣁
Braille Pattern Dots-178
28C2
⣂
Braille Pattern Dots-278
28C3
⣃
Braille Pattern Dots-1278
28C4
⣄
Braille Pattern Dots-378
28C5
⣅
Braille Pattern Dots-1378
28C6
⣆
Braille Pattern Dots-2378
28C7
⣇
Braille Pattern Dots-12378
28C8
⣈
Braille Pattern Dots-478
28C9
⣉
Braille Pattern Dots-1478
28CA
⣊
Braille Pattern Dots-2478
28CB
⣋
Braille Pattern Dots-12478
28CC
⣌
Braille Pattern Dots-3478
28CD
⣍
Braille Pattern Dots-13478
28CE
⣎
Braille Pattern Dots-23478
28CF
⣏
Braille Pattern Dots-123478
28D0
⣐
Braille Pattern Dots-578
28D1
⣑
Braille Pattern Dots-1578
28D2
⣒
Braille Pattern Dots-2578
28D3
⣓
Braille Pattern Dots-12578
28D4
⣔
Braille Pattern Dots-3578
28D5
⣕
Braille Pattern Dots-13578
28D6
⣖
Braille Pattern Dots-23578
28D7
⣗
Braille Pattern Dots-123578
28D8
⣘
Braille Pattern Dots-4578
28D9
⣙
Braille Pattern Dots-14578
28DA
⣚
Braille Pattern Dots-24578
28DB
⣛
Braille Pattern Dots-124578
28DC
⣜
Braille Pattern Dots-34578
28DD
⣝
Braille Pattern Dots-134578
28DE
⣞
Braille Pattern Dots-234578
28DF
⣟
Braille Pattern Dots-1234578
28E0
⣠
Braille Pattern Dots-678
28E1
⣡
Braille Pattern Dots-1678
28E2
⣢
Braille Pattern Dots-2678
28E3
⣣
Braille Pattern Dots-12678
28E4
⣤
Braille Pattern Dots-3678
28E5
⣥
Braille Pattern Dots-13678
28E6
⣦
Braille Pattern Dots-23678
28E7
⣧
Braille Pattern Dots-123678
28E8
⣨
Braille Pattern Dots-4678
28E9
⣩
Braille Pattern Dots-14678
28EA
⣪
Braille Pattern Dots-24678
28EB
⣫
Braille Pattern Dots-124678
28EC
⣬
Braille Pattern Dots-34678
28ED
⣭
Braille Pattern Dots-134678
28EE
⣮
Braille Pattern Dots-234678
28EF
⣯
Braille Pattern Dots-1234678
28F0
⣰
Braille Pattern Dots-5678
28F1
⣱
Braille Pattern Dots-15678
28F2
⣲
Braille Pattern Dots-25678
28F3
⣳
Braille Pattern Dots-125678
28F4
⣴
Braille Pattern Dots-35678
28F5
⣵
Braille Pattern Dots-135678
28F6
⣶
Braille Pattern Dots-235678
28F7
⣷
Braille Pattern Dots-1235678
28F8
⣸
Braille Pattern Dots-45678
28F9
⣹
Braille Pattern Dots-145678
28FA
⣺
Braille Pattern Dots-245678
28FB
⣻
Braille Pattern Dots-1245678
28FC
⣼
Braille Pattern Dots-345678
28FD
⣽
Braille Pattern Dots-1345678
28FE
⣾
Braille Pattern Dots-2345678
28FF
⣿
Braille Pattern Dots-12345678
"""

import re

def remove_braille_instances(input_string):
   input_string = re.sub(r'^.*?\n', '', input_string)
   return re.sub(r'\b[Bb]raille\w*', '', input_string, flags=re.IGNORECASE)

result = remove_braille_instances(stupid_braille)
print(result)