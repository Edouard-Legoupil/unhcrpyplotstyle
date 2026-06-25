# UNHCR Python Styling Package Demo

This folder contains a Quarto notebook demonstrating the `unhcrpyplotstyle` Python package, which provides Matplotlib styles following the UNHCR Data Visualization Guidelines.

## Contents

- `unhcrpyplotstyle_demo.qmd` - Main Quarto notebook with comprehensive examples
- `test_quarto.py` - Test script to verify the notebook can be executed
- `test_plot.png` - Sample output from the test script

## How to Use

### 1. Render the Quarto Notebook

To render the Quarto notebook to HTML:

```bash
quarto render unhcrpyplotstyle_demo.qmd
```

This will generate an HTML file with all the examples and visualizations.

### 2. Run the Test Script

To verify that everything is working:

```bash
python test_quarto.py
```

This will test that:
- The UNHCR style can be loaded
- Sample data can be created
- Basic plots can be generated with the UNHCR style

### 3. Examples Included

The notebook includes the following examples:

1. **Basic Usage**: How to apply the UNHCR style to Matplotlib charts
2. **Grid Customization**: Controlling grid lines
3. **Axis Customization**: Customizing axis visibility and appearance
4. **Text Customization**: Working with rich text formatting
5. **Data Labels**: Adding data labels to charts
6. **Color Palettes**: Using UNHCR color palettes
7. **Void Theme**: Minimal theme for pie charts and maps

## Requirements

- Python 3.7+
- Matplotlib
- NumPy
- Pandas
- Quarto (for rendering the notebook)
- `unhcrpyplotstyle` package (installed)

## UNHCR Style Features

The `unhcrpyplotstyle` package provides:

- **Typography**: 12pt bold titles, 8pt labels, proper spacing
- **Colors**: Official UNHCR color palettes (sequential, diverging, category)
- **Layout**: Consistent margins, grid lines, and axis styling
- **Accessibility**: Colors that meet AAA contrast requirements

## Available Color Palettes

- **Sequential**: `sequential_blue`, `sequential_green`, `sequential_yellow`, `sequential_red`, `sequential_cyan`, `sequential_purple`
- **Diverging**: `diverging_blue_red`, `diverging_navy_red`
- **Category**: `region`, `poc`

## Comparison with R Version

This demo is inspired by the R package `unhcrthemes` and provides similar functionality for Python users. The examples demonstrate equivalent functionality to the RMarkdown vignette but using Python and Matplotlib.

## License

This demo is provided under the same license as the `unhcrpyplotstyle` package (MIT License).