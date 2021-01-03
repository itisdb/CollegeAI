import sentiment_analysis_first

# Name of colleges
# Sample for now
college1,college2 = 'NIT Delhi','JIS'
cleaned_dataset_college1,cleaned_dataset_college2 = sentiment_analysis_first.classify_reveiews(),sentiment_analysis_first.classify_reveiews('JIS_reviews.csv')
# For college 1
positive1,negative1 = cleaned_dataset_college1[cleaned_dataset_college1['sentiment'] == 0].shape[0],cleaned_dataset_college1[cleaned_dataset_college1['sentiment'] == 1].shape[0]
sentiment_ratio_1 = positive1/negative1
# For college 2
positive2,negative2 = cleaned_dataset_college2[cleaned_dataset_college2['sentiment'] == 0].shape[0],cleaned_dataset_college2[cleaned_dataset_college2['sentiment'] == 1].shape[0]
sentiment_ratio_2 = positive2/negative2

if sentiment_ratio_1 > sentiment_ratio_2:
    sentiment = f"{college1} is better than {college2} based on alumni/current students' reviews."
elif sentiment_ratio_1 < sentiment_ratio_2:
    sentiment = f"{college2} is better than {college1} based on alumni/current students' reviews."
else:
    difference1,difference2 = (positive1 - negative1),(positive2 - negative2)
    if difference1 > difference2:
        sentiment = f"{college1} is better than {college2} based on alumni/current students' reviews."
    else:
        sentiment = f"{college2} is better than {college1} based on alumni/current students' reviews."

# Run
print(sentiment)
