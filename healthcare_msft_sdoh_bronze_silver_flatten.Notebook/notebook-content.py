# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "af1ee8e4-1fda-43d7-9a7c-5ceb869bf9a3",
# META       "default_lakehouse_name": "healthcare_msft_bronze",
# META       "default_lakehouse_workspace_id": "bb12719e-d315-4990-935f-b302e6263481"
# META     },
# META     "environment": {
# META       "environmentId": "7d7aaf4b-d582-83ad-4ac9-598ddc842ba0",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ##### WARNING
# The following notebook is intended to be read only. Please do not modify the contents of this notebook.


# CELL ********************

%run healthcare_msft_config_notebook

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

%run healthcare_msft_config_notebook {"enable_spark_setup" : true, "enable_packages_mount" : false}

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# PARAMETERS CELL ********************

inline_params = "{}"

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

# Invoke the SDOHSilverIngestionService to transform and load tables into target lakehouse

from microsoft.fabric.hls.hds.services.sdoh_silver_ingestion_service import SDOHSilverIngestionService
import json

# convert inline params into dictionary
inline_params_dict = json.loads(inline_params)

sdoh_silver_ingestion_service = SDOHSilverIngestionService(spark,
        workspace_name=workspace_name,
        solution_name=solution_name,
        admin_lakehouse_name=administration_database_name,
        inline_params=inline_params_dict,
        one_lake_endpoint=one_lake_endpoint,
        )
sdoh_silver_ingestion_service.run()

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

mssparkutils.fs.unmount(packages_mount_name)

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }
