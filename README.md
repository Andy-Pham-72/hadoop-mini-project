![20160406_1-768x396](https://user-images.githubusercontent.com/70767722/152094692-d1774f8c-5af3-48f9-8316-49b452e85d6e.png)

# Hadoop Mini Project
**Post-Sale Automobile Report**

In this project, we will utilize data from an automobile tracking platform that tracks the history of important incidents after the initial sale of a new vehicle. Such incidents include subsequent private sales, repairs, and accident reports. The platform provides a good reference for second-hand buyers to understand the vehicles they are interested in.

The report is stored as CSV files in HDFS with following schema:

<img width="907" alt="Screen Shot 2022-02-01 at 11 48 56 PM" src="https://user-images.githubusercontent.com/70767722/152094774-cb30a003-7962-4352-bd79-c38612ac7613.png">

## Learning Objectives
* Utilitzing MapReduce jobs in Python. 
* Leveraging a MapReduce processing model to process large scale data and break down a complex problem into smaller tasks.
* Getting familiar with VirtualBox environment.

## Setting up Hadoop using Hortonworks Hadoop Sandbox
* Please follow the [Instruction video to set up Hadoop with Hortonworks Hadoop Sandbox (Cloudera)](https://www.youtube.com/watch?v=735yx2Eak48)
* Extra material how to move files from Linux env to HDFS and backward in [Cloudera Hadoop Virtual Machine](https://www.youtube.com/watch?v=PLEt8FuDnjk&t=409s) 

## Step 1:
From your **Local Terminal** run [upload_files.sh](https://github.com/Andy-Pham-72/hadoop-mini-project/blob/master/upload_files.sh) to upload to the root directory in the VirtualBox:
- You have to input the password of root account in order to upload the files.

![Screen Shot 2022-02-01 at 11 56 15 PM](https://user-images.githubusercontent.com/70767722/152095515-79f4aacb-7aea-47ee-94a2-e13ffa39000d.png)

## Step 2:
From the Sandbox's Web Shell Client, logging into as `root` account and let's put the `data.csv` into hadoop file system:

```bash
$ hadoop fs -mkdir test_dir
$ hadoop fs -put data.csv /user/root/test_dir  
```

Double check the uploaded file in the Ambari `Files View`:

![Screen Shot 2022-02-02 at 12 02 14 AM](https://user-images.githubusercontent.com/70767722/152095881-93c1f30a-d5b8-4235-ad5f-9c7babe4c3f7.png)

## Step 3: 
From the Sandbox's Web Shell Client, run file [auto.sh](https://github.com/Andy-Pham-72/hadoop-mini-project/blob/master/auto.sh):

```bash
$ bash auto.sh
```

## Step 4:
After all the MapReduce jobs were successfully executed, let's check the output:
* From `all_accidents` folder:
![Screen Shot 2022-02-02 at 12 07 31 AM](https://user-images.githubusercontent.com/70767722/152096307-e636ce55-dbd6-409b-9481-902e658c63ad.png)

* From `make_year_count` folder:
* ![Screen Shot 2022-02-02 at 12 08 41 AM](https://user-images.githubusercontent.com/70767722/152096396-e229f5e8-57a9-45a6-8134-769be1049ef7.png)

**NOTE**:
- In the default Python enviroment is version 2 in VirtualBox so when you should either update the python env to 3 (or above) or tailor your code to fit the python 2.
For example, Python 2 doesn't support F-string like Python 3 which can cause error when you run the MapReduce python script. Therefore, you have to use %s acts a placeholder for a string while %d acts as a placeholder for a number. [More detail](https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/56382046)
