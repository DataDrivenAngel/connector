"""
FastMCP Echo Server
"""

from fastmcp import FastMCP

# Create server
mcp = FastMCP("Excella Demo MCP Server")



@mcp.resource("insights://static")
def excella_insights() -> str:
    """Returns a list of recent insights from Excella's blog"""

    insights = [
    {
        "url": "https://www.excella.com/resource/harnessing-genai-for-mission-success",
        "description": "Practical strategies for successful GenAI adoption that aligns with mission goals, cutting through the hype to help organizations determine if, when, and how to implement GenAI effectively."
    },
    {
        "url": "https://www.excella.com/insights/the-5-essentials-for-ai-assisted-fraud-prevention", 
        "description": "How AI transforms fraud detection from reactive to proactive by enhancing human expertise rather than replacing it, focusing on protecting taxpayer dollars with modern approaches."
    },
    {
        "url": "https://www.excella.com/insights/the-new-playbook-for-fraud-prevention-building-a-strong-foundation",
        "description": "A modernization guide for federal agencies to combat increasingly complex fraud strategies using AI and data analytics to proactively detect and prevent fraud while meeting mission requirements."
    },
    {
        "url": "https://www.excella.com/resource/ai-to-combat-fraud-hhs",
        "description": "Case study of how HHS Office of Inspector General partnered with Excella to introduce AI and automation through the Contracts & Grants Analytics Portal (CGAP) to oversee $1T in taxpayer funds and combat fraud, waste, and abuse."
    }
]

    return insights


@mcp.tool
def excella_insights() -> str:
    """Returns a list of recent insights from Excella's blog"""

    insights = [
    {
        "url": "https://www.excella.com/resource/harnessing-genai-for-mission-success",
        "description": "Practical strategies for successful GenAI adoption that aligns with mission goals, cutting through the hype to help organizations determine if, when, and how to implement GenAI effectively."
    },
    {
        "url": "https://www.excella.com/insights/the-5-essentials-for-ai-assisted-fraud-prevention", 
        "description": "How AI transforms fraud detection from reactive to proactive by enhancing human expertise rather than replacing it, focusing on protecting taxpayer dollars with modern approaches."
    },
    {
        "url": "https://www.excella.com/insights/the-new-playbook-for-fraud-prevention-building-a-strong-foundation",
        "description": "A modernization guide for federal agencies to combat increasingly complex fraud strategies using AI and data analytics to proactively detect and prevent fraud while meeting mission requirements."
    },
    {
        "url": "https://www.excella.com/resource/ai-to-combat-fraud-hhs",
        "description": "Case study of how HHS Office of Inspector General partnered with Excella to introduce AI and automation through the Contracts & Grants Analytics Portal (CGAP) to oversee $1T in taxpayer funds and combat fraud, waste, and abuse."
    }
]

    return insights