import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    data = data[data['passenger_count'] >0]
    data=  data[data['trip_distance'] >0] 
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    def to_snake_case(column_name):
    # Use regular expression to handle specific cases like "ID"
        snake_case_name = re.sub(r'(?<=[a-z])([A-Z])', r'_\1', column_name).lower()
        return snake_case_name

# Rename columns using the lambda function
    data.rename(columns=lambda x: to_snake_case(x), inplace=True)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero distance'
    assert 'vendor_id' in output.columns, "'vendor_id' column does not exist"