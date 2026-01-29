# #!/bin/bash
# echo "TASK 3: MAPREDUCE - TRANSACTION COUNT BY COUNTRY"
# echo "================================================="

# # Clean previous output
# hdfs dfs -rm -r /output/country_count 2>/dev/null

# # Run MapReduce (Country is column 10, index 9)
# hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
#     -input /retail/retail_data.csv \
#     -output /output/country_count \
#     -mapper "awk -F, 'NR>1 && NF>=10 {print \$10\"\\t1\"}'" \
#     -reducer "awk '{count[\$1] += \$2} END {for (c in count) print c\"\\t\"count[c]}'" \
#     -numReduceTasks 1

# echo -e "\nRESULTS: Top 10 Countries"
# echo "Country\tCount"
# echo "--------------"
# hdfs dfs -cat /output/country_count/part-00000 | sort -t$'\t' -k2 -nr | head -10

#!/bin/bash

echo "TASK 3: MAPREDUCE - TRANSACTION COUNT BY COUNTRY"
echo "================================================="

HDFS_INPUT=/retail/retail_data.csv
HDFS_OUTPUT=/output/country_count
HADOOP_STREAMING_JAR=$(ls $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar)

# Clean previous output (if exists)
hdfs dfs -rm -r -f $HDFS_OUTPUT 2>/dev/null

echo "Running MapReduce job..."
echo "Input : $HDFS_INPUT"
echo "Output: $HDFS_OUTPUT"
echo "-----------------------------------------------"

hadoop jar $HADOOP_STREAMING_JAR \
  -D mapreduce.job.name="Transaction Count By Country" \
  -input $HDFS_INPUT \
  -output $HDFS_OUTPUT \
  -mapper "awk -F, 'NR>1 && NF>=10 {print \$10\"\t1\"}'" \
  -reducer "awk '{count[\$1] += \$2} END {for (c in count) print c\"\t\"count[c]}'" \
  -numReduceTasks 1

echo
echo "RESULTS: Top 10 Countries"
echo "Country	Count"
echo "-------------------------"

hdfs dfs -cat $HDFS_OUTPUT/part-00000 \
  | sort -t$'\t' -k2 -nr \
  | head -10
