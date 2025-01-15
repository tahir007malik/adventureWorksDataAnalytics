import logging
import json
import os
import azure.functions as func
from azure.storage.filedatalake import DataLakeServiceClient
# from dotenv import load_dotenv
# load_dotenv()

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GitWebhookHandler")
def GitWebhookHandler(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Parse the incoming request payload (GitHub webhook)
        payload = req.get_json()

        if not payload:
            return func.HttpResponse("Empty Payload", status_code = 400)

        # Extract files added inside `Data/` directory from the payload
        data_files = []
        
        for commit in payload.get("commits", []):
        # Combine all "added" files from the commits
            added_files = commit.get("added", [])
            for file in added_files:
                # Check if the file is in the 'Data/' directory and (.csv) Extention
                if (file.startswith("Data/")) and (file.endswith(".csv")):
                    data_files.append(file)
        
        if not data_files:
            return func.HttpResponse("No files added inside 'Data/' directory with .csv extention", status_code = 200)

        # ================================================================
        #   ================== DATA LAKE CONNECTION ==================
        # ================================================================
        try:
            STORAGE_ACCOUNT_NAME = os.getenv("BUCKET_NAME")
            STORAGE_ACCOUNT_KEY = os.getenv("BUCKET_KEY")
            CONTAINER_FILE_SYSTEM = os.getenv("BUCKET_CONTAINER_FILE_SYSTEM")
            JSON_FILE_PATH = os.getenv("BUCKET_CONTAINER_JSON_FILE")

            # Initialize datalake service client
            service_client = DataLakeServiceClient(
                api_version = "2020-10-02",  # This ensures you're using ADLS Gen2's API
                credential = STORAGE_ACCOUNT_KEY,
                account_url = f"https://{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net"
            )

            # Assuming service_client is already created
            file_system_client = service_client.get_file_system_client(file_system = CONTAINER_FILE_SYSTEM)

            # Function to create dynamic entry based on the file path
            def create_dynamic_entry(filePath):
                fileNameExt = filePath.split('_')[1]
                fileNameExt = fileNameExt.lower()

                fileName = fileNameExt.split('.')[0]
                fileName = fileName.lower()

                # Create the entry dynamically
                new_entry = {
                    "p_rel_url": f"tahir007malik/adventureWorksDataAnalytics/refs/heads/main/{filePath}",
                    "p_sink_folder": f"adventure_works_{fileName}",
                    "p_sink_file": f"adventure_works_{fileNameExt}"
                }
                return new_entry

            # Read the json file
            file_client = file_system_client.get_file_client(JSON_FILE_PATH)
            try:
                # Download the file's content
                download = file_client.download_file()
                mainJSONFile = json.loads(download.readall().decode())

                # Iterate over added files and create dynamic entries for them
                for file in data_files:
                    new_entry = create_dynamic_entry(file)
                    mainJSONFile.append(new_entry)
                
                beautyJSON = json.dumps(mainJSONFile, indent = 4)
                # print(beautyJSON)

                # Now, upload the updated git.json back to ADLS Gen2
                file_client.upload_data(beautyJSON, overwrite=True)
                logging.info("git.json has been updated with the new entries.")

            except Exception as e:
                logging.error(f"Error reading or updating git.json: {e}")
                raise e


        except Exception as e:
            logging.error(f"Error initializing ADLS Gen2 service client: {e}")
            raise e


    except ValueError as e:
        logging.error(f"Error parsing JSON: {e}")
        return func.HttpResponse("Invalid JSON in request body.", status_code=400)
    except Exception as e:
        logging.error(f"Error processing payload: {e}")
        return func.HttpResponse(f"Error processing payload: {e}", status_code=500)

    return func.HttpResponse(f"{data_files} upserted successfully in git.json", status_code=201)