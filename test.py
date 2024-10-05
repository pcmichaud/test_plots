import plotly.graph_objects as go
import plotly.io as pio

# Create a simple scatter plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='markers'))

# Add titles and labels
fig.update_layout(title='Simple Scatter Plot',
                  xaxis_title='X Axis',
                  yaxis_title='Y Axis')

# Save the plot as an HTML file
pio.write_html(fig, 'scatter_plot.html')
