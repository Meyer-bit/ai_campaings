from fastapi import FastAPI
from src.collect_data import collect_ads_data
from src.analyze import analyze_campaigns
from src.decision_maker import save_decisions

app = FastAPI()

# memória simples (pra Power BI)
PIPELINE_RESULT = []

@app.post("/pipeline/run")
def run_pipeline():
    global PIPELINE_RESULT

    df = collect_ads_data()
    decisions = analyze_campaigns(df)
    save_decisions(decisions)

    result = []
    for status, items in decisions.items():
        for item in items:
            result.append({
                "campanha": item["campanha"],
                "status": status,
                "motivo": item["motivo"]
            })

    PIPELINE_RESULT = result
    return {"status": "ok", "total": len(result)}

@app.get("/pipeline/results")
def get_results():
    return PIPELINE_RESULT

