import great_expectations as ge
from great_expectations.cli.datasource import sanitize_yaml_and_save_datasource

context = ge.get_context()

config = f"""
name: my_datasource
class_name: Datasource
execution_engine:
  class_name: SqlAlchemyExecutionEngine
  credentials:
    host: 192.168.1.4
    port: '5432'
    username: demo_user
    password: demo_password
    database: postgres
    drivername: postgresql
data_connectors:
  default_runtime_data_connector_name:
    class_name: RuntimeDataConnector
    batch_identifiers:
      - default_identifier_name
  default_inferred_data_connector_name:
    class_name: InferredAssetSqlDataConnector
    name: whole_table"""

sanitize_yaml_and_save_datasource(context, config, overwrite_existing=True)
