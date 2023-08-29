#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[48]:


data=pd.read_csv(r"C:\Users\pf3l1\Downloads\ipl.py")


# In[49]:


data.tail(20)


# In[50]:


data.shape


# In[51]:


data.isnull().sum()


# In[52]:


data.describe()


# In[53]:


data.info()


# In[99]:


batters=data.loc[(data['Player_Type']=='Batter')]
batters_new=batters.loc[(batters['Capped']==1)]
capped_batters=batters_new[['Player Name','Team','Nationality','Matches_Played','Runs','Average','Strike_Rate']]
capped_batters.head(10)


# In[115]:


bowlers=data.loc[(data['Player_Type']=='Bowler ')]
bowlers_new=bowlers.loc[(bowlers['Capped']==1)]
capped_bowlers=bowlers_new[['Player Name','Team','Nationality','Matches_Played','Wickets','Economy','Bowling_average','Bowling_Strike_Rate']].reset_index()
capped_bowlers.drop('index',axis=1,inplace=True)
capped_bowlers.head(15)


# In[88]:


keepers=data.loc[(data['Player_Type']=='Keeper')]
keepers_new=keepers.loc[(keepers['Capped']==1)]
keepers_batters=keepers_new[['Player Name','Team','Nationality','Matches_Played','Runs','Average','Strike_Rate','Catches','Run_outs','Stumps']]
keepers_batters.head(15)


# In[92]:


allr=data.loc[(data['Player_Type']=='Allrounder')]
allr_new=allr.loc[(allr['Capped']==1)]
capped_allr=allr_new[['Player Name','Team','Nationality','Matches_Played','Runs','Average','Strike_Rate','Wickets','Bowling_average','Bowling_Strike_Rate','Economy']]
capped_allr.head(15)


# In[93]:


capped_batters=capped_batters.fillna(0)
capped_bowlers=capped_bowlers.fillna(0)
capped_allr=capped_allr.fillna(0)
keepers_batters=keepers_batters.fillna(0)


# In[94]:


keepers_batters.isna().sum()


# In[109]:


top_batters=capped_batters.loc[(capped_batters["Average"]>=32.0)]
#sorting
top_batters_average=top_batters.sort_values('Average',ascending=False)
top_batters_strikerate=top_batters.sort_values('Strike_Rate',ascending=False)
top_batters_runs=top_batters.sort_values('Runs',ascending=False)
top_batters_Matches_Played=top_batters.sort_values('Matches_Played',ascending=False)


# In[110]:


top_batters_average


# In[111]:


top_batters_strikerate


# In[112]:


top_batters_runs


# In[113]:


top_batters_Matches_Played


#  from analysis top batters are
#  1.david warner
#  2.kl rahul
#  3.virat kohli
#  4.

# In[216]:


top_bowlers=capped_bowlers.loc[(capped_bowlers["Bowling_average"]<=26.0)]
#sorting
top_bowlers_average=top_bowlers.sort_values('Bowling_average')
top_bowlers_strikerate=top_bowlers.sort_values('Bowling_Strike_Rate')
top_bowlers_wickets=top_bowlers.sort_values('Wickets',ascending=False)
top_bowlers_Matches_Played=top_bowlers.sort_values('Matches_Played',ascending=False)
top_bowlers_Economy=top_bowlers.sort_values('Economy')


# In[214]:


top_bowlers_average


# In[217]:


top_bowlers_strikerate


# In[218]:


top_bowlers_wickets


# In[219]:


top_bowlers_Matches_Played


# In[220]:


top_bowlers_Economy


# top bowlers
# 1.bumrah
# 2.kagiso rabada
# 3.yuzi chahal
# 4.bhuvneshwar kumar

# In[139]:


top_allrounders=capped_allr.loc[(capped_allr["Strike_Rate"]>=130 )]


# In[140]:


top_allrounders=capped_allr.loc[(capped_allr['Wickets']>=70)]


# In[141]:


top_allrounders


# In[143]:


#sorting
top_allr_average=top_allrounders.sort_values('Average',ascending=False)
top_allr_Strike_Rate=top_allrounders.sort_values('Strike_Rate',ascending=False)
top_allr_Runs=top_allrounders.sort_values('Runs',ascending=False)
top_allr_Matches=top_allrounders.sort_values('Matches_Played',ascending=False)
top_allr_Bowling_average=top_allrounders.sort_values('Bowling_average')
top_allr_Bowling_Strike_Rate=top_allrounders.sort_values('Bowling_Strike_Rate')
top_allr_Wickets=top_allrounders.sort_values('Wickets',ascending=False)
top_allr_Economy=top_allrounders.sort_values('Economy')



# In[146]:


(top_allr_average)


# In[147]:


top_allr_Strike_Rate


# In[148]:


top_allr_Runs


# In[149]:


top_allr_Matches


# In[150]:


top_allr_Bowling_average


# In[151]:


top_allr_Bowling_Strike_Rate


# In[152]:


top_allr_Wickets


# In[153]:


top_allr_Economy


# top allrounders
# 1.andre russell
# 2.Jadeja
# 3.Rashid khan
# 4.bravo
# 

# In[160]:


top_keepers=keepers_batters.loc[(keepers_batters['Average']>=25.0)]
#sorting
top_keepers_average=top_keepers.sort_values('Average',ascending=False)
top_keepers_runs=top_keepers.sort_values('Runs',ascending=False)
top_keepers_Matches_Played=top_keepers.sort_values('Matches_Played',ascending=False)
top_keepers_Strike_Rate=top_keepers.sort_values('Strike_Rate',ascending=False)
top_keepers_Catches=top_keepers.sort_values('Catches',ascending=False)
top_keepers_Run_outs=top_keepers.sort_values('Run_outs',ascending=False)
top_keepers_Stumps=top_keepers.sort_values('Stumps',ascending=False)



# In[161]:


top_keepers_average


# In[162]:


top_keepers_runs


# In[163]:


top_keepers_Matches_Played


# In[164]:


top_keepers_Strike_Rate


# In[165]:


top_keepers_Catches


# In[167]:


top_keepers_Run_outs


# In[168]:


top_keepers_Stumps


# top wicketkeepers:
# 1.MS dhoni
# 2.rishabh pant
# 3.dinesh karthik

# # batters visulisation
# 

# In[176]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Strike_Rate',data=top_batters)
plt.title("players vs strike rate")
plt.xticks(rotation=45)


# In[178]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Runs',data=top_batters)
plt.title("players vs runs")
plt.xticks(rotation=45)


# In[179]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Average',data=top_batters)
plt.title("players vs average")
plt.xticks(rotation=45)


# In[182]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Matches_Played',data=top_batters)
plt.title("players vs matches_played")
plt.xticks(rotation=45)


# # bowlers visualisation

# In[185]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Wickets',data=top_bowlers)
plt.title("players vs wickets")
plt.xticks(rotation=45)


# In[190]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Bowling_average',data=top_bowlers)
plt.title("players vs Bowling_average ")
plt.xticks(rotation=45)


# In[191]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Bowling_Strike_Rate',data=top_bowlers)
plt.title("players vs Bowling_Strike_Rate")
plt.xticks(rotation=45)


# In[192]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Economy',data=top_bowlers)
plt.title("players vs Economy")
plt.xticks(rotation=45)


# # allrounders visualisation

# In[197]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Runs',data=top_allrounders)
plt.title("players vs Runs")
plt.xticks(rotation=45)


# In[198]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Average',data=top_allrounders)
plt.title("players vs Average")
plt.xticks(rotation=45)


# In[200]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Strike_Rate',data=top_allrounders)
plt.title("players vs Strike_Rate")
plt.xticks(rotation=45)


# In[201]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Wickets',data=top_allrounders)
plt.title("players vs Wickets")
plt.xticks(rotation=45)


# # keepers visualisation

# In[204]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Runs',data=top_keepers)
plt.title("players vs Runs")
plt.xticks(rotation=45)


# In[205]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Average',data=top_keepers)
plt.title("players vs Average")
plt.xticks(rotation=45)


# In[206]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Strike_Rate',data=top_keepers)
plt.title("players vs Strike_Rate")
plt.xticks(rotation=45)


# In[207]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Catches',data=top_keepers)
plt.title("players vs Catches")
plt.xticks(rotation=45)


# In[210]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Run_outs',data=top_keepers)
plt.title("players vs Run_outs")
plt.xticks(rotation=45)


# In[212]:


plt.figure(figsize=(10,5))
sns.barplot(x='Player Name',y='Stumps',data=top_keepers)
plt.title("players vs Stumps")
plt.xticks(rotation=45)

# Forming our best 11 for the campaign based on above data analysis

#1.we will consider the two most successful ipl franchises-csk and mi
#2.Mumbai indians squad consist of- 3 Batters , 3 Allrounders , 4 Bowlers ,1 Wicketkeeper
#3.Chennai super kings squad consist of- 4 Batters , 3 Allrounders , 3 Bowlers , 1 Wicketkeeper
#4.for our final analysis we will consider the ratio :
 #  1.4 Batters
 #  2.3 Allrounders with two spin options
  # 3.3 Bowlers with one spin option
  # 4.1 wicketkeeper

#5.the team should consist maximum of 4 overseas players 

   
# In[238]:


#Batters for final 11 - Kl Rahul , david warner ,virat kohli
top_batters.reset_index(drop=True,inplace=True)
matches_values=[top_batters.iloc[6]['Matches_Played'],top_batters.iloc[2]['Matches_Played'],top_batters.iloc[5]['Matches_Played'],top_batters.iloc[4]['Matches_Played']]
runs_values=[top_batters.iloc[6]['Runs'],top_batters.iloc[2]['Runs'],top_batters.iloc[5]['Runs'],top_batters.iloc[4]['Runs']]
average_values=[top_batters.iloc[6]['Average'],top_batters.iloc[2]['Average'],top_batters.iloc[5]['Average'],top_batters.iloc[4]['Average']]
strike_rate_values=[top_batters.iloc[6]['Strike_Rate'],top_batters.iloc[2]['Strike_Rate'],top_batters.iloc[5]['Strike_Rate'],top_batters.iloc[4]['Strike_Rate']]
labels=['KL Rahul','David Warner','Virat Kohli','Kane williamson']
fig,axes=plt.subplots(2,2,figsize=(10,10))

axes[0][0].set_title('Matches played')
axes[0][1].set_title('Runs in ipl carrer')
axes[1][0].set_title('Strike rate')
axes[1][1].set_title('Average')
sns.barplot(x=labels,y=matches_values,ax=axes[0][0])
sns.barplot(x=labels,y=runs_values,ax=axes[0][1])
sns.barplot(x=labels,y=average_values,ax=axes[1][1])
sns.barplot(x=labels,y=strike_rate_values,ax=axes[1][0])






# In[247]:


#allrounders for final 11-1.Andre Russell 2.Rashid khan 3.Ravindra Jadeja
top_allrounders.reset_index(drop=True,inplace=True)
matchesa_values=[top_allrounders.iloc[3]['Matches_Played'],top_allrounders.iloc[4]['Matches_Played'],top_allrounders.iloc[5]['Matches_Played']]
runsa_values=[top_allrounders.iloc[3]['Runs'],top_allrounders.iloc[4]['Runs'],top_allrounders.iloc[5]['Runs']]
averages_values=[top_allrounders.iloc[3]['Average'],top_allrounders.iloc[4]['Average'],top_allrounders.iloc[5]['Average']]
strikes_rate_values=[top_allrounders.iloc[3]['Strike_Rate'],top_allrounders.iloc[4]['Strike_Rate'],top_allrounders.iloc[5]['Strike_Rate']]
wickets_values=[top_allrounders.iloc[3]['Wickets'],top_allrounders.iloc[4]['Wickets'],top_allrounders.iloc[5]['Wickets']]
economy_values=[top_allrounders.iloc[3]['Economy'],top_allrounders.iloc[4]['Economy'],top_allrounders.iloc[5]['Economy']]
labels=['Ravindra Jadeja','Andre Russell','Rashid khan']
fig,axes=plt.subplots(2,3,figsize=(20,10))

axes[0][0].set_title('Matches played')
axes[0][1].set_title('Runs in ipl carrer')
axes[1][0].set_title('Strike rate')
axes[1][1].set_title('Average')
axes[0][2].set_title('wickets')
axes[1][2].set_title('Economy')
sns.barplot(x=labels,y=matchesa_values,ax=axes[0][0])
sns.barplot(x=labels,y=runsa_values,ax=axes[0][1])
sns.barplot(x=labels,y=averages_values,ax=axes[1][1])
sns.barplot(x=labels,y=strikes_rate_values,ax=axes[1][0])
sns.barplot(x=labels,y=wickets_values,ax=axes[0][2])
sns.barplot(x=labels,y=economy_values,ax=axes[1][2])


# In[252]:


# bowlers for our final 11- 1.Jasprit bumrah 2.bhuvneshwar kumar 3.Yuzvendra Chahal
top_bowlers.reset_index(drop=True,inplace=True)
matchesa_values=[top_bowlers.iloc[13]['Matches_Played'],top_bowlers.iloc[1]['Matches_Played'],top_bowlers.iloc[3]['Matches_Played']]
bowling_averages_values=[top_bowlers.iloc[13]['Bowling_average'],top_bowlers.iloc[1]['Bowling_average'],top_bowlers.iloc[3]['Bowling_average']]
wickets_values=[top_bowlers.iloc[13]['Wickets'],top_bowlers.iloc[1]['Wickets'],top_bowlers.iloc[3]['Wickets']]
economy_values=[top_bowlers.iloc[13]['Economy'],top_bowlers.iloc[1]['Economy'],top_bowlers.iloc[3]['Economy']]
labels=['Jasprit bumrah','bhuvneshwar kumar','Yuzvendra Chahal']
fig,axes=plt.subplots(2,2,figsize=(20,10))

axes[0][0].set_title('Matches played')
axes[1][0].set_title('Bowling_Average')
axes[0][1].set_title('wickets')
axes[1][1].set_title('Economy')
sns.barplot(x=labels,y=matchesa_values,ax=axes[0][0])
sns.barplot(x=labels,y=bowling_averages_values,ax=axes[1][0])
sns.barplot(x=labels,y=wickets_values,ax=axes[0][1])
sns.barplot(x=labels,y=economy_values,ax=axes[1][1])


# In[255]:


top_keepers


# In[261]:


#wicket keeper for our playing 11-1.Ms dhoni 
top_keepers.reset_index(drop=True,inplace=True)
matchesa_values=[top_keepers.iloc[8]['Matches_Played'],top_keepers.iloc[4]['Matches_Played']]
averages_values=[top_keepers.iloc[8]['Average'],top_keepers.iloc[4]['Average']]
run_values=[top_keepers.iloc[8]['Runs'],top_keepers.iloc[4]['Runs']]
stumps_values=[top_keepers.iloc[8]['Stumps'],top_keepers.iloc[4]['Stumps']]
labels=['MS Dhoni','Dinesh Karthik']
fig,axes=plt.subplots(2,2,figsize=(10,10))

axes[0][0].set_title('Matches played')
axes[1][0].set_title('Average')
axes[0][1].set_title('Runs')
axes[1][1].set_title('Stumps')
sns.barplot(x=labels,y=matchesa_values,ax=axes[0][0])
sns.barplot(x=labels,y=averages_values,ax=axes[1][0])
sns.barplot(x=labels,y=run_values,ax=axes[0][1])
sns.barplot(x=labels,y=stumps_values,ax=axes[1][1])


# In[285]:


batter1= top_batters.loc[(top_batters['Player Name']=='KL Rahul ')]
batter2= top_batters.loc[(top_batters['Player Name']=='David Warner ')]
batter3= top_batters.loc[(top_batters['Player Name']=='Virat Kohli')]
batter4= top_batters.loc[(top_batters['Player Name']=='Kane Williamson')]

allrounder1= top_allrounders.loc[(top_allrounders['Player Name']=='Andre Russell')]
allrounder2= top_allrounders.loc[(top_allrounders['Player Name']=='Ravindra Jadeja ')]
allrounder3= top_allrounders.loc[(top_allrounders['Player Name']=='Rashid Khan')]

bowler1= top_bowlers.loc[(top_bowlers['Player Name']=='Jasprit Bumrah')]
bowler2= top_bowlers.loc[(top_bowlers['Player Name']=='Bhuvneshwar Kumar')]
bowler3= top_bowlers.loc[(top_bowlers['Player Name']=='Yuzvendra Chahal ')]

keeper=top_keepers.loc[(top_keepers['Player Name']=='MS Dhoni')]


# In[293]:


final=[batter1,batter2,batter3,batter4,allrounder2,keeper,allrounder1,allrounder3,bowler2,bowler1,bowler3]
final_team=pd.concat(final)
final_team=final_team.drop(labels=['Matches_Played','Runs','Average','Strike_Rate','Wickets','Bowling_average','Bowling_Strike_Rate','Economy','Catches','Run_outs','Stumps'],axis=1)
final_team.reset_index(drop=True)


# In[ ]:





# In[ ]:





# In[ ]:




