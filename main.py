from playwright.async_api import async_playwright
import asyncio

async def login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=['--start-maximized'])
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
            await signIn.click()
            await asyncio.sleep(22)
            print("button clicked")
            
            username = page.locator('input[type=text]')
            await username.wait_for(state='visible')
            await username.fill('username')
            print("username filled")
            await asyncio.sleep(5)
            
            nextbutton = page.locator('//span[contains(text(), "Next")]')
            await nextbutton.click()
            await asyncio.sleep(8)
            
            password = page.locator('input[type=password]')
            await password.click()
            await password.fill('password')
            print("password filled")
            
            login = page.locator('//span[contains(text(), "Log in")]')
            await login.click()
            await asyncio.sleep(40)
            
            await context.tracing.stop(path='trace.zip')
            await browser.close()
        except Exception as e:
            print(f"An error occurred: {e}")
            
asyncio.run(login())            