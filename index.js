const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

    // Web sayfasına gidin
    await page.goto('https://f1-tempo.com');

    // Seçim işlemi için fonksiyon
    async function selectOption(page, xpath, indexToSelect, pilot) {
        try {
            await page.click('xpath/' + xpath);
            if (pilot) {
                for (let i = 0; i < indexToSelect; i++) {
                    await console.log("Arrow");
                    await page.keyboard.press('ArrowDown'); // Aşağı ok tuşuna bas
                    await sleep(200);
                }
                await page.keyboard.press('Enter');
                return;
            }
            for (let i = 0; i < indexToSelect; i++) {
                await console.log("Arrow&enter" + indexToSelect);
                await page.keyboard.press('ArrowDown');
                await sleep(200);
                await page.keyboard.press('Enter');
            }
        } catch (error) {
            console.error(`Seçim sırasında hata: ${error.message} Index: ${indexToSelect}`);
        }
    }

    // Yıl seçimi
    await sleep(200);
    await selectOption(page, "html/body/div/div[1]/body/div/div/div[1]/div/div[1]/div/div", 0,true);//2.indis seçildi yılda

    // Pist seçimi
    await sleep(200);
    await selectOption(page, "html/body/div/div[1]/body/div/div/div[1]/div/div[2]/div/div", 2,true);//2.indis seçildi pistte

    // Session seçimi
    await sleep(200);
    await selectOption(page, 'html/body/div/div[1]/body/div/div/div[1]/div/div[3]/div/div/div[1]/div', 2,true);//0.indis seçildi sessionda
    // Pilot seçimi
    await sleep(200);
    await selectOption(page, "/html/body/div/div[1]/body/div/div/div[1]/div/div[4]/div/div/div[1]/div", 20, false);//7 pilot seçildi


    await console.log("Done!");
    // await browser.close();
})();
