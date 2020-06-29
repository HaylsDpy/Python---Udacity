# Calculate some metrics you're interested in for both groups of students. Use the same functions as earlier to look at same 3 metrics - minutes spent, lessons completed,
# and days visited - but for both passing and non-passing students (look in notebook for expected outcomes) - pretty sure my numbers are sliiiightly off

#passing_engagement_by_account = group_data(passing_engagement, 'account_key')
#non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')


print('Days Visited')
print('Non-Passing Students:')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')
non_passing_visits = sum_grouped_items(non_passing_engagement_by_account, 'has_visited')
describe_data(non_passing_visits.values())


print('Days Visited')
print('Passing Students:')
passing_engagement_by_account = group_data(passing_engagement, 'account_key')
passing_visits = sum_grouped_items(passing_engagement_by_account, 'has_visited')
describe_data(passing_visits.values())


print('Minutes Spent')
print('Non-Passing Students:')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')
non_passing_visits = sum_grouped_items(non_passing_engagement_by_account, 'total_minutes_visited')
describe_data(non_passing_visits.values())


print('Minutes Spent')
print('Passing Students:')
passing_engagement_by_account = group_data(passing_engagement, 'account_key')
passing_visits = sum_grouped_items(passing_engagement_by_account, 'total_minutes_visited')
describe_data(passing_visits.values())


print('Lessons Completed')
print('Non-Passing Students:')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')
non_passing_visits = sum_grouped_items(non_passing_engagement_by_account, 'lessons_completed')
describe_data(non_passing_visits.values())


print('Lessons Completed')
print('Passing Students:')
passing_engagement_by_account = group_data(passing_engagement, 'account_key')
passing_visits = sum_grouped_items(passing_engagement_by_account, 'lessons_completed')
describe_data(passing_visits.values())
