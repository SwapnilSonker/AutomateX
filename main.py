from playwright.async_api import async_playwright
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

usernameX = os.getenv("usernameX")
passwordX = os.getenv("passwordX")

print(usernameX)
print(passwordX)
async def login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=['--start-maximized'], slow_mo=1000)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True)
        page = await context.new_page()
        
        try:
            print("into the login page")
            await page.goto('https://x.com/i/flow/login?redirect_after_login=%2Fhome', timeout=60000)
            print("login page reached")
            
            signIn = page.locator('//span[contains(text(), "Sign in")]')
            await signIn.wait_for(state='visible')
            
            print("signIn field found")
            await asyncio.sleep(1)
            await signIn.click()
            await asyncio.sleep(22)
            print("button clicked")
            
            username = page.locator('input[type=text]')
            await username.wait_for(state='visible')
            await asyncio.sleep(1)
            await username.fill(usernameX)
            print("username filled")
            await asyncio.sleep(5)
            
            nextbutton = page.locator('//span[contains(text(), "Next")]')
            await asyncio.sleep(1)
            await nextbutton.click()
            await asyncio.sleep(8)
            
            password = page.locator('input[type=password]')
            await password.click()
            await asyncio.sleep(1)
            await password.fill(passwordX)
            print("password filled")
            
            login = page.locator('//span[contains(text(), "Log in")]')
            await login.click()
            await asyncio.sleep(20)
            
            print("searching like button")
            like = page.locator('//button[@data-testid="like"]')
            print("like button found")
            
            reply = page.locator('//button[@data-testid="reply"]')
            print("reply button found")
            
            tweet_box = page.locator("(//div[@data-testid='tweetTextarea_0'])")
            
            for i in range(3):
            
                await asyncio.sleep(1)
                
                await like.nth(i).click()
                print("like button clicked")
                
                await reply.nth(i).click()
                await asyncio.sleep(1)
                await tweet_box.click()
                print("reply section found")
                
               
                
                
                await page.evaluate("window.scrollBy(0, 300)")
            
            await asyncio.sleep(10)
            
            await context.tracing.stop(path='trace.zip')
            await browser.close()
        except Exception as e:
            print(f"An error occurred: {e}")
            
asyncio.run(login())            