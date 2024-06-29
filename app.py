from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from scipy.interpolate import interp1d

app = Flask(__name__)

# Provided Old Rating to Original Rating conversions
old_ratings = np.array([1550, 1650, 1800, 1900, 2100, 2400])
original_ratings = np.array([1612, 1835, 2171, 2394, 2841, 3512])

# Create an interpolation function
interp_function = interp1d(old_ratings, original_ratings, kind='linear', fill_value="extrapolate")

# Define known conversions and add exact points
new_to_old = {
    3500: 2600, 3250: 2500, 3000: 2400, 2700: 2300, 2500: 2200,
    2350: 2100, 2250: 2000, 2150: 1950, 2050: 1900, 1950: 1870,
    1850: 1830, 1750: 1800, 1700: 1750, 1650: 1700, 1600: 1650,
    1567: 1530, 1533: 1515, 1500: 1475, 1467: 1450, 1433: 1425,
    1400: 1400, 1367: 1367, 1333: 1333, 1300: 1300, 1267: 1267,
    1233: 1233, 1200: 1200, 1167: 1167, 1133: 1133, 1100: 1100,
    1067: 1067, 1033: 1033, 1000: 1000, 967: 967, 933: 933, 900: 900
}

def new_to_original_rating(new_rating):
    if new_rating in new_to_old:
        old_rating = new_to_old[new_rating]
        return float(interp_function(old_rating))
    else:
        # Interpolate between closest known points
        sorted_keys = sorted(new_to_old.keys())
        for i in range(len(sorted_keys) - 1):
            if sorted_keys[i] <= new_rating <= sorted_keys[i + 1]:
                x0, y0 = sorted_keys[i], new_to_old[sorted_keys[i]]
                x1, y1 = sorted_keys[i + 1], new_to_old[sorted_keys[i + 1]]
                interpolated_old_rating = y0 + (new_rating - x0) * (y1 - y0) / (x1 - x0)
                return float(interp_function(interpolated_old_rating))

# Simplified title_rankings
title_rankings = {
    "Galactic Master": 3000,
    "Grandmaster": 2350,
    "International Master": 2050,
    "Master": 1750,
    "Advanced": 1600,
    "Intermediate": 1400,
    "Rookie": 1100,
    "Beginner": 900  # Chosen as a value slightly lower than "Rookie"
}

def generate_graph(new_rating_user=None, original_rating_user=None, user_title=None):
    new_ratings = np.linspace(900, 3500, 100)  # Adjusted the range
    original_ratings = [new_to_original_rating(r) for r in new_ratings]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=original_ratings, y=new_ratings, mode='lines', name='New to Original Conversion',
        line=dict(color='blue', width=2),
        hovertemplate="<b>New Rating: %{y:.0f}<br>Original Rating: %{x:.0f}</b><extra></extra>"
    ))
    
    for title, rating in title_rankings.items():
        original_value = new_to_original_rating(rating)
        if original_value is not None:
            fig.add_annotation(
                x=original_value,
                y=rating,
                text=title,
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#636363",
                ax=0,
                ay=-30 if title != "Galactic Master" else -60,
                bgcolor="rgba(255, 255, 255, 0.8)",
                font=dict(size=10, color='#3b5998')
            )
    
    if new_rating_user is not None and original_rating_user is not None:
        fig.add_trace(go.Scatter(
            x=[original_rating_user], y=[new_rating_user], mode='markers',
            marker=dict(size=10, color='red'),
            hovertemplate="<b>New Rating: %{y:.0f}<br>Original Rating: %{x:.0f}</b><extra></extra>"
        ))
        fig.add_annotation(
            x=original_rating_user,
            y=new_rating_user,
            text=user_title,
            showarrow=False,
            bgcolor="rgba(255, 255, 255, 0.8)",
            font=dict(color='red', size=12),
            xshift=0,
            yshift=-30
        )

    fig.update_layout(
        title=dict(
            text="Galaxy Rating Conversion Chart",
            x=0.5,
            font=dict(size=24, color='#3b5998')
        ),
        xaxis=dict(
            title=dict(
                text="Original Rating",
                font=dict(size=18, color='#3b5998', family="Arial, sans-serif")
            ),
            range=[200, 4000],
            dtick=200,
            tickformat=".0f"
        ),
        yaxis=dict(
            title=dict(
                text="New Rating",
                font=dict(size=18, color='#3b5998', family="Arial, sans-serif")
            ),
            range=[900, 3500],
            dtick=200,
            tickformat=".0f"
        ),
        hovermode="x unified",
        dragmode=False,
        uirevision=True,
        showlegend=False,
        margin=dict(l=60, r=60, t=60, b=60),
        plot_bgcolor='rgba(245, 245, 245, 1)',
        paper_bgcolor='rgba(245, 245, 245, 1)',
        font=dict(family="Arial, sans-serif", size=12, color="#4e4e4e")
    )
    
    graph_html = pio.to_html(fig, full_html=False, config={'displayModeBar': False})
    return graph_html

@app.route('/')
def index():
    graph_html = generate_graph()
    return render_template('index.html', graph_html=graph_html)

@app.route('/convert', methods=['POST'])
def convert():
    try:
        current_rating = int(request.form.get('current_rating'))
        original_rating = new_to_original_rating(current_rating)
        if original_rating is None:
            raise ValueError("Invalid rating")
        original_rating = int(round(original_rating))
        
        user_title = next((title.split(" ")[0] for title, rating in sorted(title_rankings.items(), key=lambda item: item[1], reverse=True)
                           if current_rating >= rating), "Beginner")
        
        graph_html = generate_graph(new_rating_user=current_rating, original_rating_user=original_rating, user_title=user_title)
        return render_template('index.html', graph_html=graph_html, current_rating=current_rating, original_rating=original_rating)
    except ValueError:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





