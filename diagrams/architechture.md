                     ┌─────────────┐
                     │    User     │
                     └──────┬──────┘
                            │
                            ▼
                  ┌─────────────────┐
                  │  Streamlit App  │
                  └────────┬────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Coordinator Agent   │
                └───────┬─────────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Eligibility │ │   Scheme    │ │ Explainer   │
│   Agent     │ │   Agent     │ │   Agent     │
└──────┬──────┘ └──────┬──────┘ └─────────────┘
       │               │
       │               ▼
       │      ┌─────────────────┐
       │      │  Scheme Server  │
       │      └────────┬────────┘
       │               │
       ▼               ▼
      schemes.json Government Data

────────────────────────────────────

Document Agent
       │
       ▼
Planner Agent
       │
       ▼
Report Agent
       │
       ▼
PDF Report