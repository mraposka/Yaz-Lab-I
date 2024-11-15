# Formula 1 Telemetry Data Analysis

This project is designed to automatically collect historical Formula 1 race data from a dynamic web interface. Using **Node.js** as the sole backend technology, data for specific combinations of year, circuit, race, and driver are retrieved and saved in a processable format for detailed analysis.

---

## Features

- **Dynamic Web Scraping**: Collects data from an interactive web interface.
- **Custom Selections**: Allows filtering by year, circuit, race, and driver.
- **Graph Data Extraction**: Captures data by scanning the graph using mouse movements.
- **Export Options**: Saves collected data in `.txt` format.

---

## Technologies Used

- **Node.js**: Core framework for browser control, dynamic selection, and data extraction.
- **Puppeteer**: Handles browser automation and HTML element interaction.
- **Custom Tooltip Handler (tooltip.js)**: A JavaScript module for extracting data from interactive graphs.

---

## Workflow

### 1. **Selection Steps**

The user makes sequential selections for year, circuit, race, and driver. For instance, with the selection `Done for 4,1,2,16`:

- **Year**: 4th index → 2020  
- **Circuit**: 1st index  
- **Race**: 2nd index  
- **Driver**: 16th index  

### 2. **Capturing Graph Data**

- Data is displayed only during mouse movements over the graph.
- The mouse is programmatically moved from the leftmost to the rightmost position of the graph's `div` element, capturing data every 1 pixel.
- To ensure no data is missed, a reverse movement of 0.5 pixels is performed at the far right.

### 3. **Processing Tooltip Data**

- As the mouse moves, tooltip elements with the `custom-tooltip` class are generated dynamically.
- The `tooltip.js` module extracts information from the `<p>` tags within these tooltips and logs the data to the console.

### 4. **Saving Data via Node.js**

- Data logged to the browser console is captured using the `page.on('console')` event listener in Node.js.
- This data is then written to a `.txt` file for further use.

### 5. **Parallel Processing for Efficiency**

- Due to the time-consuming nature of data collection, multiple `indexX.js` files are created to scrape data from different starting points simultaneously.  
  Examples:  
  - `index6.js` → Begins collecting data from the 5th year.  
  - `index5.js` → Begins collecting data from the 4th year.  

---

## How to Run

1. Clone this repository.
2. Install dependencies with `npm install`.
3. Run individual index files for data collection:  
   ```bash
   node index.js
   ```
4. Collected data will be saved as `.txt` files in the output directory.

---

## Future Improvements

- Automating parallel processing for all year indices.
- Adding support for exporting data in additional formats like `.csv` or `.json`.
- Improving graph data extraction to handle non-linear movement scenarios.

--- 

Feel free to contribute or suggest new features! 😊
