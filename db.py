import os
from supabase import create_client

def get_client():
    return create_client(
        os.environ.get("SUPABASE_URL", ""),
        os.environ.get("SUPABASE_KEY", "")
    )

def load_notebook(name="default"):
    result = get_client().table("expert_agents").select("*").eq("name", name).execute()
    return result.data[0] if result.data else None

def save_notebook(name, data):
    supabase = get_client()
    existing = load_notebook(name)
    if existing:
        supabase.table("expert_agents").update({"notebook_data": data}).eq("name", name).execute()
    else:
        supabase.table("expert_agents").insert({"name": name, "notebook_data": data}).execute()
