Title: Bokeh in jupyter notebooks for interactive plots
Author: SergeM
Date: 2018-06-20 07:45:21
Slug: bokeh-example
Tags: python,bokeh,jupyter,plot

[Bokeh](https://bokeh.pydata.org/en/latest/) is a library for interactive visualization. One can use it in Jupyter notebooks.

Here is the example. 

Lets say we have a pandas dataframe with timestamps and some values:
```python
import pandas as pd
from io import StringIO
df = pd.read_csv(StringIO("""timestamp,value
2018-01-01T10:00:00,20
2018-01-01T12:00:00,10
2018-01-01T14:00:00,30
2018-01-02T10:30:00,40
2018-01-02T13:00:00,50
2018-01-02T18:00:40,10
"""), parse_dates=["timestamp"])
```

You can visualize it to a nice graph with zoom, selection, and mouse-over tooltips using the bokeh:

```python
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.io import output_notebook, show


output_notebook()


hover = HoverTool(
    tooltips=[
        ("timestamp", "@timestamp{%Y-%m-%d %H:%M:%S}"),
        ("value", "@value")
    ],
    formatters={
        'timestamp'      : 'datetime', # use 'datetime' formatter for 'date' field
                                       # use default 'numeral' formatter for other fields
    }
)

p = figure(plot_width=800, plot_height=400, tools=[hover,  'box_zoom', 'wheel_zoom', 'pan'],
           title="Mouse over the dots", x_axis_type='datetime')

p.line ('timestamp', 'value', source=ColumnDataSource(data=df))

show(p)
```
