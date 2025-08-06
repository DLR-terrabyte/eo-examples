import math


def estimate_download_size(source_dataarray, dataarray_selection):
    """
    Estimate the download size and the memory size of a subset of a DataArray when downloaded from Earth Data Hub.

    Parameters:
    ----------
    source_dataarray : xarray.DataArray
        The initial data array you have accessed from Earth Data Hub (one of the original EDH dataset variables).
    dataarray_selection : xarray.DataArray
        The subset of the original data array being downloaded, before you apply any reduction operation on it (such as mean() or sum())

    Returns:
    -------
    None --> The variables named below as dict, not printing
        Prints estimated values:
        - Estimated number of needed chunks.
        - Estimated memory size of the selected data (in GB).
        - Estimated download size for the selected data (in GB, assuming a 10% compression factor, which is roughly EDH data compression).
    
    Explanation:
    -----------
    - Computes the base chunk size in each dimension from the original dataset.
    - Determines the number of chunks required in each dimension for the selection.
    - Calculates the estimated download shape based on the needed chunks.
    - Computes the estimated download fields as the total number of elements in the estimated shape.
    - Estimates the memory size in bytes, converts to gigabytes, and adjusts for download size with compression.

    Notes:
    ------
    - This function assumes the data type size is the last two digits in the data type string, representing
      the number of bits per element.
    - Output is printed in gigabytes (GB) for both memory and estimated download size.
    """
    
    base_chunk_shape = {key:value[0] for key,value in source_dataarray.chunksizes.items()}
    # print('base_chunk_shape: ',base_chunk_shape)
    
    needed_chunks_count_by_dim = {key:len(value) for key,value in dataarray_selection.chunksizes.items()}
    for key in source_dataarray.chunksizes.keys():
        if key not in needed_chunks_count_by_dim.keys():
            needed_chunks_count_by_dim.update({key:1})
    # print('needed_chunks_count_by_dim: ',needed_chunks_count_by_dim)
    # print("total number of needed chunks: ", math.prod([val for val in needed_chunks_count_by_dim.values()]))
    
    estimated_download_shape = {key: base_chunk_shape[key]*needed_chunks_count_by_dim[key] for key in source_dataarray.chunksizes}
    # print('estimated_download_shape: ', estimated_download_shape)
    
    estimated_download_fields = math.prod(estimated_download_shape[key] for key in estimated_download_shape)
    # print('estimated_download_fields : ', estimated_download_fields)

    estimated_dowload_size = int(str(dataarray_selection.dtype)[-2:])//8*estimated_download_fields
    #print(f'estimated_needed_chunks: {math.prod([val for val in needed_chunks_count_by_dim.values()])}')
    #print(f'estimated_memory_size: {round(estimated_dowload_size/1000**3, 3):,} GB')
    #print(f'estimated_download_size: {round(estimated_dowload_size/1000**3/10, 3):,} GB')
    estimated_needed_chunks = math.prod([val for val in needed_chunks_count_by_dim.values()])
    estimated_memory_size = round(estimated_dowload_size/1000**3, 3)
    estimated_download_size = round(estimated_dowload_size/1000**3/10, 3)
    res = {
        "estimated_needed_credits": estimated_needed_chunks, # https://github.com/SercoSPA/DESP-UserWorkflowService-Templates/issues/51
        "estimated_needed_chunks": estimated_needed_chunks, 
        "estimated_memory_size_gb": estimated_memory_size,
        "estimated_download_size_gb": estimated_download_size,
    }
    return(res)
    
