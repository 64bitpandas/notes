
## Taking a Picture
Cameras have **sensors** that capture light onto a plane.

First, a **lens** focuses incoming light onto the sensor. A **shutter** exposes the sensor to this light for a specified duration. During exposure, the sensor accumulates [[radiometry and photometry#Irradiance|irradiance]]. Modern digital sensors then convert this captured irradiance into some digital file format.

## Field of View
FOV refers to the angle which can be viewed by the sensor:
![[/cs184/img/Pasted-image-20230419174319.png]]
For a fixed sensor size $h$, *decreasing* the focal length $f$ *increases* the field of view: 
$$FOV = 2 \arctan (\frac{h}{2f})$$
For any given FOV, the focal length should be proportional to the size of the sensor. (Smaller sensor = shorter $f$)


### Focal length vs FOV comparison
| 16mm | 50mm | 200mm |
| ---- | ---- | ----- |
| ![[/cs184/img/Pasted-image-20230419175119.png]]     |  ![[/cs184/img/Pasted-image-20230419175146.png]]    | ![[/cs184/img/Pasted-image-20230419175158.png]]      |

### Dolly Zoom
The Dolly Zoom effect occurs when the camera is moved forwards or backwards at the same time that it is zoomed in our out. The foreground will appear the same size while the background becomes stretched out.

<iframe width="560" height="315" src="https://www.youtube.com/embed/u5JBlwlnJX0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Exposure
The natural, perceptual scale of exposure is logarithmic, so exposure levels represent a doubling in exposure. These doubling factors are measured in units of "stop".

**Exposure = irradiance x time x gain**
- irradiance = power of light falling on image sensor (aperture)
- Exposure time: duration that the sensor is exposed to light (shutter speed)
- Gain: Amplificiation of sensor pixel values (ISO)

All of these give approximately the same exposure:
![[/cs184/img/Pasted-image-20230419175848.png]]


### F-Stop
The F-stop, or F-number, of a lens is defined as the focal length divided by the diameter of the aperture. 

### Exposure Time
Slower shutter speed creates motion blur.
An electronic shutter also has a rolling shutter effect: since pixel light values are read on at a time, and reading takes time, some time will have elapsed between the first and last pixels read. So, there might be a discrepancy in the image.


### Gain
ISO gain multiplies signals before ADC. It has a linear effect, so ISO 200 requires half the light as ISO 100.
More gain = more noise.
![[/cs184/img/Pasted-image-20230419175641.png]]

### Summary
![[/cs184/img/Pasted-image-20230419180059.png]]



## The Thin Lens Equation
Real lenses are highly complex and can have **aberrations** which make them unable to converge to a single point. To make them easier to simulate, we can treat them as an ideal thin lens:
- Assume all parallel rays entering the lens pass through its focal point.
- Using basic geometry, we can find the focal length of a lens using the thin lens equation below:
![[/cs184/img/Pasted-image-20230309154334.png]]

### Magnification
The magnification of a lens $m$ is calculated as follows:
$$m = \frac{h_i}{h_o} = \frac{z_i}{z_o}$$
To achieve a magnification of 1 (known as 1:1 macro), the sensor should be the same size as the object it is capturing. In this case, $z_i = z_o$.

### Defocus Blur
Lenses bring a cone of light (in the focal plane) into convergence. The **circle of confusion** (difference between convergence point and sensor plane) is proportional to the size of the aperture $A$.
![[/cs184/img/Pasted-image-20230309154737.png]]


For moving objects, there is a tradeoff between depth of field and motion blur.
 - Less background blur = more motion blur = longer exposure, smaller aperture
 - *Lowest* aperture size = most background blur

### Depth of Field
The **depth of field** is the range of depths in the world where objects appear in focus. "Shallow depth of field" = lots of background blur.

![[/cs184/img/Pasted-image-20230419194943.png]]



## Ray Tracing ideal thin lenses



## Bokeh
Bokeh is the shape and quality of out of focus blur. Small, out-of-focus lights take on the shape of the lens aperture