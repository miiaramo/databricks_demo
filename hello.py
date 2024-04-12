# Databricks notebook source
print("hello")

# dbutils 
dbutils.widgets.text("greeting", "hello")

# COMMAND ----------

dbutils.widgets.get("greeting")

# COMMAND ----------

# Multi language - Use Python, Scala, SQL, and R, all in same notebook (demo: magic commands)

# COMMAND ----------

# Collaborative - Real-time co-precense and co-editing (demo: give access)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Explorative - Built in charts and data profiles (demo: filter results)
# MAGIC
# MAGIC SELECT 'hello' as greeting
# MAGIC UNION
# MAGIC SELECT 'moi' as greeting
# MAGIC UNION
# MAGIC SELECT 'hello, world' as greeting
# MAGIC UNION
# MAGIC SELECT 'hallo' as greeting

# COMMAND ----------

# Adabtable - Install packages and import local modules (demo: install package)

# COMMAND ----------

name = "Miia"

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------

dbutils.widgets.get("greeting")

# COMMAND ----------

# Reproducable - track changes and use Git version control (demo: history)

# COMMAND ----------

# Get to production faster - Schedule noteboooks as a jobs or build a dashboard from their results in the notebook

# COMMAND ----------

# Enterprise ready - Estreprise-grade access controls, identity management, and auditability
