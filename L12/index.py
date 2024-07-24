import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

def process_data(data):
    """Cleans and preprocesses the data."""
    data = data.dropna()  # Example of cleaning: removing missing values
    data['date'] = pd.to_datetime(data['date'])
    return data

def analyze_data(data):
    """Performs statistical analysis on the data."""
    analysis = data.describe()  # Example of analysis: summary statistics
    return analysis

def generate_report(analysis):
    """Generates a report from the analysis."""
    report = analysis.to_string()
    return report

def export_results(report, file_path):
    """Exports the report to a text file."""
    with open(file_path, 'w') as file:
        file.write(report)
    print(f"Report saved to {file_path}")

if __name__ == "__main__":
    data = load_data('data.csv')
    if data is not None:
        processed_data = process_data(data)
        analysis = analyze_data(processed_data)
        report = generate_report(analysis)
        export_results(report, 'report.txt')
