from altair import Chart, Tooltip

def chart(df, x, y, target) -> Chart:
    """
        Returns a scatterplot of the selected continuous varables 
        in the dataframe with the target variable indicating the categorical
        variables.
        
        parameters
        ----------
        df: pandas DataFrame object
        x: str
        y:  str
        target: str
        """
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph




if __name__ == '__main__':
    import pandas as pd
    import altair_viewer
    df = pd.read_csv("/Users/ara_vartomian/Downloads/insurance_data.csv")
    gr = chart(df, x ="age", y = "claim", target = "diabetic")
    altair_viewer.display(gr)

