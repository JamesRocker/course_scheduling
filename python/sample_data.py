sample_data = [
        {
            'facultyName': 'C',
            'courses': [
                {"courseCode": "BIO 200","isLab": False},
                {"courseCode": "PHYS 100","isLab": False},
                {"courseCode": "Course 25","isLab": False},
            ],
            'availableTime': {
                'C': {'priority': 1},
                'A': {'priority': 3},
                'G_1': {'priority': 2},
                'K_2': {'priority': 1},
                'D': {'priority': 1},
                'L': {'priority': 3},
                'H_2': {'priority': 3}
            }
        },
        {
            'facultyName': 'A',
            'courses': [
                {"courseCode": "Course 2","isLab": False},
                {"courseCode": "Lab 1A","isLab": True},
                {"courseCode": "CMPT 100","isLab": False},
                {"courseCode": "Course 3","isLab": False},
                {"courseCode": "Lab 2A","isLab": True},
            ],
            'availableTime': {
                'U': {'priority': 1},
                'G_1': {'priority': 3},
                'Y': {'priority': 2},
                'A': {'priority': 1},
                'H_3': {'priority': 2},
                'C': {'priority': 3},
                'AA': {'priority': 3}
            }
        },
        {
            'facultyName': 'B',
            'courses': [
                {"courseCode": "Lab 3A","isLab": True},
                {"courseCode": "MATH 100","isLab": False},
                {"courseCode": "Lab 3B","isLab": True},
                {"courseCode": "CHEM 100","isLab": False},
                {"courseCode": "MATH 400","isLab": False}
            ],
            'availableTime': {
                'Z': {'priority': 1},
                'I_2': {'priority': 2},
                'K_3': {'priority': 3},
                'X': {'priority': 3},
                'H_3': {'priority': 2},
                'C': {'priority': 1},
                'BB': {'priority': 1},
                'V': {'priority': 3}
            }
        }
      
    ]

# sample_data = [
#     {
#         'facultyName': 'C',
#         'courses': [
#             {"courseCode": "BIOL 200","isLab": True},
#             # {"courseCode": "PHYS 100","isLab": False},
#             # {"courseCode": "Course 25","isLab": False},
#         ],
#         'availableTime': {
#             'C': {'priority': 1},
#             'A': {'priority': 3},
#             'G_1': {'priority': 2},
#             'K_2': {'priority': 1},
#             'D': {'priority': 1},
#             'L': {'priority': 3},
#             'H_2': {'priority': 3},
#             'X': {'priority': 1},
#             'Y': {'priority': 2}
#         }
#     },
#     {
#         'facultyName': 'A',
#         'courses': [
#             # {"courseCode": "Course 2","isLab": False},
#             {"courseCode": "Lab 1A","isLab": True},
#             # {"courseCode": "CMPT 100","isLab": False},
#             # {"courseCode": "Course 3","isLab": False},
#             {"courseCode": "Lab 2A","isLab": True},
#         ],
#         'availableTime': {
#             'U': {'priority': 1},
#             # 'G_1': {'priority': 3},
#             'Y': {'priority': 2},
#             # 'A': {'priority': 1},
#             # 'H_3': {'priority': 2},
#             # 'C': {'priority': 3},
#             'AA': {'priority': 3}
#         }
#     },
#     {
#         'facultyName': 'B',
#         'courses': [
#             {"courseCode": "Lab 3A","isLab": True},
#             {"courseCode": "MATH 100","isLab": False},
#             {"courseCode": "Lab 3B","isLab": True},
#             {"courseCode": "CHEM 100","isLab": False},
#             {"courseCode": "MATH 400","isLab": False}
#         ],
#         'availableTime': {
#             'Z': {'priority': 1},
#             'I_2': {'priority': 2},
#             'K_3': {'priority': 3},
#             'X': {'priority': 3},
#             'H_3': {'priority': 2},
#             'C': {'priority': 1},
#             'BB': {'priority': 1},
#             'V': {'priority': 3}
#         }
#     }
    
# ]