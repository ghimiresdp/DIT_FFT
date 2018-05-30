# DIT_FFT
This is tha sample of 8 point Fast Fourier Transform (Decimation In Time) [DIT-FFT] with Python and visualization of data with matplotlib
to install matplotlib, please look the website of matplotlib.
If you use pip then you can install pip by

pip install matplotlib



x0 will be input values 
x1,x2 ,x3 will be different phases used in the butterfly structure
x3 will be the final output of the FFT
To be more clear about the DIT-FFT, Please read about it.
Do not forget to take a look on Butterfly structure of DITFFT

Decimation in time includes different processes in which the input values will be broken down into following pattern at first stage:

{0,1,2,3,4,5,6,7}

    ->  {odd_occurence},    {even_occurence}     
    ->  {0,2,4,6},  {1,3,5,7}

        ->  { {odd_occurence}, {even_occurence}},   {{odd_occurence}, {even_occurence}} 
        ->  {{0,4}, {2,6}},   {{1,5}, {3,7}}

To be more clear, please look for the butterfly structure of The DIT-FFT