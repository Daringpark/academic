
from Datamake import train_x_us, train_y_us
from Datamake import train_x_my, train_y_my
from Datamake import train_x_gw, train_y_gw
from Datamake import train_x_gn, train_y_gn

### time step 3  # us, my, gw
# us # t0 to t18
train_x_1 = train_x_us[0:3,...]
train_x_2 = train_x_us[1:4,...]
train_x_3 = train_x_us[2:5,...]
train_x_4 = train_x_us[3:6,...]
train_x_5 = train_x_us[4:7,...]
train_x_6 = train_x_us[5:8,...]
train_x_7 = train_x_us[6:9,...]
train_x_8 = train_x_us[7:10,...]
train_x_9 = train_x_us[8:11,...]
train_x_10 = train_x_us[9:12,...]
train_x_11 = train_x_us[10:13,...]
train_x_12 = train_x_us[11:14,...]
train_x_13 = train_x_us[12:15,...]
train_x_14 = train_x_us[13:16,...]
train_x_15 = train_x_us[14:17,...]
train_x_16 = train_x_us[15:18,...]
train_x_17 = train_x_us[16:19,...]

train_y_1 = train_y_us[0:3]
train_y_2 = train_y_us[1:4]
train_y_3 = train_y_us[2:5]
train_y_4 = train_y_us[3:6]
train_y_5 = train_y_us[4:7]
train_y_6 = train_y_us[5:8]
train_y_7 = train_y_us[6:9]
train_y_8 = train_y_us[7:10]
train_y_9 = train_y_us[8:11]
train_y_10 = train_y_us[9:12]
train_y_11 = train_y_us[10:13]
train_y_12 = train_y_us[11:14]
train_y_13 = train_y_us[12:15]
train_y_14 = train_y_us[13:16]
train_y_15 = train_y_us[14:17]
train_y_16 = train_y_us[15:18]
train_y_17 = train_y_us[16:19]

# my # t0 to t6
train_x_18 = train_x_my[0:3,...]
train_x_19 = train_x_my[1:4,...]
train_x_20 = train_x_my[2:5,...]
train_x_21 = train_x_my[3:6,...]
train_x_22 = train_x_my[4:7,...]

train_y_18 = train_y_my[0:3]
train_y_19 = train_y_my[1:4]
train_y_20 = train_y_my[2:5]
train_y_21 = train_y_my[3:6]
train_y_22 = train_y_my[4:7]

# gw # t0 to t3
train_x_23 = train_x_gw[0:3,...]
train_x_24 = train_x_gw[1:4,...]

train_y_23 = train_y_gw[0:3]
train_y_24 = train_y_gw[1:4]

### time step 4  # us, my, gw
# us # t0 to t18
train_x_25 = train_x_us[0:4,...]
train_x_26 = train_x_us[1:5,...]
train_x_27 = train_x_us[2:6,...]
train_x_28 = train_x_us[3:7,...]
train_x_29 = train_x_us[4:8,...]
train_x_30 = train_x_us[5:9,...]
train_x_31 = train_x_us[6:10,...]
train_x_32 = train_x_us[7:11,...]
train_x_33 = train_x_us[8:12,...]
train_x_34 = train_x_us[9:13,...]
train_x_35 = train_x_us[10:14,...]
train_x_36 = train_x_us[11:15,...]
train_x_37 = train_x_us[12:16,...]
train_x_38 = train_x_us[13:17,...]
train_x_39 = train_x_us[14:18,...]
train_x_40 = train_x_us[15:19,...]

train_y_25 = train_y_us[0:4]
train_y_26 = train_y_us[1:5]
train_y_27 = train_y_us[2:6]
train_y_28 = train_y_us[3:7]
train_y_29 = train_y_us[4:8]
train_y_30 = train_y_us[5:9]
train_y_31 = train_y_us[6:10]
train_y_32 = train_y_us[7:11]
train_y_33 = train_y_us[8:12]
train_y_34 = train_y_us[9:13]
train_y_35 = train_y_us[10:14]
train_y_36 = train_y_us[11:15]
train_y_37 = train_y_us[12:16]
train_y_38 = train_y_us[13:17]
train_y_39 = train_y_us[14:18]
train_y_40 = train_y_us[15:19]

# my # t0 to t6
#train_x_41 = train_x_my[0:4,...] # validetion data
train_x_42 = train_x_my[1:5,...]
train_x_43 = train_x_my[2:6,...]
train_x_44 = train_x_my[3:7,...]

#train_y_41 = train_y_my[0:4]  # validetion data
train_y_42 = train_y_my[1:5]
train_y_43 = train_y_my[2:6]
train_y_44 = train_y_my[3:7]

# gw # t0 to t3
train_x_45 = train_x_gw[0:4,...]

train_y_45 = train_y_gw[0:4]

### time step 5  # us, my
# us # t0 to t18
train_x_46 = train_x_us[0:5,...]
train_x_47 = train_x_us[1:6,...]
train_x_48 = train_x_us[2:7,...]
train_x_49 = train_x_us[3:8,...]
train_x_50 = train_x_us[4:9,...]
train_x_51 = train_x_us[5:10,...]
train_x_52 = train_x_us[6:11,...]
train_x_53 = train_x_us[7:12,...]
train_x_54 = train_x_us[8:13,...]
train_x_55 = train_x_us[9:14,...]
train_x_56 = train_x_us[10:15,...]
train_x_57 = train_x_us[11:16,...]
train_x_58 = train_x_us[12:17,...]
train_x_59 = train_x_us[13:18,...]
train_x_60 = train_x_us[14:19,...]

train_y_46 = train_y_us[0:5]
train_y_47 = train_y_us[1:6]
train_y_48 = train_y_us[2:7]
train_y_49 = train_y_us[3:8]
train_y_50 = train_y_us[4:9]
train_y_51 = train_y_us[5:10]
train_y_52 = train_y_us[6:11]
train_y_53 = train_y_us[7:12]
train_y_54 = train_y_us[8:13]
train_y_55 = train_y_us[9:14]
train_y_56 = train_y_us[10:15]
train_y_57 = train_y_us[11:16]
train_y_58 = train_y_us[12:17]
train_y_59 = train_y_us[13:18]
train_y_60 = train_y_us[14:19]

# my # t0 to t6
train_x_61 = train_x_my[0:5,...]
train_x_62 = train_x_my[1:6,...]
train_x_63 = train_x_my[2:7,...]

train_y_61 = train_y_my[0:5]
train_y_62 = train_y_my[1:6]
train_y_63 = train_y_my[2:7]

### time step 6  # us, my
# us # t0 to t18
train_x_64 = train_x_us[0:6,...]
train_x_65 = train_x_us[1:7,...]
train_x_66 = train_x_us[2:8,...]
train_x_67 = train_x_us[3:9,...]
train_x_68 = train_x_us[4:10,...]
train_x_69 = train_x_us[5:11,...]
train_x_70 = train_x_us[6:12,...]
train_x_71 = train_x_us[7:13,...]
train_x_72 = train_x_us[8:14,...]
train_x_73 = train_x_us[9:15,...]
train_x_74 = train_x_us[10:16,...]
train_x_75 = train_x_us[11:17,...]
train_x_76 = train_x_us[12:18,...]
train_x_77 = train_x_us[13:19,...]

train_y_64 = train_y_us[0:6]
train_y_65 = train_y_us[1:7]
train_y_66 = train_y_us[2:8]
train_y_67 = train_y_us[3:9]
train_y_68 = train_y_us[4:10]
train_y_69 = train_y_us[5:11]
train_y_70 = train_y_us[6:12]
train_y_71 = train_y_us[7:13]
train_y_72 = train_y_us[8:14]
train_y_73 = train_y_us[9:15]
train_y_74 = train_y_us[10:16]
train_y_75 = train_y_us[11:17]
train_y_76 = train_y_us[12:18]
train_y_77 = train_y_us[13:19]

# my # t0 to t6
train_x_78 = train_x_my[0:6,...]
train_x_79 = train_x_my[1:7,...]

train_y_78 = train_y_my[0:6]
train_y_79 = train_y_my[1:7]

### time step 7  # us, my
# us # t0 to t18
train_x_80 = train_x_us[0:7,...]
train_x_81 = train_x_us[1:8,...]
train_x_82 = train_x_us[2:9,...]
train_x_83 = train_x_us[3:10,...]
train_x_84 = train_x_us[4:11,...]
train_x_85 = train_x_us[5:12,...]
train_x_86 = train_x_us[6:13,...]
train_x_87 = train_x_us[7:14,...]
train_x_88 = train_x_us[8:15,...]
train_x_89 = train_x_us[9:16,...]
train_x_90 = train_x_us[10:17,...]
train_x_91 = train_x_us[11:18,...]
train_x_92 = train_x_us[12:19,...]

train_y_80 = train_y_us[0:7]
train_y_81 = train_y_us[1:8]
train_y_82 = train_y_us[2:9]
train_y_83 = train_y_us[3:10]
train_y_84 = train_y_us[4:11]
train_y_85 = train_y_us[5:12]
train_y_86 = train_y_us[6:13]
train_y_87 = train_y_us[7:14]
train_y_88 = train_y_us[8:15]
train_y_89 = train_y_us[9:16]
train_y_90 = train_y_us[10:17]
train_y_91 = train_y_us[11:18]
train_y_92 = train_y_us[12:19]

# my # t0 to t6
train_x_93 = train_x_my[0:7,...]

train_y_93 = train_y_my[0:7]

### time step 8~18  # us
# us # t0 to t18
train_x_94 = train_x_us[0:8,...]
train_x_95 = train_x_us[0:9,...]
train_x_96 = train_x_us[0:10,...]
train_x_97 = train_x_us[0:11,...]
train_x_98 = train_x_us[0:12,...]
train_x_99 = train_x_us[0:13,...]
train_x_100 = train_x_us[0:14,...]
train_x_101 = train_x_us[0:15,...]
train_x_102 = train_x_us[0:16,...]
train_x_103 = train_x_us[0:17,...]
train_x_104 = train_x_us[0:18,...]
train_x_105 = train_x_us[0:19,...]

train_y_94 = train_y_us[0:8]
train_y_95 = train_y_us[0:9]
train_y_96 = train_y_us[0:10]
train_y_97 = train_y_us[0:11]
train_y_98 = train_y_us[0:12]
train_y_99 = train_y_us[0:13]
train_y_100 = train_y_us[0:14]
train_y_101 = train_y_us[0:15]
train_y_102 = train_y_us[0:16]
train_y_103 = train_y_us[0:17]
train_y_104 = train_y_us[0:18]
train_y_105 = train_y_us[0:19]

### time step 1  # us, my, gw
# us # t0 to t18
train_x_106 = train_x_us[0:1,...]
train_x_107 = train_x_us[1:2,...]
train_x_108 = train_x_us[2:3,...]
train_x_109 = train_x_us[3:4,...]
train_x_110 = train_x_us[4:5,...]
train_x_111 = train_x_us[5:6,...]
train_x_112 = train_x_us[6:7,...]
train_x_113 = train_x_us[7:8,...]
train_x_114 = train_x_us[8:9,...]
train_x_115 = train_x_us[9:10,...]
train_x_116 = train_x_us[10:11,...]
train_x_117 = train_x_us[11:12,...]
train_x_118 = train_x_us[12:13,...]
train_x_119 = train_x_us[13:14,...]
train_x_120 = train_x_us[14:15,...]
train_x_121 = train_x_us[15:16,...]
train_x_122 = train_x_us[16:17,...]
train_x_123 = train_x_us[17:18,...]
train_x_124 = train_x_us[18:19,...]

train_y_106 = train_y_us[0:1,...]
train_y_107 = train_y_us[1:2,...]
train_y_108 = train_y_us[2:3,...]
train_y_109 = train_y_us[3:4,...]
train_y_110 = train_y_us[4:5,...]
train_y_111 = train_y_us[5:6,...]
train_y_112 = train_y_us[6:7,...]
train_y_113 = train_y_us[7:8,...]
train_y_114 = train_y_us[8:9,...]
train_y_115 = train_y_us[9:10,...]
train_y_116 = train_y_us[10:11,...]
train_y_117 = train_y_us[11:12,...]
train_y_118 = train_y_us[12:13,...]
train_y_119 = train_y_us[13:14,...]
train_y_120 = train_y_us[14:15,...]
train_y_121 = train_y_us[15:16,...]
train_y_122 = train_y_us[16:17,...]
train_y_123 = train_y_us[17:18,...]
train_y_124 = train_y_us[18:19,...]

# my # t0 to t6
train_x_125 = train_x_my[0:1,...]
train_x_126 = train_x_my[1:2,...]
train_x_127 = train_x_my[2:3,...]
train_x_128 = train_x_my[3:4,...]
train_x_129 = train_x_my[4:5,...]
train_x_130 = train_x_my[5:6,...]
train_x_131 = train_x_my[6:7,...]

train_y_125 = train_y_my[0:1,...]
train_y_126 = train_y_my[1:2,...]
train_y_127 = train_y_my[2:3,...]
train_y_128 = train_y_my[3:4,...]
train_y_129 = train_y_my[4:5,...]
train_y_130 = train_y_my[5:6,...]
train_y_131 = train_y_my[6:7,...]

# gw # t0 to t3
train_x_132 = train_x_gw[0:1,...]
train_x_133 = train_x_gw[1:2,...]
train_x_134 = train_x_gw[2:3,...]
train_x_135 = train_x_gw[3:4,...]

train_y_132 = train_y_gw[0:1,...]
train_y_133 = train_y_gw[1:2,...]
train_y_134 = train_y_gw[2:3,...]
train_y_135 = train_y_gw[3:4,...]

### time step 2  # us, my, gw
# us # t0 to t18
train_x_136 = train_x_us[0:2,...]
train_x_137 = train_x_us[1:3,...]
train_x_138 = train_x_us[2:4,...]
train_x_139 = train_x_us[3:5,...]
train_x_140 = train_x_us[4:6,...]
train_x_141 = train_x_us[5:7,...]
train_x_142 = train_x_us[6:8,...]
train_x_143 = train_x_us[7:9,...]
train_x_144 = train_x_us[8:10,...]
train_x_145 = train_x_us[9:11,...]
train_x_146 = train_x_us[10:12,...]
train_x_147 = train_x_us[11:13,...]
train_x_148 = train_x_us[12:14,...]
train_x_149 = train_x_us[13:15,...]
train_x_150 = train_x_us[14:16,...]
train_x_151 = train_x_us[15:17,...]
train_x_152 = train_x_us[16:18,...]
train_x_153 = train_x_us[17:19,...]

train_y_136 = train_y_us[0:2,...]
train_y_137 = train_y_us[1:3,...]
train_y_138 = train_y_us[2:4,...]
train_y_139 = train_y_us[3:5,...]
train_y_140 = train_y_us[4:6,...]
train_y_141 = train_y_us[5:7,...]
train_y_142 = train_y_us[6:8,...]
train_y_143 = train_y_us[7:9,...]
train_y_144 = train_y_us[8:10,...]
train_y_145 = train_y_us[9:11,...]
train_y_146 = train_y_us[10:12,...]
train_y_147 = train_y_us[11:13,...]
train_y_148 = train_y_us[12:14,...]
train_y_149 = train_y_us[13:15,...]
train_y_150 = train_y_us[14:16,...]
train_y_151 = train_y_us[15:17,...]
train_y_152 = train_y_us[16:18,...]
train_y_153 = train_y_us[17:19,...]

# my # t0 to t6
train_x_154 = train_x_my[0:2,...]
train_x_155 = train_x_my[1:3,...]
train_x_156 = train_x_my[2:4,...]
train_x_157 = train_x_my[3:5,...]
train_x_158 = train_x_my[4:6,...]

train_y_154 = train_y_my[0:2,...]
train_y_155 = train_y_my[1:3,...]
train_y_156 = train_y_my[2:4,...]
train_y_157 = train_y_my[3:5,...]
train_y_158 = train_y_my[4:6,...]

# gw # t0 to t3
train_x_159 = train_x_gw[0:2,...]
train_x_160 = train_x_gw[1:3,...]
train_x_161 = train_x_gw[2:4,...]

train_y_159 = train_y_gw[0:2,...]
train_y_160 = train_y_gw[1:3,...]
train_y_161 = train_y_gw[2:4,...]

# validation data set ==> gunwi data .. time step 4
val_x = train_x_my[0:4,...]
val_y = train_y_my[0:4,...]

print(val_x.shape, val_y.shape)

import numpy as np
# Test Data
# time step,, all # GN data
test_x = np.stack((t0_arrays_gn, t1_arrays_gn, t2_arrays_gn, t3_arrays_gn, t4_arrays_gn, t5_arrays_gn), axis=0)
test_y = np.stack((GN_t1_fire, GN_t2_fire, GN_t3_fire, GN_t4_fire, GN_t5_fire), axis=0)
