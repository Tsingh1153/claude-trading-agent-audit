from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT/"private"/"decisions.jsonl"
OUT = ROOT/"data"/"decisions_public.csv"

KEEP = ["ts", "symbol", "action", "price", "entry", "stop", "target",
        "stated_rr", "horizon_days", "reason_tags", "rules_invoked", ""
        "prompt_version", "model"]

df = pd.read_json(RAW, lines=True)
public = df[KEEP].copy()
public["ts"] = (pd.to_datetime(public["ts"], utc=True)
                .dt.tz_convert("America/New_york")
                .dt.strftime("%Y-%m-%d %H:%M"))
public["stated_rr"] = public["stated_rr"].round(2)

public.to_csv(OUT, index=False)
print(len(public), "records written to", OUT.relative_to(ROOT))
