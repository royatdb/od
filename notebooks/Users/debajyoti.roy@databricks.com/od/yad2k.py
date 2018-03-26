# Databricks notebook source
# MAGIC %md
# MAGIC # Create a Keras Model using:
# MAGIC [YAD2K](https://github.com/allanzelener/YAD2K)
# MAGIC 
# MAGIC # Official YOLO site:
# MAGIC [darknet/yolo](https://pjreddie.com/darknet/yolo/)

# COMMAND ----------

# MAGIC %sh
# MAGIC curl https://bootstrap.pypa.io/get-pip.py | python3

# COMMAND ----------

# MAGIC %sh
# MAGIC python3 -m pip install -U setuptools

# COMMAND ----------

# MAGIC %sh
# MAGIC python3 -m pip install keras

# COMMAND ----------

# MAGIC %sh
# MAGIC python3 -m pip install tensorflow

# COMMAND ----------

# MAGIC %sh
# MAGIC python3 -m pip install numpy h5py pillow

# COMMAND ----------

# MAGIC %sh git clone https://github.com/allanzelener/yad2k.git

# COMMAND ----------

# MAGIC %sh wget http://pjreddie.com/media/files/yolo.weights

# COMMAND ----------

# MAGIC %sh wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov2.cfg

# COMMAND ----------

# MAGIC %sh ls .

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC python3 yad2k/yad2k.py yolov2.cfg yolo.weights yad2k/model_data/yolo.h5

# COMMAND ----------

# MAGIC %sh cp yad2k/model_data/yolo.h5 /dbfs/mnt/roy/object-detection/model_data/

# COMMAND ----------

