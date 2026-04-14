# Multimode Fiber Based High-Dimensional Light Analyzer

Yuxuan Xiong, Hao Wu , Mingming Zhang, Yucheng Yao , and Ming Tang , Senior Member, IEEE

Abstract—The wavelength and state of polarization (SOP) are fundamental properties of an optical field which are essential for applications in optical communications, imaging and other fields. However, it is challenging for existing spectrometers and polarimeters to measure these parameters simultaneously, resulting in reduced spatial and temporal efficiency. To overcome this limitation, we propose and demonstrate a compact multimode fiber (MMF)- based high-dimensional light analyzer capable of simultaneously performing high-precision measurements of both wavelength and SOP. Core-offset splicing is introduced in the MMF to reshuffle the mode coupling. A neural network named WP-Net has been designed dedicated to wavelength and SOP synchronization measurements. Physics-informed loss function based on optical prior knowledge is used to optimize the learning process. These advancements have enhanced the sensitivity, achieving a wavelength accuracy of 0.045 pm and an SOP accuracy of 0.0088.

Index Terms—Convolutional neural network, multimode fiber, speckle, spectropolarimeter.

# I. INTRODUCTION

T is essential to measure both the wavelength and state of po-I larization (SOP) of light simultaneously. This comprehensive understanding of the properties of light facilitates a wide range of critical applications, including optical communication [1], remote sensing [2], chemical and biological studies [3], and astronomical observation [4]. Despite significant advancements in the design of polarimeters and spectrometers, it remains challenging to capture high-dimensional information including polarization and wavelength simultaneously. Modern instruments are typically limited to measuring only wavelength or polarization. Recent research has demonstrated the potential for

Received 24 February 2025; revised 25 April 2025 and 10 June 2025; accepted 13 June 2025. Date of publication 17 June 2025; date of current version 16 August 2025. This work was supported in part by Hubei Optical Fundamental Research Center, in part by the National Natural Science Foundation of China under Grant 62225110, Grant 61931010 and in part by the Major Program (JD) of Hubei Province under Grant 2023BAA013. (Corresponding authors: Ming Tang; Hao Wu.)

Yuxuan Xiong, Hao Wu, Mingming Zhang, and Yucheng Yao are with the Wuhan National Laboratory for Optoelectronics (WNLO), National Engineering Laboratory for Next Generation Internet Access System, School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: wuhaoboom@hust.edu.cn).

Ming Tang is with the Wuhan National Laboratory for Optoelectronics (WNLO), National Engineering Laboratory for Next Generation Internet Access System, School of Optical and Electronic Information, Optical Fundamental Research Center, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: tangming@mail.hust.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JLT.2025.3580158.

Digital Object Identifier 10.1109/JLT.2025.3580158

simultaneous wavelength and SOP measurement using tunable liquid crystal metasurfaces [5]. However, the spectral range is limited to near-infrared light, and the reflective design introduces additional complexity of the system. A multidimensional light field sensor based on disordered nematic liquid crystal was also demonstrated [6]. But the system was insufficient in measurement accuracy, which could only support 15 wavelengths $\mathrm { ~ x ~ } 1 4 ~ \mathrm { S O P s }$ , but the system necessitates a free-space experimental setup, which introduces significant alignment challenges and operational complexity. Some researchers have used simple thin-film interfaces with spatial and frequency dispersion to synchronously measure wavelength and polarization. This miniaturized system has a simple structure, but the accuracy of polarization state identification is relatively low [7].Other researchers have constructed a multiplexing system that can simultaneously measure wavelength and SOP by multiplexing time-division and space-division methods [8], [9]. Inevitably, the multiplexing leads to a further increase in the shape factor and complexity of the system. Therefore, it is indispensable to propose a simple-structure and high-precision system capable of simultaneous wavelength and SOP measurement.

The MMF, which is cost-effective and sensitive to the characteristics of the input light, has exhibited the potential to be a solution for achieving simultaneous wavelength and SOP measurements. This functionality is realized through MMF mode coupling, with a camera serving as the detector to capture the resulting speckle [10], [11], [12]. Based on this, Hui Cao et al. achieved 1 pm resolution at $1 5 0 0 ~ \mathrm { n m }$ utilizing a $1 0 0 ~ \mathrm { m }$ long MMF and 1 nm resolution in a large bandwidth of 400- $7 5 0 ~ \mathrm { n m }$ using a $4 \ \mathrm { c m }$ long MMF. [13] Moreover, researchers utilize techniques based on speckle imaging and advanced data analysis methods, including image differencing [14], [15], zero-normalized cross-correlation [16], [17], and normalized inner product coefficients [18], for quantitative characterization, which has significantly expanded the utility of MMF in various applications including fiber sensors and spectrometers. There has been research conducted to demonstrate the sensitivity of MMF to wavelength and SOP [19], [20]. The feasibility of measuring both wavelength and polarization simultaneously using MMF with the transmission matrix algorithm has been demonstrated [21]. However, this approach still has potential for improvement due to the slow update rate of large-dimension matrices, especially when measuring two parameters simultaneously [22]. Consequently, a more efficient analytical approach is essential. Deep learning techniques have been proved to be highly effective for analyzing speckle images. Speckle images

![](images/94aa3142614fefa6dac7201a2f46299406c92fced7969898a28cbb29fa3f6a84.jpg)  
Fig. 1. Scheme of the high-dimensional analyzer based on MMF. The introduction of core-offset splicing and WP-Net has improved the sensitivity and accuracy.

are utilized to train models and correlations can be established between intricate variations in the speckles and the target measurements. Researchers have already employed deep learning in combination with MMF to achieve sensing measurements of parameters, such as temperature, strain and tactile response [10], [23], [24], [25], [26]. There has been research implemented the simultaneous measurement of wavelength and polarization based on MMF and ResNet [27]. However, additional fabrication steps for tapered MMF increased the system complexity. And the ResNet50 they employed was with substantial computational overhead. Therefore, there exists a critical need for a solution that simultaneously simplifies operational procedures and reduces computational overhead.

In this work, we propose a high-dimensional light analyzer based on MMF, as illustrated in Fig. 1. Light with random wavelength and SOP generates corresponding speckle patterns at the output end of MMF. Accurate multi-parameter measurement is achieved by establishing a mapping relationship via a CNN. To enhance sensitivity, the intermediate mode reshuffle is introduced through core-offset splicing, as shown in the dotted box in Fig. 1. Additionally, a physical principle is integrated into the loss function, which improves the general applicability of the model and results in higher accuracy. We refer to this neural network for simultaneous wavelength and polarization measurement as WP-Net. Experimental results demonstrate high-precision simultaneous measurements of wavelength and SOP, with accuracy of 0.045 pm and 0.0088, respectively.

# II. PRINCIPLE

The large diameter of the core of an MMF enables the transmission of a multitude of modes. Different modes transmit

across MMF with various speeds, resulting in a phase difference that produces a bright and dark mode interference pattern at the end facet of MMF, as illustrated in (1) [28]. In this equation, $I$ is the speckle image at the end facet of MMF. $N$ denotes the number of modes. The amplitude and polarization of the ith mode is represented by $a _ { i }$ and $\hat { e } _ { i } ( x , y )$ , respectively [29]. A change in the wavelength or SOP of the incident light results in a differential alteration of the optical range length of each mode. This causes a shift in the relative phase of the modes, resulting in a modification of the speckle pattern. Consequently, MMFs are capable of effectively measuring the optical field characteristics of the incident light, as variations in wavelength and SOP are directly reflected in changes to the speckles.

$$
I (x, y, L) = \left| \sum_ {i = 1} ^ {N} a _ {i} \hat {e} _ {i} (x, y) \exp \left(j \frac {2 \pi}{\lambda} n _ {e f f, i} L\right) \right| ^ {2} \tag {1}
$$

Similarity is used to evaluate the sensitivity of MMF-based measurement systems [30], as shown in (2). In (2), $I$ and $I ^ { \prime }$ are the two speckle images before and after a change in $\alpha$ , where $\alpha$ is the parameter to be measured. $x$ is position on the speckle, $\langle \rangle _ { x }$ is averaging over the speckle image and $\sigma$ is the standard deviation of the speckle image. The similarity does not directly determine the accuracy limit. When measuring a single parameter, the accuracy is defined by the smallest detectable variation in the speckle. The speckle correlation limit indicates the minimum distance at which neighboring parameter values can still be distinguished. A faster decline in the similarity curve over the same measurement range suggests a faster decorrelation of speckle patterns, which in turn reflects a higher resolution capability [31]. Long MMF system exhibits faster decorrelation rate between speckles, leading to better resolution compared to

![](images/cb83bc78f28f81a9e43f061ad11f71ea94990b77c4cf805b7045537173b5c1a4.jpg)  
Fig. 2. Schematic of the experimental setup.

![](images/b22f9ad4ea6887a6e94ba87ccfcf138b0c5b2c9792b3b539a3a3331574d24c57.jpg)  
Fig. 3. The spectral correlation bandwidth of the MMF.

short MMF system. [30]

$$
S (\Delta \alpha) = \left\langle \left(\frac {I - \langle I \rangle_ {x}}{\sigma_ {I}}\right) \left(\frac {I ^ {\prime} - \langle I ^ {\prime} \rangle_ {x}}{\sigma_ {I ^ {\prime}}}\right) \right\rangle_ {x} \tag {2}
$$

# III. METHODS

Fig. 2 schematically illustrates the measurement system. Tunable laser (TSL 570, Santec) emits spectrally known light which passes through a motorized polarization controller (MPC, fiberpro, containing two independent rotating 1/4 waveplates) to produce an output in any SOP. This output light enters a MMF as the light to be measured. The experiment utilized a 2 m MMF (SI 105/125-22/250, YOFC) with a $1 0 5 \mathrm { { u m } }$ core diameter. Fig. 3 shows the spectral correlation curve of the MMF at $1 5 5 0 ~ \mathrm { n m }$ exhibiting a full width at half maximum of $0 . 0 0 7 4 5 9 \ \mathrm { n m }$ . The input light excites mode coupling and forms a speckle at the end facet of the MMF, which is detected by a charge coupled device (CCD, SP620U-1550, Spiricon). The original image captured by the CCD has a resolution of $1 2 0 0 \times 1 6 0 0$ . Only the portion containing the complete scattering is cropped out, with a size of $6 0 0 \times 6 0 0$ . To shorten the learning time, we preprocessed the image with a kernel of $3 \times 3$ for maximum pooling, reducing the size to $2 0 0 \times 2 0 0$ .

The cropped speckles are input into a neural network as shown in Fig. 4(a). Each speckle is labeled with its corresponding wavelength and Stokes parameters, depicted in Fig. 4(b). The deep learning model used here is a convolutional neural network.

![](images/9142b56d184cdaab17a9e9f821938c6ef226217cbd2b48785cdbe69db43e9bf0.jpg)

![](images/5cd7615f83da84bd4ac2c7c97f8097232ffd98a699ac717305710939ef9abfda.jpg)  
Fig. 4. (a) Structure of the CNN to establish the mapping relationship between speckle, wavelength and SOP; (b) Each speckle corresponds to different wavelength and SOP.

The structure comprises 9 convolutional layers. ReLU is utilized as activation functions. The odd-numbered convolutional layers are sequentially processed with BN layers. To enhance system generalization, dropout layers $( \mathrm { p } { = } 0 . 3 ,$ ) are strategically inserted after the 3 rd and 5th convolutional layers. The initial value of the learning rate is set at 0.0003, which gradually decreases as the learning process progresses. The performance of CNN is evaluated using two metrics: the mean absolute error (MAE) for wavelength prediction, shown in Equation (3), and the root-mean square error (RMSE) for SOP prediction, shown in (4). The MAE quantifies the accuracy of wavelength prediction as the absolute difference between the predicted and actual wavelengths, while the RMSE measures the accuracy of SOP prediction as the vector difference between the predicted and actual Stokes parameters. The loss function of the network is defined as the sum of these two-error metrics, as expressed in (5). The training process is terminated if the loss does not decrease after 600 iterations.

$$
M A E _ {\lambda} = \left| \lambda_ {\text {p r e}} - \lambda_ {\text {a c t}} \right| \tag {3}
$$

$$
R M S E _ {S O P} = \sqrt {\sum_ {i = 1} ^ {3} \left(S _ {i p r e} - S _ {i a c t}\right) ^ {2}} \tag {4}
$$

$$
\text {L o s s} = M A E _ {\lambda} + R M S E _ {S O P} \tag {5}
$$

# IV. RESULTS AND DISCUSSION

# A. Wavelength and SOP Analyzer

To address the trade-off between range and accuracy in the MMF speckle measurement system, high-precision measurement is achieved by integrating models with two measurement ranges and intervals. Two datasets were collected. The large-step dataset to assess the performance across a wide bandwidth consists of 28,400 speckles, covering a bandwidth of $3 5 \ \mathrm { n m }$ with an interval of $0 . 5 \ \mathrm { n m }$ . For each wavelength, 400 speckles are acquired corresponding to different SOPs covering the entire Poincare sphere. The average vector distance of the adjacent

![](images/1ae7a61f049e3dfbd0a271e9c5253b566ef8178d10092fbb87a05b67bbb4b14d.jpg)

![](images/e7f9f01c8ca4a4be4b91855a8aefdfcb80a5e7086596530309749dd0039979cd.jpg)

![](images/9cab90e0daf3c7c8f8e919b3b133481ba55ddda2b0cfcd46cde2b5eac9a74ab8.jpg)

![](images/bd480f03db9089a9721a308ec202b6fd8133fa189f4c1eae0dc987e7331511f5.jpg)  
Fig. 5. The accuracy of the MMF-based analyzer for different parameter intervals. (a)-(b) Wavelength and SOP in the large-step dataset; (c)-(d) Wavelength and SOP in the small-step dataset.

TABLE I THE ACCURACY OF THE MMF-BASED ANALYZER AT DIFFERENT PARAMETER INTERVALS   

<table><tr><td>Dataset</td><td>Large-step</td><td>small-step</td></tr><tr><td>Bandwidth</td><td>35 nm</td><td>100 pm</td></tr><tr><td>Wavelength interval</td><td>0.5 nm</td><td>2 pm</td></tr><tr><td>Wavelength error (MAE)</td><td>0.026 nm</td><td>0.085 pm</td></tr><tr><td>SOP interval</td><td>0.1856</td><td>0.0115</td></tr><tr><td>SOP error (RMSE)</td><td>0.1606</td><td>0.0138</td></tr><tr><td>S1 (MAE)</td><td>0.0947</td><td>0.0079</td></tr><tr><td>S2 (MAE)</td><td>0.0983</td><td>0.0086</td></tr><tr><td>S3 (MAE)</td><td>0.0846</td><td>0.0081</td></tr></table>

SOP vectors on the Poincare sphere in the large-step data set is 0.1856. The other dataset is the small-step dataset which aims to determine the accuracy limit of the system. It contains 20,400 speckles, with a bandwidth of $0 . 1 \mathrm { n m }$ and an interval of 2 pm. Similarly, 400 speckles corresponding to different SOPs are acquired for each wavelength. The average vector distance of the adjacent SOPs in the small-step dataset is 0.0115. Both datasets were divided into training, validation, and test sets in an

8:1:1 ratio. The results are summarized in Table I and illustrated in Fig. 5.

The system has been demonstrated to provide highly accurate wavelength measurements across different bandwidths. Notably, the wavelength error in the large-step dataset $( 2 6 \mathrm { p m } )$ is smaller than the bandwidth of the small-step dataset $1 0 0 ~ \mathrm { p m } )$ ). This suggests that, when the two datasets are combined, the system can offer both a wide range and high accuracy in wavelength measurements. In the large-step dataset, the system can cover a broad range of wavelength and SOP measurements. However, in the small-step dataset, the system can only provide accurate wavelength measurements, with significant errors in the SOP measurements, as shown in Fig. 5(d). This limitation arises because the system relies on the MMF characteristics to extract input light field features and map them onto the speckle spatial distribution. As a result, it is challenging to distinguish the effects of wavelength and SOP by analyzing the spatial intensity distribution alone. Additionally, the resolution of MMF-based system is positively correlated with the fiber length. However, increasing the fiber length not only raises the cost but also makes

TABLE II COMPARISON OF SYSTEM ACCURACY BEFORE AND AFTER MODE RESHUFFLE   

<table><tr><td>Displacement</td><td>Origin</td><td>1/8</td></tr><tr><td>Wavelength error (MAE)</td><td>0.085 pm</td><td>0.065 pm</td></tr><tr><td>SOP error (RMSE)</td><td>0.0138</td><td>0.0103</td></tr><tr><td>S1 (MAE)</td><td>0.0079</td><td>0.0059</td></tr><tr><td>S2 (MAE)</td><td>0.0086</td><td>0.0064</td></tr><tr><td>S3 (MAE)</td><td>0.0081</td><td>0.0045</td></tr></table>

the system more sensitive to external environmental factors. To improve the feature extraction capability of short MMFs, we introduce mode reshuffle, which enhances the measurement accuracy of the system.

# B. Mode Reshuffle

Core-offset splicing is introduced to reshuffle the mode coupling and enhance the sensitivity. To identify the accuracy improvement introduced by different displacements, 5 distinct displacement groups are established for comparison. These groups include: displacement 0, 1/8 fiber diameter, 1/4 fiber diameter, 3/8 fiber diameter, and 1/2 fiber diameter. The 0-displacement group was designed to examine the effect of the fusion splice point on accuracy.

Similarity, as defined in (2), is utilized to quantify the sensitivity of the system. A change in the measured value leads to a reduction in the similarity between the images before and after the change. Within the same measurement range, a faster decorrelation rate corresponds to a higher system sensitivity. The wavelength and SOP similarity curves are shown in Fig. 6. The mode reshuffle has significantly increased the decorrelation rate of wavelength and has slightly impact on the SOP. It is shown in Fig. 6 that the decorrelation rate does not follow a linear relationship with displacement. The 1/8 displacement demonstrates the fastest decorrelation rate and optimal mode reshuffle effects to enhance the sensitivity of both wavelength and SOP.

Based on the above conclusion, the 1/8 displacement provides the greatest improvement in sensitivity. Therefore, the same dataset for the displacement of 1/8 was collected. The dataset contains 20,400 speckles with a bandwidth of $1 0 0 \ \mathrm { p m }$ , an interval of $2 \mathrm { p m }$ , with each wavelength corresponding to 400 different SOPs. The results are shown in Table II. Comparing with the original system, the wavelength accuracy of the 1/8 displacement group reaches $0 . 0 6 5 ~ \mathrm { p m }$ . And the SOP accuracy is reduced to 0.0103, smaller than the interval of SOP. There are improvements of $2 3 . 5 3 \%$ and $2 5 . 3 6 \%$ in wavelength and SOP respectively compared to the original system. The accuracy distribution is shown in Fig. 7.

# C. WP-Net With Loss Function Optimization

During the training process, it is notable that the 1/8 displacement case is more prone to overfitting. This is attributed to the higher decorrelation rate of the 1/8 displacement group, which results in increased sensitivity and more noticeable variations in the speckle compared to the original system. Therefore, we propose the WP-Net with additional physical constraint based on

![](images/58d9bfdb7058511c6d2d5e0572975405a565274f54be8f957e9e6389ab124c9c.jpg)

![](images/c642e78966ed02c844ab8b793954bd58f0186115d74843504bade715dd05e53c.jpg)  
Fig. 6. Similarity curves of the variance to be measured corresponding to different displacements. (a) Wavelength; (b) SOP.

optical principles to the loss function. The WP-Net based on the optical principles aims to achieve simultaneous wavelength and SOP measurements with enhanced generalization capability. In this experiment, since fully polarized light, with a polarization degree of 1, is used in this experiment, the Stokes parameters satisfy the relationship of $S _ { 0 } ^ { 2 ^ { - } } { = } S _ { 1 } ^ { \ 2 } + S _ { 2 } ^ { \ 2 } + S _ { 3 } ^ { \ 2 }$ .This optical prior knowledge can be integrated into the loss function, as shown in (6). The modified loss function is expressed in (7).

$$
l o s s _ {D O P} = \frac {S _ {1} ^ {2} + S _ {2} ^ {2} + S _ {3} ^ {2}}{S _ {0} ^ {2}} - 1 \tag {6}
$$

$$
\operatorname {L o s s} ^ {\prime} = M A E _ {\lambda} + R M S E _ {S O P} + \operatorname {l o s s} _ {D O P} \tag {7}
$$

Training with WP-Net, the loss curve with and without additional physics-informed loss function are shown in Fig. 8. Before using the WP-Net, the loss exhibited a little overfitting. However, with the implementation of WP-Net, the losses of training and validation decrease synchronously indicating an improvement in generalization capability. The accuracy results

![](images/fe42fef55377640cdd4e0aec5e4063901927b66d0091b672b3a8dcdce722ccc9.jpg)

![](images/b6041b1ac71664116d4af5ce6214e18ae3da29eaa9a1a2363c4e499864692446.jpg)  
Fig. 7. The accuracy after introduction of mode reshuffle. (a) Wavelength; (b) SOP.

![](images/89395885b6d7c4123c9a7513ba8be383c0ae386b5663caec2360fa6979272e1e.jpg)  
Fig. 8. The comparison of loss curves with and without WP-Net.

are shown in Table III. In summary, with the introduction of mode reshuffle and WP-Net, the accuracy of wavelength and SOP improved significantly, from 0.085 pm and 0.0138 to 0.045 pm and 0.0088, respectively. This represents an enhancement of $4 7 . 0 6 \%$ in wavelength accuracy and $3 6 . 2 3 \%$ in SOP accuracy compared to the original system.

TABLE III WAVELENGTH AND SOP ACCURACY COMPARISON BETWEEN ORIGINAL SYSTEM AND SYSTEM WITH MODE RESHUFFLE AND WP-NET   

<table><tr><td>Displacement</td><td>Origin</td><td>1/8 with WP-Net</td></tr><tr><td>Wavelength error (MAE)</td><td>0.085 pm</td><td>0.045 pm</td></tr><tr><td>SOP error (RMSE)</td><td>0.0138</td><td>0.0088</td></tr><tr><td>S1 (MAE)</td><td>0.0079</td><td>0.0057</td></tr><tr><td>S2 (MAE)</td><td>0.0086</td><td>0.0056</td></tr><tr><td>S3 (MAE)</td><td>0.0081</td><td>0.0044</td></tr></table>

# D. Discussion

In speckle-based MMF systems, environmental perturbations inevitably induce temporal instability in fiber transmission characteristics. To improve system stability, researchers have adopted multiple strategies, including the expansion of training datasets to learn speckle patterns under different perturbations [32], the application of spatial-frequency tracking adaptive beacon light-field-encoded technique [33], and the implementation of a self-supervised dynamic algorithm [34]. It is demonstrated that these approaches have enhanced the robustness of speckle-based system. Beyond enhancing robustness, there remains significant potential for improving the accuracy of the system. The proposed system in this study can achieve greater precision by incorporating additional mode coupling into the structure, such as bending. Future research could integrate these methods with the existing system to achieve a wavelength and SOP analysis system with higher precision and capable of long-term stable operation.

# V. CONCLUSION

We proposed an MMF-based analyzer for high-dimensional light achieving precise wavelength and SOP measurements. Mode reshuffle introduced by core-offset splicing enhances short MMF system sensitivity. A WP-Net with physics-informed loss function based on the optical knowledge is designed to accelerate network convergence and augment prediction precision. The system merges two models covering distinct measurement ranges, enabling simultaneous detection of wavelength and SOP across an extensive spectral range with elevated accuracy. The MMF-based analyzer attains a wavelength accuracy of 0.045 pm and an SOP accuracy of 0.0088. It offers a compact, costeffective, and spatiotemporally efficient solution suitable for optical communications, imaging, and other fields.

# REFERENCES

[1] Y. Awaji, “Review of space-division multiplexing technologies in optical communications,” IEICE Trans. Commun., vol. E102.B, no. 1, pp. 1–16, 2019.   
[2] F. A. Iglesias and A. Feller, “Instrumentation for solar spectropolarimetry: State of the art and prospects,” Opt. Eng., vol. 58, no. 08, 2019, Art. no. 082417.   
[3] Y. Liu et al., “A multimode microfiber specklegram biosensor for measurement of CEACAM5 through AI diagnosis,” Biosensors, vol. 14, no. 1, 2024, Art. no. 57.   
[4] D. A. Glenar, J. J. Hillman, B. Saif, and J. Bergstralh, “Acousto-optic imaging spectropolarimetry for remote sensing,” Appl. Opt., vol. 33, no. 31, pp. 7412–7424, 1994.   
[5] Y. Ni, C. Chen, S. Wen, X. Xue, L. Sun, and Y. Yang, “Computational spectropolarimetry with a tunable liquid crystal metasurface,” eLight, vol. 2, no. 1, 2022, Art. no. 23.

[6] S.-K. Zhu et al., “Harnessing disordered photonics via multi-task learning towards intelligent four-dimensional light field sensors,” PhotoniX, vol. 4, no. 1, 2023, Art. no. 26, doi: 10.1186/s43074-023-00102-7.   
[7] Y. Fan et al., “Dispersion-assisted high-dimensional photodetector,” Nature, vol. 630, no. 8015, pp. 77–83, 2024.   
[8] D. Stam et al., “The spectropolarimeter for planetary exploration: SPEX,” in Proc. Int. Conf. Space Opt., SPIE, 2017, pp. 595–601.   
[9] M. F. Sterzik, S. Bagnulo, and E. Palle, “Biosignatures as revealed by spectropolarimetry of earthshine,” Nature, vol. 483, no. 7387, pp. 64–66, 2012.   
[10] J. Liu et al., “Deep learning-based simultaneous temperature- and curvature-sensitive scatterplot recognition,” Sensors, vol. 24, no. 13, 2024, Art. no. 4409.   
[11] H. Gao and H. Hu, “Spatially-resolved bending recognition based on a learning-empowered fiber specklegram sensor,” Opt. Exp., vol. 31, no. 5, pp. 7671–7683, 2023.   
[12] B. Redding, S. F. Liew, R. Sarma, and H. Cao, “Compact spectrometer based on a disordered photonic chip,” Nature Photon., vol. 7, no. 9, pp. 746–751, 2013.   
[13] B. Redding, M. Alam, M. Seifert, and H. Cao, “High-resolution and broadband all-fiber spectrometers,” Optica, vol. 1, no. 3, pp. 175–180, Sep. 2014. [Online]. Available: https://opg.optica.org/optica/abstract. cfm?URI=optica-1-3-175   
[14] E. Fujiwara, Y. Ri, Y. T. Wu, H. Fujimoto, and C. K. Suzuki, “Evaluation of image matching techniques for optical fiber specklegram sensor analysis,” Appl. Opt., vol. 57, no. 33, pp. 9845–9854, 2018.   
[15] F. M. Reis, P. F. Da Costa Antunes, N. M. Mendes Maia, A. R. Carvalho, and P. S. De Brito Andre, “Structural health monitoring suitable for airborne components using the speckle pattern in plastic optical fibers,” IEEE Sensors J., vol. 17, no. 15, pp. 4791–4796, Aug. 2017.   
[16] Y. Cai et al., “Reflective tactile sensor assisted by multimode fiber-based optical coupler and fiber specklegram,” Opt. Laser Technol., vol. 160, 2023, Art. no. 109062.   
[17] Y. Liu et al., “Reflective optical tactile sensor based on fiber specklegram analysis with the capability of contact position identification,” J. Lightw. Technol., vol. 41, no. 8, pp. 2540–2546, Apr. 2023.   
[18] F. T. S. Yu, M. Wen, S. Yin, and C.-M. Uang, “Submicrometer displacement sensing using inner-product multimode fiber speckle fields,” Appl. Opt., vol. 32, no. 25, pp. 4685–4689, 1993.   
[19] T. Wang, Y. Li, B. Xu, B. Mao, Y. Qiu, and Y. Meng, “High-resolution wavemeter based on polarization modulation of fiber speckles,” APL Photon., vol. 5, no. 12, 2020, Art. no. 126101.   
[20] Y. Xiong et al., “Multimode fiber speckle stokes polarimeter,” Adv. Photon. Nexus, vol. 3, no. 04, 2024, Art. no. 046010.

[21] M. Mounaix and J. Carpenter, “Control of the temporal and polarization response of a multimode fiber,” Nature Commun., vol. 10, no. 1, 2019, Art. no. 5085. [Online]. Available: https://www.nature.com/articles/ s41467-019-13059-8   
[22] Q. Zhou, Y. Wan, X. Fan, and H. Zuyuan, “High-accuracy simultaneous measurement of spectrum and full-stokes polarization based on speckle pattern,” in Proc. CLEO, Appl. Technol., 2024, pp. AF1D.4.   
[23] J. Kang, S. He, O. Alsalman, X. Liu, and C. Zhu, “Deep learning-enabled two-directional stretchable strain sensor based on a single multimode fiber,” IEEE Sensors J., vol. 24, no. 12, pp. 19143–19150, Jun. 2024.   
[24] Z. Ding and Z. Zhang, “2D tactile sensor based on multimode interference and deep learning,” Opt. Laser Technol., vol. 136, 2021, Art. no. 106760.   
[25] X. Wang et al., “An ultrasensitive fiber-end tactile sensor with large sensing angle based on specklegram analysis,” IEEE Sensors J., vol. 23, no. 24, pp. 30394–30402, Dec. 2023.   
[26] M. N. I. Sarkar, L. V. Nguyen, A. D. Kilpatrick, D. G. Lancaster, and S. C. Warren-Smith, “Dynamic multimode fiber specklegram sensor smart bed enabled by deep learning,” J. Lightw. Technol., vol. 42, no. 18, pp. 6342–6350, Sep. 2024.   
[27] C. Shen et al., “Intelligent optical fiber-integrated near-infrared polarimeter based on upconversion nanoparticles,” Adv. Opt. Mater., vol. 11, no. 22, 2023, Art. no. 2301259, doi: 10.1002/adom.202301259.   
[28] N. Takai and T. Asakura, “Statistical properties of laser speckles produced under illumination from a multimode optical fiber,” J. Opt. Soc. America A, vol. 2, no. 8, pp. 1282–1290, 1985.   
[29] M. Istiaque Reja, D. L. Smith, L. Viet Nguyen, H. Ebendorff-Heidepriem, and S. C. Warren-Smith, “Multimode optical fiber specklegram pressure sensor using deep learning,” IEEE Trans. Instrum. Meas., vol. 73, 2024, Art. no. 7003910.   
[30] B. Redding, S. M. Popoff, and H. Cao, “All-fiber spectrometer based on speckle pattern reconstruction,” Opt. Exp., vol. 21, no. 5, pp. 6584–6600, 2013.   
[31] M. Facchin, S. N. Khan, K. Dholakia, and G. D. Bruce, “Unveiling the significance of intrinsic sensitivity and multiple scattering in speckle metrology,” Nature Rev. Phys., vol. 6, pp. 500–508, 2024.   
[32] S. Resisi, S. M. Popoff, and Y. Bromberg, “Image transmission through a dynamically perturbed multimode fiber by deep learning,” Laser Photon. Rev., vol. 15, no. 10, 2021, Art. no. 2000553, doi: 10.1002/lpor.202000553.   
[33] Z. Wen, “Single multimode fibre for in vivo light-field-encoded endoscopic imaging,” Nature Photon., vol. 17, pp. 679–687, 2023.   
[34] Z. Li et al., “Self-supervised dynamic learning for long-term high-fidelity image transmission through unstabilized diffusive media,” Nature Commun., vol. 15, no. 1, 2024, Art. no. 1498. [Online]. Available: https: //www.nature.com/articles/s41467-024-45745-7