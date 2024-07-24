import pytest
import pandas as pd
from io import StringIO
from my_program import load_data, process_data, analyze_data, generate_report, export_results

def test_load_data():
    # Create a mock CSV file
    csv_data = "date,value\n2024-01-01,100\n2024-01-02,200"
    mock_csv = StringIO(csv_data)
    
    # Read the mock CSV file using pandas
    expected_data = pd.read_csv(mock_csv)
    
    # Save mock CSV to a temporary file path
    mock_csv_path = "mock_data.csv"
    expected_data.to_csv(mock_csv_path, index=False)
    
    # Test the function
    data = load_data(mock_csv_path)
    
    # Assert that the loaded data matches the expected data
    pd.testing.assert_frame_equal(data, expected_data)

def test_process_data():
    # Create mock data
    data = pd.DataFrame({'date': ['2024-01-01', '2024-01-02'], 'value': [100, 200]})
    expected_data = data.copy()
    expected_data['date'] = pd.to_datetime(expected_data['date'])
    
    # Test the function
    processed_data = process_data(data)
    
    # Assert that the processed data matches the expected data
    pd.testing.assert_frame_equal(processed_data, expected_data)

def test_analyze_data():
    # Create mock data
    data = pd.DataFrame({'date': ['2024-01-01', '2024-01-02'], 'value': [100, 200]})
    
    # Expected analysis
    expected_analysis = data.describe()
    
    # Test the function
    analysis = analyze_data(data)
    
    # Assert that the analysis matches the expected analysis
    pd.testing.assert_frame_equal(analysis, expected_analysis)

def test_generate_report():
    # Create mock analysis data
    analysis = pd.DataFrame({'value': [100, 200]})
    
    # Expected report
    expected_report = analysis.to_string()
    
    # Test the function
    report = generate_report(analysis)
    
    # Assert that the report matches the expected report
    assert report == expected_report

def test_export_results(tmpdir):
    # Create mock report
    report = "Mock report"
    
    # Define file path
    file_path = tmpdir.join("report.txt")
    
    # Test the function
    export_results(report, str(file_path))
    
    # Assert that the file was created and the content matches the report
    with open(file_path, 'r') as file:
        content = file.read()
        assert content == report
