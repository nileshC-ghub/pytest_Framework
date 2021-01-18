import pandas as pd
import numpy as np
import pytest
from os import path

#file_path='D:\\Software\\Python\\python_git\\src\\pytest_Framework\\test_beta\\'
file_path='/mnt/d/Software/Python/python_git/src/pytest_Framework/'
emplst=pd.read_csv(str(file_path+'emp_id_list_for_testing.csv'))
print(emplst)
redf=[]
for i in emplst['Emp_id']:
    if (path.exists(str(file_path+'casestudy_'+str(i)+'.py'))):
        pytest.main(['-v',str(file_path+'test_casestudy.py'),'--ifile',str('casestudy_'+str(i)),'--csv','tests_res.csv','--csv-columns','id,module,name,file,doc,markers,status,message,duration'])
        testdf=pd.read_csv('tests_res.csv')
        testdf['Emp_id']=[str(i)]*len(testdf.index)
        #print([str(i)]*len(testdf.index))
        redf.append(testdf)
    else:
         print(str(file_path+'functions_'+str(i)+'.py')+' file does not exists')
res_final=pd.concat(redf,ignore_index=True)
res_ex=res_final[['Emp_id','name','markers','status','duration','message']]
res_ex.to_excel('report.xlsx', engine='xlsxwriter',index=False)
Total_test_cases=res_ex.groupby(['Emp_id','markers']).size().reset_index(name='total')['total'].iloc[0]
res_ex['Total_test_cases']=[str(Total_test_cases)]*len(res_ex.index)
res_sum=res_ex.groupby(['Emp_id','markers','Total_test_cases','status'])['name'].apply(','.join).reset_index()
res_sum['counts']=res_sum['name'].apply(lambda x : len(x.split(',')))
res_sum['score %']=res_sum.apply(lambda x : ((x.counts/int(x.Total_test_cases))*100) if x.status=='passed' else np.nan,axis = 1)
res_sum['name']=res_sum.apply(lambda x : x['name'] if x.status=='failed' else np.nan,axis = 1)
res_sum.set_index(['Emp_id','markers','Total_test_cases','status'],inplace=True)
res_sum.to_excel('report_sum.xlsx', engine='xlsxwriter')
print(res_sum)
