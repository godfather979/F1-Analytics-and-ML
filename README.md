<h1><strong>F1 Race Analysis</strong><br></h1>
<p align="left">
  
  F1 Race Analysis is a data science project that leverages machine learning techniques to predict Formula 1 lap times. By analyzing historical race data and environmental factors, the project aims to provide valuable insights into race strategies and driver performance.
</p>

<h2>Idea</h2>
<p>
  The primary goal of this project is to develop a machine learning model capable of predicting lap times in Formula 1 races. It incorporates data such as driver characteristics, car specifications, track conditions, and weather dynamics to:
</p>
<ul>
  <li>Predict lap times with high accuracy.</li>
  <li>Estimate race outcomes and probabilities for each driver.</li>
  <li>Provide data-driven support for race strategies, including pit stops and tyre management.</li>
</ul>

<h2>Features</h2>
<ul>
  <li><strong>Dynamic Lap Time Prediction:</strong> Uses a Random Forest model to accurately predict lap times for individual laps based on multiple variables.</li>
  <li><strong>Comprehensive Race Time Estimation:</strong> Aggregates lap predictions to compute total race durations and support pit-stop strategy planning.</li>
  <li><strong>Probability-Based Outcome Analysis:</strong> Calculates win probabilities for drivers using race time predictions.</li>
  <li><strong>Advanced Feature Engineering:</strong>
    <ul>
      <li>Includes metrics such as tyre degradation and fuel load impact on lap times.</li>
      <li>Handles complex weather and track dynamics to refine predictions.</li>
    </ul>
  </li>
  <li><strong>Interactive Dashboard:</strong> A user-friendly Streamlit interface for visualizing predictions, lap time progressions, and model performance metrics.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
  <li><strong>Programming Language:</strong> Python</li>
  <li><strong>Libraries:</strong>
    <ul>
      <li>Data Processing: Pandas, NumPy</li>
      <li>Visualization: Matplotlib, Seaborn</li>
      <li>Machine Learning: Scikit-learn, RandomForestRegressor</li>
    </ul>
  </li>
  <li><strong>Frontend:</strong> Streamlit for interactive data visualization and user input handling.</li>
  <li><strong>Environment:</strong> Google Colab (initial development), Local Setup (VS Code, Jupyter Notebooks).</li>
  <li><strong>Dataset Source:</strong> FastF1 API and historical F1 data from 2019–2024.</li>
</ul>

<h2>Key Methodologies</h2>
<ol>
  <li><strong>Data Preprocessing:</strong>
    <ul>
      <li>Cleaned and merged lap data with weather data using FastF1 API.</li>
      <li>Filtered outliers and handled missing values to ensure robust analysis.</li>
    </ul>
  </li>
  <li><strong>Feature Engineering:</strong>
    <ul>
      <li>Tyre degradation calculated based on tyre life and compound type (Soft, Medium, Hard).</li>
      <li>Fuel load dynamics incorporated to reflect race progress.</li>
    </ul>
  </li>
  <li><strong>Machine Learning:</strong>
    <ul>
      <li>Random Forest Regressor chosen for its robustness and ability to handle nonlinear relationships.</li>
      <li>Evaluated models using MSE, MAE, and R² metrics.</li>
    </ul>
  </li>
  <li><strong>Visualization:</strong>
    <ul>
      <li>Scatter plots, histograms, line graphs, and correlation heatmaps to analyze relationships between variables and model performance.</li>
    </ul>
  </li>
</ol>

<h2>Results</h2>
<ul>
  <li>Achieved high prediction accuracy with an R² score of 0.993 using the Random Forest Regressor.</li>
  <li>Demonstrated reliable lap time predictions and win probabilities.</li>
  <li>Insights into tyre degradation patterns and fuel load effects on performance.</li>
</ul>

<h2>Key Learnings</h2>
<ul>
  <li><strong>Data Handling and Engineering:</strong>
    <ul>
      <li>Learned advanced preprocessing techniques for merging, cleaning, and engineering datasets.</li>
      <li>Mastered feature engineering for complex systems like tyre degradation and fuel load.</li>
    </ul>
  </li>
  <li><strong>Machine Learning Expertise:</strong>
    <ul>
      <li>Explored multiple ML models and fine-tuned the Random Forest Regressor for optimal performance.</li>
      <li>Applied key evaluation metrics (MSE, MAE, R²) to validate model reliability.</li>
    </ul>
  </li>
  <li><strong>Real-World Application:</strong>
    <ul>
      <li>Gained experience in applying machine learning to solve real-world problems in motorsports.</li>
      <li>Developed a scalable pipeline for integrating historical and real-time data.</li>
    </ul>
  </li>
  <li><strong>Visualization and User Interaction:</strong>
    <ul>
      <li>Built a Streamlit-based dashboard to make predictions accessible and visually intuitive.</li>
    </ul>
  </li>
</ul>

<h2>Demo</h2>
<p><a href="https://youtu.be/ERZi9ZD6KZc">Watch the video demo here</a></p>

<h2>References</h2>
<ul>
  <li>FastF1 API Documentation: <a href="https://docs.fastf1.dev/">https://docs.fastf1.dev/</a></li>
  <li>Formula 1 Race Analysis Using Machine Learning: <a href="https://www.researchgate.net/publication/368762920_Formula_One_Race_Analysis_Using_Machine_Learning">ResearchGate Article</a></li>
  <li>Towards Data Science: <a href="https://towardsdatascience.com/formula-1-race-predictor-5d4bfae887da">Formula 1 Race Predictor</a></li>
</ul>
