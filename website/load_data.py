# import pandas as pd
# import sqlite3
# from datetime import datetime
#
#
# def load_data_into_db():
#     # Load CSV into a DataFrame
#     df = pd.read_csv('Outbreaks.csv')
#
#     # Add a new column with the current timestamp
#     df['search_timestamp'] = datetime.utcnow()
#
#     # Create a SQLite database connection
#     conn = sqlite3.connect('outbreak.db')
#
#     # Store the DataFrame in the database
#     df.to_sql('outbreak_data', conn, index=False, if_exists='replace')
#
#     # Commit changes and close connection
#     conn.commit()
#     conn.close()
#
#
# if __name__ == "__main__":
#     load_data_into_db()
