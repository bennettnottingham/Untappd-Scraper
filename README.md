# Untappd-Scraper

**Project Description: Scraping Top-Rated Beers from Untappd by Style and Country**

In this project, I created a web scraping script using Python and libraries like Requests and BeautifulSoup to extract information about top-rated beers from the website "https://untappd.com/beer/top_rated." The main goal of the project was to gather data about the best-rated beers categorized by different beer styles across various countries.

**Project Overview:**

The project involved two main functions:

1. **`get_styles()`**: This function was responsible for retrieving a list of beer styles from the website's filter options. It used web scraping techniques to fetch the available styles, excluding some specific categories such as 'Historical' styles. The extracted styles were then processed and formatted for further use.

2. **`get_beer_data(beer_type)`**: This function took a beer style as a parameter and fetched the top-rated beers within that style. It sent an HTTP request to the website's URL with the specific beer style as a query parameter. The response HTML content was parsed using BeautifulSoup to extract relevant information such as beer name, brewery, ABV (alcohol by volume), rating, and the number of ratings. The extracted data for each beer was then structured and stored in a list.

**Implementation:**

The script utilized the Requests library to send HTTP requests and retrieve web content. BeautifulSoup was used to parse the HTML and navigate through the DOM elements to locate and extract the desired information.

The main steps of the project included:
- Fetching the list of available beer styles using the `get_styles()` function.
- Iterating through the list of styles and using the `get_beer_data(beer_type)` function to scrape the top-rated beers for each style.
- Storing the extracted beer data in a structured format, such as dictionaries within a list.

**Output:**

The output of the script, based on the provided code, is a series of dictionaries containing information about top-rated beers within various styles. Here's an example of the printed output:

<img width="1164" alt="Screenshot 2023-08-25 at 10 01 25 AM" src="https://github.com/bennettnottingham/Untappd-Scraper/assets/65934399/4e1d6ab1-6950-4c2a-8079-383ba4536602">


**Data Volume:**

It's important to note that the code, as provided, retrieves data for over 11,000 rows of top-rated beers, spanning various styles and breweries.

**Data Export:**

To further utilize the extracted data, it can be saved to a CSV file. This would allow for easy sharing, analysis, and integration into other applications. By uncommenting the relevant parts of the code that create a DataFrame and save it to a CSV file, the project can seamlessly transition from data extraction to data storage and utilization.

**Conclusion:**

By utilizing web scraping techniques, the project successfully scraped data about the top-rated beers across different styles available on the Untappd website. This small-scale project showcases the application of Python libraries to gather valuable information from online sources, and it has the potential to serve as a foundation for further analysis, visualization, or integration into other applications related to beer recommendations, reviews, or insights.
