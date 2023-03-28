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

    title = f"{y.capitalize()} vs {x.capitalize()} for {target.capitalize()}"
    graph = Chart(
        df,
        autosize = "pad",
        background='#aaaaaa',
        title=title, 
        padding={"left":10, "top":50, "right":10, "bottom":10}
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).configure_title(fontSize=30, dy =-30, anchor='middle'
    )
    return graph




if __name__ == '__main__':
    import pandas as pd
    import altair_viewer
    df = pd.read_csv("/Users/ara_vartomian/Downloads/insurance_data.csv")
    gr = chart(df, x ="age", y = "claim", target = "diabetic")
    altair_viewer.display(gr)

