#	Descriptive statistics using Pandas

import numpy
import csv
import pandas
import matplotlib.pyplot as plt

dataAttributes = []

# list of Attributes
Attributes = {
	"1": {},	# State_Name
	"2": {},	# State_District_Name
	"3": {},	# AA_Sample_Units_Total
	"4": {},	# AA_Sample_Units_Rural
	"5": {},	# AA_Sample_Units_Urban
	"6": {},	# AA_Households_Total
	"7": {},	# AA_Households_Rural
	"8": {},	# AA_Households_Urban
	"9": {},	# AA_Population_Total
	"10": {},	# AA_Population_Rural
	"11": {},	# AA_Population_Urban
	"12": {},	# AA_Ever_Married_Women_Aged_15_49_Years_Total
	"13": {},	# AA_Ever_Married_Women_Aged_15_49_Years_Rural
	"14": {},	# AA_Ever_Married_Women_Aged_15_49_Years_Urban
	"15": {},	# AA_Currently_Married_Women_Aged_15_49_Years_Total
	"16": {},	# AA_Currently_Married_Women_Aged_15_49_Years_Rural
	"17": {},	# AA_Currently_Married_Women_Aged_15_49_Years_Urban
	"18": {},	# AA_Children_12_23_Months_Total
	"19": {},	# AA_Children_12_23_Months_Rural
	"20": {},	# AA_Children_12_23_Months_Urban
	"21": {},	# BB_Average_Household_Size_Sc_Total
	"22": {},	# BB_Average_Household_Size_Sc_Rural
	"23": {},	# BB_Average_Household_Size_Sc_Urban
	"24": {},	# BB_Average_Household_Size_St_Total
	"25": {},	# BB_Average_Household_Size_St_Rural
	"26": {},	# BB_Average_Household_Size_St_Urban
	"27": {},	# BB_Average_Household_Size_All_Total
	"28": {},	# BB_Average_Household_Size_All_Rural
	"29": {},	# BB_Average_Household_Size_All_Urban
	"30": {},	# BB_Population_Below_Age_15_Years_Total
	"31": {},	# BB_Population_Below_Age_15_Years_Rural
	"32": {},	# BB_Population_Below_Age_15_Years_Urban
	"33": {},	# BB_Dependency_Ratio_Total
	"34": {},	# BB_Dependency_Ratio_Rural
	"35": {},	# BB_Dependency_Ratio_Urban
	"36": {},	# BB_Currently_Married_Illiterate_Women_Aged_15_49_Years_Total
	"37": {},	# BB_Currently_Married_Illiterate_Women_Aged_15_49_Years_Rural
	"38": {},	# BB_Currently_Married_Illiterate_Women_Aged_15_49_Years_Urban
	"39": {},	# CC_Sex_Ratio_At_Birth_Total
	"40": {},	# CC_Sex_Ratio_At_Birth_Rural
	"41": {},	# CC_Sex_Ratio_At_Birth_Urban
	"42": {},	# CC_Sex_Ratio_0_4_Years_Total
	"43": {},	# CC_Sex_Ratio_0_4_Years_Rural
	"44": {},	# CC_Sex_Ratio_0_4_Years_Urban
	"45": {},	# CC_Sex_Ratio_All_Ages_Total
	"46": {},	# CC_Sex_Ratio_All_Ages_Rural
	"47": {},	# CC_Sex_Ratio_All_Ages_Urban
	"48": {},	# DD_Person_Total
	"49": {},	# DD_Person_Rural
	"50": {},	# DD_Person_Urban
	"51": {},	# DD_Male_Total
	"52": {},	# DD_Male_Rural
	"53": {},	# DD_Male_Urban
	"54": {},	# DD_Female_Total
	"55": {},	# DD_Female_Rural
	"56": {},	# DD_Female_Urban
	"57": {},	# EE_Marriages_Among_Females_Below_Legal_Age_18_Years_Total
	"58": {},	# EE_Marriages_Among_Females_Below_Legal_Age_18_Years_Rural
	"59": {},	# EE_Marriages_Among_Females_Below_Legal_Age_18_Years_Urban
	"60": {},	# EE_Marriages_Among_Males_Below_Legal_Age_21_Years_Total
	"61": {},	# EE_Marriages_Among_Males_Below_Legal_Age_21_Years_Rural
	"62": {},	# EE_Marriages_Among_Males_Below_Legal_Age_21_Years_Urban
	"63": {},	# EE_Currently_Married_Women_Aged_20_24_Years_Married_Before_Legal_Age_18_Years_Total
	"64": {},	# EE_Currently_Married_Women_Aged_20_24_Years_Married_Before_Legal_Age_18_Years_Rural
	"65": {},	# EE_Currently_Married_Women_Aged_20_24_Years_Married_Before_Legal_Age_18_Years_Urban
	"66": {},	# EE_Currently_Married_Men_Aged_25_29_Years_Married_Before_Legal_Age_21_Years_Total
	"67": {},	# EE_Currently_Married_Men_Aged_25_29_Years_Married_Before_Legal_Age_21_Years_Rural
	"68": {},	# EE_Currently_Married_Men_Aged_25_29_Years_Married_Before_Legal_Age_21_Years_Urban
	"69": {},	# EE_Mean_Age_At_Marriage_Male_Total
	"70": {},	# EE_Mean_Age_At_Marriage_Male_Rural
	"71": {},	# EE_Mean_Age_At_Marriage_Male_Urban
	"72": {},	# EE_Mean_Age_At_Marriage_Female_Total
	"73": {},	# EE_Mean_Age_At_Marriage_Female_Rural
	"74": {},	# EE_Mean_Age_At_Marriage_Female_Urban
	"75": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Person_Total
	"76": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Person_Rural
	"77": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Person_Urban
	"78": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Male_Total
	"79": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Male_Rural
	"80": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Male_Urban
	"81": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Female_Total
	"82": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Female_Rural
	"83": {},	# FF_Children_Currently_Attending_School_Age_6_17_Years_Female_Urban
	"84": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Person_Total
	"85": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Person_Rural
	"86": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Person_Urban
	"87": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Male_Total
	"88": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Male_Rural
	"89": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Male_Urban
	"90": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Female_Total
	"91": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Female_Rural
	"92": {},	# FF_Children_Attended_Before_Drop_Out_Age_6_17_Years_Female_Urban
	"93": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Person_Total
	"94": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Person_Rural
	"95": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Person_Urban
	"96": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Male_Total
	"97": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Male_Rural
	"98": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Male_Urban
	"99": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Female_Total
	"100": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Female_Rural
	"101": {},	# GG_Children_Aged_5_14_Years_Engaged_In_Work_Female_Urban
	"102": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Person_Total
	"103": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Person_Rural
	"104": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Person_Urban
	"105": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Male_Total
	"106": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Male_Rural
	"107": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Male_Urban
	"108": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Female_Total
	"109": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Female_Rural
	"110": {},	# GG_Work_Participation_Rate_15_Years_And_Above_Female_Urban
	"111": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Person_Total
	"112": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Person_Rural
	"113": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Person_Urban
	"114": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Male_Total
	"115": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Male_Rural
	"116": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Male_Urban
	"117": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Female_Total
	"118": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Female_Rural
	"119": {},	# HH_Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Female_Urban
	"120": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Person_Total
	"121": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Person_Rural
	"122": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Person_Urban
	"123": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Male_Total
	"124": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Male_Rural
	"125": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Male_Urban
	"126": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Female_Total
	"127": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Female_Rural
	"128": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Severe_Female_Urban
	"129": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Person_Total
	"130": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Person_Rural
	"131": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Person_Urban
	"132": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Male_Total
	"133": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Male_Rural
	"134": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Male_Urban
	"135": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Female_Total
	"136": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Female_Rural
	"137": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Major_Female_Urban
	"138": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Person_Total
	"139": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Person_Rural
	"140": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Person_Urban
	"141": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Male_Total
	"142": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Male_Rural
	"143": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Male_Urban
	"144": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Female_Total
	"145": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Female_Rural
	"146": {},	# II_Number_Of_Injured_Persons_By_Type_Of_Treatment_Received_Per_100000_Population_Minor_Female_Urban
	"147": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Person_Total
	"148": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Person_Rural
	"149": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Person_Urban
	"150": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Male_Total
	"151": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Male_Rural
	"152": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Male_Urban
	"153": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Female_Total
	"154": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Female_Rural
	"155": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Female_Urban
	"156": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Person_Total
	"157": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Person_Rural
	"158": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Person_Urban
	"159": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Male_Total
	"160": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Male_Rural
	"161": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Male_Urban
	"162": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Female_Total
	"163": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Female_Rural
	"164": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Female_Urban
	"165": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Person_Total
	"166": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Person_Rural
	"167": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Person_Urban
	"168": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Male_Total
	"169": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Male_Rural
	"170": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Male_Urban
	"171": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Female_Total
	"172": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Female_Rural
	"173": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Female_Urban
	"174": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Person_Total
	"175": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Person_Rural
	"176": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Person_Urban
	"177": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Male_Total
	"178": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Male_Rural
	"179": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Male_Urban
	"180": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Female_Total
	"181": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Female_Rural
	"182": {},	# JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Any_Type_Of_Acute_Illness_Female_Urban
	"183": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Person_Total
	"184": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Person_Rural
	"185": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Person_Urban
	"186": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Male_Total
	"187": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Male_Rural
	"188": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Male_Urban
	"189": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Female_Total
	"190": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Female_Rural
	"191": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Any_Source_Female_Urban
	"192": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Person_Total
	"193": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Person_Rural
	"194": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Person_Urban
	"195": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Male_Total
	"196": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Male_Rural
	"197": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Male_Urban
	"198": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Female_Total
	"199": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Female_Rural
	"200": {},	# JJ_Persons_Suffering_From_Acute_Illness_And_Taking_Treatment_From_Government_Source_Female_Urban
	"201": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Person_Total
	"202": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Person_Rural
	"203": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Person_Urban
	"204": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Male_Total
	"205": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Male_Rural
	"206": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Male_Urban
	"207": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Female_Total
	"208": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Female_Rural
	"209": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_Per_100000_Population_Female_Urban
	"210": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Person_Total
	"211": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Person_Rural
	"212": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Person_Urban
	"213": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Male_Total
	"214": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Male_Rural
	"215": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Male_Urban
	"216": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Female_Total
	"217": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Female_Rural
	"218": {},	# KK_Having_Any_Kind_Of_Symptoms_Of_Chronic_Illness_And_Sought_Medical_Care_Female_Urban
	"219": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Person_Total
	"220": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Person_Rural
	"221": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Person_Urban
	"222": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Male_Total
	"223": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Male_Rural
	"224": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Male_Urban
	"225": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Female_Total
	"226": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Female_Rural
	"227": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Female_Urban
	"228": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Person_Total
	"229": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Person_Rural
	"230": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Person_Urban
	"231": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Male_Total
	"232": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Male_Rural
	"233": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Male_Urban
	"234": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Female_Total
	"235": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Female_Rural
	"236": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Female_Urban
	"237": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Person_Total
	"238": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Person_Rural
	"239": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Person_Urban
	"240": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Male_Total
	"241": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Male_Rural
	"242": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Male_Urban
	"243": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Female_Total
	"244": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Female_Rural
	"245": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Female_Urban
	"246": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Person_Total
	"247": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Person_Rural
	"248": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Person_Urban
	"249": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Male_Total
	"250": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Male_Rural
	"251": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Male_Urban
	"252": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Female_Total
	"253": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Female_Rural
	"254": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Female_Urban
	"255": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Person_Total
	"256": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Person_Rural
	"257": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Person_Urban
	"258": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Male_Total
	"259": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Male_Rural
	"260": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Male_Urban
	"261": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Female_Total
	"262": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Female_Rural
	"263": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Arthritis_Female_Urban
	"264": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Person_Total
	"265": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Person_Rural
	"266": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Person_Urban
	"267": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Male_Total
	"268": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Male_Rural
	"269": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Male_Urban
	"270": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Female_Total
	"271": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Female_Rural
	"272": {},	# KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Any_Kind_Of_Chronic_Illness_Female_Urban
	"273": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Person_Total
	"274": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Person_Rural
	"275": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Person_Urban
	"276": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Male_Total
	"277": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Male_Rural
	"278": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Male_Urban
	"279": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Female_Total
	"280": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Female_Rural
	"281": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_Female_Urban
	"282": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Person_Total
	"283": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Person_Rural
	"284": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Person_Urban
	"285": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Male_Total
	"286": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Male_Rural
	"287": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Male_Urban
	"288": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Female_Total
	"289": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Female_Rural
	"290": {},	# KK_Having_Diagnosed_For_Any_Kind_Of_Chronic_Illness_And_Getting_Regular_Treatment_From_Government_Source_Female_Urban
	"291": {},	# LL_Crude_Birth_Rate_Cbr_Total
	"292": {},	# LL_Crude_Birth_Rate_Cbr_Rural
	"293": {},	# LL_Crude_Birth_Rate_Cbr_Urban
	"294": {},	# LL_Natural_Growth_Rate_Total
	"295": {},	# LL_Natural_Growth_Rate_Rural
	"296": {},	# LL_Natural_Growth_Rate_Urban
	"297": {},	# LL_Total_Fertility_Rate_Total
	"298": {},	# LL_Total_Fertility_Rate_Rural
	"299": {},	# LL_Total_Fertility_Rate_Urban
	"300": {},	# LL_Women_Aged_20_24_Reporting_Birth_Of_Order_2__Above_Total
	"301": {},	# LL_Women_Aged_20_24_Reporting_Birth_Of_Order_2__Above_Rural
	"302": {},	# LL_Women_Aged_20_24_Reporting_Birth_Of_Order_2__Above_Urban
	"303": {},	# LL_Women_Reporting_Birth_Of_Order_3__Above_Total
	"304": {},	# LL_Women_Reporting_Birth_Of_Order_3__Above_Rural
	"305": {},	# LL_Women_Reporting_Birth_Of_Order_3__Above_Urban
	"306": {},	# LL_Women_With_Two_Children_Wanting_No_More_Children_Total
	"307": {},	# LL_Women_With_Two_Children_Wanting_No_More_Children_Rural
	"308": {},	# LL_Women_With_Two_Children_Wanting_No_More_Children_Urban
	"309": {},	# LL_Women_Aged_15_19_Years_Who_Were_Already_Mothers_Or_Pregnant_At_The_Time_Of_Survey_Total
	"310": {},	# LL_Women_Aged_15_19_Years_Who_Were_Already_Mothers_Or_Pregnant_At_The_Time_Of_Survey_Rural
	"311": {},	# LL_Women_Aged_15_19_Years_Who_Were_Already_Mothers_Or_Pregnant_At_The_Time_Of_Survey_Urban
	"312": {},	# LL_Median_Age_At_First_Live_Birth_Of_Women_Aged_15_49_Years_Total
	"313": {},	# LL_Median_Age_At_First_Live_Birth_Of_Women_Aged_15_49_Years_Rural
	"314": {},	# LL_Median_Age_At_First_Live_Birth_Of_Women_Aged_15_49_Years_Urban
	"315": {},	# LL_Median_Age_At_First_Live_Birth_Of_Women_Aged_25_49_Years_Total
	"316": {},	# LL_Median_Age_At_First_Live_Birth_Of_Women_Aged_25_49_Years_Rural
	"317": {},	# LL_Median_Age_At_First_Live_Birth_Of_Women_Aged_25_49_Years_Urban
	"318": {},	# LL_Live_Births_Taking_Place_After_An_Interval_Of_36_Months_Total
	"319": {},	# LL_Live_Births_Taking_Place_After_An_Interval_Of_36_Months_Rural
	"320": {},	# LL_Live_Births_Taking_Place_After_An_Interval_Of_36_Months_Urban
	"321": {},	# LL_Mean_Number_Of_Children_Ever_Born_To_Women_Aged_15_49_Years_Total
	"322": {},	# LL_Mean_Number_Of_Children_Ever_Born_To_Women_Aged_15_49_Years_Rural
	"323": {},	# LL_Mean_Number_Of_Children_Ever_Born_To_Women_Aged_15_49_Years_Urban
	"324": {},	# LL_Mean_Number_Of_Children_Surviving_To_Women_Aged_15_49_Years_Total
	"325": {},	# LL_Mean_Number_Of_Children_Surviving_To_Women_Aged_15_49_Years_Rural
	"326": {},	# LL_Mean_Number_Of_Children_Surviving_To_Women_Aged_15_49_Years_Urban
	"327": {},	# LL_Mean_Number_Of_Children_Ever_Born_To_Women_Aged_45_49_Years_Total
	"328": {},	# LL_Mean_Number_Of_Children_Ever_Born_To_Women_Aged_45_49_Years_Rural
	"329": {},	# LL_Mean_Number_Of_Children_Ever_Born_To_Women_Aged_45_49_Years_Urban
	"330": {},	# MM_Pregnancy_To_Women_Aged_15_49_Years_Resulting_In_Abortion_Total
	"331": {},	# MM_Pregnancy_To_Women_Aged_15_49_Years_Resulting_In_Abortion_Rural
	"332": {},	# MM_Pregnancy_To_Women_Aged_15_49_Years_Resulting_In_Abortion_Urban
	"333": {},	# MM_Women_Who_Received_Any_Anc_Before_Abortion_Total
	"334": {},	# MM_Women_Who_Received_Any_Anc_Before_Abortion_Rural
	"335": {},	# MM_Women_Who_Received_Any_Anc_Before_Abortion_Urban
	"336": {},	# MM_Women_Who_Went_For_Ultrasound_Before_Abortion_Total
	"337": {},	# MM_Women_Who_Went_For_Ultrasound_Before_Abortion_Rural
	"338": {},	# MM_Women_Who_Went_For_Ultrasound_Before_Abortion_Urban
	"339": {},	# MM_Average_Month_Of_Pregnancy_At_The_Time_Of_Abortion_Total
	"340": {},	# MM_Average_Month_Of_Pregnancy_At_The_Time_Of_Abortion_Rural
	"341": {},	# MM_Average_Month_Of_Pregnancy_At_The_Time_Of_Abortion_Urban
	"342": {},	# MM_Abortion_Performed_By_Skilled_Health_Personnel_Total
	"343": {},	# MM_Abortion_Performed_By_Skilled_Health_Personnel_Rural
	"344": {},	# MM_Abortion_Performed_By_Skilled_Health_Personnel_Urban
	"345": {},	# MM_Abortion_Taking_Place_In_Institution_Total
	"346": {},	# MM_Abortion_Taking_Place_In_Institution_Rural
	"347": {},	# MM_Abortion_Taking_Place_In_Institution_Urban
	"348": {},	# NN_Current_Usage_Any_Method_Total
	"349": {},	# NN_Current_Usage_Any_Method_Rural
	"350": {},	# NN_Current_Usage_Any_Method_Urban
	"351": {},	# NN_Current_Usage_Any_Modern_Method_Total
	"352": {},	# NN_Current_Usage_Any_Modern_Method_Rural
	"353": {},	# NN_Current_Usage_Any_Modern_Method_Urban
	"354": {},	# NN_Current_Usage_Female_Sterilization_Total
	"355": {},	# NN_Current_Usage_Female_Sterilization_Rural
	"356": {},	# NN_Current_Usage_Female_Sterilization_Urban
	"357": {},	# NN_Current_Usage_Male_Sterilization_Total
	"358": {},	# NN_Current_Usage_Male_Sterilization_Rural
	"359": {},	# NN_Current_Usage_Male_Sterilization_Urban
	"360": {},	# NN_Current_Usage_Copper_T_Iud_Total
	"361": {},	# NN_Current_Usage_Copper_T_Iud_Rural
	"362": {},	# NN_Current_Usage_Copper_T_Iud_Urban
	"363": {},	# NN_Current_Usage_Pills_Total
	"364": {},	# NN_Current_Usage_Pills_Rural
	"365": {},	# NN_Current_Usage_Pills_Urban
	"366": {},	# NN_Current_Usage_Condom_Nirodh_Total
	"367": {},	# NN_Current_Usage_Condom_Nirodh_Rural
	"368": {},	# NN_Current_Usage_Condom_Nirodh_Urban
	"369": {},	# NN_Current_Usage_Emergency_Contraceptive_Pills_Total
	"370": {},	# NN_Current_Usage_Emergency_Contraceptive_Pills_Rural
	"371": {},	# NN_Current_Usage_Emergency_Contraceptive_Pills_Urban
	"372": {},	# NN_Current_Usage_Any_Traditional_Method_Total
	"373": {},	# NN_Current_Usage_Any_Traditional_Method_Rural
	"374": {},	# NN_Current_Usage_Any_Traditional_Method_Urban
	"375": {},	# NN_Current_Usage_Periodic_Abstinence_Total
	"376": {},	# NN_Current_Usage_Periodic_Abstinence_Rural
	"377": {},	# NN_Current_Usage_Periodic_Abstinence_Urban
	"378": {},	# NN_Current_Usage_Withdrawal_Total
	"379": {},	# NN_Current_Usage_Withdrawal_Rural
	"380": {},	# NN_Current_Usage_Withdrawal_Urban
	"381": {},	# NN_Current_Usage_Lam_Total
	"382": {},	# NN_Current_Usage_Lam_Rural
	"383": {},	# NN_Current_Usage_Lam_Urban
	"384": {},	# OO_Unmet_Need_For_Spacing_Total
	"385": {},	# OO_Unmet_Need_For_Spacing_Rural
	"386": {},	# OO_Unmet_Need_For_Spacing_Urban
	"387": {},	# OO_Unmet_Need_For_Limiting_Total
	"388": {},	# OO_Unmet_Need_For_Limiting_Rural
	"389": {},	# OO_Unmet_Need_For_Limiting_Urban
	"390": {},	# OO_Total_Unmet_Need_Total
	"391": {},	# OO_Total_Unmet_Need_Rural
	"392": {},	# OO_Total_Unmet_Need_Urban
	"393": {},	# PP_Currently_Married_Pregnant_Women_Aged_15_49_Years_Registered_For_Anc_Total
	"394": {},	# PP_Currently_Married_Pregnant_Women_Aged_15_49_Years_Registered_For_Anc_Rural
	"395": {},	# PP_Currently_Married_Pregnant_Women_Aged_15_49_Years_Registered_For_Anc_Urban
	"396": {},	# PP_Mothers_Who_Received_Any_Antenatal_Check_Up_Total
	"397": {},	# PP_Mothers_Who_Received_Any_Antenatal_Check_Up_Rural
	"398": {},	# PP_Mothers_Who_Received_Any_Antenatal_Check_Up_Urban
	"399": {},	# PP_Mothers_Who_Had_Antenatal_Check_Up_In_First_Trimester_Total
	"400": {},	# PP_Mothers_Who_Had_Antenatal_Check_Up_In_First_Trimester_Rural
	"401": {},	# PP_Mothers_Who_Had_Antenatal_Check_Up_In_First_Trimester_Urban
	"402": {},	# PP_Mothers_Who_Received_3_Or_More_Antenatal_Care_Total
	"403": {},	# PP_Mothers_Who_Received_3_Or_More_Antenatal_Care_Rural
	"404": {},	# PP_Mothers_Who_Received_3_Or_More_Antenatal_Care_Urban
	"405": {},	# PP_Mothers_Who_Received_At_Least_One_Tetanus_Toxoid_Tt_Injection_Total
	"406": {},	# PP_Mothers_Who_Received_At_Least_One_Tetanus_Toxoid_Tt_Injection_Rural
	"407": {},	# PP_Mothers_Who_Received_At_Least_One_Tetanus_Toxoid_Tt_Injection_Urban
	"408": {},	# PP_Mothers_Who_Consumed_Ifa_For_100_Days_Or_More_Total
	"409": {},	# PP_Mothers_Who_Consumed_Ifa_For_100_Days_Or_More_Rural
	"410": {},	# PP_Mothers_Who_Consumed_Ifa_For_100_Days_Or_More_Urban
	"411": {},	# PP_Mothers_Who_Had_Full_Antenatal_Check_Up_Total
	"412": {},	# PP_Mothers_Who_Had_Full_Antenatal_Check_Up_Rural
	"413": {},	# PP_Mothers_Who_Had_Full_Antenatal_Check_Up_Urban
	"414": {},	# PP_Mothers_Who_Received_Anc_From_Govt_Source_Total
	"415": {},	# PP_Mothers_Who_Received_Anc_From_Govt_Source_Rural
	"416": {},	# PP_Mothers_Who_Received_Anc_From_Govt_Source_Urban
	"417": {},	# PP_Mothers_Whose_Blood_Pressure_Bp_Taken_Total
	"418": {},	# PP_Mothers_Whose_Blood_Pressure_Bp_Taken_Rural
	"419": {},	# PP_Mothers_Whose_Blood_Pressure_Bp_Taken_Urban
	"420": {},	# PP_Mothers_Whose_Blood_Taken_For_Hb_Total
	"421": {},	# PP_Mothers_Whose_Blood_Taken_For_Hb_Rural
	"422": {},	# PP_Mothers_Whose_Blood_Taken_For_Hb_Urban
	"423": {},	# PP_Mothers_Who_Underwent_Ultrasound_Total
	"424": {},	# PP_Mothers_Who_Underwent_Ultrasound_Rural
	"425": {},	# PP_Mothers_Who_Underwent_Ultrasound_Urban
	"426": {},	# QQ_Institutional_Delivery_Total
	"427": {},	# QQ_Institutional_Delivery_Rural
	"428": {},	# QQ_Institutional_Delivery_Urban
	"429": {},	# QQ_Delivery_At_Government_Institution_Total
	"430": {},	# QQ_Delivery_At_Government_Institution_Rural
	"431": {},	# QQ_Delivery_At_Government_Institution_Urban
	"432": {},	# QQ_Delivery_At_Private_Institution_Total
	"433": {},	# QQ_Delivery_At_Private_Institution_Rural
	"434": {},	# QQ_Delivery_At_Private_Institution_Urban
	"435": {},	# QQ_Delivery_At_Home_Total
	"436": {},	# QQ_Delivery_At_Home_Rural
	"437": {},	# QQ_Delivery_At_Home_Urban
	"438": {},	# QQ_Delivery_At_Home_Conducted_By_Skilled_Health_Personnel_Total
	"439": {},	# QQ_Delivery_At_Home_Conducted_By_Skilled_Health_Personnel_Rural
	"440": {},	# QQ_Delivery_At_Home_Conducted_By_Skilled_Health_Personnel_Urban
	"441": {},	# QQ_Safe_Delivery_Total
	"442": {},	# QQ_Safe_Delivery_Rural
	"443": {},	# QQ_Safe_Delivery_Urban
	"444": {},	# QQ_Caesarean_Out_Of_Total_Delivery_Taken_Place_In_Government_Institutions_Total
	"445": {},	# QQ_Caesarean_Out_Of_Total_Delivery_Taken_Place_In_Government_Institutions_Rural
	"446": {},	# QQ_Caesarean_Out_Of_Total_Delivery_Taken_Place_In_Government_Institutions_Urban
	"447": {},	# QQ_Caesarean_Out_Of_Total_Delivery_Taken_Place_In_Private_Institutions_Total
	"448": {},	# QQ_Caesarean_Out_Of_Total_Delivery_Taken_Place_In_Private_Institutions_Rural
	"449": {},	# QQ_Caesarean_Out_Of_Total_Delivery_Taken_Place_In_Private_Institutions_Urban
	"450": {},	# RR_Less_Than_24_Hrs_Stay_In_Institution_After_Delivery_Total
	"451": {},	# RR_Less_Than_24_Hrs_Stay_In_Institution_After_Delivery_Rural
	"452": {},	# RR_Less_Than_24_Hrs_Stay_In_Institution_After_Delivery_Urban
	"453": {},	# RR_Mothers_Who_Received_Post_Natal_Check_Up_Within_48_Hrs_Of_Delivery_Total
	"454": {},	# RR_Mothers_Who_Received_Post_Natal_Check_Up_Within_48_Hrs_Of_Delivery_Rural
	"455": {},	# RR_Mothers_Who_Received_Post_Natal_Check_Up_Within_48_Hrs_Of_Delivery_Urban
	"456": {},	# RR_Mothers_Who_Received_Post_Natal_Check_Up_Within_1_Week_Of_Delivery_Total
	"457": {},	# RR_Mothers_Who_Received_Post_Natal_Check_Up_Within_1_Week_Of_Delivery_Rural
	"458": {},	# RR_Mothers_Who_Received_Post_Natal_Check_Up_Within_1_Week_Of_Delivery_Urban
	"459": {},	# RR_Mothers_Who_Did_Not_Receive_Any_Post_Natal_Check_Up_Total
	"460": {},	# RR_Mothers_Who_Did_Not_Receive_Any_Post_Natal_Check_Up_Rural
	"461": {},	# RR_Mothers_Who_Did_Not_Receive_Any_Post_Natal_Check_Up_Urban
	"462": {},	# RR_New_Borns_Who_Were_Checked_Up_Within_24_Hrs_Of_Birth_Total
	"463": {},	# RR_New_Borns_Who_Were_Checked_Up_Within_24_Hrs_Of_Birth_Rural
	"464": {},	# RR_New_Borns_Who_Were_Checked_Up_Within_24_Hrs_Of_Birth_Urban
	"465": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Delivery_Under_Jsy_Total
	"466": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Delivery_Under_Jsy_Rural
	"467": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Delivery_Under_Jsy_Urban
	"468": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Institutional_Delivery_Under_Jsy_Total
	"469": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Institutional_Delivery_Under_Jsy_Rural
	"470": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Institutional_Delivery_Under_Jsy_Urban
	"471": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Government_Institutional_Delivery_Under_Jsy_Total
	"472": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Government_Institutional_Delivery_Under_Jsy_Rural
	"473": {},	# SS_Mothers_Who_Availed_Financial_Assistance_For_Government_Institutional_Delivery_Under_Jsy_Urban
	"474": {},	# TT_Children_Aged_12_23_Months_Having_Immunization_Card_Total
	"475": {},	# TT_Children_Aged_12_23_Months_Having_Immunization_Card_Rural
	"476": {},	# TT_Children_Aged_12_23_Months_Having_Immunization_Card_Urban
	"477": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_Bcg_Total
	"478": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_Bcg_Rural
	"479": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_Bcg_Urban
	"480": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Polio_Vaccine_Total
	"481": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Polio_Vaccine_Rural
	"482": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Polio_Vaccine_Urban
	"483": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Dpt_Vaccine_Total
	"484": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Dpt_Vaccine_Rural
	"485": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Dpt_Vaccine_Urban
	"486": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_Measles_Vaccine_Total
	"487": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_Measles_Vaccine_Rural
	"488": {},	# TT_Children_Aged_12_23_Months_Who_Have_Received_Measles_Vaccine_Urban
	"489": {},	# TT_Children_Aged_12_23_Months_Fully_Immunized_Total
	"490": {},	# TT_Children_Aged_12_23_Months_Fully_Immunized_Rural
	"491": {},	# TT_Children_Aged_12_23_Months_Fully_Immunized_Urban
	"492": {},	# TT_Children_Who_Have_Received_Polio_Dose_At_Birth_Total
	"493": {},	# TT_Children_Who_Have_Received_Polio_Dose_At_Birth_Rural
	"494": {},	# TT_Children_Who_Have_Received_Polio_Dose_At_Birth_Urban
	"495": {},	# TT_Children_Who_Did_Not_Receive_Any_Vaccination_Total
	"496": {},	# TT_Children_Who_Did_Not_Receive_Any_Vaccination_Rural
	"497": {},	# TT_Children_Who_Did_Not_Receive_Any_Vaccination_Urban
	"498": {},	# TT_Children_Aged_6_35_Months_Who_Received_At_Least_One_Vitamin_A_Dose_During_Last_Six_Months_Total
	"499": {},	# TT_Children_Aged_6_35_Months_Who_Received_At_Least_One_Vitamin_A_Dose_During_Last_Six_Months_Rural
	"500": {},	# TT_Children_Aged_6_35_Months_Who_Received_At_Least_One_Vitamin_A_Dose_During_Last_Six_Months_Urban
	"501": {},	# TT_Children_Aged_6_35_Months_Who_Received_Ifa_Tablets_Syrup_During_Last_3_Months_Total
	"502": {},	# TT_Children_Aged_6_35_Months_Who_Received_Ifa_Tablets_Syrup_During_Last_3_Months_Rural
	"503": {},	# TT_Children_Aged_6_35_Months_Who_Received_Ifa_Tablets_Syrup_During_Last_3_Months_Urban
	"504": {},	# TT_Children_Whose_Birth_Weight_Was_Taken_Total
	"505": {},	# TT_Children_Whose_Birth_Weight_Was_Taken_Rural
	"506": {},	# TT_Children_Whose_Birth_Weight_Was_Taken_Urban
	"507": {},	# TT_Children_With_Birth_Weight_Less_Than_2_5_Kg_Total
	"508": {},	# TT_Children_With_Birth_Weight_Less_Than_2_5_Kg_Rural
	"509": {},	# TT_Children_With_Birth_Weight_Less_Than_2_5_Kg_Urban
	"510": {},	# UU_Children_Suffering_From_Diarrhoea_Total
	"511": {},	# UU_Children_Suffering_From_Diarrhoea_Rural
	"512": {},	# UU_Children_Suffering_From_Diarrhoea_Urban
	"513": {},	# UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Total
	"514": {},	# UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Rural
	"515": {},	# UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Urban
	"516": {},	# UU_Children_Suffering_From_Acute_Respiratory_Infection_Total
	"517": {},	# UU_Children_Suffering_From_Acute_Respiratory_Infection_Rural
	"518": {},	# UU_Children_Suffering_From_Acute_Respiratory_Infection_Urban
	"519": {},	# UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Total
	"520": {},	# UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Rural
	"521": {},	# UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Urban
	"522": {},	# UU_Children_Suffering_From_Fever_Total
	"523": {},	# UU_Children_Suffering_From_Fever_Rural
	"524": {},	# UU_Children_Suffering_From_Fever_Urban
	"525": {},	# UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Total
	"526": {},	# UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Rural
	"527": {},	# UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Urban
	"528": {},	# VV_Children_Breastfed_Within_One_Hour_Of_Birth_Total
	"529": {},	# VV_Children_Breastfed_Within_One_Hour_Of_Birth_Rural
	"530": {},	# VV_Children_Breastfed_Within_One_Hour_Of_Birth_Urban
	"531": {},	# VV_Children_Aged_6_35_Months_Exclusively_Breastfed_For_At_Least_Six_Months_Total
	"532": {},	# VV_Children_Aged_6_35_Months_Exclusively_Breastfed_For_At_Least_Six_Months_Rural
	"533": {},	# VV_Children_Aged_6_35_Months_Exclusively_Breastfed_For_At_Least_Six_Months_Urban
	"534": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Water_Total
	"535": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Water_Rural
	"536": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Water_Urban
	"537": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Animal_Formula_Milk_Total
	"538": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Animal_Formula_Milk_Rural
	"539": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Animal_Formula_Milk_Urban
	"540": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Semi_Solid_Mashed_Food_Total
	"541": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Semi_Solid_Mashed_Food_Rural
	"542": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Semi_Solid_Mashed_Food_Urban
	"543": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Solid_Adult_Food_Total
	"544": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Solid_Adult_Food_Rural
	"545": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Solid_Adult_Food_Urban
	"546": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Vegetables_Fruits_Total
	"547": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Vegetables_Fruits_Rural
	"548": {},	# VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Vegetables_Fruits_Urban
	"549": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Water_Total
	"550": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Water_Rural
	"551": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Water_Urban
	"552": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Animal_Formula_Milk_Total
	"553": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Animal_Formula_Milk_Rural
	"554": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Animal_Formula_Milk_Urban
	"555": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Semi_Solid_Mashed_Food_Total
	"556": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Semi_Solid_Mashed_Food_Rural
	"557": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Semi_Solid_Mashed_Food_Urban
	"558": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Solid_Adult_Food_Total
	"559": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Solid_Adult_Food_Rural
	"560": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Solid_Adult_Food_Urban
	"561": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Vegetables_Fruits_Total
	"562": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Vegetables_Fruits_Rural
	"563": {},	# VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Vegetables_Fruits_Urban
	"564": {},	# WW_Birth_Registered_Total
	"565": {},	# WW_Birth_Registered_Rural
	"566": {},	# WW_Birth_Registered_Urban
	"567": {},	# WW_Children_Whose_Birth_Was_Registered_And_Received_Birth_Certificate_Total
	"568": {},	# WW_Children_Whose_Birth_Was_Registered_And_Received_Birth_Certificate_Rural
	"569": {},	# WW_Children_Whose_Birth_Was_Registered_And_Received_Birth_Certificate_Urban
	"570": {},	# XX_Women_Who_Are_Aware_Of_Hiv_Aids_Total
	"571": {},	# XX_Women_Who_Are_Aware_Of_Hiv_Aids_Rural
	"572": {},	# XX_Women_Who_Are_Aware_Of_Hiv_Aids_Urban
	"573": {},	# XX_Women_Who_Are_Aware_Of_Rti_Sti_Total
	"574": {},	# XX_Women_Who_Are_Aware_Of_Rti_Sti_Rural
	"575": {},	# XX_Women_Who_Are_Aware_Of_Rti_Sti_Urban
	"576": {},	# XX_Women_Who_Are_Aware_Of_Haf_Ors_Ort_Zinc_Total
	"577": {},	# XX_Women_Who_Are_Aware_Of_Haf_Ors_Ort_Zinc_Rural
	"578": {},	# XX_Women_Who_Are_Aware_Of_Haf_Ors_Ort_Zinc_Urban
	"579": {},	# XX_Women_Who_Are_Aware_Of_Danger_Signs_Of_Ari_Pneumonia_Total
	"580": {},	# XX_Women_Who_Are_Aware_Of_Danger_Signs_Of_Ari_Pneumonia_Rural
	"581": {},	# XX_Women_Who_Are_Aware_Of_Danger_Signs_Of_Ari_Pneumonia_Urban
	"582": {},	# YY_Crude_Death_Rate_Cdr_Total_Person
	"583": {},	# YY_Crude_Death_Rate_Cdr_Total_Male
	"584": {},	# YY_Crude_Death_Rate_Cdr_Total_Female
	"585": {},	# YY_Crude_Death_Rate_Cdr_Rural_Person
	"586": {},	# YY_Crude_Death_Rate_Cdr_Rural_Male
	"587": {},	# YY_Crude_Death_Rate_Cdr_Rural_Female
	"588": {},	# YY_Crude_Death_Rate_Cdr_Urban_Person
	"589": {},	# YY_Crude_Death_Rate_Cdr_Urban_Male
	"590": {},	# YY_Crude_Death_Rate_Cdr_Urban_Female
	"591": {},	# YY_Infant_Mortality_Rate_Imr_Total_Person
	"592": {},	# YY_Infant_Mortality_Rate_Imr_Total_Male
	"593": {},	# YY_Infant_Mortality_Rate_Imr_Total_Female
	"594": {},	# YY_Infant_Mortality_Rate_Imr_Rural_Person
	"595": {},	# YY_Infant_Mortality_Rate_Imr_Rural_Male
	"596": {},	# YY_Infant_Mortality_Rate_Imr_Rural_Female
	"597": {},	# YY_Infant_Mortality_Rate_Imr_Urban_Person
	"598": {},	# YY_Infant_Mortality_Rate_Imr_Urban_Male
	"599": {},	# YY_Infant_Mortality_Rate_Imr_Urban_Female
	"600": {},	# YY_Neo_Natal_Mortality_Rate_Total
	"601": {},	# YY_Neo_Natal_Mortality_Rate_Rural
	"602": {},	# YY_Neo_Natal_Mortality_Rate_Urban
	"603": {},	# YY_Post_Neo_Natal_Mortality_Rate_Total
	"604": {},	# YY_Post_Neo_Natal_Mortality_Rate_Rural
	"605": {},	# YY_Post_Neo_Natal_Mortality_Rate_Urban
	"606": {},	# YY_Under_Five_Mortality_Rate_U5MR_Total_Person
	"607": {},	# YY_Under_Five_Mortality_Rate_U5MR_Total_Male
	"608": {},	# YY_Under_Five_Mortality_Rate_U5MR_Total_Female
	"609": {},	# YY_Under_Five_Mortality_Rate_U5MR_Rural_Person
	"610": {},	# YY_Under_Five_Mortality_Rate_U5MR_Rural_Male
	"611": {},	# YY_Under_Five_Mortality_Rate_U5MR_Rural_Female
	"612": {},	# YY_Under_Five_Mortality_Rate_U5MR_Urban_Person
	"613": {},	# YY_Under_Five_Mortality_Rate_U5MR_Urban_Male
	"614": {},	# YY_Under_Five_Mortality_Rate_U5MR_Urban_Female
	"615": {},	# ZZ_Crude_Birth_Rate_Total_Lower_Limit
	"616": {},	# ZZ_Crude_Birth_Rate_Total_Upper_Limit
	"617": {},	# ZZ_Crude_Birth_Rate_Rural_Lower_Limit
	"618": {},	# ZZ_Crude_Birth_Rate_Rural_Upper_Limit
	"619": {},	# ZZ_Crude_Birth_Rate_Urban_Lower_Limit
	"620": {},	# ZZ_Crude_Birth_Rate_Urban_Upper_Limit
	"621": {},	# ZZ_Crude_Death_Rate_Total_Lower_Limit
	"622": {},	# ZZ_Crude_Death_Rate_Total_Upper_Limit
	"623": {},	# ZZ_Crude_Death_Rate_Rural_Lower_Limit
	"624": {},	# ZZ_Crude_Death_Rate_Rural_Upper_Limit
	"625": {},	# ZZ_Crude_Death_Rate_Urban_Lower_Limit
	"626": {},	# ZZ_Crude_Death_Rate_Urban_Upper_Limit
	"627": {},	# ZZ_Infant_Mortality_Rate_Total_Lower_Limit
	"628": {},	# ZZ_Infant_Mortality_Rate_Total_Upper_Limit
	"629": {},	# ZZ_Infant_Mortality_Rate_Rural_Lower_Limit
	"630": {},	# ZZ_Infant_Mortality_Rate_Rural_Upper_Limit
	"631": {},	# ZZ_Infant_Mortality_Rate_Urban_Lower_Limit
	"632": {},	# ZZ_Infant_Mortality_Rate_Urban_Upper_Limit
	"633": {},	# ZZ_Under_Five_Mortality_Rate_U5MR_Total_Lower_Limit
	"634": {},	# ZZ_Under_Five_Mortality_Rate_U5MR_Total_Upper_Limit
	"635": {},	# ZZ_Under_Five_Mortality_Rate_U5MR_Rural_Lower_Limit
	"636": {},	# ZZ_Under_Five_Mortality_Rate_U5MR_Rural_Upper_Limit
	"637": {},	# ZZ_Under_Five_Mortality_Rate_U5MR_Urban_Lower_Limit
	"638": {},	# ZZ_Under_Five_Mortality_Rate_U5MR_Urban_Upper_Limit
	"639": {},	# ZZ_Sex_Ratio_At_Birth_Total_Lower_Limit
	"640": {},	# ZZ_Sex_Ratio_At_Birth_Total_Upper_Limit
	"641": {},	# ZZ_Sex_Ratio_At_Birth_Rural_Lower_Limit
	"642": {},	# ZZ_Sex_Ratio_At_Birth_Rural_Upper_Limit
	"643": {},	# ZZ_Sex_Ratio_At_Birth_Urban_Lower_Limit
	"644": {},	# ZZ_Sex_Ratio_At_Birth_Urban_Upper_Limit
}

entityIndex = [
				# 9,10,11,
				# 18,19,20,
				30,31,32,
				# 33,34,35
				]
attributesIndex = [
					# 9,10,11,
					# 18,19,20,
					30,31,32,
					# 33,34,35
					]

# Loading Data
print ("Data Loading Started"), 
with open ('./HealthIndicatorONE.csv') as csvdata: 
	readCSV = csv.reader (csvdata, delimiter=',')
	next (readCSV)	# Skipping Header content
	for row in readCSV: 
		for i in entityIndex: 
			if (row[i] in Attributes[str (i)]) == False: 
				Attributes[str (i)][row[i]] = len (Attributes[str (i)].keys())
		datarow = []
		try: 
			for i in attributesIndex: 
				datarow.append (Attributes[str (i)][row[i]])
			dataAttributes.append (datarow)
		except ValueError: 
			pass
print ("Done Loading Data\n")

feats = [
		# "AA_Population_Total",
		# "AA_Population_Rural",
		# "AA_Population_Urban",
		# "AA_Children_12_23_Months_Total",
		# "AA_Children_12_23_Months_Rural",
		# "AA_Children_12_23_Months_Urban",
		"BB_Population_Below_Age_15_Years_Total",
		"BB_Population_Below_Age_15_Years_Rural",
		"BB_Population_Below_Age_15_Years_Urban",
		# "BB_Dependency_Ratio_Total",
		# "BB_Dependency_Ratio_Rural",
		# "BB_Dependency_Ratio_Urban"
		]

dataframe = pandas.DataFrame (dataAttributes)
print ("\n\nFeatures: ", feats)
print ("Means")
print (dataframe.mean())

print ("Features: ", feats)
print ("\n\nMedian")
print (dataframe.median())

print ("\n\nFeatures: ", feats)
print ("Mode")
print (dataframe.mode())

print ("\n\nFeatures: ", feats)
print ("Standard Deviation")
print (dataframe.std())

print ("\n\nFeatures: ", feats)
print ("Lower Limit")
print (dataframe.min())
print ("Upper Limit")
print (dataframe.max())

print ("\n\nFeatures: ", feats)
print ("Complete Description")
print (dataframe.describe())

dataframe.plot()
plt.show()

dataframe.plot.bar()
plt.show()

dataframe.plot.hist(bins=50)
plt.show()

dataframe.plot.hist()
plt.show()

dataframe.plot.area(stacked=False)
plt.show()

dataframe.plot.box()
plt.show()

# dataframe.plot.pie(x=0, y=1)
# plt.show()

dataframe.plot.scatter(x=0, y=1)
plt.show()
dataframe.plot.scatter(x=0, y=2)
plt.show()
dataframe.plot.scatter(x=1, y=2)
plt.show()