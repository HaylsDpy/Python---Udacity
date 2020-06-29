# refer to notes in notebook for full explanation
# to analyse the number of courses visited, arranging data by account key and summing the num_courses_visited field for each accout key would not work (would not account for
# multiple visits in one day and would skew data)
# added code to doc 9 to account for this

engagement_by_account = group_data(paid_engagement_in_first_week,'account_key')
has_visited_by_account = sum_grouped_items(engagement_by_account,'has_visited')
describe_data(has_visited_by_account.values())

# should get Mean of 2.867, SD or 2.255, Min of 0 and Max of 7
