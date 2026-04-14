# MMF-based polarization state measurement system with temperature resistance

Yuxuan Xiong School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China 754002620@qq.com

Shaojun Zhou School of Mechanical Science and Engineering, Huazhong University of Science and Technology Wuhan, China 708981573@qq.com

Ting Jiang School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China jtjt@hust.edu.cn

Zheng Gao School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China 602421710@qq.com

Zhao Ge School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China d202280977@hust.edu.cn

Hao Wu School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China wuhaoboom@qq.com

Jiajun Zhou School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China 1209433779@qq.com

Ming Tang* School of Optical and Electronic Information and Wuhan National Laboratory for Optpelectronics, Optics Valley Laboratory, Huazhong University of Science and Technology Wuhan, China tangming@mail.hust.edu.cn

Abstract—We propose a precise polarization-measurement system based on multimode fiber speckle. Convolutional neural network is used to achieve accurate identification of polarization states. The system is resistant to indoor temperature variation and the mean square error between actual and predicted Stokes parameters is less than 0.001. $^ { © }$ 2023 The Author.

Keywords—multimode fiber, polarization state, convolutional neural network;

# I. INTRODUCTION

The state of polarization (SOP) is one of the physical properties of light. It plays an important role in enhancing the capacity and the spectral efficiency of optical communication system. Therefore, the monitoring of SOP of light is very necessary. A polarimeter is a basic measurement instrument in optical communication-related applications, providing information such as SOP [1].

A typical approach acquiring the SOP involves the employment of an intricate system comprising various optical components, such as wave plates, polarizers, and polarization modulators [2]. The intensity of light traversing the optical device is measured, followed by the execution of Fourier analysis to derive Stokes parameters and subsequently ascertain the polarization state.

Traditional methodologies for polarization state measurement, such as the rotating-quarter-wave-plate technique, have been reported [3,4]. However, these methods are characterized by complex calculations and stringent requirements for wave plate-wavelength matching. Researchers have also explored SOP measurement using single metasurfaces, with a particular emphasis on the detection of partially polarized light [2,5]. Additionally, some research works have proposed employing portable fiber-optic spectrometers and neural network for such measurements and the mean square error (MSE) between actual and predicted

Stokes parameters is 0.01[6]. Nonetheless, these systems entail a multitude of optical devices, rendering them challenging to regulate.

In this paper, we present a method for acquiring SOP by capturing the output speckle of multimode fibers (MMFs) and recovering by a convolutional neural network (CNN). The input training SOP data sparsely cover the Poincare sphere and the loss of CNN between actual and predicted Stokes parameters is less than 0.001. Furthermore, the experiment results demonstrate that the method is resistant to slightly fluctuations of temperature. Compared with other SOP detection systems, the proposed MMF-based method offers a more compact, simplified, and solution.

# II. PRINCIPLE

In MMFs, the optical input excites a large number of modes. The output speckle is essentially a superposition of different modes. External environmental conditions and input characteristics can affect the coupling between different modes, leading to changes in the output speckle pattern. As the polarization state is a crucial attribute of input light, changes in polarization can impact modal coupling, consequently leading to different speckle patterns. This inherent property of MMFs facilitates their utilization as tools for polarization measurements.

CNNs are a specialized class of deep learning architectures designed for processing and analysis of images. CNNs are adept at extracting features from input images and associating them with corresponding labels. They establish a mapping relationship between input images and output parameters.

# III. EXPERIMENT SETUP

Fig. 1 illustrates the experimental setup of the multimode fiber speckle collection system. A polarization-maintaining fiber (PMF) is employed to stabilize the polarization of the

laser. A motorized polarization controller (MPC) is applied to manipulate the polarization state by remote control. It can accurately create any polarization state at any input state. The precise polarization control is achieved by rotating each quarter-wave plate over a $2 2 5 ^ { \circ }$ angular range independently. The range is divided into 1000 equal steps providing adjustment resolution of $0 . 2 2 5 ^ { \circ }$ . It is proved for a single MPC to produce all polarization states and cover the entire Poincare sphere. The MPC is utilized to generate specific polarization states, with a rotation interval of 50 steps for each plate to get 441 $( 2 1 \times 2 1 )$ images as a group of SOP data. The light emitted from the MMF enters free space and is subsequently detected by a charge-coupled device (CCD).

Images are cropped with size $2 0 0 ^ { * } 2 0 0$ as input to the CNN. The SOP of the input light is transformed into a Jones vector. It is employed to compute the output SOP after the MPC. The resulting output is then converted to $1 ^ { * } 4$ Stokes parameters, which serve as labels for the corresponding images. Fig. 2 presents the structure of the two-dimensional convolutional neural network (2D-CNN) employed in this study. We applied 3 convolution-pooling-gelu layers to reduce the data size. The output is converted to Stokes parameters via flatten and linear layers. To expedite convergence and ensure accuracy, the learning rate and batch size are set to 0.001 and 256 respectively. The loss function is defined by the mean squared error (MSE) to quantitatively evaluate the performance of the CNN in approximating the polarization state.

# IV. RESULT AND DISCUSSION

Despite we control room temperature, there are small fluctuations in room temperature. The speckle is still changing slowly without changing the input polarization state. Fig. 3 Shows the scattergram corresponding to the same polarization acquired at different times. The intensity distribution of the speckle changed significantly due to the floating indoor temperature. To account for this, we collect 10 sets of data over 8 hours. The first eight sets serve as training data, while the final two sets are partitioned into validation and test data. The CNN is capable of capturing the characteristics of the polarization state on the speckle, substantiating the feasibility of employing MMF speckles for polarization state measurements. The proposed system is harnessed to achieve more sophisticated polarization state detection. It has the potential to realize highly accurate detection with limited coarse training data.

Fig. 4(a) depicts the loss of the training and validation datasets. Following the training process, the losses for both datasets converge rapidly. The test dataset contains 441 speckles. To ensure accurate prediction of Stokes parameters, we select 30 polarization states for simplicity. The input values and predicted values for these states are compared in Fig. 4(b). Negligible differences between input and predicted data demonstrate that the detection is precise and that the impact of indoor temperature can be disregarded during the training process.

# V. CONCLUSION

We have proposed a SOP detection system that leverages the capabilities of MMFs and CNNs. Changes in polarization state are mapped onto the speckle and are effectively learned by the CNN. The results indicate that the MSE between actual and predicted parameters is less than 0.001. It implies high precision SOP recognition. In this case, we prove that the recognition accuracy is resistant to slight temperature fluctuations. It is important to note that the resistance of the system to temperature drift needs further quantitative study.

# ACKNOWLEDGMENT

This work was supported by National Key R&D Program of China under Grant 2018YFB1801002, National Natural Science Foundation of China under Grant 61722108, 61931010, and innovation Fund of WNLO.

# REFERENCES

[1] J. Dong, and H. Zhou, "Polarimeters from bulky optics to integrated optics: A review." Opt. Commun., vol. 465, 125598, February 2020.   
[2] S. Hermon, A. Ma, F. Yue, F. Kubrom, Y. Intaravanne, J. Han, Y. Ma, and X. Chen, "Metasurface hologram for polarization measurement," Opt. Lett., vol. 44, pp. 4436-4438, September 2019.   
[3] P. A. Williams, "Rotating-wave-plate Stokes polarimeter for differential group delay measurements of polarization-mode dispersion," Appl. Opt., vol. 38, pp. 6508-6515, November 1999.   
[4] C. Flueraru, S. Latoui, J. Besse, and P. Legendre, "Error Analysis of a Rotating Quarter-Wave Plate Stokes' Polarimeter," IEEE Trans. Instrum. Meas., vol. 57, no. 4, pp. 731-735, April 2008.   
[5] N. A. Rubin, A. Zaidi, M. Juhl, R. Li, J.P. Balthasar Mueller, R. C. Devlin, K. Leósson, and F. Capasso, "Polarization state generation and measurement with a single metasurface," Opt. Express, vol. 26, pp. 21455-21478, August 2018.   
[6] S. Xian, X. Yang, J. Zhou, F. Gao, and Y. Hou, "Deep learning-enabled broadband full-Stokes polarimeter with a portable fiber optical spectrometer," Opt. Lett. vol. 48, pp. 1359-1362, March 2023.

![](images/cc3b070f4488c7e5711c5d010485dfdbe1bf1ef03429e393fd7f9fb2a6003e3a.jpg)  
Fig. 1. Schematic of the measurement setup for speckle.

![](images/d971a4c7f314c9ab7b838c72fa71af8abf12768798cc944b3b58ec734167c647.jpg)  
Fig. 2. Schematic of the 2D-CNN structure.

![](images/c92b479bd1361704027fde5caa15eeec9505da3618f66ca7a80cfcffa8c4c4b4.jpg)

![](images/42a88b038003007509356b124a93fb73034497137d23c9e30cb6624872381c2e.jpg)

![](images/837985063078fcf284711af9e0e90b32ada30d072029b293ff45f4306a53c6c4.jpg)

![](images/c044d48ee8549348e145a18342146ab7cbfff2caba2093b558b9b0c1d5282029.jpg)

![](images/57334969183125a8e121833e6e60e7f667a864e4bc3fff265d3009ebad45a707.jpg)

![](images/8a9c8234cd24e8bc0785d3ba608133002459fa3f760c578853fc90d82f36056d.jpg)  
Fig. 3. Scattergrams of the same polarization state at different temperature.

![](images/c234b2c56f37a1969262d9e110a111416eb42a664a29a250804c90a3b4554d9b.jpg)  
Fig. 4. (a) Loss of training and validation datasets. (b) The input and predicted values of $\mathrm { S } _ { 1 } , \mathrm { S } _ { 2 }$ and $\mathrm { S } _ { 3 }$ for 30 polarization states.