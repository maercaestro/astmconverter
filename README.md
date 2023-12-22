# MEGAT ASTM Converter v0.1

<h3>ASTM to TBP Conversion Using Linear Regression</h3>

I'm trying to convert ASTM D1160 to TBP for works and I simply didn't know how. So I did some reasearch, and found this paper published in 2015. https://www.vurup.sk/wp-content/uploads/dlm_uploads/2017/07/pc_3_2015_stratiev_354_0.pdf

In it, it shows comparison on ASTM D1160 conversion to TBP using several methods. The least error method was using Linear Regression employed by Lukoil Neftochim Bourgas. The paper has shown the linear regression coefficient that they have obtained for each wt% of the data. But it stopped short at 80%. I want to replicate their method using linear regression but the paper simply has limited data. 

Then I transfer the notebook result to VS Code and develop a streamlit web app for this conversion. This is where the app has few issues and limitations. Currently, it is only able to convert all list, and not a single wt% value. For this, I need to employ container, or familiarize myself with Streamlit layout. So, a few improvements needs to be done. For now, it can display all converted value in a table, and plot the values in a chart. And it is also able to download the data in csv format. 

<h3>Features in version 0.1</h3>
1. Convert ASTM D1160 values to TBP

2. Plot in a graph
   
3. Download the converted value to csv.

<h3>Future Improvements</h3>
1. Convert single value instead of waiting for overall conversion

2. Include other ASTM method for conversion
   
3. Include graph as downloadable.

If you have any issues, and want to know more, you may contact me at
maercaestro@gmail.com

