#-------------------------------------------------StarDataKMeansGrouper.py-------------------------------------------------#

'''
Importing Modules:
-sklearn:-Kmeans (KM)
-matplotlib.pyplot (plt)
-seaborn (sns)
-pandas (pd)
-sys
-time (tm)
'''

from sklearn.cluster import KMeans as KM
import matplotlib.pyplot as plt
import seaborn as sns
import pandas  as pd
import sys
import time as tm


print("Welcome to StarDataKMeansGrouper.py.")

print("We provide an alogrithm for grouping the data into K-Means clusters")
tm.sleep(2.3)

view_information_cluster=input("Know about Clustering? (I Know/I Don't Know)")

#Assessing the user's knowledge on Clustering
#Case-1
if(view_information_cluster=="I Don't Know" or view_information_cluster=="i don't know" or view_information_cluster=="I don't know" or view_information_cluster=="I don't Know" or view_information_cluster=="I Don't know" or view_information_cluster=="I Dont Know" or view_information_cluster=="i dont know" or view_information_cluster=="I dont know" or view_information_cluster=="I dont Know" or view_information_cluster=="I Dont know"):
  print("Clustering, also known as Cluster Analysis is a method of grouping a set of data into groups called Clusters.")
  tm.sleep(1.1)

  print("The datapoints of a cluster, are similar to each other than they are to those of other clusters in a certain way.")
  tm.sleep(2.1)

  print("A freqently used type of Clustering is the K-Means method.")
  tm.sleep(1.1)

  print("Other methods of clustering K-Medians and K-Medoids.")
  tm.sleep(1.2)

  print("To know more about K-Medoids visit: 'https://en.wikipedia.org/wiki/Cluster_analysis'")
  print("To know more about K-Medians visit: 'https://en.wikipedia.org/wiki/K-medians_clustering'")
  print("To know more about K-Medoids visit: 'https://en.wikipedia.org/wiki/K-medoids'")

view_information_kmeans=input("Know about K-Means? (I Know/I Don't Know)")

#Aassessing the user's knowledge on KMeans
#Case-1
if(view_information_kmeans=="I Don't Know" or view_information_kmeans=="i don't know" or view_information_kmeans=="I don't know" or view_information_kmeans=="I don't Know" or view_information_kmeans=="I Don't know" or view_information_kmeans=="I Dont Know" or view_information_kmeans=="i dont know" or view_information_kmeans=="I dont know" or view_information_kmeans=="I dont Know" or view_information_kmeans=="I Dont know"):
  print("K-Means is a method of clustering a set of data n into k clusters, where each data point is assigned to the cluster with the neares mean or Centroid, thus fragmenting the data space into Voronoi Cells.")
  tm.sleep(2.3)

  print("The variance between clusters of K-Means is reduced due to the use WCSS, or Within Cluster Sum of Sqaures. WCSS is in essence the sum of the squares of Eucledian distances between the dtapints and the nearest Centroid")
  tm.sleep(5.6)

  print("To know more about K-Means visit: 'https://en.wikipedia.org/wiki/K-means_clustering'")
  print("To know more about Voronoi Cells visit: 'https://en.wikipedia.org/wiki/Voronoi_diagram'")
  
  
print("Loading Data....")
tm.sleep(2.5)  
  


  
#Reading Data rom the dataset
df=pd.read_csv("data.csv")

#Definng a function to enable the user to choose the parameters (x and y axes) for K-Means
def ChooseParameters(list_param,number_param):
  title_list=[]
  loc_input_list=[]

  #Running a for loop over a range of 1 and a  parameter to decide on the number of parameters
  for number_time in range(1,number_param):

    #Running a for loop over the enumerated list of parameters to display all possilbe options to the user
    for param_index,param in enumerate(list_param):

      #Verifying whether the index is equal to 0 or not to prevetn displaying "Unusable_Element"
      if param_index!=0:
        print("{}:{}".format(param_index,param))

    param_input=int(input("Please choose the parameter desired to be used in the K-Means grouping (Parameter Number-{}: x and y axes respectively)".format(number_time)))

    #Using a try-except bloack to assess the validity of the user's input
    #Try block
    try:
      user_test=list_param[param_input]

      #Verifying whether the input provided by the user is equal to 0 or not
      #Case-1
      if param_input==0:
        
        #Terminating the program beforehand due to an inavlid input provided by the user
        sys.exit("Invalid Input.")
    #Except block    
    except:

      #Terminating the program beforehand due to an inavlid input provided by the user
      sys.exit("Invalid Input.")  

    user_choice=list_param[param_input]   
    title_list.append(user_choice)
    loc_input_list.append(param_input)

  #Returning the chosen parameters and their indexes
  return title_list,loc_input_list   

titles,ilocs=ChooseParameters(["Unusable_Element","Mass","Gravity","Distance","Radius"],3)

df_iloced=df.iloc[:,ilocs].values

cluster_input=int(input("Please enter the number of clusters to be formed."))

#Verifyng whether the number of cluster prescribed by the user is greater than 11 or not and conducting necessary actions
#Case-1
if cluster_input>11:

  #Terminating the program beforehand due to an inavlid input provided by the user
  sys.exit("Invalid Input. Please enter an integer less than 11.")

kmeans=KM(n_clusters=cluster_input,init='k-means++',random_state=42)
y=kmeans.fit_predict(df_iloced)

colors=["darkgreen","green","yellow","blue","pink","brown","maroon","black","red","orange","purple","darkblue","violet"]

cluster=kmeans.cluster_centers_

plt.figure(figsize=(13,10))

#Running a for lopp over the range of 0 and the number of clusters as described by the user to plot scatter graphs of the clusters respectively
for i in range(cluster_input):

  sns.scatterplot(df_iloced[y==i,0],df_iloced[y==i,1],color=colors[i],label="Group {}".format(i+1))
  
sns.scatterplot(cluster[:,0],cluster[:,1],s=100,marker=",",color="grey",label="Centres")  
plt.title("K-Means Chart of Stars :- {} and {}".format(titles[0],titles[1]))
plt.xlabel(titles[0])
plt.ylabel(titles[1])
plt.show()

print("Thank You for using StarDataKMeansGrouper.py.")

#-------------------------------------------------StarDataKMeansGrouper.py-------------------------------------------------#
