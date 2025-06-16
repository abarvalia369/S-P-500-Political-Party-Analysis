Correlation Between Stock Market Trends and
Political Party in Office
Jonathan John(jjj116) and Arpeet Barvalia(aab353)
March 2025
1 Research Question and Motivation
• Clearly state the research question you aim to answer.
– ”How does the stock market performance change when under Demo-
cratic presidencies vs when under Republican presidencies?”
• Provide context and motivation for why this question is important or
interesting.
– The relationship between the performance of the stock market, and
the party that is in office, is a topic that is widely debated. This
is because it gives a very meaningful insight to the level of success
that party had during it’s term in office. The clear cut differences in
political parties lead to different sides of the debate privy that each
party can positively effect some aspect of the market. We see that it
is commonly believed that the deregulation of the Republican party
creates an environment that is favorable for a positive overall trend
of the economic business and the stock market mirrors that. While
on the other hand, some may say that the the stock market seems to
diversify and impact different sectors than usual, when the United
states in under the presidency of the Democratic Party.
– The motivation for this project is to make statistically significant
claims about the state of the stock market, differentiated by the
parties. Some examples of what we may find in the data is whether
one party may perform significantly better than the other, or maybe
some sections of the stock market do better, as well as the stability
and general bear/bull trend of the market. We are able to use data
science by analyzing this data to create a better understanding of
these perspectives of the debates.
• Discuss any relevant background knowledge or prior work (optional but
encouraged).
– We are doing this project our of curiosity of the subject.
1
2 Data Sources
• Identify the data sources you plan to use.
– Our primary data source would be the Yahoo Finance API. This is
an ideal choice, as it makes data aquisition and transformation easy.
One highlight while researching was be able to easily filter through
different sectors of the stock market using Yahoo, whether it be tech,
medicine, energy, etc.. We’ll also need to add to our data frame
information about the presidential party of the time. We can do
this by scraping the presidential terms from any history-based, valid
website.
• Explain how you will obtain, clean, and preprocess the data.
– Data acquisition here will require us both learning/getting comfort-
able with the Yahoo Finance API. Once we do, we will be able to
utilize API calls in order to get the information we want for analy-
sis. As for the presidential information, we may want to utilize some
form of webscraping like BeautifulSoup. There will be quite a few
preprocessing steps we need to take. For example, as I mentioned
earlier our data frame needs to include a value that shows whether
the party in office at the time was Democratic or Republican. We
will also want to make some other variables that will be useful for
future analysis and differentiation.
• If applicable, discuss potential challenges in data access, quality, or pre-
processing.
– One issue that may be present in our data aquisition/usability is
that as the history records of the stock market go farther and farther
back, it is more likely that there was no organized record-keeping
of the sections within the stock market such as tech or medicine.
Also there are going to be some outliers in the data, we can think
of crisis’ that don’t have strong correlation with the political party
of the time, such as the housing crisis in the late 2000s, or even the
Great Depression - if we go back that far.
3 Methodology and Analysis Plan
• Data Exploration.
– Perform exploratory data analysis (EDA) on the stock market returns
over time.
– Visualize the data to identify broad trends, outliers, or unusual mar-
ket behaviors.
• Modeling
2
– Label data points, daily or monthly, according to the political party
in office during each period.
– Create summary statistics such as mean return or volatility for each
presidency and aggregate summaries for Democratic vs. Republican
administrations.
• Evaluation
– Hypothesis testing: Compare average returns under Democratic vs.
Republican presidencies to see if differences are statistically signifi-
cant.
– Regression Analysis: Implement a time-series or regression model
that includes a categorical variable representing the party in power.
Also, we will include control for other factors such as interest rates
or market volatility to better see impacts of the political party.
– Python, Pandas, NumPy, SciPy, Matplotlib, Statsmodels
4 Expected Outcome
• Anticipated findings ◦ We expect to present whether or not there is a mean-
ingful difference in Stock Market(SP 500) performance during Democratic vs.
Republican presidencies. ◦ Analysis may reveal nuances such as certain peri-
ods of economic expansion or recession correlated with specific presidencies. •
Evaluation Criteria ◦ Return metrics: Average annualized return, cumulative
returns, Sharpe ratio, and volatility (standard deviation of returns).◦ Statis-
tical significance: p-values from hypothesis testing on the difference in mean
returns. ◦ Model accuracy(using regression): Goodness-of-fit measures such
as R²
. • Potential Extensions ◦ Extending the analysis to include additional
economic indicators, such as GDP growth, unemployment rates, and interest
rate policies, to see if party affiliation remains a significant factor when con-
trolling for broader macroeconomic variables. ◦ Exploring alternative indices
(e.g., Dow Jones, NASDAQ) or sector-based performances to see if party-driven
patterns differ by market segment. By completing this project, we will gener-
ate data-driven insights into whether political leadership correlates significantly
with market performance. This research can serve as a foundation for further
exploration of economic policy impacts on financial markets.
• Anticipated findings
– We expect to present whether or not there is a meaningful differ-
ence in Stock Market(SP 500) performance during Democratic vs.
Republican presidencies.
– Analysis may reveal nuances such as certain periods of economic ex-
pansion or recession correlated with specific presidencies.
• Potential Extensions
3
– Extending the analysis to include additional economic indicators,
such as GDP growth, unemployment rates, and interest rate policies,
to see if party affiliation remains a significant factor when controlling
for broader macroeconomic variables.
– Exploring alternative indices (e.g., Dow Jones, NASDAQ) or sector-
based performances to see if party-driven patterns differ by market
segment.
By completing this project, we will generate data-driven insights into whether
political leadership correlates significantly with market performance. This re-
search can serve as a foundation for further exploration of economic policy
impacts on financial markets.
