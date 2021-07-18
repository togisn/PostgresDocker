import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

def checkLoanBalance(row):
    if row['loan balance'] <= 100000:
        return 'less than and equal to 100K'
    elif row['loan balance'] <= 1000000:
        return 'less than and equal to 1M and more than 100K' 
    else:
        return 'more than 1M'

df = pd.read_csv("LuxuryLoanPortfolio.csv")
df1 = df.groupby(["purpose"]).size().to_frame('count').reset_index()

df['year'] = pd.to_datetime(df['funded_date']).dt.year
df2 = df['year'].astype(str).reset_index()
df2['funded_amount'] = df['funded_amount']
df2 = df2.groupby(["year"]).sum('funded_amount').reset_index()

df3 = df['duration years'].astype(str).reset_index()
df3['loan balance'] = df.apply(checkLoanBalance, axis=1)
df3 = df3.groupby(["duration years", "loan balance"]).size().to_frame('count').reset_index()
#print(df3)

def create_layout(app):
    fig1 = px.bar(df1, x="purpose", y="count", color="purpose", title="Purpose used for Loan")
    fig2 = px.line(df2, x="year", y="funded_amount", title="Total Loan Funded per Year")
    fig3 = px.bar(df3, color="duration years", x="loan balance", y="count", barmode="group", title="Count of Loan Balance per Duration")

    return html.Div(style = {
        
        }, children = [
            html.H1(
            children = 'Luxury Loan Portfolio',
            style = {
                'textAlign': 'center',
                'color': '#7FDBFF',
                'backgroundColor': '#111111'
            }
        ),

        html.Div([
            html.H3("Chart 1. What is loan used for"),
            html.P(
                "\
            Data tells that most of the loan goes to commercial property, home and investment property.\
            Meanwhile, boat and plane only have loan less than 100. \
            The biggest difference is on plane and investment property, that is 1:20. \
            Meaning that, there are 20 loan on investment property per every loan on plane."
            ),
        ]),

        dcc.Graph(
            id = 'example-graph-1',
            figure = fig1
        ),

        html.Div([
            html.Br([]),
            html.H3("Chart 2. How much loan is funded per year"),
            html.P(
                "\
            In average, loan per year is funded around 350M - 400M. \
            There is downtrend at 2017 where it goes down to 311M. \
            But the next year at 2018, there is significant uptrend loan where it goes up to 552M, it is almost 2 times bigger than 2017 loan. \
            And it returns to range of 350M - 400M at 2019."
            ),
        ]),

        dcc.Graph(
            id = 'example-graph-2',
            figure = fig2
        ),

        html.Div([
            html.Br([]),
            html.H3("Chart 3. Customer Loan balance per duration"),
            html.P(
                "\
            The most balance is served by 30 years duration that is with nominal more than 1M. \
            Meanwhile the least balance is served by 10 years duration, precisely it is 4 for nominal more than 1 M and 2 for the other one. \
            Based on the chart, seems like customer is most comfortable having loan with 30 years duration on any nominal."
            ),
        ]),

        dcc.Graph(
            id = 'example-graph-3',
            figure = fig3
        )
    ])
