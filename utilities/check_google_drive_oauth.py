import json
import os
from pathlib import Path

REQUIRED_SCOPE = "https://www.googleapis.com/auth/drive"
SECRETS_PATH = Path.home() / ".credentials" / "client_secrets.json"
CREDENTIALS_PATH = Path("credentials.json")  # Default for PyDrive

def check_secrets_file(path):
    print(f"\n🔍 Checking client_secrets.json at: {path}")
    if not path.exists():
        print("❌ File not found.")
        return False

    with open(path, "r") as f:
        data = json.load(f)

    try:
        info = data["installed"]
        client_id = info["client_id"]
        redirect_uris = info.get("redirect_uris", [])
        print(f"✅ Found client_id: {client_id}")

        if not any("localhost" in uri for uri in redirect_uris):
            print("⚠️ Warning: redirect_uris may be misconfigured (no localhost).")
        else:
            print("✅ redirect_uris look okay.")

        return True
    except KeyError:
        print("❌ File is not formatted for a Desktop App (missing 'installed' key).")
        return False

def check_scope_in_consent_screen():
    print("\n🔍 IMPORTANT: Make sure you added this scope in the Google Cloud Console → OAuth Consent Screen:")
    print(f"    🔗 {REQUIRED_SCOPE}")
    print("You must add it under 'Scopes for Google APIs'.")

def offer_to_delete_stale_credentials():
    print("\n🧹 Checking for stale credential files...")
    deleted = False

    for file_path in [CREDENTIALS_PATH, Path("token.json")]:
        if file_path.exists():
            resp = input(f"⚠️ Found {file_path}. Delete it and re-authenticate? (y/n): ").strip().lower()
            if resp == "y":
                file_path.unlink()
                print(f"✅ Deleted {file_path}")
                deleted = True

    if not deleted:
        print("✅ No stale credentials were deleted.")
    else:
        print("🗝️ You should now re-run your authentication (e.g., PyDrive `LocalWebserverAuth()`)")

def main():
    print("🛠️ Google Drive API Setup Diagnostic Tool")

    if not check_secrets_file(SECRETS_PATH):
        print("➡️ Tip: Download a Desktop OAuth client secret file from Google Cloud Console.")
        print("📁 Place it at:", SECRETS_PATH)
        return

    check_scope_in_consent_screen()
    offer_to_delete_stale_credentials()

    print("\n✅ Done! You're now ready to run your PyDrive or Drive API code.")

if __name__ == "__main__":
    main()