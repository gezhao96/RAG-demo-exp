# Super Spatial Resolution Raman Distributed Temperature Sensing via Deep Learning

Hao Wu , Can Zhao , and Ming Tang , Senior Member, IEEE

Abstract—Raman distributed temperature sensing (RDTS) can obtain temperature information along with an optical fiber. Its spatial resolution is defined by the minimum spatial range that can be resolved by the system. The spatial resolution can be improved by reducing the optical pulse width. However, simultaneously, the signal-to-noise ratio is degraded, and higher speed equipment is required. Recently, deconvolution algorithms have been employed to improve spatial resolution without hardware modification. However, conventional deconvolution algorithms have limited effectiveness. Here, we propose and experimentally demonstrate an RDTS super spatial resolution deep convolutional neural network (SSRNet) to improve the spatial resolution with high fidelity. The convolution kernel of the RDTS is estimated from the falling signal at the fiber end rather than using the waveform of pulsed light. Then a modified RDTS model is built to generate a large amount of training data. Through optimizing the structure of SSRNet, the spatial resolution is increased from 4 m to $\mathbf { 0 . 8 m }$ which has reached the limit of the sampling rate of 250 MSa/s. The simulation and experimental results show that the restored results using SSRNet are more accurate with fewer artifacts than the results using a conventional deconvolution algorithm.

Index Terms—Optical fiber sensors, Raman scattering, optical time domain reflectometry, spatial resolution, convolutional neural networks.

# I. INTRODUCTION

R AMAN distributed temperature sensing (RDTS) is widelyused to monitor the condition of pipelines and tunnels used to monitor the condition of pipelines and tunnels thanks to its capability to measure temperature information along with an optical fiber [1]. RDTS realizes temperature measurement through analyzing the temperature-dependent spontaneous Raman backscattering intensity. Through injecting a pulse light into the optical fiber, the distance information of the scattering point can be obtained based on light flight time [2]. Spatial resolution is an essential indicator of an RDTS system. It refers to the minimum fiber length where temperature can

Manuscript received 19 October 2021; revised 18 June 2022; accepted 29 July 2022. Date of publication 2 August 2022; date of current version 3 August 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1801002, in part by the National Natural Science Foundation of China under Grant 61931010, in part by Hubei Province Key Research and Development Program under Grant 2020BAA006, and in part by the Innovation Fund of WNLO. (Corresponding author: Can Zhao.)

The authors are with the Wuhan National Laboratory for Optoelectronics and National Engineering Laboratory for Next Generation Internet Access System, School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: 2019507013@hust.edu.cn; zhao_can@hust.edu.cn; tangming@mail.hust.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSTQE.2022.3195734.

Digital Object Identifier 10.1109/JSTQE.2022.3195734

be effectively measured. To improve the spatial resolution of RDTS, the simplest way is to reduce the pulse width. However, reducing pulse width requires higher-speed hardware equipment, which increases the system cost. Moreover, it will cause a drop in signal-to-noise ratio (SNR), leading to a degradation of temperature measurement accuracy.

To address this problem, researches have been conducted from the perspective of signal processing to improve spatial resolution without hardware modification. As the power of the pump light is below the stimulated Raman threshold, the RDTS signal can be considered as a linear convolution of a high spatial resolution signal and a convolution kernel. Therefore, deconvolution algorithms can theoretically restore RDTS signals with infinitely high spatial resolution [3]–[5]. However, deconvolution is an ill-posed problem due to the presence of noise. Therefore, regularizations are employed in the conventional deconvolution process. However, it is difficult to take full advantage of the RDTS’s characteristics with manually designed regularizations, resulting in a gap between the restored result and the real signal. Thus, the conventional deconvolution algorithms may reduce the SNR and even make the signal distorted. On the other hand, accurate deconvolution requires a known convolution kernel. However, the convolution kernel of the RDTS system differs from the pulsed light shape of the light source due to the dispersion and system response. Currently, there is not a simple and feasible method for estimating the convolution kernel, which leads to poor deconvolution results. In 2018, an artificial neural network method was proposed [6]. The inputs of the neural network are the measured room temperature, the heating temperature, and the length of the heated optical fiber. The outputs are the corresponding actual data. Using this neural network, the temperature of the heated optical fiber whose length is less than the spatial resolution can be obtained. However, the temperature of the training data is fixed in that study. Only the length of the heated optical fiber varies. Besides, the heating position needs to be determined in advance, making this method cannot be applied to complicated situations.

To improve the spatial resolution of RDTS with more universality and practical value, a super spatial resolution neural network (SSRNet) is proposed in this paper. The SSRNet is a deep fully convolutional neural network (CNN). Through the data-driven deep learning method, SSRNet can make full use of the prior knowledge of RDTS. Through optimizing the training data and neural network structure, the SSRNet breaks through the limitation of pulse width in RDTS and raises the spatial resolution to the limit of the Nyquist sampling theorem.

![](images/f942997969fa221ba15c760d9bd99a3d82de08c8703e1b1523072659b0a158ef.jpg)  
Fig. 1. Experimental setup of RDTS system.

Compared with the conventional deconvolution algorithm, the proposed deep learning method provides higher accuracy and fidelity.

# II. PRINCIPLES AND METHODS

# A. RDTS

Fig. 1 shows the RDTS system used in this paper. The spatial resolution in general dual-wavelength demodulation RDTS is affected by dispersion [7]. To avoid the influence of this factor and analyze the proposed method more accurately, we only use spontaneous Raman anti-Stokes backscattered light (SRAB) for temperature demodulation. A pulsed light source (PLS) with 40 ns pulse width is employed as the light source. The pulse light enters the fiber under test (FUT) through an optical circulator. When the pulse light propagates in the FUT, it will interact with the optical fiber to produce spontaneous Raman backscattered light. The SRAB passes through an optical circulator and is obtained by a Raman filter (RF). The light signal is converted into an electrical signal by a $1 2 5 ~ \mathrm { M H z }$ bandwidth avalanche photodetector (APD). The electrical signal is then acquired by a data acquisition board (DAQ) at a sampling rate of $2 5 0 \mathrm { M S a / s }$ and the SRAB traces are averaged 40000 times in 1 second.

The intensity of SRAB is sensitive to the temperature $T$ of optical fiber [7]:

$$
\begin{array}{l} P (T) = P _ {0} K v ^ {4} \\ \times \frac {1}{\exp (h \Delta v / k T) - 1} \times \exp [ - (\alpha_ {0} + \alpha_ {\mathrm {A S}}) L ], \tag {1} \\ \end{array}
$$

where $P _ { 0 }$ is the power of PLS, $K$ is the scattering coefficient, $\nu$ is the frequency of SRAB, $h$ is the Planck constant, $\Delta \nu$ is the Raman frequency shift, $k$ is the Boltzmann constant, $\alpha _ { 0 }$ and $\alpha _ { \mathrm { A S } }$ are the transmission loss factors of pulse light and SRAB, and $L$ is the fiber length. Using a SRAB signal at a known temperature $T _ { 0 }$ as a reference, temperature information of measured signal can be demodulated:

$$
T = \frac {h \Delta v / k}{\ln \left[ \frac {\exp \left(h \Delta v / k T _ {0}\right) - 1}{P (T)} P \left(T _ {0}\right) + 1 \right]}. \tag {2}
$$

According to the time t from the pulsed light emission to the scattered light return, the fiber length where the scattering occurs can be obtained:

$$
L = \frac {c t}{2 n}, \tag {3}
$$

where $c$ is the speed of light in vacuum and $n$ is the refractive index of the FUT. Theoretically, the RDTS can obtain the timedomain backscattered signal $x ( t )$ along the FUT. However, since the pulsed light has a duration, the actual obtained RDTS trace $y ( t )$ is the linear convolution of the system convolution kernel $h ( t )$ with the $x ( t )$ . Merged with an additive noise $n ( t )$ , the measured RDTS trace can be expressed as:

$$
y (t) = h (t) \otimes x (t) + n (t). \tag {4}
$$

As a result, the measured trace $y ( t )$ will be smoother than the real signal $x ( t )$ , which means it cannot accurately measure the temperature that changes sharply along the fiber. The minimum fiber length of temperature change section that an RDTS can effectively measure is called spatial resolution $S R$ , which is mainly determined by the pulse width $\tau$ :

$$
S R = \frac {c \tau}{2 n}. \tag {5}
$$

Theoretically, the pulse width of 40 ns corresponds to a spatial resolution of about 4 m. A higher spatial resolution can be achieved by reducing the pulse width, but the SNR will be reduced accordingly. In addition, to generate and detect a narrower pulse light, higher-speed devices are required, which increases the cost and implementation difficulty of the system.

# B. Total Variation Deconvolution

Theoretically, deconvoluting of $y ( t )$ can restore the real signal $x ( t )$ . The frequency domain expression of the real signal can be obtained by performing Fourier transform on (4):

$$
X (f) = \frac {Y (f) - N (f)}{H (f)}, \tag {6}
$$

where $X ( f ) , Y ( f ) , H ( f )$ , and $N ( f )$ are the frequency spectra of $x ( t )$ , $y ( t ) , h ( t )$ , and $n ( t )$ , respectively. So, the real signal $x ( t )$ can be obtained by performing an inverse Fourier transform on $X ( f )$ . However, due to the presence of noise, this simple deconvolution method is not applicable. Since some frequency components of $H ( f )$ are small, the noise will be amplified, generating a poor result.

To suppress the influence of noise, regularization such as the total variation is employed [5]:

$$
\hat {x} (t) = \underset {x (t)} {\operatorname {a r g m i n}} \| y (t) - x (t) \otimes h (t) \| _ {1} + \lambda \| D x (t) \| _ {1}, \tag {7}
$$

where $D$ is the forward finite-difference operator to count the magnitude of the signal change [8]. And $\lambda$ is the regularization parameter. When λ is 0, the highest spatial resolution can be achieved, but the results are sensitive to noise. With the increasing of λ, the total variation regularization term plays a more important role, which makes the result smoother. Therefore, λ should be manually optimized according to data characteristics and application requirements. Although total variation deconvolution (TVD) can improve the spatial resolution, it may reduce SNR and even bring some artifacts, which are undesirable.

# C. CNN Deconvolution

In recent years, with the development of machine learning techniques, CNNs have been widely used in image deblurring (i.e., deconvolution) [9], [10]. Through multi-layer convolution and nonlinear operations, deep CNNs can perform arbitrary deconvolution functions. CNNs are trained with a large amount of real signals and the corresponding convolutional data. During the training process, the parameters of a CNN will be gradually optimized so that the CNN can have the best deconvolution effect on the entire training set. This training process corresponds to the design and optimization process of the conventional deconvolution methods. It can also be understood that the CNN obtains the prior statistical knowledge of the data in this training process. Since this statistical process is only for a specific training set, the CNN can obtain a more accurate prior knowledge using its powerful fitting capabilities. Besides, when the amount of training data is sufficient, the trained CNN can also play an advantageous effect on data with similar characteristics. Therefore, compared with conventional manually optimized deconvolution algorithms, CNNs usually achieve better results.

# D. Training Data

To train a neural network to learn the RDTS’s characteristics, the first and most important thing is to prepare a large amount of training data. The training data needs to be composed of measured RDTS data and the corresponding noise-free high-SR data. However, in the actual system, the photoelectric conversion process will inevitably introduce electrical noise, and it is impossible to obtain a noise-free signal. In addition, to ensure the universality of the neural network, the training data needs to include various temperature and fiber link conditions. Getting enough data experimentally takes a lot of time and is almost infeasible. In this case, we propose a modified RDTS model to synthesize sufficient training data. To make the synthesized data have the same characteristics as the actual RDTS system, the exact convolution kernel of the system needs to be obtained. For a general time-domain distributed optical fiber sensing system, the optical pulse waveform can be considered as the convolution kernel of the system. However, the SRAB of an RDTS system has a large frequency difference from the incident light. Due to dispersion and detector response, the convolution kernel of the system differs from the pulse waveform. Here, we estimate the convolution kernel by measuring the signal at the end of the fiber, as shown in Fig. 2(a). Since the real signal at the end of the fiber is theoretically a step signal, the convolution kernel $h$ can be calculated from the measured signal I:

$$
h _ {i} = \left\{ \begin{array}{c c} I _ {2 4} & i = 0 \\ I _ {2 4 - i} - I _ {2 5 - i} & i > 0 \end{array} . \right. \tag {8}
$$

As shown in Fig. 2(b), the edges of calculated convolution kernel are smoother compared to the measured optical pulse waveform of light source. Obtaining the actual convolution kernel of the system ensures the efficient of the synthesized training data.

![](images/f3bc58a0c47c7998ad5b9e0115db466e41109c5bf6c03e23a975bdec6498bbad.jpg)

![](images/a2b2d63b615ee099087fd87d673d93e4bd3695dc4fc67e2407750c55d875d7f6.jpg)  
Fig. 2. (a) Theoretical and measured trace at the fiber end; (b) measured optical pulse waveform and calculated convolution kernel.

To make the SSRNet adaptable to any RDTS system, it is necessary to simulate various SRAB curves for different cases. The simulation can theoretically be performed by varying the parameters in (1). However, the exponential decay term will generate more low-intensity data than high-intensity data, causing the neural network to be more inclined to recover the low-intensity data. In addition, the actual SRAB data are more complex than (1) due to random losses and reflections in the fiber link. Therefore, we propose a modified RDTS model. For a CNN, each point of its output is computed using only a finite number of points of the input data, which is called the receptive field. The receptive field of SSRNet is 193, which corresponds to about $7 7 . 2 \mathrm { m }$ optical fiber. The transmission loss of $7 7 . 2 \mathrm { m }$ fiber section is about 0.04 dB which can be ignored compared with noise. Therefore, the signal in the receptive field range is only related to the temperature, fiber loss and reflectivity. To ensure the generality of the data, the signal changes due to temperature, loss, and reflection can be represented by the randomly varying intensities [11]. And the signal intensity remains consistent within a random number of sampling points to represent a relatively uniform temperature. Considering that the pulse width is 10 times the sampling interval, the random range of consistent points is within 1 to 40 to make the amount of variation area and smooth area in the curve after convolution comparable. Then we convolve the synthesized SRAB signals with the convolution kernel to generate the corresponding convolutional data. In addition, Gaussian white noise is added to the convolutional data. This noisy convolutional data is used as the training input, and its

![](images/de1f0cb24c89c3d996665ebb2835e4ee9293cdc984a28c85a15296b9b28c0b00.jpg)  
Fig. 3. A section of synthesized training data.

corresponding noise-free high-SR curve is the training label. As shown in Fig. 3, the input curve becomes smoother than the label due to the convolution process. Therefore, it cannot accurately reflect the intensity of the signal whose duration is less than the convolution kernel. We generate 3200 pairs of training curves, of which 2560 pairs are used as the training set and the remaining 640 pairs as the validation set. Each synthesized curve contains 20000 sampling points.

# E. Training and Optimization

To obtain a neural network capable of RDTS deconvolution, we first test with a plain CNN and ResNet structures [12]. As shown in Fig. 4(a), the neural network is designed in three parts, including an input part, middle blocks and an output part. It consists of convolution (Conv) layers [13], batch normalization (BN) [14], and rectified linear units (ReLU) [15]. Conv can extract different features of input data using different convolutional filters. BN is employed to normalize the data during training to help the network converge more quickly. As the most commonly used activation function, ReLU turns the result less than 0 into 0, and the data greater than 0 remains unchanged. Fig. 4(b) shows the middle block structure of a plain CNN, which is implemented by stacking the Conv, BN and ReLU layers. The input data are computed in order through each layer. Fig. 4(c) shows the middle block structure of the ResNet. The ResNet uses shortcut connections to achieve identity mapping, which reduces the training difficulty of deep neural networks. To balance the deconvolution effect with the complexity and computation amount, the architecture parameters are optimized by testing. Considering RDTS is one-dimensional data, it needs to be processed by one-dimensional Conv. Unlike the two-dimensional Conv for image processing, a large kernel size of one-dimensional Conv will increase the computational efficiency for a same receptive field. The one-dimensional Conv kernel size is 9 with 128 channels, and the number of ResBlocks is 11. Therefore, the receptive field of SSRNet is 193, which means that each point of the output is related to 193 points of the input data.

The neural networks are trained for 1000 epochs with a batch size of 64 and a learning rate of 0.0003. In each epoch, the input data is first propagated forward, and then the mean squared error

![](images/938f69951ba719afd97fa2a46b7e65d5e835861a3f157b133c6846a471c078dc.jpg)

![](images/edf63f8e92d7451253c631dbbd8da0a8b9f08b2c268b46f548848e0f76ea4273.jpg)

![](images/1f885c1502938c10e54d083704d0ff5f924d712231cacb2f820b7a5728358c5a.jpg)

![](images/beef2b7b08140f32bd94cbc47662f1752404dbbc36fb5d804dc56162a7c2d02e.jpg)  
Fig. 4. Neural network structure diagram. (a) Overall architecture of the neural networks; (b) middle block structure of plain CNN; (c) middle block structure of ResNet; (d) middle block structure of SSRNet.

(MSE) of the difference between the output and the label is calculated and propagated backward. The Adam optimization algorithm is used to update the network parameters [16]. It calculates the first-order moment estimation and second-order moment estimation of the gradient to design independent adaptive learning rates for different parameters. It takes about 32 hours for the plain CNN and 33 hours for the ResNet to complete the training process with Pytorch running on a PC with NVIDIA TITAN RTX GPU (24G). Fig. 5 shows the average peak SNR (PSNR) of training data, and validation data proceeded by the plain CNN and ResNet for each training epoch. The ResNet performs better than the plain CNN on the training set, which indicates that the introduction of shortcuts improves the fitting ability of the neural network. Unfortunately, both validation PSNR traces have large fluctuations, suggesting that the effect of the neural networks on the validation data is unstable and overfitting occurs.

To solve this anomaly, we propose an SSRNet by removing the BN in the ResNet, as shown in Fig. 4(d). It takes about 27 hours to complete the training process without BN. As shown in Fig. 5, the PSNR of the validation data is more consistent with the training set after removing the BN. Moreover, the highest validation PSNR using the ResNet is 26 dB, while the

![](images/1d821d3bd3a55ffc825b7e6b64c9ba890e1d9ad38eb30c731755f8095d3f6634.jpg)

![](images/4b5aba11b54167d957d73dddc28c0198e1f51c33b0b9362c827169e74bece09d.jpg)  
  
Fig. 5. PSNR of plain CNN, ResNet and SSRNet on (a) training and (b) validation sets as a function of training epoch.

highest validation PSNR using SSRNet is 28.6 dB, indicating that removing the BN can increase the deconvolution ability of the SSRNet. The BN normalizes its input without changing what the previous layer represents. Theoretically, the BN can reduce the internal covariate shift problem in the training process and help the neural network converge [14]. The assumption of BN is that the data are independent and identically distributed such as denoising task. Therefore, BN can optimize its normalization parameters according to the distribution of all training data. However, in the RDTS deconvolution task, the residual output distribution is related to the input data, so it is not independent and identically distributed. Therefore, the BN instead makes it more difficult to train the neural network.

To avoid overfitting, the parameters that perform best on the validation set are saved as the final parameters of the three neural networks. Fig. 6 shows a section of validation data and the results processed by the plain CNN, ResNet, and SSRNet, respectively. All three neural networks can process the input data closer to the label. Compared with the others, the SSRNet can restore the data with smaller errors. And the results are almost consistent with the label using the SSRNet.

# III. RESULTS AND DISCUSSION

# A. Simulation Results

To compare the performance between the proposed SSR-Net and the TVD quantitatively, the test is first performed by

![](images/ce78e4eb8a3867db47f8fce8a93012c5ca6e82845d1bf06033e4d9dfeb0c26f2.jpg)  
Fig. 6. A section of validation data and the results processed by the plain CNN, ResNet and SSRNet.

simulation since it is impossible to measure noise free RDTS data experimentally. As shown in Fig. 7(a), 5 SRAB traces are simulated based on (1). The sampling rate is $2 5 0 \mathrm { M S a / s }$ as the experiment setting, and the fiber length is $5 \mathrm { k m }$ corresponding to 12500 sampling points. There are 500 sampling points before the fiber and 1000 sampling points after the fiber where there is no signal. The transmission loss is $0 . 5 \ \mathrm { d B / k m }$ . The room temperature is $2 0 ^ { \circ } \mathrm { C }$ , and the temperature at $4 \mathrm { k m }$ is $8 0 ^ { \circ } \mathrm { C }$ . The sampling points corresponding to $8 0 ^ { \circ } \mathrm { C }$ of the five curves are 1, 5, 10, 15, and 20, respectively. These ideal SRAB traces are then convolved with the convolution kernel. And the $P _ { 0 } K \nu ^ { 4 }$ is set to be 0.13 to normalize the traces to between 0 and 1. Finally, Gaussian white noise is added to the normalized data. Due to the convolution effect, the intensity of $8 0 ^ { \circ } \mathrm { C }$ will be affected by the surrounding data. The fewer fiber length of $8 0 ~ ^ { \circ } \mathrm { C }$ , the more significant the impact.

We use the TVD and SSRNet to process these traces to get the information hidden in them. The regularization parameter is manually optimized to 0.05 to ensure that the TVD can restore the highest intensity at $4 \mathrm { k m }$ , as shown in Fig. 7(b). Compared with the raw signals, the TVD enhances the intensities at $4 \mathrm { k m }$ , but also carries significant signal distortion. The results provided by the SSRNet are shown in Fig. 7(c). The signals are recovered accurately with no distortion. To quantify the performance of the two methods, the MSE of the differences between the restored traces and the target traces is calculated. The averaged PSNR using the TVD is 19.7 dB, while the averaged PSNR with the SSRNet is 39.2 dB. The SSRNet can suppress noise and provide more accurate results in this task. Fig. 8 shows the demodulated temperature using the SRAB traces. When the number of points of $8 0 ^ { \circ } \mathrm { C }$ is small, RDTS cannot measure the temperature accurately. Although the TVD can make the temperature results closer to the real value, it also brings undesired noise. Compared with the TVD, the SSRNet works well for each case.

# B. Experimental Results

To demonstrate the effect of the SSRNet on actual RDTS data, heating experiments are conducted. As shown in Fig. 9, we connect a reel of about $9 0 0 \mathrm { m }$ and a reel of about $6 0 0 \mathrm { m }$ of optical

![](images/50ee894f50fb36a1f8030dcea8dbae7abe1581482f32e92d68fb3ccb2514d9be.jpg)

![](images/b345ae5c92be598041b8261aa8c68e845aa65dc0556ff4fba8bdc9c61c034e28.jpg)

![](images/1f687e29527ec2591bc36c817039d796886a5ac712e87b7c5b0188dafee930f2.jpg)  
Fig. 7. 5 km SRAB traces where temperature at $4 \mathrm { k m }$ is $8 0 ^ { \circ } \mathrm { C }$ . The sampling points corresponding to $8 0 ^ { \circ } \mathrm { C }$ are 1, 5, 10, 15, and 20, respectively. (a) Simulated raw SRAB traces; (b) SRAB traces processed by the TVD; (c) SRAB traces processed by the SSRNet.

fiber, and use a water bath to heat the fiber at $9 0 0 \mathrm { m }$ and the end of the fiber. Considering the $2 5 0 \mathrm { M S a / s }$ sampling rate and the limit of the Nyquist sampling theorem, the extreme spatial resolution of this system is $0 . 8 \mathrm { m }$ . So, we put two $0 . 8 \mathrm { m }$ fiber sections in the water bath to change their temperatures. The water temperature is set to $6 0 ~ ^ { \circ } \mathrm { C }$ , $7 0 ~ ^ { \circ } \mathrm { C }$ and $8 0 ~ ^ { \circ } \mathrm { C }$ , while the room temperature is about $2 5 ~ ^ { \circ } \mathrm { C }$ . The measured SRAB trace when the water bath is set to $8 0 ~ ^ { \circ } \mathrm { C }$ is shown in Fig. 10 as well as the processed results using the SSRNet and TVD. As shown in Fig. 10(b), the intensity change of the high-temperature section is more obvious after processing. And the data becomes steeper at the connection position of the two reels of optical fiber. The same phenomenon can be found in Fig. 10(c), indicating that deconvolution can improve spatial resolution. Compared with the TVD, the result using the SSRNet shows higher spatial resolution.

The demodulated temperature profiles when the water bath is set to $6 0 ^ { \circ } \mathrm { C }$ , $7 0 \mathrm { { } ^ { \circ } C }$ and $8 0 ^ { \circ } \mathrm { C }$ are shown in Fig. 11. Compared with the TVD, the SSRNet can restore the water temperatures more accurately. As shown in Table I, we count the absolute

![](images/b0eeb44a0d89effd3124fdc33b9e9eea59b607d8394ab3bd72bb4919ac9bfd50.jpg)

![](images/cf62771082abe32b18fd2dc56c3d213802dad8b9282f1f15b9c4e7161818fe9a.jpg)

![](images/dac5bc1a813fac1fb3121e14488ba85d750b251ef4aec9ddee9d12e1c60b4fc9.jpg)  
Fig. 8. Temperature results using different SRAB traces. (a) Raw SRAB traces; (b) processed by the TVD; (c) processed by the SSRNet.

![](images/8dc16d5b55e5d0200b77bc673f5267b51fff826181f91e3b8449bf8ea0f80606.jpg)  
Fig. 9. Experimental setup. Two $0 . 8 \mathrm { m }$ sections of optical fiber are heated in a water bath.

TABLE IABSOLUTE TEMPERATURE ERRORS OF DIFFERENT SRAB TRACES  

<table><tr><td>Water temperature</td><td>Location</td><td>Raw</td><td>TVD</td><td>SSRNet</td></tr><tr><td>60 °C</td><td>First heating section</td><td>28 °C</td><td>12.1 °C</td><td>1.2 °C</td></tr><tr><td rowspan="3">70 °C</td><td>Second heating section</td><td>27.5 °C</td><td>14 °C</td><td>0.6 °C</td></tr><tr><td>First heating section</td><td>35.2 °C</td><td>17.9 °C</td><td>0.5 °C</td></tr><tr><td>Second heating section</td><td>34.2 °C</td><td>12.2 °C</td><td>1.4 °C</td></tr><tr><td rowspan="2">80 °C</td><td>First heating section</td><td>43.2 °C</td><td>21.9 °C</td><td>0.7 °C</td></tr><tr><td>Second heating section</td><td>42 °C</td><td>17.4 °C</td><td>0.6 °C</td></tr></table>

![](images/dbf01d3d3fc48297e413290dc75fe2708ccf28f5f38b773ef3579d056caeef62.jpg)

![](images/7dc038ffcd466647799cad99316207155c2cce52efc8a0ec667f8c4a8989b2a4.jpg)

![](images/600324c2d27012eb969e7625b81db21e8586a29dd11731ba95cf2d8b3f9aec35.jpg)  
Fig. 10. Measured and processed SRAB traces when the water bath is set to $8 0 ~ ^ { \circ } \mathrm { C } .$ (a) The overall results; (b) data around the first heating section; (c) data around the second heating section.

temperature error of the heating sections of each result. Due to the convolution effect, the larger the difference between the water temperature and the room temperature, the larger the temperature error using the raw data. After deconvolution, the temperature error drops significantly. Compared with the TVD, the deconvolution effect of the SSRNet is better, and the measurement error using the SSRNet is within $1 . 5 ^ { \circ } \mathrm { C }$ . Although deconvolution process can improve the spatial resolution, it also introduces noise, leading to an increase in the measurement uncertainty of the RDTS system. Here, we estimate the temperature uncertainties by calculating the temperature standard deviation of the first 500 meters of fiber, where their temperatures should be the same. The temperature uncertainties using the raw data, the data processed by SSRNet, and data processed by the TVD are $0 . 2 3 ^ { \circ } \mathrm { C }$ , $0 . 3 7 ^ { \circ } \mathrm { C }$ , and $1 . 2 5 ^ { \circ } \mathrm { C }$ , respectively. The SSRNet can achieve higher spatial resolution improvements with higher fidelity. Moreover, it takes about 0.35 s for the SSRNet to process one SRAB trace, which is less than the sampling time of 1 s. This means that the SSRNet is capable of real-time processing.

![](images/8d539e8f05a8c01915f1ac159967b8874b19703e06e674f858fc647242c49fb9.jpg)

![](images/7d68a18065745a8faedeb8e0cc3c7d5a7edd5e6567683a05c952ecccc8095c16.jpg)

![](images/bc374cdde417efcdee10b03b2ea1f7526cbcc870b2245d661ce6d80ad76b4de0.jpg)  
Fig. 11. Demodulated temperature profiles using raw and processed SRAB traces when the water bath is set to different temperatures. The insets are the results around the heating sections. (a) Temperature is set to $6 0 ~ ^ { \circ } \mathrm { C }$ ; (b) temperature is set to $7 0 ~ ^ { \circ } \mathrm { C }$ ; (c) temperature is set to $8 0 ~ ^ { \circ } \mathrm { C }$ .

# IV. CONCLUSION

In this paper, an SSRNet is proposed for the deconvolution of RDTS. The SSRNet is designed based on the ResNet and trained with synthetic RDTS data. The network structure is optimized through removing the BN layers based on the finding that the BN layers are not suitable for the RDTS deconvolution task. The system’s convolution kernel is estimated using the falling signal at the fiber end rather than the optical pulse waveform. And a modified RDTS model is proposed to generate training data. The well-trained SSRNet can improve the spatial resolution by five times and reach the limit of the Nyquist sampling theorem. Compared with the TVD, the SSRNet can restore RDTS signals more accurately with higher fidelity. Moreover, the SSRNet is more flexible and reliable in practical applications because it does not require manual parameter adjustment.

However, the proposed method still has its limitations. For example, the convolution kernel may change due to dispersion and nonlinear effects in long-distance sensing. The greater the difference between the actual convolution kernel and the convolution kernel used for training, the greater the reconstruction error. To address this, based on the SSRNet, we are going to carry out the study of blind deconvolution in RDTS, which can be adaptive to any convolution kernel. Moreover, we believe that the proposed method could be widely applied to other time-domain distributed sensing systems with suitable training data, such as Brillouin optical time-domain reflectometry and phase optical time-domain reflectometry, to improve their spatial resolution without hardware modification.

# REFERENCES

[1] P. Lu et al., “Distributed optical fiber sensing: Review and perspective,” Appl. Phys. Rev., vol. 6, no. 4, pp. 041302–041336, 2019.   
[2] X. Bao and L. Chen, “Recent progress in distributed fiber optic sensors,” Sensors, vol. 12, pp. 8601–8639, 2012.   
[3] L. Zhang, X. Feng, W. Zhang, and X. Liu, “Improving spatial resolution in fiber Raman distributed temperature sensor by using deconvolution algorithm,” Chin. Opt. Lett., vol. 7, no. 7, pp. 560–563, 2009.   
[4] A. R. Bahrampour, A. Moosavi, M. J. Bahrampour, and L. Safaei, “Spatial resolution enhancement in fiber Raman distributed temperature sensor by employing ForWaRD deconvolution algorithm,” Opt. Fiber Technol., vol. 17, pp. 128–134, 2011.   
[5] J. P. Bazzo, D. R. Pipa, C. Martelli, E. Vagner Da Silva, and J. C. Cardozo Da Silva, “Improving spatial resolution of Raman DTS using total variation deconvolution,” IEEE Sensors J., vol. 16, no. 11, pp. 4425–4430, Jun. 2016.   
[6] S. L. C. B. da et al., “NARX neural network model for strong resolution improvement in a distributed temperature sensor,” Appl. Opt., vol. 57, no. 20, pp. 5859–5864, 2018.   
[7] M. A. Soto, F. Di Pasquale, and F. Di Pasquale, “Distributed Raman sensing,” Handbook of Optical Fibers. Berlin, Germany: Springer, 2018, pp. 1–55.   
[8] S. H. Chan, R. Khoshabeh, K. B. Gibson, P. E. Gill, and T. Q. Nguyen, “An augmented Lagrangian method for total variation video restoration,” IEEE Trans. Image Process., vol. 20, no. 11, pp. 3097–3111, Nov. 2011.   
[9] S. Elmalem, R. Giryes, and E. Marom, “Motion deblurring using spatiotemporal phase aperture coding,” Optica, vol. 7, no. 10, pp. 1332–1340, 2020.   
[10] M. Hui et al., “Image restoration for synthetic aperture systems with a nonblind deconvolution algorithm via a deep convolutional neural network,” Opt. Exp., vol. 28, no. 7, pp. 9929–9943, 2020.   
[11] Z. S. Zhang, H. Wu, C. Zhao, and M. Tang, “High-performance Raman distributed temperature sensing powered by deep learning,” J. Lightw. Technol., vol. 39, no. 2, pp. 654–659, 2021.   
[12] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recogn., 2016, pp. 770–778.

[13] H. Habibi Aghdam and E. Jahani Heravi, Guide to Convolutional Neural Networks. New York, NY, USA: Springer Publishing, 2017.   
[14] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” in Proc. Int. Conf. Mach. Learn., 2015, pp. 448–456.   
[15] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classification with deep convolutional neural networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2012, pp. 1097–1105.   
[16] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” 2014, arXiv:1412.6980.

Hao Wu received the B.S., M.S., and Ph.D. degrees in optical engineering from the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, in 2013, 2016, and 2019, respectively. Since 2019, he has been a Postdoctor with the Huazhong University of Science and Technology. His research interests include the application of special optical fiber and machine learning algorithm in distributed optical fiber sensing.

Can Zhao received the B.S. and Ph.D. degrees in optical engineering from the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, in 2014 and 2019, respectively. Since 2019, he has been a Postdoctor with the Huazhong University of Science and Technology. His research interests include scheme and algorithm optimization of distributed optical fiber sensing.

Ming Tang (Senior Member, IEEE) received the B.Eng. degree from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technology Research Centre. He was focused on the optical fiber amplifier, high-power fiber lasers, nonlinear fiber optics, and all-fiber signal processing. From February 2009 to 2011, he was a Research Scientist with Tera-Photonics Group, led by Prof. H. Ito in RIKEN, Sendai, Japan, conducting research on terahertz-wave generation, detection, and application using nonlinear optical technologies. Since March 2011, he has been a Professor with the School of Optics and Electronic Information, Wuhan National Laboratory for Optoelectronics, HUST. He has authored or coauthored more than 100 technical papers in the international recognized journals and conferences. His current research interests include optical fiber-based linear and nonlinear effects for communication and sensing applications. He has been a Member of the IEEE Photonics Society since 2001, and also a Member of the Optical Society of America.