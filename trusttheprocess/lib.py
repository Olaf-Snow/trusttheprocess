import plotly.express as px

def first_plot():
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    fig.show()
    return fig


def try_me():
    return 'TRUST THE PROCESS!! - Learn to trust, git ur hub!'
