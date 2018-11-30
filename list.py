school_list=[{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [4,4,4,5,5]},{'school_class': '4c', 'scores': [1,3,5,2,2]},{'school_class': '4d', 'scores': [5,4,5,5,5]}]



school_list = [sum(item['scores']) for item in school_list]
for cls in school_list:
    print(cls)

