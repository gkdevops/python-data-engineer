# main_program.py

import analytics_tools
from analytics_tools import plotting # Use a module from the package
import analytics_tools.stats     # Another way to use a module
from analytics_tools.aws import aws_stats

chart = plotting.create_bar_chart([1,2,3])
print(chart) # Output: Bar chart created!

avg = analytics_tools.stats.calculate_mean([10, 20, 30])
print(avg) # Output: 20.0

aws_avg = aws_stats.aws_calculate_mean([10, 20, 30, 40])
print(aws_avg)