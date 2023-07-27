import great_expectations as ge
from ruamel.yaml import YAML

yaml = YAML()
context = ge.get_context()

config = f"""
name: my_checkpoint
config_version: 1.0
class_name: SimpleCheckpoint
run_name_template: "%Y%m%d-%H%M%S-validation-run"
validations:
  - batch_request:
      datasource_name: my_datasource
      data_connector_name: default_inferred_data_connector_name
      data_asset_name: yellow_tripdata_sample_2019_02
      data_connector_query:
        index: -1
    expectation_suite_name: my_suite
"""

context.add_checkpoint(**yaml.load(config))
