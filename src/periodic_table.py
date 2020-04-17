METAL = 'Metal'
NON_METAL = 'Non Metal'
METALLOID = 'Metalloid'

PERIODIC_TABLE = {
    '1': {'atomic_num': 1, 'symbol': 'H', 'name': 'Hydrogen', 'group': 1, 'period': 1, 'atomic_weight': 1.008,
          'density': 8.988e-05, 'melting_point': 14.01, 'boiling_point': 20.28, 'heat_capacity': 14.304,
          'electronegativity': 2.2, 'precise': True, 'type': NON_METAL},
    '2': {'atomic_num': 2, 'symbol': 'He', 'name': 'Helium', 'group': 18, 'period': 1, 'atomic_weight': 4.002602,
          'density': 0.0001785, 'melting_point': None, 'boiling_point': 4.22, 'heat_capacity': 5.193,
          'electronegativity': None, 'precise': True, 'type': NON_METAL},
    '3': {'atomic_num': 3, 'symbol': 'Li', 'name': 'Lithium', 'group': 1, 'period': 2, 'atomic_weight': 6.94,
          'density': 0.534, 'melting_point': 453.69, 'boiling_point': 1560, 'heat_capacity': 3.582,
          'electronegativity': 0.98, 'precise': True, 'type': METAL},
    '4': {'atomic_num': 4, 'symbol': 'Be', 'name': 'Beryllium', 'group': 2, 'period': 2, 'atomic_weight': 9.0121831,
          'density': 1.85, 'melting_point': 1560, 'boiling_point': 2742, 'heat_capacity': 1.825,
          'electronegativity': 1.57, 'precise': True, 'type': METAL},
    '5': {'atomic_num': 5, 'symbol': 'B', 'name': 'Boron', 'group': 13, 'period': 2, 'atomic_weight': 10.81,
          'density': 2.34, 'melting_point': 2349, 'boiling_point': 4200, 'heat_capacity': 1.026,
          'electronegativity': 2.04, 'precise': True, 'type': METALLOID},
    '6': {'atomic_num': 6, 'symbol': 'C', 'name': 'Carbon', 'group': 14, 'period': 2, 'atomic_weight': 12.011,
          'density': 2.267, 'melting_point': 3800, 'boiling_point': 4300, 'heat_capacity': 0.709,
          'electronegativity': 2.55, 'precise': True, 'type': NON_METAL},
    '7': {'atomic_num': 7, 'symbol': 'N', 'name': 'Nitrogen', 'group': 15, 'period': 2, 'atomic_weight': 14.007,
          'density': 0.0012506, 'melting_point': 63.15, 'boiling_point': 77.36, 'heat_capacity': 1.04,
          'electronegativity': 3.04, 'precise': True, 'type': NON_METAL},
    '8': {'atomic_num': 8, 'symbol': 'O', 'name': 'Oxygen', 'group': 16, 'period': 2, 'atomic_weight': 15.999,
          'density': 0.001429, 'melting_point': 54.36, 'boiling_point': 90.2, 'heat_capacity': 0.918,
          'electronegativity': 3.44, 'precise': True, 'type': NON_METAL},
    '9': {'atomic_num': 9, 'symbol': 'F', 'name': 'Fluorine', 'group': 17, 'period': 2, 'atomic_weight': 18.998403163,
          'density': 0.001696, 'melting_point': 53.53, 'boiling_point': 85.03, 'heat_capacity': 0.824,
          'electronegativity': 3.98, 'precise': True, 'type': NON_METAL},
    '10': {'atomic_num': 10, 'symbol': 'Ne', 'name': 'Neon', 'group': 18, 'period': 2, 'atomic_weight': 20.1797,
           'density': 0.0008999, 'melting_point': 24.56, 'boiling_point': 27.07, 'heat_capacity': 1.03,
           'electronegativity': None, 'precise': True, 'type': NON_METAL},
    '11': {'atomic_num': 11, 'symbol': 'Na', 'name': 'Sodium', 'group': 1, 'period': 3, 'atomic_weight': 22.98976928,
           'density': 0.971, 'melting_point': 370.87, 'boiling_point': 1156, 'heat_capacity': 1.228,
           'electronegativity': 0.93, 'precise': True, 'type': METAL},
    '12': {'atomic_num': 12, 'symbol': 'Mg', 'name': 'Magnesium', 'group': 2, 'period': 3, 'atomic_weight': 24.305,
           'density': 1.738, 'melting_point': 923, 'boiling_point': 1363, 'heat_capacity': 1.023,
           'electronegativity': 1.31, 'precise': True, 'type': METAL},
    '13': {'atomic_num': 13, 'symbol': 'Al', 'name': 'Aluminium', 'group': 13, 'period': 3, 'atomic_weight': 26.9815384,
           'density': 2.698, 'melting_point': 933.47, 'boiling_point': 2792, 'heat_capacity': 0.897,
           'electronegativity': 1.61, 'precise': True, 'type': METAL},
    '14': {'atomic_num': 14, 'symbol': 'Si', 'name': 'Silicon', 'group': 14, 'period': 3, 'atomic_weight': 28.085,
           'density': 2.3296, 'melting_point': 1687, 'boiling_point': 3538, 'heat_capacity': 0.705,
           'electronegativity': 1.9, 'precise': True, 'type': METALLOID},
    '15': {'atomic_num': 15, 'symbol': 'P', 'name': 'Phosphorus', 'group': 15, 'period': 3,
           'atomic_weight': 30.973761998, 'density': 1.82, 'melting_point': 317.3, 'boiling_point': 550,
           'heat_capacity': 0.769, 'electronegativity': 2.19, 'precise': True, 'type': NON_METAL},
    '16': {'atomic_num': 16, 'symbol': 'S', 'name': 'Sulfur', 'group': 16, 'period': 3, 'atomic_weight': 32.06,
           'density': 2.067, 'melting_point': 388.36, 'boiling_point': 717.87, 'heat_capacity': 0.71,
           'electronegativity': 2.58, 'precise': True, 'type': NON_METAL},
    '17': {'atomic_num': 17, 'symbol': 'Cl', 'name': 'Chlorine', 'group': 17, 'period': 3, 'atomic_weight': 35.45,
           'density': 0.003214, 'melting_point': 171.6, 'boiling_point': 239.11, 'heat_capacity': 0.479,
           'electronegativity': 3.16, 'precise': True, 'type': NON_METAL},
    '18': {'atomic_num': 18, 'symbol': 'Ar', 'name': 'Argon', 'group': 18, 'period': 3, 'atomic_weight': 39.948,
           'density': 0.0017837, 'melting_point': 83.8, 'boiling_point': 87.3, 'heat_capacity': 0.52,
           'electronegativity': None, 'precise': True, 'type': NON_METAL},
    '19': {'atomic_num': 19, 'symbol': 'K', 'name': 'Potassium', 'group': 1, 'period': 4, 'atomic_weight': 39.0983,
           'density': 0.862, 'melting_point': 336.53, 'boiling_point': 1032, 'heat_capacity': 0.757,
           'electronegativity': 0.82, 'precise': True, 'type': METAL},
    '20': {'atomic_num': 20, 'symbol': 'Ca', 'name': 'Calcium', 'group': 2, 'period': 4, 'atomic_weight': 40.078,
           'density': 1.54, 'melting_point': 1115, 'boiling_point': 1757, 'heat_capacity': 0.647,
           'electronegativity': 1, 'precise': True, 'type': METAL},
    '21': {'atomic_num': 21, 'symbol': 'Sc', 'name': 'Scandium', 'group': 3, 'period': 4, 'atomic_weight': 44.955908,
           'density': 2.989, 'melting_point': 1814, 'boiling_point': 3109, 'heat_capacity': 0.568,
           'electronegativity': 1.36, 'precise': True, 'type': METAL},
    '22': {'atomic_num': 22, 'symbol': 'Ti', 'name': 'Titanium', 'group': 4, 'period': 4, 'atomic_weight': 47.867,
           'density': 4.54, 'melting_point': 1941, 'boiling_point': 3560, 'heat_capacity': 0.523,
           'electronegativity': 1.54, 'precise': True, 'type': METAL},
    '23': {'atomic_num': 23, 'symbol': 'V', 'name': 'Vanadium', 'group': 5, 'period': 4, 'atomic_weight': 50.9415,
           'density': 6.11, 'melting_point': 2183, 'boiling_point': 3680, 'heat_capacity': 0.489,
           'electronegativity': 1.63, 'precise': True, 'type': METAL},
    '24': {'atomic_num': 24, 'symbol': 'Cr', 'name': 'Chromium', 'group': 6, 'period': 4, 'atomic_weight': 51.9961,
           'density': 7.15, 'melting_point': 2180, 'boiling_point': 2944, 'heat_capacity': 0.449,
           'electronegativity': 1.66, 'precise': True, 'type': METAL},
    '25': {'atomic_num': 25, 'symbol': 'Mn', 'name': 'Manganese', 'group': 7, 'period': 4, 'atomic_weight': 54.938043,
           'density': 7.44, 'melting_point': 1519, 'boiling_point': 2334, 'heat_capacity': 0.479,
           'electronegativity': 1.55, 'precise': True, 'type': METAL},
    '26': {'atomic_num': 26, 'symbol': 'Fe', 'name': 'Iron', 'group': 8, 'period': 4, 'atomic_weight': 55.845,
           'density': 7.874, 'melting_point': 1811, 'boiling_point': 3134, 'heat_capacity': 0.449,
           'electronegativity': 1.83, 'precise': True, 'type': METAL},
    '27': {'atomic_num': 27, 'symbol': 'Co', 'name': 'Cobalt', 'group': 9, 'period': 4, 'atomic_weight': 58.933194,
           'density': 8.86, 'melting_point': 1768, 'boiling_point': 3200, 'heat_capacity': 0.421,
           'electronegativity': 1.88, 'precise': True, 'type': METAL},
    '28': {'atomic_num': 28, 'symbol': 'Ni', 'name': 'Nickel', 'group': 10, 'period': 4, 'atomic_weight': 58.6934,
           'density': 8.912, 'melting_point': 1728, 'boiling_point': 3186, 'heat_capacity': 0.444,
           'electronegativity': 1.91, 'precise': True, 'type': METAL},
    '29': {'atomic_num': 29, 'symbol': 'Cu', 'name': 'Copper', 'group': 11, 'period': 4, 'atomic_weight': 63.546,
           'density': 8.96, 'melting_point': 1357.77, 'boiling_point': 2835, 'heat_capacity': 0.385,
           'electronegativity': 1.9, 'precise': True, 'type': METAL},
    '30': {'atomic_num': 30, 'symbol': 'Zn', 'name': 'Zinc', 'group': 12, 'period': 4, 'atomic_weight': 65.38,
           'density': 7.134, 'melting_point': 692.88, 'boiling_point': 1180, 'heat_capacity': 0.388,
           'electronegativity': 1.65, 'precise': True, 'type': METAL},
    '31': {'atomic_num': 31, 'symbol': 'Ga', 'name': 'Gallium', 'group': 13, 'period': 4, 'atomic_weight': 69.723,
           'density': 5.907, 'melting_point': 302.9146, 'boiling_point': 2673, 'heat_capacity': 0.371,
           'electronegativity': 1.81, 'precise': True, 'type': METAL},
    '32': {'atomic_num': 32, 'symbol': 'Ge', 'name': 'Germanium', 'group': 14, 'period': 4, 'atomic_weight': 72.63,
           'density': 5.323, 'melting_point': 1211.4, 'boiling_point': 3106, 'heat_capacity': 0.32,
           'electronegativity': 2.01, 'precise': True, 'type': METALLOID},
    '33': {'atomic_num': 33, 'symbol': 'As', 'name': 'Arsenic', 'group': 15, 'period': 4, 'atomic_weight': 74.921595,
           'density': 5.776, 'melting_point': 1090, 'boiling_point': 887, 'heat_capacity': 0.329,
           'electronegativity': 2.18, 'precise': True, 'type': METALLOID},
    '34': {'atomic_num': 34, 'symbol': 'Se', 'name': 'Selenium', 'group': 16, 'period': 4, 'atomic_weight': 78.971,
           'density': 4.809, 'melting_point': 453, 'boiling_point': 958, 'heat_capacity': 0.321,
           'electronegativity': 2.55, 'precise': True, 'type': NON_METAL},
    '35': {'atomic_num': 35, 'symbol': 'Br', 'name': 'Bromine', 'group': 17, 'period': 4, 'atomic_weight': 79.904,
           'density': 3.122, 'melting_point': 265.8, 'boiling_point': 332.0, 'heat_capacity': 0.474,
           'electronegativity': 2.96, 'precise': True, 'type': NON_METAL},
    '36': {'atomic_num': 36, 'symbol': 'Kr', 'name': 'Krypton', 'group': 18, 'period': 4, 'atomic_weight': 83.798,
           'density': 0.003733, 'melting_point': 115.79, 'boiling_point': 119.93, 'heat_capacity': 0.248,
           'electronegativity': 3, 'precise': True, 'type': NON_METAL},
    '37': {'atomic_num': 37, 'symbol': 'Rb', 'name': 'Rubidium', 'group': 1, 'period': 5, 'atomic_weight': 85.4678,
           'density': 1.532, 'melting_point': 312.46, 'boiling_point': 961, 'heat_capacity': 0.363,
           'electronegativity': 0.82, 'precise': True, 'type': METAL},
    '38': {'atomic_num': 38, 'symbol': 'Sr', 'name': 'Strontium', 'group': 2, 'period': 5, 'atomic_weight': 87.62,
           'density': 2.64, 'melting_point': 1050, 'boiling_point': 1655, 'heat_capacity': 0.301,
           'electronegativity': 0.95, 'precise': True, 'type': METAL},
    '39': {'atomic_num': 39, 'symbol': 'Y', 'name': 'Yttrium', 'group': 3, 'period': 5, 'atomic_weight': 88.90584,
           'density': 4.469, 'melting_point': 1799, 'boiling_point': 3609, 'heat_capacity': 0.298,
           'electronegativity': 1.22, 'precise': True, 'type': METAL},
    '40': {'atomic_num': 40, 'symbol': 'Zr', 'name': 'Zirconium', 'group': 4, 'period': 5, 'atomic_weight': 91.224,
           'density': 6.506, 'melting_point': 2128, 'boiling_point': 4682, 'heat_capacity': 0.278,
           'electronegativity': 1.33, 'precise': True, 'type': METAL},
    '41': {'atomic_num': 41, 'symbol': 'Nb', 'name': 'Niobium', 'group': 5, 'period': 5, 'atomic_weight': 92.90637,
           'density': 8.57, 'melting_point': 2750, 'boiling_point': 5017, 'heat_capacity': 0.265,
           'electronegativity': 1.6, 'precise': True, 'type': METAL},
    '42': {'atomic_num': 42, 'symbol': 'Mo', 'name': 'Molybdenum', 'group': 6, 'period': 5, 'atomic_weight': 95.95,
           'density': 10.22, 'melting_point': 2896, 'boiling_point': 4912, 'heat_capacity': 0.251,
           'electronegativity': 2.16, 'precise': True, 'type': METAL},
    '43': {'atomic_num': 43, 'symbol': 'Tc', 'name': 'Technetium', 'group': 7, 'period': 5, 'precise': False,
           'atomic_weight': 98, 'density': 11.5, 'melting_point': 2430, 'boiling_point': 4538, 'heat_capacity': None,
           'electronegativity': 1.9, 'type': METAL},
    '44': {'atomic_num': 44, 'symbol': 'Ru', 'name': 'Ruthenium', 'group': 8, 'period': 5, 'atomic_weight': 101.07,
           'density': 12.37, 'melting_point': 2607, 'boiling_point': 4423, 'heat_capacity': 0.238,
           'electronegativity': 2.2, 'precise': True, 'type': METAL},
    '45': {'atomic_num': 45, 'symbol': 'Rh', 'name': 'Rhodium', 'group': 9, 'period': 5, 'atomic_weight': 102.90549,
           'density': 12.41, 'melting_point': 2237, 'boiling_point': 3968, 'heat_capacity': 0.243,
           'electronegativity': 2.28, 'precise': True, 'type': METAL},
    '46': {'atomic_num': 46, 'symbol': 'Pd', 'name': 'Palladium', 'group': 10, 'period': 5, 'atomic_weight': 106.42,
           'density': 12.02, 'melting_point': 1828.05, 'boiling_point': 3236, 'heat_capacity': 0.244,
           'electronegativity': 2.2, 'precise': True, 'type': METAL},
    '47': {'atomic_num': 47, 'symbol': 'Ag', 'name': 'Silver', 'group': 11, 'period': 5, 'atomic_weight': 107.8682,
           'density': 10.501, 'melting_point': 1234.93, 'boiling_point': 2435, 'heat_capacity': 0.235,
           'electronegativity': 1.93, 'precise': True, 'type': METAL},
    '48': {'atomic_num': 48, 'symbol': 'Cd', 'name': 'Cadmium', 'group': 12, 'period': 5, 'atomic_weight': 112.414,
           'density': 8.69, 'melting_point': 594.22, 'boiling_point': 1040, 'heat_capacity': 0.232,
           'electronegativity': 1.69, 'precise': True, 'type': METAL},
    '49': {'atomic_num': 49, 'symbol': 'In', 'name': 'Indium', 'group': 13, 'period': 5, 'atomic_weight': 114.818,
           'density': 7.31, 'melting_point': 429.75, 'boiling_point': 2345, 'heat_capacity': 0.233,
           'electronegativity': 1.78, 'precise': True, 'type': METAL},
    '50': {'atomic_num': 50, 'symbol': 'Sn', 'name': 'Tin', 'group': 14, 'period': 5, 'atomic_weight': 118.71,
           'density': 7.287, 'melting_point': 505.08, 'boiling_point': 2875, 'heat_capacity': 0.228,
           'electronegativity': 1.96, 'precise': True, 'type': METAL},
    '51': {'atomic_num': 51, 'symbol': 'Sb', 'name': 'Antimony', 'group': 15, 'period': 5, 'atomic_weight': 121.76,
           'density': 6.685, 'melting_point': 903.78, 'boiling_point': 1860, 'heat_capacity': 0.207,
           'electronegativity': 2.05, 'precise': True, 'type': METALLOID},
    '52': {'atomic_num': 52, 'symbol': 'Te', 'name': 'Tellurium', 'group': 16, 'period': 5, 'atomic_weight': 127.6,
           'density': 6.232, 'melting_point': 722.66, 'boiling_point': 1261, 'heat_capacity': 0.202,
           'electronegativity': 2.1, 'precise': True, 'type': METALLOID},
    '53': {'atomic_num': 53, 'symbol': 'I', 'name': 'Iodine', 'group': 17, 'period': 5, 'atomic_weight': 126.90447,
           'density': 4.93, 'melting_point': 386.85, 'boiling_point': 457.4, 'heat_capacity': 0.214,
           'electronegativity': 2.66, 'precise': True, 'type': NON_METAL},
    '54': {'atomic_num': 54, 'symbol': 'Xe', 'name': 'Xenon', 'group': 18, 'period': 5, 'atomic_weight': 131.293,
           'density': 0.005887, 'melting_point': 161.4, 'boiling_point': 165.03, 'heat_capacity': 0.158,
           'electronegativity': 2.6, 'precise': True, 'type': NON_METAL},
    '55': {'atomic_num': 55, 'symbol': 'Cs', 'name': 'Caesium', 'group': 1, 'period': 6, 'atomic_weight': 132.90545196,
           'density': 1.873, 'melting_point': 301.59, 'boiling_point': 944, 'heat_capacity': 0.242,
           'electronegativity': 0.79, 'precise': True, 'type': METAL},
    '56': {'atomic_num': 56, 'symbol': 'Ba', 'name': 'Barium', 'group': 2, 'period': 6, 'atomic_weight': 137.327,
           'density': 3.594, 'melting_point': 1000, 'boiling_point': 2170, 'heat_capacity': 0.204,
           'electronegativity': 0.89, 'precise': True, 'type': METAL},
    '57': {'atomic_num': 57, 'symbol': 'La', 'name': 'Lanthanum', 'group': 3, 'period': 6, 'atomic_weight': 138.90547,
           'density': 6.145, 'melting_point': 1193, 'boiling_point': 3737, 'heat_capacity': 0.195,
           'electronegativity': 1.1, 'precise': True, 'type': METAL},
    '58': {'atomic_num': 58, 'symbol': 'Ce', 'name': 'Cerium', 'group': None, 'period': 6, 'atomic_weight': 140.116,
           'density': 6.77, 'melting_point': 1068, 'boiling_point': 3716, 'heat_capacity': 0.192,
           'electronegativity': 1.12, 'precise': True, 'type': NON_METAL},
    '59': {'atomic_num': 59, 'symbol': 'Pr', 'name': 'Praseodymium', 'group': None, 'period': 6,
           'atomic_weight': 140.90766, 'density': 6.773, 'melting_point': 1208, 'boiling_point': 3793,
           'heat_capacity': 0.193, 'electronegativity': 1.13, 'precise': True, 'type': NON_METAL},
    '60': {'atomic_num': 60, 'symbol': 'Nd', 'name': 'Neodymium', 'group': None, 'period': 6, 'atomic_weight': 144.242,
           'density': 7.007, 'melting_point': 1297, 'boiling_point': 3347, 'heat_capacity': 0.19,
           'electronegativity': 1.14, 'precise': True, 'type': NON_METAL},
    '61': {'atomic_num': 61, 'symbol': 'Pm', 'name': 'Promethium', 'group': None, 'period': 6, 'precise': False,
           'atomic_weight': 145, 'density': 7.26, 'melting_point': 1315, 'boiling_point': 3273, 'heat_capacity': None,
           'electronegativity': 1.13, 'type': NON_METAL},
    '62': {'atomic_num': 62, 'symbol': 'Sm', 'name': 'Samarium', 'group': None, 'period': 6, 'atomic_weight': 150.36,
           'density': 7.52, 'melting_point': 1345, 'boiling_point': 2067, 'heat_capacity': 0.197,
           'electronegativity': 1.17, 'precise': True, 'type': NON_METAL},
    '63': {'atomic_num': 63, 'symbol': 'Eu', 'name': 'Europium', 'group': None, 'period': 6, 'atomic_weight': 151.964,
           'density': 5.243, 'melting_point': 1099, 'boiling_point': 1802, 'heat_capacity': 0.182,
           'electronegativity': 1.2, 'precise': True, 'type': NON_METAL},
    '64': {'atomic_num': 64, 'symbol': 'Gd', 'name': 'Gadolinium', 'group': None, 'period': 6, 'atomic_weight': 157.25,
           'density': 7.895, 'melting_point': 1585, 'boiling_point': 3546, 'heat_capacity': 0.236,
           'electronegativity': 1.2, 'precise': True, 'type': NON_METAL},
    '65': {'atomic_num': 65, 'symbol': 'Tb', 'name': 'Terbium', 'group': None, 'period': 6, 'atomic_weight': 158.925354,
           'density': 8.229, 'melting_point': 1629, 'boiling_point': 3503, 'heat_capacity': 0.182,
           'electronegativity': 1.2, 'precise': True, 'type': NON_METAL},
    '66': {'atomic_num': 66, 'symbol': 'Dy', 'name': 'Dysprosium', 'group': None, 'period': 6, 'atomic_weight': 162.5,
           'density': 8.55, 'melting_point': 1680, 'boiling_point': 2840, 'heat_capacity': 0.17,
           'electronegativity': 1.22, 'precise': True, 'type': NON_METAL},
    '67': {'atomic_num': 67, 'symbol': 'Ho', 'name': 'Holmium', 'group': None, 'period': 6, 'atomic_weight': 164.930328,
           'density': 8.795, 'melting_point': 1734, 'boiling_point': 2993, 'heat_capacity': 0.165,
           'electronegativity': 1.23, 'precise': True, 'type': NON_METAL},
    '68': {'atomic_num': 68, 'symbol': 'Er', 'name': 'Erbium', 'group': None, 'period': 6, 'atomic_weight': 167.259,
           'density': 9.066, 'melting_point': 1802, 'boiling_point': 3141, 'heat_capacity': 0.168,
           'electronegativity': 1.24, 'precise': True, 'type': NON_METAL},
    '69': {'atomic_num': 69, 'symbol': 'Tm', 'name': 'Thulium', 'group': None, 'period': 6, 'atomic_weight': 168.934218,
           'density': 9.321, 'melting_point': 1818, 'boiling_point': 2223, 'heat_capacity': 0.16,
           'electronegativity': 1.25, 'precise': True, 'type': NON_METAL},
    '70': {'atomic_num': 70, 'symbol': 'Yb', 'name': 'Ytterbium', 'group': None, 'period': 6, 'atomic_weight': 173.045,
           'density': 6.965, 'melting_point': 1097, 'boiling_point': 1469, 'heat_capacity': 0.155,
           'electronegativity': 1.1, 'precise': True, 'type': NON_METAL},
    '71': {'atomic_num': 71, 'symbol': 'Lu', 'name': 'Lutetium', 'group': None, 'period': 6, 'atomic_weight': 174.9668,
           'density': 9.84, 'melting_point': 1925, 'boiling_point': 3675, 'heat_capacity': 0.154,
           'electronegativity': 1.27, 'precise': True, 'type': NON_METAL},
    '72': {'atomic_num': 72, 'symbol': 'Hf', 'name': 'Hafnium', 'group': 4, 'period': 6, 'atomic_weight': 178.49,
           'density': 13.31, 'melting_point': 2506, 'boiling_point': 4876, 'heat_capacity': 0.144,
           'electronegativity': 1.3, 'precise': True, 'type': METAL},
    '73': {'atomic_num': 73, 'symbol': 'Ta', 'name': 'Tantalum', 'group': 5, 'period': 6, 'atomic_weight': 180.94788,
           'density': 16.654, 'melting_point': 3290, 'boiling_point': 5731, 'heat_capacity': 0.14,
           'electronegativity': 1.5, 'precise': True, 'type': METAL},
    '74': {'atomic_num': 74, 'symbol': 'W', 'name': 'Tungsten', 'group': 6, 'period': 6, 'atomic_weight': 183.84,
           'density': 19.25, 'melting_point': 3695, 'boiling_point': 5828, 'heat_capacity': 0.132,
           'electronegativity': 2.36, 'precise': True, 'type': METAL},
    '75': {'atomic_num': 75, 'symbol': 'Re', 'name': 'Rhenium', 'group': 7, 'period': 6, 'atomic_weight': 186.207,
           'density': 21.02, 'melting_point': 3459, 'boiling_point': 5869, 'heat_capacity': 0.137,
           'electronegativity': 1.9, 'precise': True, 'type': METAL},
    '76': {'atomic_num': 76, 'symbol': 'Os', 'name': 'Osmium', 'group': 8, 'period': 6, 'atomic_weight': 190.23,
           'density': 22.61, 'melting_point': 3306, 'boiling_point': 5285, 'heat_capacity': 0.13,
           'electronegativity': 2.2, 'precise': True, 'type': METAL},
    '77': {'atomic_num': 77, 'symbol': 'Ir', 'name': 'Iridium', 'group': 9, 'period': 6, 'atomic_weight': 192.217,
           'density': 22.56, 'melting_point': 2719, 'boiling_point': 4701, 'heat_capacity': 0.131,
           'electronegativity': 2.2, 'precise': True, 'type': METAL},
    '78': {'atomic_num': 78, 'symbol': 'Pt', 'name': 'Platinum', 'group': 10, 'period': 6, 'atomic_weight': '195.084*9',
           'density': 21.46, 'melting_point': 2041.4, 'boiling_point': 4098, 'heat_capacity': 0.133,
           'electronegativity': 2.28, 'precise': True, 'type': METAL},
    '79': {'atomic_num': 79, 'symbol': 'Au', 'name': 'Gold', 'group': 11, 'period': 6, 'atomic_weight': 196.96657,
           'density': 19.282, 'melting_point': 1337.33, 'boiling_point': 3129, 'heat_capacity': 0.129,
           'electronegativity': 2.54, 'precise': True, 'type': METAL},
    '80': {'atomic_num': 80, 'symbol': 'Hg', 'name': 'Mercury', 'group': 12, 'period': 6, 'atomic_weight': 200.592,
           'density': 13.5336, 'melting_point': 234.43, 'boiling_point': 629.88, 'heat_capacity': 0.14,
           'electronegativity': 2, 'precise': True, 'type': METAL},
    '81': {'atomic_num': 81, 'symbol': 'Tl', 'name': 'Thallium', 'group': 13, 'period': 6, 'atomic_weight': 204.38,
           'density': 11.85, 'melting_point': 577, 'boiling_point': 1746, 'heat_capacity': 0.129,
           'electronegativity': 1.62, 'precise': True, 'type': METAL},
    '82': {'atomic_num': 82, 'symbol': 'Pb', 'name': 'Lead', 'group': 14, 'period': 6, 'atomic_weight': 207.2,
           'density': 11.342, 'melting_point': 600.61, 'boiling_point': 2022, 'heat_capacity': 0.129,
           'electronegativity': 1.87, 'precise': True, 'type': METAL},
    '83': {'atomic_num': 83, 'symbol': 'Bi', 'name': 'Bismuth', 'group': 15, 'period': 6, 'atomic_weight': 208.9804,
           'density': 9.807, 'melting_point': 544.7, 'boiling_point': 1837, 'heat_capacity': 0.122,
           'electronegativity': 2.02, 'precise': True, 'type': METAL},
    '84': {'atomic_num': 84, 'symbol': 'Po', 'name': 'Polonium', 'group': 16, 'period': 6, 'precise': False,
           'atomic_weight': 209, 'density': 9.32, 'melting_point': 527, 'boiling_point': 1235, 'heat_capacity': None,
           'electronegativity': 2.0, 'type': METAL},
    '85': {'atomic_num': 85, 'symbol': 'At', 'name': 'Astatine', 'group': 17, 'period': 6, 'precise': False,
           'atomic_weight': 210, 'density': 7, 'melting_point': 575, 'boiling_point': 610, 'heat_capacity': None,
           'electronegativity': 2.2, 'type': METALLOID},
    '86': {'atomic_num': 86, 'symbol': 'Rn', 'name': 'Radon', 'group': 18, 'period': 6, 'precise': False,
           'atomic_weight': 222, 'density': 0.00973, 'melting_point': 202, 'boiling_point': 211.3,
           'heat_capacity': 0.094, 'electronegativity': 2.2, 'type': NON_METAL},
    '87': {'atomic_num': 87, 'symbol': 'Fr', 'name': 'Francium', 'group': 1, 'period': 7, 'precise': False,
           'atomic_weight': 223, 'density': 1.87, 'melting_point': 281, 'boiling_point': 890, 'heat_capacity': None,
           'electronegativity': 0.7, 'type': METAL},
    '88': {'atomic_num': 88, 'symbol': 'Ra', 'name': 'Radium', 'group': 2, 'period': 7, 'precise': False,
           'atomic_weight': 226, 'density': 5.5, 'melting_point': 973, 'boiling_point': 2010, 'heat_capacity': 0.094,
           'electronegativity': 0.9, 'type': METAL},
    '89': {'atomic_num': 89, 'symbol': 'Ac', 'name': 'Actinium', 'group': 3, 'period': 7, 'precise': False,
           'atomic_weight': 227, 'density': 10.07, 'melting_point': 1323, 'boiling_point': 3471, 'heat_capacity': 0.12,
           'electronegativity': 1.1, 'type': METAL},
    '90': {'atomic_num': 90, 'symbol': 'Th', 'name': 'Thorium', 'group': None, 'period': 7, 'atomic_weight': 232.0377,
           'density': 11.72, 'melting_point': 2115, 'boiling_point': 5061, 'heat_capacity': 0.113,
           'electronegativity': 1.3, 'precise': True, 'type': NON_METAL},
    '91': {'atomic_num': 91, 'symbol': 'Pa', 'name': 'Protactinium', 'group': None, 'period': 7,
           'atomic_weight': 231.03588, 'density': 15.37, 'melting_point': 1841, 'boiling_point': 4300,
           'heat_capacity': None, 'electronegativity': 1.5, 'precise': True, 'type': NON_METAL},
    '92': {'atomic_num': 92, 'symbol': 'U', 'name': 'Uranium', 'group': None, 'period': 7, 'atomic_weight': 238.02891,
           'density': 18.95, 'melting_point': 1405.3, 'boiling_point': 4404, 'heat_capacity': 0.116,
           'electronegativity': 1.38, 'precise': True, 'type': NON_METAL},
    '93': {'atomic_num': 93, 'symbol': 'Np', 'name': 'Neptunium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 237, 'density': 20.45, 'melting_point': 917, 'boiling_point': 4273, 'heat_capacity': None,
           'electronegativity': 1.36, 'type': NON_METAL},
    '94': {'atomic_num': 94, 'symbol': 'Pu', 'name': 'Plutonium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 244, 'density': 19.84, 'melting_point': 912.5, 'boiling_point': 3501, 'heat_capacity': None,
           'electronegativity': 1.28, 'type': NON_METAL},
    '95': {'atomic_num': 95, 'symbol': 'Am', 'name': 'Americium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 243, 'density': 13.69, 'melting_point': 1449, 'boiling_point': 2880, 'heat_capacity': None,
           'electronegativity': 1.13, 'type': NON_METAL},
    '96': {'atomic_num': 96, 'symbol': 'Cm', 'name': 'Curium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 247, 'density': 13.51, 'melting_point': 1613, 'boiling_point': 3383, 'heat_capacity': None,
           'electronegativity': 1.28, 'type': NON_METAL},
    '97': {'atomic_num': 97, 'symbol': 'Bk', 'name': 'Berkelium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 247, 'density': 14.79, 'melting_point': 1259, 'boiling_point': 2900, 'heat_capacity': None,
           'electronegativity': 1.3, 'type': NON_METAL},
    '98': {'atomic_num': 98, 'symbol': 'Cf', 'name': 'Californium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 251, 'density': 15.1, 'melting_point': 1173, 'boiling_point': 1743, 'heat_capacity': None,
           'electronegativity': 1.3, 'type': NON_METAL},
    '99': {'atomic_num': 99, 'symbol': 'Es', 'name': 'Einsteinium', 'group': None, 'period': 7, 'precise': False,
           'atomic_weight': 252, 'density': 8.84, 'melting_point': 1133, 'boiling_point': 1269, 'heat_capacity': None,
           'electronegativity': 1.3, 'type': NON_METAL},
    '100': {'atomic_num': 100, 'symbol': 'Fm', 'name': 'Fermium', 'group': None, 'period': 7, 'precise': False,
            'atomic_weight': 257, 'density': 9.7, 'melting_point': 1125, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': 1.3, 'type': NON_METAL},
    '101': {'atomic_num': 101, 'symbol': 'Md', 'name': 'Mendelevium', 'group': None, 'period': 7, 'precise': False,
            'atomic_weight': 258, 'density': 10.3, 'melting_point': 1100, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': 1.3, 'type': NON_METAL},
    '102': {'atomic_num': 102, 'symbol': 'No', 'name': 'Nobelium', 'group': None, 'period': 7, 'precise': False,
            'atomic_weight': 259, 'density': 9.9, 'melting_point': 1100, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': 1.3, 'type': NON_METAL},
    '103': {'atomic_num': 103, 'symbol': 'Lr', 'name': 'Lawrencium', 'group': None, 'period': 7, 'precise': False,
            'atomic_weight': 266, 'density': 15.6, 'melting_point': 1900, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': 1.3, 'type': NON_METAL},
    '104': {'atomic_num': 104, 'symbol': 'Rf', 'name': 'Rutherfordium', 'group': 4, 'period': 7, 'precise': False,
            'atomic_weight': 267, 'density': 23.2, 'melting_point': 2400, 'boiling_point': 5800, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '105': {'atomic_num': 105, 'symbol': 'Db', 'name': 'Dubnium', 'group': 5, 'period': 7, 'precise': False,
            'atomic_weight': 268, 'density': 29.3, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '106': {'atomic_num': 106, 'symbol': 'Sg', 'name': 'Seaborgium', 'group': 6, 'period': 7, 'precise': False,
            'atomic_weight': 269, 'density': 35.0, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '107': {'atomic_num': 107, 'symbol': 'Bh', 'name': 'Bohrium', 'group': 7, 'period': 7, 'precise': False,
            'atomic_weight': 270, 'density': 37.1, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '108': {'atomic_num': 108, 'symbol': 'Hs', 'name': 'Hassium', 'group': 8, 'period': 7, 'precise': False,
            'atomic_weight': 270, 'density': 40.7, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '109': {'atomic_num': 109, 'symbol': 'Mt', 'name': 'Meitnerium', 'group': 9, 'period': 7, 'precise': False,
            'atomic_weight': 278, 'density': 37.4, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '110': {'atomic_num': 110, 'symbol': 'Ds', 'name': 'Darmstadtium', 'group': 10, 'period': 7, 'precise': False,
            'atomic_weight': 281, 'density': 34.8, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '111': {'atomic_num': 111, 'symbol': 'Rg', 'name': 'Roentgenium', 'group': 11, 'period': 7, 'precise': False,
            'atomic_weight': 282, 'density': 28.7, 'melting_point': None, 'boiling_point': None, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '112': {'atomic_num': 112, 'symbol': 'Cn', 'name': 'Copernicium', 'group': 12, 'period': 7, 'precise': False,
            'atomic_weight': 285, 'density': 14.0, 'melting_point': 283, 'boiling_point': 340, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '113': {'atomic_num': 113, 'symbol': 'Nh', 'name': 'Nihonium', 'group': 13, 'period': 7, 'precise': False,
            'atomic_weight': 286, 'density': 16, 'melting_point': 700, 'boiling_point': 1400, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '114': {'atomic_num': 114, 'symbol': 'Fl', 'name': 'Flerovium', 'group': 14, 'period': 7, 'precise': False,
            'atomic_weight': 289, 'density': 14, 'melting_point': None, 'boiling_point': 210, 'heat_capacity': None,
            'electronegativity': None, 'type': METAL},
    '115': {'atomic_num': 115, 'symbol': 'Mc', 'name': 'Moscovium', 'group': 15, 'period': 7, 'precise': False,
            'atomic_weight': 290, 'density': 13.5, 'melting_point': 700, 'boiling_point': 1400, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '116': {'atomic_num': 116, 'symbol': 'Lv', 'name': 'Livermorium', 'group': 16, 'period': 7, 'precise': False,
            'atomic_weight': 293, 'density': 12.9, 'melting_point': 700, 'boiling_point': 1100, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '117': {'atomic_num': 117, 'symbol': 'Ts', 'name': 'Tennessine', 'group': 17, 'period': 7, 'precise': False,
            'atomic_weight': 294, 'density': 7.2, 'melting_point': 700, 'boiling_point': 883, 'heat_capacity': None,
            'electronegativity': None, 'type': None},
    '118': {'atomic_num': 118, 'symbol': 'Og', 'name': 'Oganesson', 'group': 18, 'period': 7, 'precise': False,
            'atomic_weight': 294, 'density': 5.0, 'melting_point': 320, 'boiling_point': 350, 'heat_capacity': None,
            'electronegativity': None, 'type': None}}
