#loop through dictionary
student_dict ={'student': ['Angela','James','Lily'],
               'score': [56, 76, 98]
}

# for (key,value) in student_dict.items()
#     print(value)

# loop through a data frame
import pandas

student_df = pandas.DataFrame(student_dict)
# print(student_df)
# for (key, value) in student_df.items():
#     print(key) #titles of the column

# Loop through the rows via Pandas
for (index, row) in student_df.iterrows():
    print(row.score) #row是1個series物件

#{new_key:new_value for (index,row) in df.iterrows()}