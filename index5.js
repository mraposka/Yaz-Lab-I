const puppeteer = require('puppeteer');
const fs = require('fs');
let x=true;
let y=true;
(async () => {
    const scriptContent = fs.readFileSync('tooltip.js', 'utf8');
    const browser = await puppeteer.launch({
        headless: true,
        args: [`--window-size=1920,1080`],
        defaultViewport: {
            width: 1920,
            height: 1080
        }
    });

    for (let _i = 4; _i < 5; _i++) {
        for (let _j = 0; _j < 22; _j++) {
            if(x){
                _j=11; x=false;
            }
            for (let _k = 0; _k < 5; _k++) {
                if(y){
                    _k=2; y=false;
                }
                for (let _p = 0; _p < 20; _p++) {
                    if(z){
                        _p=13; z=false;
                    }
                    const page = await browser.newPage();
                    page.on('console', msg => {
                        // Log each argument from the console
                        msg.args().forEach(async (arg) => {
                            const value = await arg.jsonValue();
                            //console.log(value);
                            try {
                                fs.appendFile('output5.txt', value + '\n', (err) => {
                                    if (err) {
                                        console.error('Error writing to file:', err);
                                    } else {
                                        //console.log('File has been written');
                                    }
                                });
                            }catch{}
                        });
                    });
                    const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
                    let sleepms = 300;

                    await page.goto('https://f1-tempo.com');

                    async function selectOption(page, xpath, indexToSelect, pilot) {
                        try {
                            await page.click('xpath/' + xpath);
                            if (pilot) {
                                for (let i = 0; i < indexToSelect; i++) {
                                    //await console.log("Arrow");
                                    await page.keyboard.press('ArrowDown');
                                    await sleep(sleepms);
                                }
                                await page.keyboard.press('Enter');
                                return;
                            }
                            for (let i = 0; i < indexToSelect; i++) {
                                //await console.log("Arrow&enter" + indexToSelect);
                                await page.keyboard.press('ArrowDown');
                                await sleep(sleepms);
                                await page.keyboard.press('Enter');
                            }
                        } catch (error) {
                            console.error(`Seçim sırasında hata: ${error.message} Index: ${indexToSelect}`);
                        }
                    }

                    async function moveMouse(page, xpath) {
                        try {
                            const [element] = await page.$$(xpath);
                            if (!element) {
                                console.log('XPath öğesi bulunamadı!');
                                return;
                            }

                            const box = await element.boundingBox();
                            if (!box) {
                                console.log('Öğe boyutu alınamadı!');
                                return;
                            }

                            const startX = box.x;
                            const endX = box.x + box.width;
                            const y = box.y + box.height / 2;

                            // Sol tık basılı tutarak sağa doğru hareket etme
                            //await page.mouse.move(startX, y);

                            await page.mouse.down(); // Sol tık basılı tut
                            for (let x = startX; x <= endX; x += 1) {
                                await page.mouse.move(x, y);
                                await sleep(sleepms / 200);
                            }
                            for (let x = endX; x >= startX; x -= 0.5) {
                                await page.mouse.move(x, y);
                                await sleep(sleepms / 200);
                            }

                            //await page.mouse.up(); // Sol tıkı bırak

                        } catch (error) {
                            console.error(`Mouse Move sırasında hata: ${error.message}`);
                        }
                    }

                    await sleep(sleepms);
                    await selectOption(page, "html/body/div/div[1]/body/div/div/div[1]/div/div[1]/div/div", _i, true);
                    await sleep(sleepms);
                    await selectOption(page, "html/body/div/div[1]/body/div/div/div[1]/div/div[2]/div/div", _j, true);
                    await sleep(sleepms);
                    await selectOption(page, 'html/body/div/div[1]/body/div/div/div[1]/div/div[3]/div/div/div[1]/div', _k, true);
                    await sleep(sleepms);
                    await selectOption(page, "/html/body/div/div[1]/body/div/div/div[1]/div/div[4]/div/div/div[1]/div", _p, true);
                    await sleep(sleepms * 5);

                    await page.evaluate(scriptContent);

                    await moveMouse(page, "xpath/html/body/div/div[1]/body/div/div/div[2]/div/div[1]");
                    await sleep(sleepms);
                    await console.log("Done For " + _i + "," + _j + "," + _k + "," + _p);
                    await page.evaluate("console.log('Done For " + _i + "," + _j + "," + _k + "," + _p + "');");
                    await page.close();
                    await console.log("Waiting for cache clearing...");
                    //await sleep(sleepms*10);
                    await console.log("Cache cleaned, starting to new iteration...");
                }
            }
        }
    }
    await console.log("Done!");
    /*
    YIllar:7
    Pistler:22
    Pilot:20
    Şimdi şöyle
    birden fazla pilot ekleyince arada veri kaçıyor o yüzden 1er 1er yaptım
    ilk pilotu ekleyip sonra silip sonra ikincisini eklettirmiyor çünkü oradaki çarpı butonlarına bastırmıyor allah kahretsinki
    full xpath vermeyince bulamıyor çünkü aynı class çok nesnede var ve class isimleri dinamik olabiliyor
    pilotları toplu çekebiliyorum ama tek tek çekince daha sağlam oluyor.
    sleepms azaltılırsa daha hızlı çalışır fakat min 100 olsun bence(internet hızına göre değişebiliyor)
    aynı zamanda site arkada curl atıyor daha detaylı datalara erişebiliyoruz ama web scrapping ile bu şekilde oluyor geliştirilebilir tabii
    */
})();
