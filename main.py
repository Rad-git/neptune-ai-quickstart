import neptune

# Create a Neptune run object
run = neptune.init_run(
    project="your-workspace-name/your-project-name",  
    api_token="YourNeptuneApiToken",  

)

# Track metadata and hyperparameters by assigning them to fields in the run
run["JIRA"] = "NPT-952"
run["algorithm"] = "ConvNet"

PARAMS = {
    "batch_size": 64,
    "dropout": 0.2,
    "learning_rate": 0.001,
    "optimizer": "Adam",
}
run["parameters"] = PARAMS

# Track the training process by logging your training metrics
for epoch in range(10):
    run["train/accuracy"].append(epoch * 0.6)  
    run["train/loss"].append(epoch * 0.4)

# Record the final results
run["f1_score"] = 0.66

# File
run["train_dataset"].track_files("./datasets/train.csv")

# Folder
run["train/tables"].track_files("./datasets/tables")

# S3 compatible filesystem
run["train/images"].track_files("s3://datasets/images")

# Stop the connection and synchronize the data with the Neptune servers
run.stop()
