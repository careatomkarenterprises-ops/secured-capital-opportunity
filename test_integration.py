import os
import sys
from strategy_advisory_generator import generate_strategy_advisory, fetch_market_news

def run_diagnostic():
    print("=" * 50)
    print("🔍 OMKAR SERVICES: INTEGRATION DIAGNOSTIC")
    print("=" * 50)

    # 1. Check API Key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY not found in environment variables.")
        print("   Fix: Run 'set GEMINI_API_KEY=your_key_here' on Windows")
        return
    print("✅ Gemini API Key: Found")

    # 2. Test News API
    print("\n📡 Testing News API Connectivity...")
    try:
        title, desc = fetch_market_news()
        print(f"✅ News API: Success")
        print(f"   Current Headline: {title}")
    except Exception as e:
        print(f"❌ News API: Failed - {str(e)}")

    # 3. Test Full Generation
    print("\n🤖 Testing AI Content Generation & File Saving...")
    try:
        # This calls your actual logic
        slug = generate_strategy_advisory()
        if slug:
            print(f"✅ Generation: Success")
            print(f"   File Created: blog/post/{slug}.html")
            
            # Verify file exists
            if os.path.exists(f"blog/post/{slug}.html"):
                print("✅ File Integrity: Verified on Disk")
            else:
                print("❌ File Integrity: Path not found (Check FileManager settings)")
        else:
            print("❌ Generation: Failed (Check Gemini API limits)")
    except Exception as e:
        print(f"❌ Script Error: {str(e)}")

    print("\n" + "=" * 50)
    print("🏁 DIAGNOSTIC COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    run_diagnostic()
