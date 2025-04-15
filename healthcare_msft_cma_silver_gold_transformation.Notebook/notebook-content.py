# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0f273690-2e70-455b-b335-f9ccf3d940a8",
# META       "default_lakehouse_name": "healthcare_msft_gold_cma",
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
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

%run healthcare_msft_config_notebook {"enable_spark_setup" : true, "enable_packages_mount" : false}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# PARAMETERS CELL ********************

inline_params = "{}"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

# Invoke the CMAIngestionService to transform and load tables into target lakehouse
from microsoft.fabric.hls.hds.services.cm_analytics_gold_ingestion_service import CMAnalyticsGoldIngestionService
from microsoft.fabric.hls.hds.utils.utils import FolderPath
import json

# convert inline params into dictionary
inline_params_dict = json.loads(inline_params)

# Invoke the CMAIngestionService to transform and load tables into target lakehouse
cma_ingestion_service = CMAnalyticsGoldIngestionService(spark,
        workspace_name=workspace_name,
        solution_name=solution_name,
        inline_params=inline_params_dict,
        admin_lakehouse_name=administration_database_name,
        one_lake_endpoint=one_lake_endpoint
        )
cma_ingestion_service.run()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

mssparkutils.fs.unmount(packages_mount_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }
