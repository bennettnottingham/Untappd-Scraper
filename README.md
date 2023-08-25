# Untappd-Scraper

**Project Description: Scraping Top-Rated Beers from Untappd by Style and Country**

In this project, I created a web scraping script using Python, leveraging libraries like Requests and BeautifulSoup, to extract information about top-rated beers from the website "https://untappd.com/beer/top_rated." The primary objective was to compile data about the highest-rated beers categorized by various beer styles across different countries.

**Project Overview:**

The project encompassed the development of two core functions:

1. **`get_styles()`**: I designed this function to acquire a list of available beer styles from the filter options on the website. Employing web scraping techniques, I retrieved the styles, while intentionally excluding specific categories such as 'Historical' styles. Subsequently, I formatted and processed the extracted styles for ease of use.

2. **`get_beer_data(beer_type)`**: By passing a beer style as a parameter, this function gathered data about the top-rated beers within that particular style. To achieve this, I sent an HTTP request to the website's URL with the designated beer style as a query parameter. I employed the BeautifulSoup library to parse the HTML response, facilitating the extraction of crucial details such as beer name, brewery, ABV (alcohol by volume), rating, and the number of ratings. I then systematically structured the gathered data into a list.

**Implementation:**

I employed the Requests library to facilitate the transmission of HTTP requests and the retrieval of web content. To align with my specific device, I personalized the user agent by omitting the default one. Moreover, I discovered an innovative approach to circumvent the login screen. By converting a cURL request using an online converter tool (https://curlconverter.com/), I effortlessly obtained the necessary request format, eliminating the need to contend with intricate login procedures.

Throughout the project, I executed the following key steps:
- Acquiring a list of available beer styles through the `get_styles()` function.
- Iterating through the styles list and utilizing the `get_beer_data(beer_type)` function to extract data on the top-rated beers for each style.
- Organizing the extracted beer data systematically, using dictionaries nested within a list.

**Output:**

The output of the script, as per the provided code, comprises a collection of dictionaries, each containing pertinent information about the highest-rated beers across various styles. The extracted data is presented in the format exemplified earlier.

**Data Volume:**

My implementation successfully procured data for over 11,000 rows of top-rated beers. This extensive dataset encompasses a wide range of styles and breweries.

**Data Export:**

To enhance the utilization of the extracted data, I incorporated the capability to save it in CSV format. This facilitates seamless sharing, in-depth analysis, and integration into diverse applications.

**Note on User Agent and Login Bypass:**

To align with my device, I personalized the user agent by excluding the default setting. Additionally, I circumvented the login screen by skillfully converting a cURL request through the online converter tool (https://curlconverter.com/). This innovative tactic provided me with the precise request format, eliminating the complexities of dealing with the login process.

**Conclusion:**

This project underscores my resourcefulness in employing web scraping techniques to harvest valuable data from online sources. By combining personalized headers, cURL conversion, and Python scripting, I engineered an effective data extraction system. This accomplishment serves as a strong foundation for further exploration and utilization of the procured beer data—whether for comprehensive analysis, dynamic visualization, or integration into applications catering to beer enthusiasts and aficionados.
