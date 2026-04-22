# L10 - AI Agents in Production: Observability with Microsoft Agent Framework
# Source: https://github.com/microsoft/ai-agents-for-beginners/tree/main/10-ai-agents-production

from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass


# Manual span creation with Langfuse Python SDK
# pip install langfuse
from langfuse import get_client

langfuse = get_client()

span = langfuse.start_span(name="my-span")

span.end()
