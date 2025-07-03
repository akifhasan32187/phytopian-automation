const { chromium } = require('playwright');
const delay = ms => new Promise(res => setTimeout(res, ms));

(async () => {
  // Launch browser and open new page with a large window (simulate maximize)
  const browser = await chromium.launch({
    headless: false,
    args: ['--start-maximized']
  });

  const context = await browser.newContext({
    viewport: null  // allow full native resolution
  });

  const page = await context.newPage();

  // Go to login page
  await page.goto('https://app.phytopian.com/login');

  // Fill email
  await page.locator('.MuiInputBase-input').first().fill('company@phytopian.com');
  await delay(3000);

  // Fill password
  await page.locator('.MuiInputBase-inputAdornedEnd').fill('12345678');
  await delay(3000);

  // Click login button
  await page.locator('.MuiButton-containedPrimary').click();
  await delay(5000); // Wait for popup

  // Click "OK" popup using coordinates (adjust if needed)
  await page.mouse.click(856, 347);
  await delay(3000);

  // Click avatar
  await page.locator('.MuiAvatar-img').click();
  await delay(3000);

  // Scroll logout button into view using JS + click
  const logoutLocator = page.locator('.MuiButton-containedError');
  await logoutLocator.waitFor({ state: 'visible' });

  // Scroll into view using page.evaluate()
  const logoutHandle = await logoutLocator.elementHandle();
  await page.evaluate(el => el.scrollIntoView({ behavior: 'smooth', block: 'center' }), logoutHandle);
  await delay(1500);

  // Click logout
  await logoutLocator.click();
  await delay(3000);

  // Close browser
  await browser.close();
})();
