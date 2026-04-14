# Wavelength and polarization state synchronization measurement based on MMF scattering pattern

Yuxuan Xiong

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics, Opti

Valley Laboratory,Huazhong University

of Science and Technology

Wuhan, China

754002620@qq.com

Ting Jiang

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics, Optics

Valley Laboratory,Huazhong University

of Science and Technology

Wuhan, China

jtjt@hust.edu.cn

Zheng Gao

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics, Optics

Valley Laboratory,Huazhong University

of Science and Technology

Wuhan, China

602421710@qq.com

Hao Wu

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics, Optics

Valley Laboratory,Huazhong University

of Science and Technology

Wuhan, China

wuhaoboom@qq.com

Shaojun Zhou

School of Mechanical Science and

Engineering, Huazhong University of

Science and Technology

Wuhan, China

708981573@qq.com

Ming Tang*

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics, Optics

Valley Laboratory,Huazhong University

of Science and Technology

Wuhan, China

tangming@mail.hust.edu.cn

Abstract—We presented a system for the measurement of wavelength and polarization state synchronization based on multimode fiber speckle. By employing convolutional neural network, we successfully established the mapping relationship between speckle patterns and wavelengths, as well as between speckle patterns and Stokes parameters. Consequently, the system accomplishes synchronized measurement of both wavelengths and polarization states. The system achieves a wavelength resolution of $\mathbf { 0 . 5 \ n m }$ and can distinguish two SOPs on the Poincaré sphere with a vector difference of 0.365.

Keywords—multimode fiber, specklegram, convolutional neural networks, wavelength, polarization state

# I. INTRODUCTION

A spectrometer constitutes an essential instrument for the precise determination and evaluation of the wavelength distribution and intensity of light. It operates on the principle of effectuating a comprehensive mapping of output signals corresponding to varying wavelengths onto discrete spatial locations of highly sensitive detectors. Traditional spectrometer uses gratings as the dispersion medium for spectral separation, requiring a large number of optical components and making the system bulky and cumbersome. Therefore, in order to simplify the system, some scholars have used optical fibers as the dispersion medium. The characteristic of using optical fibers is that it can differentiate different light with only a few devices. Therefore, researchers have utilized fibers, such as multimode fibers (MMF) [1] and multi-core multimode integrated fibers [2], as dispersion elements to replace gratings in traditional spectrometers.

Some scholars have utilized fibers as the dispersion medium based on the concept of Sagnac fiber interferometer and constructed a fiber spectrometer using Acousto-Optic Modulation (AOM)[3]. This approach aims to reduce the complexity of the system, but the introduction of polarization devices still poses challenges in optical path adjustment. In order to simplify the system completely, some scholars have used multimode fibers (MMFs) as the dispersion medium. The entire system only requires MMFs and a camera. By employing a matrix pseudo-inverse algorithm combined with

a nonlinear optimization program, the input signal spectrum was reconstructed from the output speckle pattern. This approach achieved a spectral resolution of $0 . 1 5 \mathrm { n m }$ within a $2 5 \mathrm { { n m } }$ bandwidth using a 1m long MMF[5]. The system in this scheme is extremely simple, but the drawback is that the calibration matrix needs to be computed every time, resulting in computational complexity. In addition, some scholars have used multicore fibers as the dispersion medium[11]. Although costly camera is not required in this system, the inclusion of a spatial light modulator still introduces complexity.

Apart from the wavelength of light, polarization is also a crucial feature of light. In the field of quantum communication, researchers have prepared polarization-based quantum cat states and discussed the properties of quantum superposition generated using biphoton fields in SOPs[5]. Furthermore, researchers have utilized MMF speckle for the measurement of SOP[6]. Therefore, considering spatial utilization, it becomes an intriguing research question whether it is possible to integrate a spectrometer with SOP measurement of light within a single system.

In this paper, we presented a MMF-based system for simultaneous wavelength and SOP measurements. The speckles emitted from MMF are put into a convolutional neural network (CNN) to extract the features and establish the mapping relationship. The experimental results proved the feasibility of this method.

# II. PRINCIPLE

# A. Mode coupling in MMF

MMFs have the capability to simultaneously propagate a multitude of distinct guided wave modes, each characterized by different phase velocities[7]. The intensity distribution at the output end of fiber, known as the scattering pattern, is the results of interference between different modes. It carries a significant amount of spatial state information of MMF[8] and reflects various properties of the input light.

The spatial state information can reflect changes in the external environment. External disturbances, such as

temperature, stress, and vibration, can alter the refractive index distribution of MMF, thereby impacting mode coupling and altering the scattering pattern. Consequently, MMF can be employed in the field of sensing. Besides, the sensitivity of MMF to input light properties [1] enables its application in the measurement of incident light characteristics.

# B. CNN dealing with specklegrams

CNN have been demonstrated to be effective in complicated nonlinear modeling and classification tasks in MMF transmission when intensity-only detection is employed[9]. It extracts features from the scattering pattern, associates them with labels, and is capable of discerning imperceptible changes to the naked eye. In the field of MMF imaging, researchers have demonstrated that CNNs can achieve image reconstruction fidelity of up to $94 \%$ by learning the input-output relationship in a 0.75m MMF[10].

# III. EXPERIMENT SETUP

The acquisition system for mode field profile is depicted in Fig. 1. The laser utilized in the system demonstrates characteristics of a narrow linewidth, adjustable and stable wavelength. It emits light with a wavelength range of 1545- $1 5 5 5 \mathrm { n m }$ for experimental purposes. To facilitate data labeling for CNN, a polarizer is incorporated into the system. Its output Stokes parameters are pre-measured. A motorized polarization controller (MPC) is employed to realize arbitrary knowable SOP. It contains two individual quarter-wave plate. In this experiment, each plate is rotated $1 8 ^ { \circ }$ at a time to change the SOP and 100 $( 1 0 \times 1 0 )$ different SOP are obtained as a group of data for every wavelength. MMF transmits light of different wavelengths and SOP, and the resulting speckle is detected by a charge-coupled device (CCD). The wavelength

![](images/06a962776c40764d33227d5aeb877fb9a7b963c92d9fdab656830484bc2a915a.jpg)  
Fig. 1. Schematic of the measurement setup.

intervals are 1nm and $0 . 5 \mathrm { n m }$ within a bandwidth of 10nm. On the Poincaré sphere, the average Euclidean distance between adjacent points representing polarization states is 0.638.

Images are cropped with size $6 0 0 ~ \times ~ 6 0 0$ and are preprocessed to a maximum pooled size of $2 0 0 \times 2 0 0$ . The actual SOP for the input of MMF is determined through Jones vector calculation and then converted to $1 \times 4$ Stokes parameters. The wavelength is determined by the laser. The 1 $\times 5$ data serve as label for corresponding images to realize the simultaneous measurement and analysis of two parameters. Fig. 2 shows the two-dimensional CNN employed. Four residual structures are applied to fully learn the characteristics of SOP and wavelength in speckles. The Gelu function is used as an activation function to avoid neuronal inactivation due to the Relu function. The learning rate and batch size are set to 0.001 and 128. The loss function of wavelength is defined by the mean absolute error (MAE) indicating the physical

significance of predicted differences. And the root mean squared error (RMSE) defines the loss function of Stokes parameters. The physical significance of this is the vector difference between the predicted and actual SOP vectors on the Poincaré sphere.

# IV. RESULTS AND DISCUSSION

Fig. 3. shows the comparison of input and predicted wavelengths. Fig. 3. (a) and (b) same SOP with different wavelengths The wavelength spacing in Fig. 3. (a) and (b) is $0 . 5 \mathrm { n m }$ and 1nm, respectively. The difference between two values is smaller than the corresponding interval, indicating that both resolutions of $0 . 5 \mathrm { n m }$ and 1nm are achievable.

Fig. 4. demonstrates the system's resolution capability for different SOPs, with the RMSE being smaller than the average vector difference between two adjacent SOPs. The network simultaneously learns wavelength and SOP. It should be noted that when the resolution of the wavelength increases, the corresponding loss weight is also increased to accurately identify the changes in wavelength.

According to the research findings of other scholars[1], the number of modes that MMF can support limits the resolution of system. Therefore, when measuring two or more parameters and requiring measurement accuracy, it is essential to ensure that higher-order modes are adequately excited.

# V. CONCLUSION

We proposed a system capable of simultaneous measurement of wavelength and SOP. CNN has established the mapping relationship between the mode patterns and wavelength as well as SOP. The system is capable of simultaneously achieving wavelength recognition with a resolution of $0 . 5 \mathrm { n m }$ within a bandwidth of $1 0 \mathrm { n m } .$ , as well as resolving two SOPs on the Poincaré sphere that have a vector difference of 0.365. In the case of simultaneous measurements, the resolution of both parameters exceeds their data intervals. It should be noted that the precision limit of simultaneously measuring both wavelength and SOP is still subject to further research.

# ACKNOWLEDGMENT

This work was supported by National Key R&D Program of China under Grant 2018YFB1801002, National Natural Science Foundation of China under Grant 61722108, 61931010, and innovation Fund of WNLO.

# REFERENCES

[1] R. Brandon, S. M. Popoff, and H. Cao, "All-fiber spectrometer based on speckle pattern reconstruction." Opt. Express, vol. 21, pp. 6584- 6600, March 2013.   
[2] Z. Meng, J. Li, C. Yin, T. Zhang, Z. Yu, M. Tang, W. Tong, and K. Xu, "Multimode fiber spectrometer with scalable bandwidth using space-division multiplexing." AIP advances, vol. 9, June 2019.   
[3] S. E. Higley, E. Udd, R. J. Michal, J. P. Theriault, and D. A. Jolin, "Fiber-optic spectrometer." Fiber optic and laser sensors V , vol. 838, pp. 318-324, March 1988.   
[4] R. Brandon, and H. Cao. "Using a multimode fiber as a high-resolution, low-loss spectrometer." Opt. Lett, vol. 37, pp. 3384-3386, 2012.   
[5] Yu. I. Bogdanov, E. V. Moreva, G. A. Maslennikov, R. F. Galeev, S. S. Straupe, and S. P. Kulik, "Polarization states of four-dimensional systems based on biphotons." Phys. Rev., vol. 73, June 2006.

[6] Y. Xiong, T. Jiang, Z. Ge, H. Wu, S. Zhou, Z. Gao, J. Zhou, and M. Tang, “MMF-based polarization state measurement system with temperature resistance,” 2023 Opto-Electronics and Communications Conference (OECC), Shanghai, China, 2023, pp. 1-3, doi: 10.1109/OECC56963.2023.10209861.   
[7] Y. Li, Z. Yu, Y. Chen, T. He, J. Zhang, R. Zhao, and K. Xu, "Image reconstruction using pre-trained autoencoder on multimode fiber imaging system." IEEE Photonics Technol. Lett., vol. 32, pp. 779-782, July 2020.   
[8] L. Cai, M. Wang, and Y. Zhao. "Investigation on refractive index sensing characteristics based on multimode fiber specklegram." Meas. Sci. Technol., vol. 34, 2022.

[9] M. Wei, G. Tang, J. Liu , L. Zhu, J. Liu, C. Huang, J. Zhang, L. Shen, and S. Yu "Neural network based perturbation-location fiber specklegram sensing system towards applications with limited number of training samples." J. Lightwave Technol., vol. 39, pp. 6315-6326, October 2021.   
[10] B. Rahmani, D. Loterie, G. Konstantinou, D. Psaltis, and C. Moser, L Multimode optical fiber transmission with a deep learning network,”Light, Sci. Appl., vol. 7, pp. 69, October 2018.   
[11] Y. Li, Z. Yu, Y. Chen, T. He, J. Zhang, R. Zhao, and K. Xu. "Image reconstruction using pre-trained autoencoder on multimode fiber imaging system." IEEE Photonics Technol. Lett., vol. 32, pp.779-782, July 2020.

![](images/466b3ba647d1c2522491e3ccf5eab719091a4d63d0a9f21babb7d43c87901df8.jpg)  
Fig. 2. Structure of the 2D-CNN.

![](images/8fcd02eee1c67b2716d5319b322ff8cf6c5ab1b05429b42b716733e2e4874d4e.jpg)  
(a)

![](images/a3fa5925bc7c4eff8c1f77513d0b6fe0a0d1e4d8a075b3fafa15410177c6b4ce.jpg)  
(b)   
Fig. 3. Comparison of actual input and predicted wavelengths. (a) The interval of wavelength is $0 . 5 \mathrm { n m }$ . (b) The interval of wavelength is 1nm.

![](images/544263e29da3639e8577f67615da510954321790adda53b48bd47536b5583da9.jpg)

![](images/aed224dea76383bc43fe1573a4ceba97a9d78d4d59bafdf36173f22df1570043.jpg)  
Fig. 4. The RMSE corresponding to each SOP on the Poincaré sphere. (a) The interval of wavelength is $0 . 5 \mathrm { n m }$ . (b) The interval of wavelength is 1nm.