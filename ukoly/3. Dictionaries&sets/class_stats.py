classes = {'Biology' : ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann'],
            'Math' : ['Marcus','Alex','Glenn','Samuel','Clara','Chelsea'],
            'PE'  : ['Adam','Tyler', 'Alex','Clara'],
            'Social Sciences': ['Abraham','Marcus','Alex','Glenn','Clara'],
            'Chemistry' : ['Alfred', 'Curt','Oliver','Alex','Tyler','Ann']}

students_all_classes = set(classes['Biology']) & set(classes['Math']) & set(classes['PE']) & set(classes['Social Sciences']) & set(classes['Chemistry'])

print('Students inscribed into all the subjects: ', students_all_classes)