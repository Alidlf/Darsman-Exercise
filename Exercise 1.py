import numpy as np
import pandas as pd
from scipy import stats



#----------------------------------------------------------------------------------------
#------------------------------پاک سازی داده ها----------------------------------


# خواندن فایل داده ها
data=pd.read_csv("data.csv")

#نمایش داده ها
#def display_data(data):
#    print(data)
#    print(100*'*')



#جایگزین داده های اشتباه
#def fill_noisy_data(data):
#    data.loc[data.MaritalStatus.astype("str").str.isnumeric(),"MaritalStatus"]=data.MaritalStatus.mode()[0],
#    data.loc[~data.Weight.astype("str").str.isnumeric(),"Weight"]=data.Weight.mode()[0]
#    return data
#data=fill_noisy_data(data)
#display_data(data)


#پر کرئنن خانه های خالی 
#def fillna_record_none(data):
#    data.fillna(value={
#        "December income": data["December income"].mean()  
#    },inplace=True)
#    return data
#data=fillna_record_none(data)
#display_data(data)

# حذف یک ردیف خاص
#def remove_row(data):
#    new_data = data.drop(2) 
#    return new_data
#data=remove_row(data)

#ذخیره داده پاکسازی شده در یک فایل جدید
#def load(data,filepath):
#    data.to_csv(filepath,index=False) 
#load(data,"clean_data.csv")

#-----------------------------------main program--------------------------------------

# خواندن فایل داده ها
data=pd.read_csv("clean_data.csv")

def display_data(data):
    print(data)
    print(100*'*')
#display_data(data)


#سوال اول >>  برنامهاي بنويسيد كه ميانگين و ميانه را براي ستونهاي سن و وزن محاسبه نمايد 
def mean_median_value (data):
    mean=np.mean(data)
    median=np.median(data)
    return mean , median

print("Age -> Mean:", mean_median_value(data["Age"])[0], "| Median:", mean_median_value(data["Age"])[1])
print("Weight -> Mean:", mean_median_value(data["Weight"])[0], "| Median:", mean_median_value(data["Weight"])[1])
print(100*"-")

#سوال دوم>> برنامهاي بنويسيد كه مد را براي ستونهاي قد، جنسيت و مدرك تحصيلي محاسبه نمايد
def mode_Calculation(data):
    result = data.mode()[0] 
    return result

print("Height -> Mode:", mode_Calculation(data["Height"]))
print("Gender -> Mode:", mode_Calculation(data["Gender"]))
print("Education -> Mode:", mode_Calculation(data["Education"]))
print(100*"-")



#سوال سوم>> برنامهاي بنويسيد كه بازه را براي ستونهاي سن، قد و وزن محاسبه نمايد
def range_Calculation(data):
    result=np.ptp(data)
    return result

print("Age -> Range :", range_Calculation(data["Age"]))
print("Height -> Range:", range_Calculation(data["Height"]))
print("Weight -> Range:", range_Calculation(data["Weight"]))
print(100*"-")



#سوال چهارم >> برنامهاي بنويسيد كه واريانس و انحراف معيار را براي ستونهاي سن، قد و وزن محاسبه نمايد

def variance_std_Calculation (data):
    variance=np.var(data)
    std=np.std(data)
    return variance, std

print("Age -> variance:", variance_std_Calculation(data["Age"])[0], "| std_deviation:", variance_std_Calculation(data["Age"])[1])
print("Weight -> variance:", variance_std_Calculation(data["Weight"])[0], "| std_deviation:",variance_std_Calculation(data["Weight"])[1])
print("Height -> variance:", variance_std_Calculation(data["Height"])[0], "| std_deviation:", variance_std_Calculation(data["Height"])[1])
print(100*"-")


# سوال پنجم>>رنامهاي بنويسيد كه چاركهاي اول، دوم و سوم را براي ستونهاي سن، قد و وزن محاسبه

def quartiles_Calculation (data):
    result=np.percentile(data,[25,50,75])
    return result

print("Age -> Quartiles :", quartiles_Calculation(data["Age"]))
print("Height -> Quartiles:",quartiles_Calculation(data["Height"]))
print("Weight -> Quartiles:", quartiles_Calculation(data["Weight"]))
print(100*"-")


# را براي ستونهاي سن، قد و وزن محاسبه نمايد IQR سوال ششم>> برنامهاي بنويسيد كه
def iqr_Calculation (data):
    q1=np.percentile(data,25)
    q3=np.percentile(data,75)
    IQR=q3-q1
    return IQR
print("Age -> IQR :", iqr_Calculation(data["Age"]))
print("Height -> IQR:",iqr_Calculation(data["Height"]))
print("Weight -> IQR:", iqr_Calculation(data["Weight"]))
print(100*"-")

