#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-files /user/maria_dev/mapper1.py -mapper "python3 mapper1.py" \
-files /user/maria_dev/reducer1.py -reducer "python3 reducer1.py" \
-input /user/maria_dev/data/data.csv -output /user/maria_dev/all_accidents

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-files /user/maria_dev/mapper2.py -mapper "python3 mapper2.py" \
-files /user/maria_dev/reducer2.py -reducer "python3 reducer2.py" \
-input /user/maria_dev/all_accidents -output /user/maria_dev/make_year_count

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files /user/maria_dev/mapper1.py -mapper "python3 mapper1.py" -files /user/maria_dev/reducer1.py -reducer "python3 reducer1.py" -input /user/maria_dev/data/data.csv -output /user/maria_dev/all_accidents
