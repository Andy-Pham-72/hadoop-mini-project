#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \

# Note we have to use the linux directory for python files which we uploaded in the Step 1
-file /tmp/mapper1.py -mapper  "python mapper1.py" \
-file /tmp/reducer1.py -reducer "python reducer1.py" \

# Note for input and output used the HDFS directory
-input /user/root/test_dir/data.csv -output /user/root/test_dir/output/all_accidents

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /tmp/mapper2.py -mapper "python mapper2.py" \
-file /tmp/reducer2.py -reducer "python reducer2.py" \
-input /user/root/test_dir/output/all_accidents -output /user/root/test_dir/output/make_year_count
