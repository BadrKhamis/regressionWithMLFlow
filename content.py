

from config import title_style, bold_style , normal_style
title = "Report for AirB&B and optimize best prediction model"

introduction = ''' 
Regression analysis is a powerful statistical technique used to 
examine the relationship between a dependent variable and one or more independent variables.
It's widely used in various fields such as economics, finance, social sciences, and machine learning.
When working with regression models, it's essential to determine the most suitable model for your data.
In this report, we will delve into the process of comparing different regression 
models and selecting the optimal one that best fits the data and provides accurate predictions.
'''
purpose = ''' 
The purpose of this report is to analyze and compare various regression models to identify the model that produces the best results for a specific dataset.
We aim to provide insights into the strengths and weaknesses of different regression techniques, 
enabling informed decision-making when choosing a model for predictive tasks.
'''
Business_Objectives = ''' 
The primary objective of this project is to perform a comprehensive descriptive analysis of the company's
operational data and provide actionable insights to the management team. Additionally, the project aims to
identify the key drivers and factors that significantly influence the data,
allowing the management to make informed decisions and optimize business strategies.
'''



objectives = [
    ("Key Goals:", title_style),
    ("Descriptive Analysis:", bold_style),
    ("Conduct a thorough descriptive analysis of the company's operational data, highlighting trends, patterns, and anomalies to gain a deep understanding of its performance.", normal_style),
    ("Insights Generation:", bold_style),
    ("Extract valuable insights from the analyzed data, translating complex findings into clear and actionable recommendations for the management team.", normal_style),
]

Data_Understanding = '''
In this section, we embark on a comprehensive exploration of the Airbnb dataset, a crucial preliminary step in any data analysis endeavor.
Our primary objective is to gain a deep understanding of the data, uncover meaningful insights,
and lay the foundation for implementing statistical models. Through careful examination, we will dissect the dataset's structure, identify key trends, patterns, and outliers, and distill valuable information.
Armed with this knowledge, we will be well-equipped to make informed decisions, formulate hypotheses, and construct statistical models that can provide actionable solutions and drive data-driven strategies in the realm of Airbnb hosting and accommodation.
'''



roomBookingsummary = '''In summary, the graph provides insights into the distribution of room types in the dataset,
showing that "Entire home/apt" is the most common type, with a value of approximately 0.483 or 48.3%. This suggests that nearly half of the accommodations in the dataset or context are "Entire home/apartment" rentals.
followed by "Private room," and "Shared room" is the least common '''
neighbrhood = '''In this section, we will examine the room distribution within neighborhoods. We will calculate the number of rooms per neighborhood and visualize this data through mapping and graphing. '''
neighbrhoodSummary = '''Based on the graph, it appears that a significant portion of Airbnb properties lacks neighborhood information. Therefore, we have utilized latitude and longitude coordinates to map these properties. Additionally, among the properties with neighborhood information, Queen Anne neighborhood stands out as having the highest number of properties. '''
propertiyType = ''' '''
propertyBookingRatio = ''''''
priceNeighbrhood = ''''''
priceDistribution = ''' '''
removeOutlier = ''' '''
summary= ''' '''


roomTitle = 'room type:'
roomTitleDescribe = ''' In this section, we will analyze the various room types available on Airbnb with the aim of gaining valuable insights.
Our goal is to understand which room types play a predominant role within the platform. '''
graph = ''
roomType = ''' as the graph show that most of our airB&B room type is entire home or apartment and it count more thatn 50% of the entire data '''
bookingRatio = 'Booking Ratio'
roomBookingRatio = ''' To determine the booking ratio for a specific room type, we need to assess its availability over the next 30 days and incorporate this information by adding a new column to our data frame. '''
roomtableRatio = ' '
graphRatio = ''
