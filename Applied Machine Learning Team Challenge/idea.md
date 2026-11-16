# ⚠️ This Repository Has Moved

The **FTL Syria — Crop Yield Prediction** project (Group 4) has moved to a new,
dedicated repository:

👉 **https://github.com/AhmedGDeeb/ftl-syria-crop-yield**

All active development — the data pipeline, feature engineering, modeling,
serving, and deployment — now lives there. This repository is kept for
historical reference only and will no longer be updated.

The full project details are retained below for archival purposes.

---

# 🌾 FTL Syria — Crop Yield Prediction

A reproducible machine learning pipeline that predicts crop yield in Syria from
historical climate data. Built as part of the **Frontier Tech Leaders (FTL)
Syria Programme — AI for Climate** Machine Learning Challenge, **Group 4**.

---

## 📖 Project Overview

Agriculture is central to Syria's economy and food security, but crop yields are
highly sensitive to climate variability — rainfall, temperature extremes, heat
waves, and drought. This project builds machine learning models that predict
crop yield (hg/ha) using historical climate data from **NASA POWER** and
agricultural production statistics from **FAOSTAT**.

The goal is to understand **which climate variables most influence crop yields**
and to support the development of **climate-resilient agriculture** strategies.

### 🎯 Research Question

> **Can historical weather conditions help predict crop yields in Syria, and
> which machine learning model produces the most accurate predictions?**

The primary evaluation metric is **RMSE on a held-out test set**, with MAE and R²
reported alongside. RMSE is used because it penalizes large errors on extreme
(drought/conflict) years more heavily — and those extremes are precisely the
years a yield-prediction system must handle well.

---

## 👥 Team Members (Group 4)

| Name | Field |
| :--- | :--- |
| **Nimra Afzaal** | Electrical and Power Engineering |
| **Sular Albalkhi** | Electronics and Communications Engineering |
| **Zaid Aldeen Mohammad Kiki** | Electrical and Power Engineering |
| **Ahmad Deeb** | Electronics and Communications Engineering |

---

## 📚 Datasets

### 1. FAOSTAT — Crop Production (target variable)

- **Source:** [FAOSTAT — Crops and Livestock Products (QCL)](https://www.fao.org/faostat/en/#data/QCL)
- **Country:** Syrian Arab Republic (UN M49 code `760`)
- **Coverage:** 1991 → present, one file per year
- **Target:** `Value` where `Element == "Yield"`, in `hg/ha`

**Data flags** (`A` = official, `E` = estimated, `P` = provisional,
`I` = imputed) are retained so reliability can be assessed in sensitivity
analyses.

**Avoiding data leakage:** Production and Area Harvested are deliberately **not
used as features**, since `Yield = Production / Area Harvested`. Using them
would leak the target.

### 2. NASA POWER — Daily Climate (features)

- **Source:** [NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/)
- **Coverage:** 1991 → present, daily, all 13 Syrian governorates
- **Raw format:** one file per (governorate, year, month)

**Variables downloaded:**

| API name | Column | Unit | Meaning |
|---|---|---|---|
| `T2M` | `t2m` | °C | Mean air temperature at 2 m |
| `T2M_MAX` | `t2m_max` | °C | Daily max temperature |
| `T2M_MIN` | `t2m_min` | °C | Daily min temperature |
| `PRECTOTCORR` | `prectotcorr` | mm/day | Corrected total precipitation |
| `RH2M` | `rh2m` | % | Relative humidity at 2 m |
| `ALLSKY_SFC_SW_DWN` | `solar_kwh_m2` | kWh/m²/day | Surface solar irradiance |
| `WS2M` | `ws2m` | m/s | Wind speed at 2 m |

NASA POWER fill values (`-999.0`) are replaced with `NA` during ingestion.

---

## 🔗 Merging the Datasets

The FAOSTAT data is **annual** (one value per year per crop), while the NASA
POWER data is **daily**. The pipeline:

1. **Aggregates** daily NASA POWER data to **annual statistics per governorate**
   (mean temperature, total rainfall, heat-stress days at >35 °C, cold-stress
   days at <0 °C, mean humidity, mean solar radiation, mean wind speed).
2. **Averages** the per-governorate statistics across the 13 governorates to
   obtain **country-level annual climate features** (one row per year).
3. **Joins** the annual climate table with the FAO yield table on `year`. The
   `crop` column stays as a feature so the model can learn crop-specific
   climate sensitivities.

The final model-ready table has:

- **Target:** Crop yield (hg/ha) from FAOSTAT
- **Features:** Climate variables from NASA POWER + `crop`

### Temporal Split

Random splits would leak future climate data into training. The pipeline uses a
**temporal split** — train on earlier years, validate and test on later years —
reflecting how the model would actually be used (predict a future year's yield
from that year's climate).

---

## 🔍 Anomaly Detection — Detection, Not Removal

A key design decision: instead of dropping drought and conflict years, the
pipeline runs **two independent detectors** — a 2D Gaussian density diagnostic
plus a detrended residual z-score (`|z| > 2`) — on both the FAO yield series
(per crop) and the NASA climate series (per governorate × feature). Both
flagged the same real-world events:

| Period | Interpreted cause |
|---|---|
| 2007–2008 | Multi-year drought |
| 2010–2012 | Conflict onset + dry spell |
| 2018–2021 | Renewed drought + instability |

**No rows are dropped.** Instead, four binary indicator features are attached
(`yield_anomaly`, `climate_anomaly`, `drought_year`, `conflict_year`) so the
model *learns from* the extremes rather than failing on them. Only partial
years (the current incomplete year) are dropped as measurement artifacts.

All anomaly thresholds and rules live in a single file
(`src/data/anomaly_check.py`), so the policy is explicit, reversible, and
isolated from the downstream pipeline.

---

## 🤖 Modeling & Training

Training is driven by `notebooks/02_models.ipynb` for exploration and
`train.py` for headless, production-style runs:

- **Model families:** Decision Tree Regressor and XGBoost Regressor.
- **Tuning:** `GridSearchCV` with `KFold(5, shuffle=True, random_state=42)`,
  scored on `neg_root_mean_squared_error`.
- **Tracking:** every baseline, grid-search trial, and final refit is logged to
  **MLflow** (experiment `Syria_Crop_Yield_Baseline`), including per-split RMSE,
  MAE, R², sMAPE, and unit-free `rmse_ratio` metrics.
- **Final fit:** the winning estimator is refit on `train + val` before being
  saved.
- **Outputs:** `models/dt_<crop>.pkl` and `models/xgb_<crop>.pkl` (15 crops ×
  2 families = 30 models), plus `models/feature_schema.json` — the exact
  training column order that both training and serving agree on.

**Result pattern:** XGBoost won every completed crop, consistently favouring
`learning_rate=0.01` with shallow trees (`max_depth` 2–3) and 50–100
estimators — strong regularization beats capacity on ~25 samples per crop.

---

## 🛠️ Tools and Technologies

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, MLflow, DVC, FastAPI
- **Environment:** Jupyter Notebook
- **Data Sources:** FAOSTAT, NASA POWER
- **Containerization:** Docker
- **Deployment:** Render (FastAPI web service)

---

## 📂 Repository Structure (archived)

```
ftl-syria-crop-yield/
├── data/
│   ├── raw/          ← FAO + NASA downloads (DVC-tracked)
│   ├── interim/      ← train/val/test splits (DVC-tracked)
│   └── processed/    ← model-ready table (DVC-tracked)
├── notebooks/        ← EDA and modeling notebooks
├── src/              ← ingestion, feature engineering, training code
├── models/           ← trained model artifacts
├── predict.py        ← FastAPI service
├── Dockerfile
├── requirements-serve.txt
└── README.md
```

---

## 🐳 Docker

The serving stack is containerized so the API runs identically on any machine.
The image installs only the **slim runtime dependencies**
(`requirements-serve.txt` — FastAPI, uvicorn, pandas, scikit-learn, xgboost,
joblib), not the full training stack, keeping the image small.

**Build the image:**

```bash
docker build -t ftl-syria-crop-yield .
```

**Run the container:**

```bash
docker run -p 9696:9696 ftl-syria-crop-yield
```

**Verify it's up:**

```bash
curl -s http://localhost:9696/health
# → {"status":"ok","models_loaded":30}
```

Then test the same `/predict` endpoint as the local service (see the new repo
for full request/response examples):

```bash
curl -X POST http://localhost:9696/predict \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

The container exposes the same three frontends on one process — the HTML form
at `/`, Swagger UI at `/docs`, and the JSON API at `POST /predict`.

---

## ☁️ Deployment (Render)

The project is deployed on **[Render](https://render.com)** as a FastAPI web
service serving both a JSON API and a minimal HTML UI.

| Item | Value |
|---|---|
| Live service URL | `https://ftl-syria-crop-yield.onrender.com/` |
| Swagger UI | `https://ftl-syria-crop-yield.onrender.com/docs` |
| Health check | `https://ftl-syria-crop-yield.onrender.com/health` |
| Source branch | `deploy` (runtime files only) |
| Runtime | Python 3 |
| Plan | Free tier (Starter recommended for 30-model preload) |

### Deployment approach

Production runs from a dedicated **`deploy` orphan branch** that contains only
runtime files — no notebooks, no raw data, no training scripts:

```
deploy/
├── main.py                  # entry point: from src.deploy.predict import app
├── requirements-serve.txt   # runtime deps only
├── render.yaml              # Render infrastructure-as-code config
├── config.yaml              # optional; predict.py falls back to defaults
├── src/
│   ├── __init__.py
│   └── deploy/
│       ├── __init__.py      # REQUIRED for package import
│       └── predict.py       # FastAPI app (routes, model cache, HTML UI)
├── models/
│   ├── feature_schema.json  # crop list, feature list, model filenames
│   ├── dt_*.pkl             # 15 decision-tree models
│   └── xgb_*.pkl            # 15 XGBoost models
└── data/interim/train.csv   # optional; UI input defaults only
```

### `render.yaml`

```yaml
services:
  - type: web
    name: crop-yield-api
    runtime: python
    branch: deploy
    buildCommand: pip install -r requirements-serve.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    healthCheckPath: /health
    autoDeploy: true
```

Key points:

- `startCommand` binds `0.0.0.0` and uses Render's injected `$PORT` — required,
  otherwise Render reports *"No open ports detected"*.
- `healthCheckPath: /health` lets Render decide when the service is live.
- `branch: deploy` makes Render build from the orphan branch, not `main`.

### Verifying the deployment

```bash
BASE=https://ftl-syria-crop-yield.onrender.com

curl -s $BASE/health          # → {"status":"ok","models_loaded":30}
curl -s -o /dev/null -w "%{http_code}\n" $BASE/        # → 200 (HTML UI)
curl -s -o /dev/null -w "%{http_code}\n" $BASE/docs    # → 200 (Swagger)

curl -s -X POST $BASE/predict \
  -H "Content-Type: application/json" \
  -d '{"crop":"Wheat","model":"xgb","features":{...}}'
```

### Known operational notes

- **Free-tier memory:** preloading all 30 `.pkl` files can OOM on Render's
  512 MB free tier. Mitigation: upgrade to Starter (1 GB), or disable
  `CACHE.preload_all()` so models load lazily on first request per
  `(crop, model)` pair.
- **Cold starts:** the free tier sleeps after 15 min idle; the first request
  after idle takes ~30–60 s.
- **Common failure:** `ModuleNotFoundError: No module named 'src.deploy.predict'`
  almost always means `src/deploy/__init__.py` was not committed to the
  `deploy` branch. Verify with `git ls-files src/deploy` — both `__init__.py`
  and `predict.py` (lowercase) must be listed.

Full deployment instructions, troubleshooting, and the deploy checklist are
maintained in the new repository.

---

## 🙏 Acknowledgements

This project was made possible by the **FTL Syria Programme — AI for Climate**
Machine Learning Challenge, and by the collaboration of our **Group 4** team
members: Nimra Afzaal, Sular Albalkhi, Zaid Aldeen Mohammad Kiki, and Ahmad
Deeb.

We also thank the open data providers — **FAO** (FAOSTAT) and **NASA** (POWER) —
for making their datasets publicly available.

---

## 📬 Contact

For questions about this project, please reach out to any team member. The
primary maintainer is **Ahmad Deeb** —
[ahmaddeebdev@gmail.com](mailto:ahmaddeebdev@gmail.com) ·
[GitHub](https://github.com/AhmedGDeeb).
```