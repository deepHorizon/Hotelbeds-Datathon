# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:52:34 2017

@author: Shaurya Rawat
"""

import pandas as pd
 actbook=pd.read_csv("D:\IE MBD 2016\IE Datathon Project\Q1_Activities_Bookings.txt",sep="|")
 actbook.columns
 trfbook=pd.read_csv("D:\IE MBD 2016\IE Datathon Project\Q2_Transfers_Bookings.txt",sep="|")
 trfbook.columns
 
 actbook.columns.difference(trfbook.columns)
 actbook.columns = map(str.lower, actbook.columns)

 trfbook.columns.difference(actbook.columns)
 trfbook.columns=map(str.lower,trfbook.columns)
 
 actbook.shape
 trfbook.shape
 
 actbook.head()
 actbook.describe()
 
 #office: operating company
 # Incoming_office: internal code for company and office
 # booking: booking code, a booking is identified by incoming office and booking
 # interface: online channel- hotelbeds or bedsonline
 # interface_desc: interface description
 # client: client code
 # branch: branch code
 # country_market: country of origin of client
 # country_market_desc: country market description
 # application : has nominal values
 #                  evolution: web; 
 #                  appservices/interface: xml
 #              `   actapi: Activities api
 #                  tuiuk: irrelevant
 # sales_method: cross-selling: along with accomodation
 actbook['incoming_office'].head()
 
 #### Inspect attributes
 #company
 actbook.company.head()
 type(actbook.company)
 actbook.company.unique()
 len(actbook.company.unique()) # 23 unique operative companies
 company=actbook.company.groupby(actbook.company).count()
company.sort(ascending=False)
company # E10,U10,MX1,U02 largest
actbook.company.isnull().any()

#office
actbook.office.head()
len(actbook.office.unique()) # 120 unique values
actbook.office.isnull().any()
office=actbook.office.groupby(actbook.office).count()
office.sort(ascending=False)
office # 1,92,713 largest

#incoming_office
actbook.incoming_office.head()
len(actbook.incoming_office.unique()) # 148 unique offices
actbook.incoming_office.isnull().any()
incoming_office=actbook.incoming_office.groupby(actbook.incoming_office).count()
incoming_office.sort_values(inplace=True,ascending=False)
incoming_office # 235,102,207,197 largest

#booking
actbook.booking.head()
actbook.booking.isnull().any()
len(actbook.booking.unique()) #421299
actbook.booking.groupby(actbook.booking).count()

#interface
actbook.interface.head()
actbook.interface.isnull().any()
len(actbook.interface.unique()) # 36 interfaces
interfaces=actbook.interface.groupby(actbook.interface).count()
interfaces.sort_values(inplace=True,ascending=False)
interfaces # H and E largest

#interface_desc
actbook.interface_desc.head()
actbook.interface_desc.isnull().any()
actbook.interface_desc.unique()
# H: hotelbeds touroperacion, E: Bedsonline Espana
actbook.interface,actbook.interface_desc
interface_desc=actbook.interface_desc.groupby(actbook.interface_desc).count()
interface_desc.sort_values(inplace=True,ascending=False)
interface_desc # Same as interface

#client
actbook.client.head()
actbook.client.isnull().any()
len(actbook.client.unique()) # 15546 unique clients
clients=actbook.client.groupby(actbook.client).count()
clients.sort_values(inplace=True,ascending=False)
clients.head() # 2347,29082,39320 are some of the biggest clients

####branch
actbook.branch.head()
actbook.branch.isnull().any()
len(actbook.branch.unique()) # 2202 unique branches
branches=actbook.branch.groupby(actbook.branch).count()
branches.sort_values(inplace=True,ascending=False)
branches.head() # 1 is significantly larger 0 and 2 follow

####country_market
actbook.country_market.head()
actbook.country_market.isnull().any()
actbook.country_market.mode()
# this attribute has null values
# ES is the most occuring value, so it's likely the client may be from ES. we replace with ES
actbook.country_market=actbook.country_market.fillna('ES')
actbook.country_market.isnull().any() #False
len(actbook.country_market.unique()) # 122 countries
countries=actbook.country_market.groupby(actbook.country_market).count()
countries.sort_values(inplace=True,ascending=False)
countries.head() # ES,MX,UK leading

#country_market_desc
actbook.country_market_desc.head()
# its the same as country_market. we dont need this attribute. we might eliminate it

#### application
actbook.application.head()
actbook.application.isnull().any()
actbook.application.unique()
# categorical variables
# we'll convert this variable into the ones described in the excel sheet
actbook.application=actbook.application.map({'EVOLUTION':'web','BOL':'web','APPSERVICES':'xml','HBEDS':'web','TUIUK-WEB':'irrelevant','INTERFACE_XML_C2':'xml','ACTAPI':'activities_api'})
actbook.application.unique()
actbook=actbook[actbook.application != 'irrelevant']
# we drop the rows with irrelevant rows with tuiuk-web
actbook.application.groupby(actbook.application).count() # almost all come from "web"

#### sales_method
actbook.sales_method.head()
actbook.sales_method.unique()
actbook.sales_method.mode() #looks like most of the booking comes from cross-selling with accomodation
actbook.sales_method.groupby(actbook.sales_method).count() #cross-17440, offline=11285
actbook.sales_method.isnull().sum() #497292 too many null values
# looks like we dont need this column. might drop it

#### destination_country
actbook.destination_country.head()
actbook.destination_country.isnull().any()
actbook.destination_country.mode() # US is the most visited nation
actbook.destination_country=actbook.destination_country.fillna('US')
dest_countries=actbook.destination_country.groupby(actbook.destination_country).count()
dest_countries.sort_values(inplace=True,ascending=False)
dest_countries.head() # US most visited. then Spain

#### destination_country_desc
actbook.destination_country_desc.head()
actbook.destination_country_desc.unique()

# we dont need this attribute. might eliminate it

#### destination
actbook.destination.head()
len(actbook.destination.unique()) # 540 cities
actbook.destination.isnull().any()
destinations=actbook.destination.groupby(actbook.destination).count()
destinations.sort_values(inplace=True,ascending=False)
destinations.head() # MCO, PAR, NYC, ROE, MAD

#### destination_name
actbook.destination_name.head()
#same as the destination attribute so we might eliminate it.

#### service_order
actbook.service_order.head()
len(actbook.service_order.unique()) # 27 service orders
actbook.service_order.groupby(actbook.service_order).count()
# 1 is significantly more , then 2 and 3,4 etc.
actbook.service_order.isnull().any()

##### activity_type
actbook.activity_type.head()
actbook.activity_type.isnull().any()
actbook.activity_type.unique()
actbook.activity_type.groupby(actbook.activity_type).count() # E 

#### service
actbook.service.head()
actbook.service.isnull().any()
len(actbook.service.unique()) # 8701 unique services
services=actbook.service.groupby(actbook.service).count()
services.sort_values(inplace=True,ascending=False)
services.head() # WDWBASETTO, UNIVLATAM, 3C AM VATI, NYCITYPASS

#### service_desc
actbook.service_desc.head()
# same as the service attribute
actbook.service_desc.isnull().any() #true
actbook.service_desc.isnull().sum() # 158 missing values
actbook.service[actbook.service_desc.isnull()] 
                # we anyway dont need service description

                
#### modeality
actbook.modality.head()
actbook.modality.isnull().any()
len(actbook.modality.unique()) #6866 unique modality
modality=actbook.modality.groupby(actbook.modality).count()
modality.sort_values(inplace=True,ascending=False)
modality.head() # GENERAL, 1, SPANISH

#### modality_desc
actbook.modality_desc.head()
modality_desc=actbook.modality_desc.groupby(actbook.modality_desc).count()
modality_desc.sort_values(inplace=True,ascending=False)
modality_desc.head() # GENERAL ENTRANCE, SPANISH, TOUR

#### Booking_date
actbook.booking_date.head()
actbook.booking_date.isnull().any()
len(actbook.booking_date.unique())
booking_date=actbook.booking_date.groupby(actbook.booking_date).count()
booking_date.sort_values(inplace=True,ascending=False)
booking_date.head() # 14th feb 2014 etc. doesnt matter

#### cancellation_date
actbook.cancellation_date.head()
len(actbook.cancellation_date[actbook.cancellation_date!='\\N']) # 118671
# 20 % of the bookings were cancelled
actbook.cancellation_date.isnull().any()
len(actbook.cancellation_date.unique()) #105911
actbook=actbook[actbook.cancellation_date != '\\N']
#### service_date_from and to
actbook.service_date_from.head()
actbook.service_date_to.head()
actbook.service_date_from.isnull().any()
actbook.service_date_to.isnull().any()

### units number of units booked
actbook.units.head()
actbook.units.unique()
actbook.units.isnull().any()
units=actbook.units.groupby(actbook.units).count()
units.sort_values(inplace=True,ascending=False)
units.head() # 1 units rest are negligible

#### adults
actbook.adults.head()
actbook.adults.isnull().any()
len(actbook.adults.unique())
adults=actbook.adults.groupby(actbook.adults).count()
adults.sort_values(inplace=True,ascending=False)
adults.head() # max 2 adults 3,4 less afterwards

#### children
actbook.children.head()
actbook.children.isnull().any()
len(actbook.children.unique())
children=actbook.children.groupby(actbook.children).count()
children.sort_values(inplace=True,ascending=False)
children.head() # max people book without children but then max 1 and 2

#### Infants
actbook.infants.head()
actbook.infants.isnull().any()
actbook.infants.unique()
infants=actbook.infants.groupby(actbook.infants).count()
infants.sort_values(inplace=True,ascending=False)
infants.head() # all travel without infants

#### contract name
actbook.contract.head()
actbook.contract.isnull().any()
len(actbook.contract.unique()) # 18213 
contract=actbook.contract.groupby(actbook.contract).count()
contract.sort_values(inplace=True,ascending=False)
contract.head() # WDWROWTO2014 6620, PAV 2015 BOL/HB 4884

#### supplier code
actbook.supplier_code.head()
actbook.supplier_code.isnull().any()
len(actbook.supplier_code.unique()) # 1643 unique
suppliers=actbook.supplier_code.groupby(actbook.supplier_code).count()
suppliers.sort_values(inplace=True,ascending=False)
suppliers.head() # 3917,4682

#### content factsheet code
actbook.content_factsheet_code.head()
actbook.content_factsheet_code.isnull().any()
actbook.content_factsheet_code.unique()
actbook[actbook.content_factsheet_code=='\\N'] # 36935
actbook=actbook[actbook.content_factsheet_code!='\\N']

#### currency
actbook.currency.head()
actbook.currency.isnull().any()
len(actbook.currency.unique()) # 26
currency=actbook.currency.groupby(actbook.currency).count()
currency.sort_values(inplace=True,ascending=False)
currency.head() # EUR, USD, MXN, GBP,PHP

#### TTV
actbook.ttv.head()
actbook.ttv.isnull().any()
len(actbook.ttv.unique()) # 69924
ttv=actbook.ttv.groupby(actbook.ttv).count()
ttv.sort_values(inplace=True,ascending=False)
ttv.head() # max ttv is 0. followed by 78,100,112 and 76

#### ttv_euro
actbook.ttv_eur.head()
actbook.ttv_eur.isnull().any()
len(actbook.ttv_eur.unique()) # 72905
ttv_eur=actbook.ttv_eur.groupby(actbook.ttv_eur).count()
ttv_eur.sort_values(inplace=True,ascending=False)
ttv_eur.head() # 0 is max

#### pct_commission
actbook.pct_commission.head()
actbook.pct_commission.isnull().any()
actbook[actbook.pct_commission=='\\N'].shape # 225684 have no value
actbook.shape
actbook.shape[0]-actbook[actbook.pct_commission=='\\N'].shape[0] # 300333
len(actbook.pct_commission.unique()) # 27
commissions=actbook.pct_commission.groupby(actbook.pct_commission).count()
commissions.sort_values(inplace=True,ascending=False)
commissions.head() # 12% commission is the maximmum followed by 14,10,15
actbook=actbook[actbook.pct_commission!='\\N']
len(actbook.columns) # 37 columns

# drop the columns not needed
actbook=actbook.drop(['country_market_desc','sales_method','destination_country_desc','destination_name','service_desc'],axis=1)
actbook.columns

# client and country
clients countries
import matplotlib.pyplot as plt
count_clients=pd.value_counts(actbook['country_market'],sort=True).sort_index()
count_clients.plot(kind="bar")
plt.xlabel("Country")
plt.ylabel("Client")
plt.title("Clients per Country")

import seaborn as sns
def plot_categories(df,cat,target,**kwargs):
       row=kwargs.get('row',None)
       col=kwargs.get('col',None)
       facet=sns.FacetGrid(df,row=row,col=col)
       facet.map(sns.barplot,cat,target)
       facet.add_legend()

# application and booking
plot_categories(actbook,cat='application',target='booking')
count_application=pd.value_counts(actbook['application'],sort=True).sort_index()
count_application.plot(kind="bar")
plt.xlabel("Application")
plt.ylabel("Frequency")
plt.title("Frequency Histogram for Application")

# incoming_office
count_incomoffice=pd.value_counts(actbook['incoming_office'],sort=True).sort_index()
count_incomoffice.plot(kind="bar")
plt.xlabel("Incoming_office")
plt.ylabel("Frequency")
plt.title("Frequency histogram for Incoming_office")

correlation=actbook.corr()
sns.heatmap(correlation,vmax=1,square=True,annot=True)

actbook=actbook.drop(['modality_desc'],axis=1)
# numerical variables standard scaler fit transform

import matplotlib.cm as cm
import numpy as np
from collections import defaultdict
d=defaultdict(LabelEncoder)
from sklearn.decomposition import PCA
import pylab as pl
import hdbscan
from sklearn.preprocessing import LabelEncoder
actbook=actbook.apply(LabelEncoder().fit_transform)
pca=PCA(n_components=2).fit(actbook)
pca_2d=pca.transform(actbook)
clusterer=hdbscan.HDBSCAN(min_cluster_size=10)
cluster_labels=clusterer.fit_predict(actbook)
pl.figure('HDBSCAN Clustering')
colors = cm.rainbow(np.linspace(0, 1, len(pca_2d[:,1])))
for y, col in zip(pca_2d[:,1], colors):
    plt.scatter(pca_2d[:,0],pca_2d[:,1], color=col,c=cluster_labels)
pl.scatter(pca_2d[:,0],pca_2d[:,1],c=cluster_labels)
pl.show()




 
 
 
 
 
 
 
 
 
 
 
 
 