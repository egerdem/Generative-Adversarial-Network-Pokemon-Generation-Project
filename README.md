# pokeGAN

## Overview
This code is from Siraj Raval's PokeGAN Project (https://youtu.be/yz6dNf7X7SA) which he uses a WGAN to create new kinds of Pokemon.
I tried to make some experiments to achieve similar results. Although I could not reach a new pokemon like Siraj', I documented the process and explain some experiments that I made. Anybody who are making experiments about hyper-parameters of the pokeGAN project can be benefit from the results for an idea of the process and to see some results. Failure may be the result of insufficient epoch numbers due to the usage of limited AWS account that I have. I advise you to use Siraj's original codes. 

note : gpu usage is a must for this project

I changed the original "resize" code to manipulate the original pokemon pictures differently, in my way (also to make sure preprocessing of the dataset is correct) 

Details of the changes are written on the "report" pdf. Sorry for not having a ipynb, I lost the original notebook that I prepare while taking a "Deep Learning" course.

## Dependencies (pip install) 
```
cv2
tensorflow( >=1.0)
scipy
numpy
```

## Usage
```
cd pokeGAN
python resize.py
python pokeGAN.py
```

## Credits

The credits for this project go to https://github.com/llSourcell/Pokemon_GAN 
