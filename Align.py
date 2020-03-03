def restructure(data):
    keywords={'IBNK':'Issuing Bank','APCT':'Applicant','BNFR':'Beneficiary','DCDE':'Destination Swift','PCNT':'Destination Country',
             'DATE':'Document Date','PRTY':'Destination Party','SCDE':'Source Swift','ILOC':'Issuing Bank Location',
             'DLOC':'Destination Bank Location','DBNK':'Destination Bank'}
    matched={}
    for j in keywords.keys():
        matched[j]=[]
    for i in data:
        try:
            if i[1] in keywords.keys():
                matched[i[1]].append(i[0])
        except:
            pass
    results={}
    for k in matched.keys():
        if len(matched[k])>0:
            results[keywords[k]]=matched[k][0]
    return results

