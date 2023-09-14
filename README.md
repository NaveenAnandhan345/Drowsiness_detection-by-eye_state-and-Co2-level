# Drowsiness detection based on Eye state and Co2 level inside car

This code can detect your eyes and c02 level inside car and alert when the user is drowsy.

# Applications 🎯
This can be used by riders who tend to drive for a longer period of time that may lead to accidents.

# Modules
- Raspberry Pi
- Pi Camera
- C02 Module (MG811 Co2 sensor)

# Packages Used
- Tensorflow
- OpenCV
- numpy
- keras
- pygame

# Description 📌
**By Eye state:** Camera automatically detect driver drowsiness in a real-time video stream and then play an alarm if the driver appears to be drowsy.

**By Co2 Module:** Sensor will read the co2 level inside the car and once the level reaches to 1100ppm, intimation will given to turnoff re-circulation and lower the window. 
## Execution 🐉
```sh
python drowsiness detection.py
```

```sh
Co2 detection.py
```
