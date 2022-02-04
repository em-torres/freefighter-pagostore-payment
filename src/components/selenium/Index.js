const {Builder, By, Key, until} = require('selenium-webdriver');


function Selenium() {
  // const webdriver = require("selenium-webdriver");
  // const driver = new webdriver.Builder().forBrowser("firefox").build();
  // // Instantiate a web browser page
  // driver.navigate().to("Yahoo");

  // const By = webdriver.By; // useful Locator utility to describe a query for a WebElement
  // driver.navigate().to("Yahoo")
  // .then(() => driver.findElement(By.css("#login-username")))
  // .then(element => element.getAttribute("value"))
  // .then(value => console.log(value));

  return (
    <div className="Selenium">
      <p>Hola Mundo</p>
    </div>
  );
}

export default Selenium;
