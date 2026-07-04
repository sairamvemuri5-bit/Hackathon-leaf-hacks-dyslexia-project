import httpx
import json

def test_endpoints():
    print("Starting API integration tests for DyslexiEase...")
    
    test_text = "The Water Cycle is how water moves all around Earth. First, the sun warms up the water in lakes, rivers, and oceans. This turns liquid water into vapor."
    
    # Test Comic Generation Endpoint (Heuristic fallback mode since no API key is set)
    print("\n--- Testing /api/generate-comic ---")
    try:
        response = httpx.post("http://127.0.0.1:8000/api/generate-comic", json={
            "text": test_text
        }, timeout=10.0)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("Response contains panels:")
            for panel in data.get("panels", []):
                print(f"Panel {panel['panel_number']}:")
                print(f"  Text: {panel['text']}")
                print(f"  Caption: {panel['caption']}")
                print(f"  Prompt: {panel['prompt']}")
                print(f"  Image URL: {panel['image_url'][:70]}...")
            print("SUCCESS: Comic generation works!")
        else:
            print(f"FAILURE: Got status {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"ERROR: Comic request failed: {e}")
        
    # Test Recommendations Endpoint
    print("\n--- Testing /api/recommendations ---")
    try:
        response = httpx.post("http://127.0.0.1:8000/api/recommendations", json={
            "text": test_text
        }, timeout=10.0)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Extracted Topic: {data.get('topic')}")
            print("Recommendations:")
            for rec in data.get("recommendations", []):
                print(f"  - Title: {rec['title']} ({rec['source']})")
                print(f"    URL: {rec['url']}")
            print("SUCCESS: Recommendations search works!")
        else:
            print(f"FAILURE: Got status {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"ERROR: Recommendations request failed: {e}")

if __name__ == "__main__":
    test_endpoints()
