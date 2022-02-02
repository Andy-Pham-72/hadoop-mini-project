#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file mapper1.py -mapper  "python mapper1.py" \
-file reducer1.py -reducer "python reducer1.py" \
-input /user/root/test_dir/data.csv -output /user/root/test_dir/output/all_accidents

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file mapper2.py -mapper "python mapper2.py" \
-file reducer2.py -reducer "python reducer2.py" \
-input /user/root/test_dir/output/all_accidents -output /user/root/test_dir/output/make_year_count