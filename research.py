#!/usr/bin/env python3
"""
Research Script - Build Your Own Perplexity
Performs 1-depth web search and AI-powered analysis using Cerebras and Exa APIs.
Extracts at least 5 sources and synthesizes them into a comprehensive answer.
"""

import os
import sys
from exa_py import Exa
from cerebras.cloud.sdk import Cerebras


def setup_clients():
    """Initialize API clients with credentials from environment variables"""
    exa_api_key = os.environ.get("EXA_API_KEY")
    cerebras_api_key = os.environ.get("CEREBRAS_API_KEY")
    
    if not exa_api_key:
        print("❌ Error: EXA_API_KEY environment variable not set")
        sys.exit(1)
    
    if not cerebras_api_key:
        print("❌ Error: CEREBRAS_API_KEY environment variable not set")
        sys.exit(1)
    
    client = Cerebras(api_key=cerebras_api_key)
    exa = Exa(api_key=exa_api_key)
    
    return client, exa


def search_web(exa, query, num=5):
    """Search the web using Exa's auto search"""
    result = exa.search_and_contents(
        query,
        type="auto",
        num_results=num,
        text={"max_characters": 1000}
    )
    return result.results


def ask_ai(client, prompt):
    """Get AI response from Cerebras"""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-4-scout-17b-16e-instruct",
        max_tokens=600,
        temperature=0.2
    )
    return chat_completion.choices[0].message.content


def research_topic(client, exa, query):
    """Main research function that orchestrates the entire process"""
    print(f"🔍 Researching: {query}")
    
    results = search_web(exa, query, 5)
    print(f"📊 Found {len(results)} sources")
    
    sources = []
    for result in results:
        content = result.text
        title = result.title
        if content and len(content) > 200:
            sources.append({
                "title": title,
                "content": content
            })
    
    print(f"📄 Scraped {len(sources)} sources")
    
    if not sources:
        return {"summary": "No sources found", "insights": []}
    
    context = f"Research query: {query}\n\nSources:\n"
    for i, source in enumerate(sources[:4], 1):
        context += f"{i}. {source['title']}: {source['content'][:400]}...\n\n"
    
    prompt = f"""{context}

Based on these sources, provide:
1. A comprehensive summary (2-3 sentences)
2. Three key insights as bullet points

Format your response exactly like this:
SUMMARY: [your summary here]

INSIGHTS:
- [insight 1]
- [insight 2]
- [insight 3]"""
    
    response = ask_ai(client, prompt)
    print("🧠 Analysis complete")
    
    return {"query": query, "sources": len(sources), "response": response}


def main():
    """Main entry point for the research script"""
    if len(sys.argv) < 2:
        print("Usage: python research.py <query>")
        print('Example: python research.py "latest AI breakthroughs"')
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    
    print("✅ Setting up API clients...")
    client, exa = setup_clients()
    print("✅ Setup complete\n")
    
    result = research_topic(client, exa, query)
    
    print("\n" + "=" * 50)
    print("RESEARCH RESULTS")
    print("=" * 50)
    print(f"Query: {result['query']}")
    print(f"Sources analyzed: {result['sources']}")
    print(f"\n{result['response']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
