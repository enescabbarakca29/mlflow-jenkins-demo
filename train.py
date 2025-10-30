import os
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

alpha = float(os.getenv("ALPHA", "0.3"))
l1_ratio = float(os.getenv("L1_RATIO", "0.7"))

X, y = load_diabetes(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run() as run:
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds) ** 0.5

    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.sklearn.log_model(model, "model")

    with open("run_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Run ID: {run.info.run_id}\nRMSE: {rmse:.4f}\n")
