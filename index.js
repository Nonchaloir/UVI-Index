const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox']
  });

  const page = await browser.newPage();
  await page.goto('https://www.nea.gov.sg/corporate-functions/weather/ultraviolet-index', {
    waitUntil: 'networkidle2'
  });

  // Wait for the UV index element to appear
  await page.waitForSelector('.uvindexlevel');

  const uvIndex = await page.evaluate(() => {
    const el = document.querySelector('.uvindexlevel');
    return el ? el.innerText : 'Not found';
  });

  console.log('UV Index:', uvIndex);

  await browser.close();
})();
