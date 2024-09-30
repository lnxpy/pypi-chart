from string import Template
from typing import List, Any

CHART_TEMPLATE = Template("""---
config:
    xyChart:
        width: $chart_width
        height: $chart_height
        xAxis:
          tickLength: 5
          tickWidth: 1
        yAxis:
          tickLength: 5
          tickWidth: 1

    themeVariables:
        xyChart:
            titleColor: "#4492F9"
            backgroundColor: transparent 
            plotColorPalette: "#0D74E6"
---
xychart-beta
    title "$chart_title"
    x-axis "Date" $dates
    y-axis "Downloads" line $downloads""")


def mermaidify_list(lst: List[Any]) -> str:
    return "[" + ", ".join(map(str, lst)) + "]"
