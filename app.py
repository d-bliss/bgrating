from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from datetime import datetime

app = Flask(__name__)

def v2_to_v1(v2_rating):
    return (v2_rating - 828.9) / 0.4474

# Define title_rankings as a global variable
title_rankings = {
    "Galactic-GM 2400": 2400,
    "Grandmaster 2100": 2100,
    "International-Master 1900": 1900,
    "Master 1800": 1800,
    "Advanced 1650": 1650,
    "Experienced 1550": 1550
}

def generate_graph(v2_rating_user=None, v1_rating_user=None, user_title=None):
    def v1_to_v2(v1_rating):
        return 0.4474 * v1_rating + 828.9

    v1_ratings = np.linspace(1300, 3600, 100)
    v2_ratings = v1_to_v2(v1_ratings)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=v1_ratings, y=v2_ratings, mode='lines', name='V1 to V2 Conversion',
                             hovertemplate="V2 Rating: %{y:.2f}<extra></extra>"))
    
    for title, rating in title_rankings.items():
        v1_value = (rating - 828.9) / 0.4474
        fig.add_annotation(
            x=v1_value,
            y=rating,
            text=title,
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=0,
            ay=40,
            bgcolor="rgba(255, 255, 255, 0.8)"
        )
    
    if v2_rating_user is not None and v1_rating_user is not None:
        fig.add_trace(go.Scatter(x=[v1_rating_user], y=[v2_rating_user], mode='markers',
                                marker=dict(size=10, color='red')))
        fig.add_annotation(
            x=v1_rating_user,
            y=v2_rating_user,
            text=user_title,
            showarrow=False,
            bgcolor="rgba(255, 255, 255, 0.8)",
            font=dict(color='red', size=12),
            xshift=0,
            yshift=40
        )

    
    fig.update_layout(
        title=dict(
            text="V2 Rating to V1 Rating Conversion Chart",
            x=0.5,
            font=dict(size=24, color='#3b5998')
        ),
        xaxis=dict(
            title="V2 Rating",
            dtick=200,
            tickformat=".2f"
        ),
        yaxis_title="V1 Rating",
        hovermode="x",
        dragmode=False,
        uirevision=True,
        showlegend=False
    )
    
    graph_html = pio.to_html(fig, full_html=False, config={'displayModeBar': False})
    return graph_html

@app.route('/')
def index():
    graph_html = generate_graph()
    year = datetime.now().year
    return render_template('index.html', graph_html=graph_html, year=year)

@app.route('/convert', methods=['POST'])
def convert():
    try:
        v2_rating = int(request.form.get('v1_rating'))
        v1_rating = int(round(v2_to_v1(v2_rating)))
        
        user_title = next((title.split(" ")[0] for title, rating in sorted(title_rankings.items(), key=lambda item: item[1], reverse=True)
                           if v2_rating >= rating), "Beginner")
        
        graph_html = generate_graph(v2_rating_user=v2_rating, v1_rating_user=v1_rating, user_title=user_title)
        year = datetime.now().year
        return render_template('index.html', graph_html=graph_html, year=year, v1_rating=v1_rating, v2_rating=v2_rating)
    except ValueError:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
