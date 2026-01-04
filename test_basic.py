#!/usr/bin/env python3
"""
Basic functionality test for Migration Engine
"""

import pandas as pd
from src.config import Config
from src.validators import DataValidator
from src.transformers import DataTransformer

def test_validation():
    """Test data validation"""
    print("Testing data validation...")

    # Load sample data
    df = pd.read_csv('sample_data.csv')
    print(f"Loaded {len(df)} rows with {len(df.columns)} columns")

    # Create config and validator
    config = Config()
    validator = DataValidator(config)

    # Validate
    result = validator.validate_dataframe(df)

    print("Validation results:")
    print(f"   Errors: {len(result['errors'])}")
    print(f"   Warnings: {len(result['warnings'])}")

    if result['warnings']:
        print("   Warnings:")
        for warning in result['warnings'][:5]:  # Show first 5
            print(f"   • {warning}")

    return result

def test_transformation():
    """Test data transformation"""
    print("\nTesting data transformation...")

    # Load sample data
    df = pd.read_csv('sample_data.csv')
    print(f"Original columns: {list(df.columns)}")
    print(f"Original dtypes:\n{df.dtypes}")

    # Create config and transformer
    config = Config()
    transformer = DataTransformer(config)

    # Transform
    df_transformed = transformer.transform(df)

    print("Transformation completed:")
    print(f"   New columns: {list(df_transformed.columns)}")
    print(f"   New dtypes:\n{df_transformed.dtypes}")
    print(f"   Shape: {df_transformed.shape}")

    return df_transformed

def main():
    """Run basic tests"""
    print("Migration Engine - Basic Functionality Test")
    print("=" * 50)

    try:
        # Test validation
        validation_result = test_validation()

        # Test transformation
        transformed_df = test_transformation()

        print("\nAll basic tests completed successfully!")
        print("\nSample transformed data:")
        print(transformed_df.head())

    except Exception as e:
        print(f"\nTest failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()