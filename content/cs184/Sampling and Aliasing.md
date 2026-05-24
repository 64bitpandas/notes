## Signal Reconstruction
How do we actually convert data from the rasterizer into signals that can be displayed on a monitor?

### Jaggies
Right now, if we just display what we rasterized in the function from the [[Drawing Triangles|previous section]], the triangle will look a bit off:
![[/cs184/img/Pasted-image-20230119163826.png|300]]
There's some irregularities (like the isolated pixel on the bottom left) that make this look unnatural. This is an example of **aliasing-** which are rendering errors and artifacts that are created as a result of sampling being unable to perfectly represent the original image.

Let's try to fix this.

## Frequency

### Fourier Transform
Decompose any function into a sum of sines and cosines. In other words, transform functions from the spatial domain $f(x)$ into the frequency domain $F(\omega)$.

$$F(\omega) = \int_{-\infty}^{\infty} f(x) e^{-2 \pi i \omega x} dx$$
Inverse transform:
$$f(x) = \int_{-\infty}^{\infty} F(\omega) e^{2 \pi i \omega x} dx$$

When sampling, we can take points at each of the decompose frequencies. However, the sampling rate must be faster to capture higher frequencies, or else we risk **undersampling**:
![[/cs184/img/Pasted-image-20230126113459.png|300]]

Two frequencies that are indistinguishable at a given sampling rate are called **aliases**.

We can filter different frequencies to get different results. Essentially, frequencies represent the rate of change of information over some unit of space or time (for example, edges in a picture have high frequencies).
- Filtering out high frequencies will create a blur effect.
- Filtering out low frequencies will only keep the outline.

### Convolution

Convolution involves combining a *signal* with a *filter* by pointwise multiplying their values over time.

**Convolution Theorem:** The convolution of two functions is the pointwise product of their Fourier transforms.
So if we take the Fourier transform of two functions, multiply them, then take the inverse transform of the result, we'll get the convolved function back. 

Convolution is used to apply filters (such as a box filter, which is a square of light around small frequencies). 

### Nyquist Theorem and Supersampling
We get no aliasing from frequencies in the signal that are less than the Nyquist frequency (half of the sampling frequency).

As a consequence, sampling at twice the highest frequency in the signal will eliminate aliasing.

The basic idea of antialising is to remove/reduce signal frequencies above the Nyquist frequency before sampling.

Thus, a 1-pixel-wide box filter will attenuate all frequencies whose period is less than or equal to 1 pixel width, which is an effective pre-filter that already prevents some aliasing.
- This is equivalent to computing the average value of the function in the pixel. **Supersampling** is the act of taking multiple samples per pixel and getting the average.

To summarize:
 - **Nyquist Frequency** = 1/2 sampling frequency: the highest frequency that can be sampled at a given rate before losing information
 - **Nyquist Rate** = 2x max signal frequency: the minimum frequency we can sample at before losing information



## Antialiasing
**Main idea:** filter out high frequencies before sampling. (In other words, *blur* the signal to make it change less quickly before sampling-- aliasing occurs when we sample too slowly, or with too low resolution, compared to the rate of change of the signal).

To emphasize, **antialiasing (pre-blurring) must be done before sampling, not after**. (The alternative is not viable algorithmically.)

