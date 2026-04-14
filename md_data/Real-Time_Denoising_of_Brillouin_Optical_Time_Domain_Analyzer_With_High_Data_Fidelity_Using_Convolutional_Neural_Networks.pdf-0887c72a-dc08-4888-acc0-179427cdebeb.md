# Real-Time Denoising of Brillouin Optical Time Domain Analyzer With High Data Fidelity Using Convolutional Neural Networks

Hao Wu, Yangyang Wan, Ming Tang , Senior Member, IEEE, Member, OSA, Yunjin Chen , Can Zhao, Ruolin Liao , Yiqing Chang, Songnian Fu , Perry Ping Shum, and Deming Liu

Abstract—In recent years, many conventional image denoising techniques have been intensively studied to enhance the signal to noise ratio (SNR) of Brillouin optical time domain analyzer (BOTDA), due to their superior denoising performance to onedimensional methods. However, in the case of low sampling rate, the details of the signal are smoothed out due to less useful information, resulting in a degradation of the spatial resolution. Moreover, these conventional denoising algorithms are quite time-consuming compared with the BOTDA measuring time. To overcome these drawbacks, we employ a feed-forward convolutional neural networks (CNN) based image denoising for BOTDA. A conventional BOTDA system with 15 ns pulse width is implemented to demonstrate the effectiveness of the exploited CNN-based denoising method. The actual electrical noise signals of the BOTDA at different sampling rates are collected to synthesize training samples. The CNN model is trained with the noise and simulated BOTDA signals. Experimental results show that SNR improvement of 13.43 dB, 13.57 dB, and $1 2 . 9 \ \mathrm { d B }$ is achieved at a sampling rate of 500 MSa/s, 250 MSa/s, and 125 MSa/s, respectively, via the trained CNN denoiser. No spatial resolution distortion can be observed in the denoised BOTDA signals. Besides, the CNN denoiser only takes 0.045 s to process a $\mathbf { 1 5 1 } \times \mathbf { 5 0 0 0 0 }$ image benefiting from GPU computing. This processing time is negligible compared with the acquisition time of BOTDA, which makes real-time denoising possible.

Manuscript received July 14, 2018; revised October 9, 2018; accepted October 16, 2018. Date of publication October 19, 2018; date of current version May 1, 2019. This work was supported in part by the National Natural Science Foundation of China under Grant 61331010 and Grant 61722108, in part by the Fundamental Research Funds for the Central Universities under Grant 2016YXZD038, in part by the Major Program of the Technical Innovation of Hubei Province of China under Grant 2016AAA014, and in part by the Open Fund of State Key Laboratory of Optical Fiber and Cable Manufacture Technology under Grant SKLD1706. (Corresponding author: Ming Tang.)

H. Wu, Y. Wan, M. Tang, C. Zhao, R. Liao, Y. Chang, S. Fu, and D. Liu are with the Wuhan National Laboratory for Optoelectronics and National Engineering Laboratory for Next Generation Internet Access System, School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail:, wuhaoboom@hust.edu.cn; wyy576355724@ qq.com; tangming@mail.hust.edu.cn; zhao_can@hust.edu.cn; rlliao@hust.edu. cn; chuhanluocyq@gmail.com; songnian@mail.hust.edu.cn; dmliu@mail.hust. edu.cn).

Y. Chen is with ULSee Inc., Hangzhou 310020, China (e-mail:, chenyunjin _nudt@hotmail.com).

P. P. Shum is with the School of Electrical and Electronics Engineering, Nanyang Technological University, 637553, Singapore (e-mail:, perryshum $9 1 6 @$ gmail.com).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/JLT.2018.2876909

Index Terms—Brillouin scattering, convolutional neural networks, distributed optical fiber sensors, fiber optics sensors, image denoising.

# I. INTRODUCTION

B RILLOUIN optical time-domain analyzer (BOTDA) is oneof the most wildly used fiber optic sensors in practical applications [1]. It has been intensively investigated due to the capability to measure distributed strain and temperature through Brillouin frequency shift (BFS) of optical fiber [2]. In a BOTDA system, a continuous wave downshifted probe light is introduced and interacted with the pump pulses in the fiber. If the frequency difference between the pump and probe lights is close to the local BFS, stimulated Brillouin scattering would occur and the higherfrequency pump would convert part of its energy to the probe through the acoustic wave field. By scanning the frequency of probe light and detecting the intensity gains of the probe signal, the Brillouin gain spectrum (BGS) is attained. The distributed BFS profile consists of the peak gain frequency of each fiber position. Therefore, the performance of BOTDA is limited by the signal-to-noise ratio (SNR) of the measured BGS, leading to tradeoffs among spatial resolution, sensing accuracy, sensing range, and response speed (averaging times) [3].

To enhance the SNR, signal processing techniques such as optical pulse coding [4], one-dimensional (1D) wavelet transform [5] have been proposed. However, their exploitation for BOTDA is restricted to 1D arrays of data. Recently, image processing methods have been employed for BOTDA system considering the measured BGSs along fiber as a two-dimensional (2D) image, which turns out to be more efficient [6]–[10]. Although these processing techniques can reduce noise, some useful information may also be removed. It has been pointed out that the spatial resolution will degrade as the SNR improvement increase when using conventional image denoising methods such as wavelet denoising, non-local means, and block matching 3D filter (BM3D) [10]. Besides, the degradation is intensified with a lower sampling rate because the details of the image are blurred due to less useful information [10]. So, it is necessary to oversample the BOTDA traces when using the conventional image denoising methods [9]. In addition, these algorithms are generally non-convex and involve several manually chosen parameters, resulting in complex parameter

![](images/7c3d03c210208d4b5cb859f60a182722ed8ac457a983c7122e22a297683faff9.jpg)  
Fig. 1. The architecture of the DnCNN.

adjustment processes [9], [11]. Moreover, the processing time of these algorithms is quite long compared to the BOTDA measuring time, so they cannot perform real-time denoising in practical applications.

To overcome these drawbacks, we apply convolutional neural network (CNN) based image denoising to BOTDA. CNN based methods are discriminative denoising methods which learn the underlying image prior from a training set of degraded and ground-truth image pairs. There are several successful CNN based methods which have similar or even better results than the traditional denoising methods [12]–[19]. Among them, the denoising convolutional neural network (DnCNN) has achieved very competitive denoising performance with relatively plain net structure [16]. In this work, we use the DnCNN for BOTDA denoising as a representative.

To demonstrate the feasibility of the CNN based image denoising method, a conventional BOTDA is implemented with 15 ns pump pulse width, 64 averaging times, and 151 scanning frequencies at a step of 2 MHz. The BGSs along the fiber are acquired at sampling rates of 500 MSa/s, $2 5 0 ~ \mathrm { M S a / s }$ , and $1 2 5 \mathrm { M S a / s }$ , respectively. Moreover, the actual noise signals of the BOTDA at these sampling rates are collected when the pump light is off. One DnCNN model is trained using simulated BOTDA traces and the actual noise. We train only one model to show the ability of the DnCNN to handle different noise characteristics. This feature makes the DnCNN more flexible in practical applications. After training, the DnCNN model is used to denoise the actual measured data of the BOTDA system. SNR improvement of 13.43 dB, 13.57 dB, and $1 2 . 9 \ \mathrm { d B }$ is achieved at $5 0 0 ~ \mathrm { M S a / s }$ , $2 5 0 ~ \mathrm { M S a / s }$ , and $1 2 5 ~ \mathrm { M S a / s }$ sampling rate, respectively. It takes only 0.045 s to process a $1 5 1 \times 5 0 0 0 0$ size image using GPU. This processing time is negligible for the acquisition time of BOTDA, which shows the potential of realtime denoising. To demonstrate the advantages of the trained model, one of the state-of-the-art conventional image denoising algorithms, BM3D is used as a comparison [20]. There is almost no degradation of spatial resolution using DnCNN whereas noticeable degradation is observed when using BM3D to achieve the same SNR improvement as the DnCNN.

# II. DNCNN

The architecture of the DnCNN is shown in Fig. 1. There are three operations in the DnCNN: convolution (Conv), batch normalization (BN), and rectified linear units (ReLU). Convolution operation can extract different feature maps from images using different convolutional filters. In shallow layers, the elementary visual features such as edges, end-points, corners are obtained. These features are then combined in higher layers to

learn characteristic of the inputs. This is why CNN can recognize or restore an image. However, it is hard to train the net with only convolution operation, so BN and ReLU are introduced to help the training process.

The BN operation is incorporated to speed up training as well as boost the denoising performance [21]. BN operation is proposed to solve the internal covariate shift (ICS) problem in the training process, which is defined as the change in the distribution of each layer’s inputs during training due to the change in the previous layers’ parameters. ICS makes it difficult to train the model and slows down the process. By normalizing the layer’s input without changing what the previous layer represents, BN operation can reduce the ICS.

To solve more complex problems, activation functions are adopted to add nonlinear factors. ReLU is one of the most popular activation functions. By using ReLU, a network can converge quicker during training and the problem of gradient vanish will be mitigated. By incorporating the convolution operation with ReLU [22], DnCNN can gradually separate image structure from the noisy observation through the hidden layers.

The depth of DnCNN is chosen to be 20, which means the receptive field is $4 1 \times 4 1$ . The 20 layers can be divided into three types: (1) for the first layer, 64 filters of size $3 \times 3$ are used to generate 64 feature maps from noisy input image, and ReLU are then utilized for nonlinearity; (2) for layers 2-19, 64 filters of size $3 \times 3 \times 6 4$ are used, and BN is added between convolution and ReLU; (3) for the last layer, a $3 \times 3 \times 6 4$ size filter is used to reconstruct the output.

$$
l (\Theta) = \frac {1}{2 N} \sum_ {\mathrm {i} = 1} ^ {N} \| R \left(y _ {i}; \Theta\right) - v _ {i} \| _ {F} ^ {2} \tag {1}
$$

The input of the DnCNN is a noisy image $y = x + \nu$ , where $x$ is the clean image and $\nu$ is the noise. For DnCNN, the residual learning formulation is adopted to train a residual mapping R(y) $\approx \nu$ , and then the clean image can be obtained by $x = y - R ( y )$ [19]. The residual (noise) output follows a Gaussian distribution which facilitates the Gaussian normalization step of batch normalization. Equation (1) is the loss function of DnCNN, which is the average mean squared error between the desired noises and estimated ones from noisy input [16]. To minimize the value of (1), the DnCNN is trained to obtain the characteristics of noise $\nu$ from the noise image y. In the back propagation phase of the training process, the trainable parameters $\Theta$ of each Conv, BN and ReLU are automatically changed to minimize the loss function. Through training, the DnCNN can estimate the distribution of noise from the input image based on the acquired knowledge.

# III. TRAINING PROCESS

To demonstrate the effectiveness of DnCNN in the BOTDA system, a conventional BOTDA system is implemented. As shown in Fig. 2, a narrow linewidth laser operating at $1 5 5 0 \mathrm { n m }$ is split into two distinct branches through a 3 dB coupler to generate both pump and probe light. In the probe wave branch, the light is double-sideband intensity modulated with a highextinction-ratio ( ${ \it > } 3 0$ dB) electro-optic modulator (EOM), operating in carrier-suppression mode. The EOM is driven by

![](images/d617b185751d63f29c1eefd0a0c4867e28be89acbe3e205b7baf70a7239aa904.jpg)  
Fig. 2. Experiment setup of BOTDA.

a microwave synthesizer (MS) to sweep the probe frequency from $1 0 . 5 5 \mathrm { G H z }$ to 10.85 GHz at a 2 MHz step. Then the probe is launched into the fiber through a polarization switch (PS) to mitigate the polarization effects. In the pump branch, a semiconductor optical amplifier (SOA) driven by an arbitrary function generator (AFG) is exploited to generate high-extinction-ratio $\mathit { \Omega } > 5 0$ dB) pulses (15 ns width with 2.5 ns rise and fall edges). The optical pulses are then boosted by an erbium-doped fiber amplifier (EDFA), and followed by an optical band-pass filter (BPF) to filter out the amplified spontaneous emission noise. Then the pump pulses are launched into the other end of the fiber through an optical circulator. At the receiver side, the Brillouinamplified probe wave is obtained through a bandwidth-variable tunable filter (BVTF). A $1 2 5 ~ \mathrm { M H z }$ high-transimpedance photodetector is employed to convert optical signals into electrical signals. Two fiber reels of about $5 ~ \mathrm { k m }$ are used for the test, and a section of about $1 0 0 \mathrm { ~ m ~ }$ fiber is put in a temperature controlled chamber (TCC). The room temperature is $2 2 \ { } ^ { \circ } \mathrm { C } .$ while the TCC is set to be $6 5 ~ ^ { \circ } \mathrm { C }$ . To demonstrate the influence of the sampling rate, the BGSs along the fiber are acquired at sampling rates of 500 MSa/s, 250 MSa/s, and $1 2 5 ~ \mathrm { M S a / s }$ , respectively.

The 125 MHz high-transimpedance photodetector makes the system thermal-noise dominated [23]. For an ideal resistor, its thermal noise is approximately white. When limited to a finite bandwidth, thermal noise has a nearly Gaussian distribution [24]. However, the actual resistance is defective, which makes the noise don not satisfy the ideal Gaussian distribution. The noise characteristics of photodetectors will vary depending on material properties, conversion principles, and bandwidth. Therefore, it is necessary to train the DnCNN using the actual noise signal rather than ideal Gaussian noise which is usually used in CNN training. To acquire the noise signals for training, we collect the output of the photodetector at different sampling rates when the pump light is off.

As the noise of the photodetector always exists, the groundtrue signal of BOTDA is unavailable. So, we simulate the BOTDA signal by combining ideal BGSs. The BGSs satisfy Lorentz distribution with random center frequencies, intensities, and bandwidth. Note that there may be a gap between the training and the testing due to the lack of real noisy free BOTDA signal, which will be investigated further in our future studies.

![](images/77d1a0a65bf2354ef3362f353d1c8afa8325224790437b5ed73bfd5207283003.jpg)  
Fig. 3. Training process of the DnCNN.

To speed up the training process, the mini-batch stochastic gradient descent (SGD) is used with weight decay of 0.0001, a momentum of 0.9 and a mini-batch size of 128. The images and noise signals are divided into patches of size $5 0 ~ \times ~ 5 0$ . The model is trained for 40 epochs. For each training epoch, random patch pairs of image and noise signal are combined as inputs of the DnCNN, and the corresponding noise signals are marked as the labels. A total of $1 2 8 \times 3 0 0 0$ patch pairs is used to train the model for one epoch. The learning rate is decayed exponentially from $1 0 ^ { - 2 }$ to $1 0 ^ { - 5 }$ for 40 training epochs. We employ the Nvidia CUDA Toolkit 8.0 and cuDNN v-8.0 deep learning library to accelerate the GPU computation. The MatConvNet package [25] is used. It takes about 45 hours to train the model based on Matlab (R2017b) running on a PC with AMD Ryzen 7 1700 eight-core processor and an Nvidia GeForce GTX 1070 Ti (8GB) GPU. To reduce the training time, the simplest way is to reduce the training data set, training epochs, or the network layers. However, the performance of the CNN may degrade. Another way is to use better hardware or more efficient software. Moreover, the optimization of the network structure can also improve the training speed.

Fig. 3 shows one of the simulated images used for training and the residual learning strategy of the DnCNN. The DnCNN predicts the noise image of the noisy input, then restores a clean image. During the training process, the parameters of the DnCNN are gradually optimized to minimize the difference between the acquired noise and the predicted result. Therefore, the trained DnCNN can be well adapted to the actual BOTDA system.

# IV. RESULT AND DISCUSSION

To demonstrate the performance of the trained model on denoising the actual BOTDA system, the measured BGSs along the sensing fiber are combined into one 2D image. As shown in Fig. 4, for better visual perception, different colors represent different Brillouin gain strength. It should be noted that the actual processed images have no color information. Fig. 4(a) shows one measurement result at the 500 MSa/s sampling rate, and

![](images/0b46ae091aef0df9bf0fe0950315aded87b49e222ab0982be993823c4d1826eb.jpg)  
(a)

![](images/01ad9c1b0dbd2900da429691c077d9d365bef204e6889224e5645e92b85c89b9.jpg)  
(b)

![](images/41493003601d2cee358091cd8bf9a21c9a813246bf658f7c9e56e86a3f6c827d.jpg)  
Fig. 4. BGSs of raw data (a) and denoised result with DnCNN (b) along the fiber at 500 MSa/s sampling rate.   
Fig. 5. BGS near the fiber end of raw data and denoised result with DnCNN at $5 0 0 \mathrm { M S a / s }$ sampling rate.

![](images/a36421c66b1c8a9ca603480abc4962f64bac06ceb222e31f80b1f8544d523b15.jpg)  
Fig. 6. BFS along the fiber of raw data and denoised result with DnCNN at $5 0 0 \mathrm { M S a / s }$ sampling rate.

Fig. 4(b) is the denoised result using the trained model, which shows a significant reduction of noise.

For more details, the BGS at the fiber end is shown in Fig. 5, where the blue one is the raw data, and orange one is the processed result using the DnCNN. A noticeable enhancement in the BGS measurement and considerable noise reduction is achieved with the DnCNN. Besides, no distortion can be observed in the BGS obtained after the denoising process. The distributed BFS profiles of raw data and processed data are then obtained by fitting Lorentz curves to the BGSs of each fiber location, as shown in Fig. 6. The fluctuations of the BFS profile is not representative of the noise and is mainly given by the coiling strain in the fibers, inducing BFS oscillations along the entire sensing range. The frequency uncertainty of the results is calculated by the mean error of the retrieved BFSs of consecutive measurements. The frequency uncertainty at $1 0 \mathrm { k m }$ distance of

raw data is $1 . 7 ~ \mathrm { M H z }$ . It is improved down to $0 . 2 ~ \mathrm { M H z }$ using the trained model, which indicates the effect of the proposed denoising method.

To objectively evaluate the effectiveness of the DnCNN, we calculate the SNR of the time-domain trace obtained at the peak Brillouin gain frequency. The SNR is calculated by the ratio between the mean amplitude of the measured local response and its standard deviation. SNR improvement of 13.43 dB, 13.57 dB, and $1 2 . 9 \ \mathrm { d B }$ is achieved at the $5 0 0 ~ \mathrm { M S a / s }$ , $2 5 0 ~ \mathrm { M S a / s }$ , and $1 2 5 \mathrm { M S a / s }$ sampling rate, respectively. The reason that the SNR improvement is smaller at $1 2 5 ~ \mathrm { M S a / s }$ sampling rate may attribute to the 125 MHz 3 dB bandwidth of the photodetector. The noise is bandlimited white noise at $5 0 0 ~ \mathrm { M S a / s }$ and $2 5 0 ~ \mathrm { M S a / s }$ sampling rate, whereas it becomes ideal white noise when the sampling rate is $1 2 5 \mathrm { M S a / s }$ .

In [10], the authors have confirmed that the spatial resolution may degrade using conventional image denoising methods, and BM3D turns out to be more effective to preserve the useful signal. To compare the data fidelity of BM3D with the trained DnCNN model, BM3D is used to process the same measured data. The BM3D code is the open source Matlab code proposed in [20]. The algorithm of BM3D includes three primary operations: block matching, collaborative filtering and reconstruction. By modifying the threshold of the filtering, the same SNR improvement as DnCNN at different sampling rates is guaranteed for a fair comparison. It runs on the same version of Matlab as the DnCNN on the same computer.

Fig. 7 shows the BFS profiles of the raw data, denoised data using DnCNN, and BM3D around the start of the heat section at different sampling rates. The experimental spatial resolution is defined as the fiber length of the temperature transition region between $10 \%$ and $90 \%$ of the peak amplitude. As shown in Table I, the spatial resolution of data processed by the BM3D deteriorates significantly, especially when the sampling rate is low. Because there is too little valid data in this variation area, it is difficult to recover the real data using BM3D. However, the results of DnCNN are consistent with the raw data at different sampling rates. The variations of the signal can be well preserved because the characteristics of the noise are different from the useful signal and can be recognized by the DnCNN. This future makes the DnCNN more reliable, and there is no need to use a high sampling rate device to secure the spatial resolution.

In addition to data fidelity, another critical aspect of a denoising method is the processing speed. Our BOTDA system has 151 scanning frequencies and 64 averages times. In theory, to achieve a detection range of $1 0 ~ \mathrm { k m }$ , the minimum acquisition time is $1 5 1 \times 6 4 \times 2 \times 1 0 0 ~ \mu \mathrm { s }$ (about 2 s). Besides, this acquisition time decreases with the average times. For the DnCNN, it takes only 0.045 s to process a $1 5 1 \times 5 0 0 0 0$ image, thanks to its suitable net structure for parallel computation on GPU. The memory transfer time between CPU and GPU are not counted, and the memory space of GPU is pre-allocated. Whereas, it takes about 70 s for BM3D to process a $1 5 1 \times 5 0 0 0 0$ image running in single thread model with the CPU. Although the speed of BM3D can be boosted by 7.5 times using GPU [26], its processing time is still much longer than DnCNN.

![](images/c91bd8fa8240194aa1ee827df6b90c5c16c96673d72f7aa64159250340c8e725.jpg)  
(a)

![](images/50255ac406fce7cc33c289716ff9f85a9f6249643ccf0f4c5e08e7e211e2fee7.jpg)  
(b)

![](images/eec75cfadd083d6fdf75ad796a5de5a4beb10b30595e9850d41a496803f4b9a7.jpg)  
(c）  
Fig. 7. BFS profiles of raw data (blue), denoised data using DnCNN (orange), and BM3D (green) around the start of heat section at different sampling rates.

TABLE I SPATIAL RESOLUTION IMPACT OF DNCNN AND BM3D PROCESSING ON BOTDA MEASUREMENTS   

<table><tr><td></td><td>500 MSa/s</td><td>250 MSa/s</td><td>125 MSa/s</td></tr><tr><td>Raw data</td><td>1.01 m</td><td>1.12 m</td><td>1.4 m</td></tr><tr><td>DnCNN</td><td>1.02 m</td><td>1.1 m</td><td>1.38 m</td></tr><tr><td>BM3D</td><td>2.01 m</td><td>3.58 m</td><td>6.9 m</td></tr></table>

# V. CONCLUSION AND DISCUSSION

A CNN based image denoising is employed for BOTDA denoising. The noise of an actual BOTDA system is acquired to train a DnCNN model. The trained DnCNN model brings significant SNR improvement and reduction of the BFS uncertainty. It takes only 0.045 s for the DnCNN to process a $1 5 1 \times 5 0 0 0 0$ image running on GPU, which is much faster than conventional image denoising methods. This processing time is negligible compared with the acquisition time of BOTDA, which makes real-time denoising possible. Besides, no signal distortion can be observed in the results using DnCNN, even when the sampling rate is low. This high data fidelity makes the DnCNN more reliable. Also, it reduces the need for high sampling speed devices, which is necessary when using conventional image denoising methods.

In practical applications, the noise characteristics of the photodetector may change due to the variations of temperature or power supply. This could lead to performance degradation or even failure of the DnCNN. To overcome this problem, the noise of the photodetector under different circumstances may be collected to improve the robustness of the DnCNN. Besides, the signal of a distributed optical fiber sensor is composed of the useful signal and pure noise. Therefore, the DnCNN can be fine-tuned based on the noise signal continuously so that it can adapt to environmental change after the initial training process.

The proposed denoising method is not limited to BOTDA but can also be applied to other fiber optic sensing systems, such as distributed, quasi-distributed and multiplexed fiber sensors by combining different periods into one 2D image. Once a sensing system is settled, its noise characteristic is determined, and the DnCNN can learn to separate it. Moreover, the deep learning field is evolving very quickly, and there may be some networks

that can provide better results than DnCNN. Therefore, it is meaningful to find or design denoising algorithms that are more suitable for fiber optic sensing systems.

It must be noted that denoising is only a basic task in image enhancement. We anticipate other image processing techniques such as single image super-resolution, image identification and classification based on deep convolutional neural networks can be applied to fiber optic sensing with impressive benefits.

# REFERENCES

[1] D. Zhou et al., “Single-shot BOTDA based on an optical chirp chain probe wave for distributed ultrafast measurement,” Light, Sci. Appl., vol. 7, Jul. 2018, Art. no. 32.   
[2] Z. Zhao, M. A. Soto, M. Tang, and L. Thevenaz, “Distributed shape sensing ´ using Brillouin scattering in multicore fibers,” Opt. Express, vol. 24, no. 22, pp. 25211–25223, Oct. 2016.   
[3] M. A. Soto and L. Thevenaz, “Modeling and evaluating the performance ´ of Brillouin distributed optical fiber sensors,” Opt. Express, vol. 21, no. 25, pp. 31347–31366, Dec. 2013.   
[4] M. A. Soto, G. Bolognini, P. F. Di, and L. The´venaz, “Simplex-coded BOTDA fiber sensor with 1 m spatial resolution over a 50 km range,” Opt. Lett., vol. 35, no. 2, pp. 259–261, Jan. 2010.   
[5] M. A. Farahani, M. T. V. Wylie, E. C. Guerra, and B. G. Colpitts, “Reduction in the number of averages required in BOTDA sensors using wavelet denoising techniques,” J. Lightw. Technol., vol. 30, no. 8, pp. 1134–1142, Apr. 2012.   
[6] M. A. Soto, J. A. Ram´ırez, and L. Thevenaz, “Intensifying the response ´ of distributed optical fibre sensors using 2D and 3D image restoration,” Nature Commun., vol. 7, Mar. 2016, Art. no. 10870.   
[7] N. Guo, L. Wang, H. Wu, C. Jin, H. Y. Tam, and C. Lu, “Enhanced coherent BOTDA system without trace averaging,” J. Lightw. Technol., vol. 36, no. 4, pp. 871–878, Feb. 2018.   
[8] X. Qian et al., “Noise level estimation of BOTDA for optimal nonlocal means denoising,” Appl. Opt., vol. 56, no. 16, pp. 4727–4734, Jun. 2017.   
[9] M. A. Soto, J. A. Ram´ırez, and L. Thevenaz, “Optimizing image denoising ´ for long-range Brillouin distributed fiber sensing,” J. Lightw. Technol., vol. 36, no. 4, pp. 1168–1177, Feb. 2018.   
[10] H. Wu, L. Wang, Z. Zhao, N. Guo, C. Shu, and C. Lu, “Brillouin optical time domain analyzer sensors assisted by advanced image denoising techniques,” Opt. Express, vol. 26, no. 5, pp. 5126–5139, Mar. 2018.   
[11] W. Dong, L. Zhang, G. Shi, and X. Li, “Nonlocally centralized sparse representation for image restoration,” IEEE Trans. Image Process., vol. 22, no. 4, pp. 1620–1630, Apr. 2013.   
[12] V. Jain and H. S. Seung, “Natural image denoising with convolutional networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., Dec. 2008, pp. 769– 776.   
[13] H. C. Burger, C. J. Schuler, and S. Harmeling, “Image denoising: Can plain neural networks compete with BM3D?,” in Proc. IEEE Conf. Comput. Vision Pattern Recogn., Jun. 2012, pp. 2392–2399.   
[14] J. Xie, L. Xu, and E. Chen, “Image denoising and inpainting with deep neural networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., Dec. 2012, pp. 341–349.

[15] Y. Chen and T. Pock, “Trainable nonlinear reaction diffusion: A flexible framework for fast and effective image restoration,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 6, pp. 1256–1272, Jun. 2017.   
[16] K. Zhang, W. Zuo, Y. Chen, D. Meng, and L. Zhang, “Beyond a Gaussian denoiser: Residual learning of deep CNN for image denoising,” IEEE Trans. Image Process., vol. 26, no. 7, pp. 3142–3155, Jul. 2017.   
[17] K. Zhang, W. Zuo, and L. Zhang, “FFDNet: Toward a fast and flexible solution for CNN based image denoising,” IEEE Trans. Image Process., vol. 27, no. 9, pp. 4608–4622, Sep. 2018.   
[18] X. Mao, C. Shen, and Y. Yang, “Image restoration using very deep convolutional encoder-decoder networks with symmetric skip connections,” in Proc. Adv. Neural Inf. Process. Syst., 2016, pp. 2802–2810.   
[19] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recogn., Jun. 2016, pp. 770–778.   
[20] K. Dabov, A. Foi, V. Katkovnik, and K. Egiazarian, “Image denoising by sparse 3-D transform-domain collaborative filtering,” IEEE Trans. Image Process., vol. 16, no. 8, pp. 2080–2095, Aug. 2007.   
[21] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” in Proc. Int. Conf. Mach. Learn., 2015, pp. 448–456.   
[22] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classification with deep convolutional neural networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., Dec. 2012, pp. 1097–1105.   
[23] J. Urricelqui, M. A. Soto, and L. Thevenaz, “Sources of noise in Brillouin ´ optical time-domain analyzers,” Proc. SPIE, vol. 9634, Sep. 2015, Art. no. 963434.   
[24] J. R. Barry, E. A. Lee, and D. G. Messerschmitt, Digital Communications. New York, NY, USA: Springer, 2004.   
[25] A. Vedaldi and K. Lenc, “MatConvNet: Convolutional neural networks for MATLAB,” in Proc. ACM Int. Conf. Multimedia, Oct. 2015, pp. 689–692.   
[26] S. Sarjanoja, J. Boutellier, and J. Hannuksela, “BM3D image denoising using heterogeneous computing platforms,” in Proc. IEEE Conf. Design Arch. Signal Image Proc., Sep. 2015, pp. 1026–1034.

Ming Tang (SM’11) received the B.Eng. degree from Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technology Research Centre that was focused on the optical fiber amplifier, high-power fiber lasers, nonlinear fiber optics, and all-fiber signal processing. From February 2009 to 2011, he was a Research Scientist with Tera-Photonics Group, led by Prof. H. Ito in RIKEN, Sendai, Japan, conducting research on terahertz-wave generation, detection, and application using nonlinear optical technologies. Since March 2011, he has been a Professor with the School of Optical and Electronic Information, Wuhan National Laboratory for Optoelectronics, HUST. He has published more than 100 technical papers in the international recognized journals and conferences. His current research interests include optical fiber-based linear and nonlinear effects for communication and sensing applications.   
Dr. Tang has been a member of the IEEE Photonics Society since 2001, and also a Member of the Optical Society of America.

Yunjin Chen, biography not available at the time of publication.

Can Zhao, biography not available at the time of publication.

Ruolin Liao, biography not available at the time of publication.

Yiqing Chang, biography not available at the time of publication.

Songnian Fu, biography not available at the time of publication.

Perry Ping Shum, biography not available at the time of publication.

Deming Liu, biography not available at the time of publication.

Hao Wu received the B.S. and M. Eng degrees from the School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, in 2013 and 2016, respectively. He has been working toward the Ph.D. degree at the Huazhong University of Science and Technology since 2016. His current research interests include the application of special optical fiber and machine learning algorithm in distributed optical fiber sensing.

Yangyang Wan, biography not available at the time of publication.