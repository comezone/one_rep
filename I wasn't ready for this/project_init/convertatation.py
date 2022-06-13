def join(x):

    hemi = ['id',
            'name',
            'surname',
            'login',
            'password',
            'date']

    result = []
    for i in x:
        ji = []
        for j in i:
            ji.append(j)
        de= dict(zip(hemi, ji))
        result.append(de)
    return result







