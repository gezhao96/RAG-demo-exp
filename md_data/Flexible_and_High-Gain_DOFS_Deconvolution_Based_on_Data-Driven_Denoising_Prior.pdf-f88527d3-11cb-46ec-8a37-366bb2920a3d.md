# Flexible and High-Gain DOFS Deconvolution Based on Data-Driven Denoising Prior

Hao Wu , Mingming Zhang, Zhao Ge, Zhongyao Luo, Can Zhao , and Ming Tang , Senior Member, IEEE

Abstract—Spatial resolution is an essential parameter for distributed optical fiber sensing (DOFS). Deconvolution is a promising solution to improve spatial resolution because of its good universality and ability to restore infinitely high spatial resolution in theory. However, conventional iterative deconvolution algorithms require manually designed priors, which makes it difficult to restore the signal accurately. Although end-to-end methods based on artificial neural networks provide more accurate results based on data-driven priors, a neural network can only be applied to data with similar characteristics to its training data. For systems with different parameters, the neural network needs to be retrained or fine-tuned, which is time and computational resource consuming. Here, we employ a new deconvolution method for DOFS based on half-quadratic splitting and denoising neural networks that exploits the advantages of both iterative and machine learning methods. Besides, we propose a method to calculate the deconvolution gain to evaluate the deconvolution performance quantitatively. In an experiment with 10 deconvolution ratios, the deconvolution gain of the employed method is 15.8 dB, while that of a conventional iterative method and an end-to-end machine learning method are $7 . 9 \ \mathrm { d B }$ and $\mathbf { 1 5 \ d B }$ , respectively. Moreover, this new deconvolution method can be adapted to data with arbitrary system parameters, making it more flexible than end-to-end neural networks in practical applications.

Index Terms—Convolutional neural networks, deconvolution, fiber optics sensors, optical time domain reflectometry, spatial resolution.

# I. INTRODUCTION

D ISTRIBUTED optical fiber sensing (DOFS) is widely usedto monitor large structures, long distance lines, and geological activities because it enables measurement of any point on a long-distance optical fiber [1]. By injecting pulsed light into an optical fiber and analyzing its scattered light, fiber information such as temperature, strain, loss, vibration, and bending can

Manuscript received 5 January 2023; revised 24 April 2023; accepted 21 May 2023. Date of publication 24 May 2023; date of current version 2 October 2023. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1801002, in part by the National Natural Science Foundation of China under Grant 61931010, in part by Hubei Province Key Research and Development Program under Grant 2020BAA006, and in part by the Innovation Fund of WNLO. (Corresponding author: Ming Tang.)

This work did not involve human subjects or animals in its research.

The authors are with the Wuhan National Laboratory for Optoelectronics and National Engineering Laboratory for Next Generation Internet Access System, School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: wuhaoboom@hust. edu.cn; carlzhang@hust.edu.cn; m201977113@hust.edu.cn; zluo@hust.edu.cn; zhao_can@hust.edu.cn; tangming@mail.hust.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JLT.2023.3279465.

Digital Object Identifier 10.1109/JLT.2023.3279465

be measured [2]. The positioning principle is called optical time-domain reflectometry (OTDR), which obtains the distance information based on the flight time of scattering light. Spatial resolution is an essential indicator of a DOFS system, which refers to the minimum fiber length of distinguishable event separation. Generally, the spatial resolution can be effectively improved by reducing the pulse duration. However, reducing pulse duration requires higher-speed hardware equipment and will cause signal-to-noise ratio (SNR) drop.

To solve this problem, post-processing techniques have been developed to improve the spatial resolution, such as iterative subdivision [3], [4], rising edge demodulation [5], gain-profile tracing [6], [7], slope-assisted method [8], deconvolution methods [9], [10], [11], [12], [13], [14], [15], [16], [17], [18]. Among them, deconvolution has attracted much attention because of its good universality and ability to restore infinitely high spatial resolution in theory [9], [10]. However, high spatial resolution restoration using deconvolution is an ill-posed inverse problem, with no unique solution. Therefore, conventional iterative deconvolution process requires constraints to obtain reasonable results [9], [10], [11], [12], [13], [14], [15]. These constraints need to be tuned based on prior knowledge of the DOFS signals. However, manually summarized prior can hardly represent the characteristics of the DOFS signals adequately and may even introduce artifacts. To obtain more accurate results, artificial neural networks (ANNs) have recently been used to implement end-to-end DOFS deconvolution [16], [17], [18]. ANNs use large amounts of data to learn the characteristics of DOFS signals, and this data-driven approach can obtain more comprehensive prior information. Although end-to-end machine learning methods show significant advantages over conventional iterative methods in terms of accuracy, a trained ANN can only be applied to its target system with pre-defined parameters. In other words, it cannot be applied to systems, for example, with different pulse widths. Therefore, end-to-end methods are not ideal for practical applications due to lack of universality.

To overcome the shortcomings of conventional iterative methods and end-to-end machine learning methods, we apply a new deconvolution technique to DOFS signals. This deconvolution method uses denoising neural networks to obtain more accurate priors for the iterative deconvolution process. This idea has been successfully applied in the field of image processing [19], [20], but to our knowledge, it has not been reported in DOFS field. In addition, we note that the existing DOFS deconvolution studies mainly focus on enhancing spatial resolution without considering the signal distortion or SNR change due to the deconvolution

![](images/4e87166488bbf6b5d5e7b8af1931d318b0695acd069d7dad146016d8a8069a6a.jpg)  
Fig. 1. Schematic diagram of DOFS.

process. Therefore, we propose an evaluation method called deconvolution gain that integrates the deconvolution rate and SNR to evaluate the deconvolution performance quantitatively. Simulation and experimental results show that the new method employed can provide deconvolution gain comparable with that of end-to-end machine learning methods, which is much higher than that of conventional iterative methods. Moreover, compared with end-to-end machine learning methods, this new method can be adapted to data with arbitrary system parameters, making it more flexible in practical applications.

# II. PRINCIPLES AND METHODS

# A. DOFS Deconvolution

DOFS emits pulsed light into a sensing fiber, as shown in Fig. 1. When the pulsed light propagates in the optical fiber, it will interact with the optical fiber to produce backscattered light, which contains the local information of the fiber. According to the time t from the pulse light emission to the scattered light return, the fiber distance $L$ where the scattering occurs can be obtained:

$$
L = \frac {c t}{2 n}, \tag {1}
$$

where $c$ is the speed of light in vacuum and $n$ is the refractive index of the sensing fiber. This positioning technique is called optical time-domain reflectometry (OTDR). Theoretically, OTDR can obtain the fiber information $x$ along the sensing fiber. However, since the pulsed light has a duration, the actual obtained OTDR signal $y$ is the convolution of the pulsed light profile $h$ with the fiber information $x$ . Merged with an additive noise $n$ , the OTDR trace $y$ can be expressed as:

$$
y = x \otimes h + n. \tag {2}
$$

As a result, the measured trace y will be smoother than the real fiber information $x .$ , which means it cannot accurately measure the event that changes rapidly along the fiber. The minimum fiber length that an OTDR can effectively measure is called spatial resolution SR, which is determined by the pulse duration $\tau$ , detection response time $q$ , and sampling interval time $\nu$ :

$$
S R = \max  (\tau , q, 2 \nu) \times \frac {c}{2 n}. \tag {3}
$$

2Therefore, high spatial resolution can be obtained by using high-speed devices. However, this also increases the cost and

implementation difficulty. More critically, the SNR of the system is positively correlated with the pulse duration. Thus, reducing the pulse duration will reduce the measurement accuracy accordingly. Therefore, in most cases, the spatial resolution of DOFS is mainly limited by the pulse duration to obtain a suitable SNR.

To break the limitation of pulse duration, fiber information $x$ can be restored by deconvolution of measured OTDR trace y. However, deconvolution is an ill-posed inverse problem. It has no unique solution. Therefore, the process of deconvolution can be thought of as finding the most probable value of $x$ :

$$
\hat {x} = \underset {x} {\arg \max } P (x | y). \tag {4}
$$

According to the Bayesian rule, this maximum posterior probability problem can be converted to a maximum prior probability problem:

$$
\hat {x} = \underset {x} {\arg \max } P (y | x) P (x), \tag {5}
$$

where $P ( y | x )$ represents the likelihood of detecting y from x, $P ( x )$ represents the prior of fiber information $x$ and is independent of y. It can be reformulated as:

$$
\hat {x} = \arg \min  _ {x} \frac {\lambda}{2 \sigma^ {2}} \| h \otimes x - y \| ^ {2} + N (x), \tag {6}
$$

where $\sigma$ is the noise level of measured OTDR trace y, λ is a regularization parameter. The solution minimizes an energy function composed of a data term and a prior regularization term $N ( \mathbf { x } )$ . The data term guarantees that the solution accords with the convolution process, while the prior regularization term alleviates the ill-posedness by enforcing desired property on the solution.

This problem can be solved using an iterative optimization approach with manually summarized prior or an end-to-end approach based on data-driven prior. The latter generally gives better results than the former. However, the end-to-end approach is not flexible. It will fail when the actual system parameters and training parameters are not consistent. Therefore, we apply an iterative optimization method with data-driven denoising prior for OTDR data deconvolution, which has good flexibility while providing more accurate results [19], [20].

# B. Alternating Direction Method With Total Variation Prior

The iterative deconvolution method based on total variation regularization is employed as a comparison, which has been used in many DOFS systems [10], [12], [13], [18]. The total variation deconvolution (TVD) uses the total variation as the prior regularization term [21]:

$$
N (x) = \| D x \| _ {1} = \sum_ {n} | x _ {n + 1} - x _ {n} |, \tag {7}
$$

where $D$ is the forward finite-difference operator. To solve (6), an intermediate variable $a$ is introduced:

$$
\hat {x} = \underset {x} {\arg \min } \frac {\lambda}{2 \sigma^ {2}} \| h \otimes x - y \| ^ {2} + \| a \| _ {1}
$$

$$
\text {s u b j e c t} a = D x. \tag {8}
$$

![](images/b95edd60bf4b7053f47bcf4e397bb3e0d392bcd9923a324a7983b0d17246fdd0.jpg)  
Fig. 2. Neural Network structure diagram of the SSRNet.

The augmented Lagrangian of (8) is [21]:

$$
\begin{array}{l} L (x, a, w) = \frac {\lambda}{2 \sigma^ {2}} \| h \otimes x - y \| ^ {2} + \| a \| _ {1} - w ^ {T} (a - D x) \\ + \frac {\rho}{2} \| a - D x \| ^ {2}, \tag {9} \\ \end{array}
$$

where $w$ is the Lagrange multiplier, $\rho$ is a regularization parameter. To solve (6) is equal to find a saddle point of $L ( x , a , w )$ , which can be estimated using the alternating direction method (ADM) to iteratively solve the following subproblems [21]:

$$
x _ {k + 1} = F ^ {- 1} \left[ \frac {F \left(\lambda h ^ {T} / \sigma^ {2} \otimes y + \rho D ^ {T} a _ {k} - D ^ {T} w\right)}{\lambda / \sigma^ {2} | F (h) | ^ {2} + \rho | F (D) | ^ {2}} \right], \tag {10}
$$

$$
a _ {k + 1} = \max  \left\{\left| D x _ {k + 1} + (1 / \rho) w _ {k} \right|, 0 \right\} \cdot \frac {D x _ {k + 1} + (1 / \rho) w _ {k}}{\left| D x _ {k + 1} + (1 / \rho) w _ {k} \right|}, \tag {11}
$$

$$
w _ {k + 1} = w _ {k} - \rho \left(a _ {k + 1} - D x _ {k + 1}\right), \tag {12}
$$

where $F$ represents the fast Fourier transform, $F ^ { - 1 }$ represents the inverse Fourier transform. The initial value of $\rho$ is 2, and it is doubled for each iteration to accelerate convergence.

# C. End-to-End Deconvolution Neural Network

Unlike iterative deconvolution, end-to-end machine learning methods explore the mapping between the measured signal $y$ and fiber information x. The prior information is implicitly included in the parameters of the neural network during the training process. We have proposed a super spatial resolution neural network (SSRNet) for DOFS deconvolution [18]. The input of the SSRNet is the measured signal, and the output is the corresponding deconvolution result. As shown in Fig. 2, the SSRNet consists of convolution (Conv) layers and rectified linear units (ReLU). Shortcut connections are introduced to reduces the training difficulty. The commonly used batch normalization (BN) layer is not employed because we found that the BN is not suitable for DOFS deconvolution task and can lead to deteriorating results [18]. The one-dimensional Conv kernel size is 9. The channel number of the first and last Conv layers is 1, while the channel number of the rest Conv layers is set to 128. The SSRNet consists of 24 Conv layers. Therefore, the receptive field of SSRNet is 193, which means that each point of the output is related to 193 points of the input data.

A simplified OTDR simulation model is used to generate a large amount of training data. We use curves with random intensity to simulate arbitrary OTDR traces [18]. The signal

changes due to loss and reflection are represented by the randomly varying intensities. The signal intensity remains consistent within a random number of sampling points to represent a relatively uniform scattering. Then we convolve the synthesized OTDR signals with the pulsed light profile to generate the corresponding convolutional data. In addition, Gaussian white noise is added to the convolutional data. The pulsed light profile and noise level should be set according to the actual data.

We generate 3200 pairs of training curves, of which 2560 pairs are used as the training set and the remaining 640 pairs as the validation set. Each synthesized curve contains 20000 sampling points. The SSRNet is trained for 1000 epochs with a batch size of 64 and a learning rate of 0.0003. It takes about 27 hours to complete the training process with Pytorch running on a PC with NVIDIA TITAN RTX GPU (24G). For systems with different parameters, the training data set needs to be regenerated and the SSRNet needs to be retrained or fine-tuned, which is time and computational resource consuming.

# D. Half-Quadratic Splitting With Denoising Prior

Like the TVD, we first introduce an intermediate variable:

$$
\hat {x} = \arg \min  _ {x} \frac {\lambda}{2 \sigma^ {2}} \| h \otimes x - y \| ^ {2} + N (b)
$$

$$
\text {s u b j e c t} b = x. \tag {13}
$$

According to the half-quadratic splitting (HQS) method, it can be solved by calculating a saddle point of the following equation [20]:

$$
L (x, b) = \frac {\lambda}{2 \sigma^ {2}} \| h \otimes x - y \| ^ {2} + N (b) + \frac {\mu}{2} \| b - x \| ^ {2}, \tag {14}
$$

where $\mu$ is a regularization parameter. Such a problem can be addressed by iteratively solving the following subproblems for $x$ and $b$ while keeping the rest of the variables fixed:

$$
x _ {k + 1} = \arg \min  _ {x} \frac {\lambda}{\sigma^ {2}} \| h \otimes x - y \| ^ {2} + \mu \| b _ {k} - x \| ^ {2}, \tag {15}
$$

$$
b _ {k + 1} = \underset {b} {\arg \min } \frac {1}{2 (\sqrt {1 / \mu}) ^ {2}} \| b - x _ {k + 1} \| ^ {2} + N (b). \tag {16}
$$

Equation (15) can be solved as [20]:

$$
x _ {k + 1} = F ^ {- 1} \left[ \frac {\lambda \overline {{F (h)}} F (y) + \mu \sigma^ {2} F \left(b _ {k}\right)}{\lambda \overline {{F (h)}} F (h) + \mu \sigma^ {2}} \right]. \tag {17}
$$

As for (16), from a Bayesian perspective, it corresponds to Gaussian denoising on $x _ { \mathrm { k + 1 } }$ with noise level $\mu ^ { - I / 2 }$ :

$$
b _ {k + 1} = \operatorname {D e n o i s e r} \left(x _ {k + 1}, \sqrt {1 / \mu}\right). \tag {18}
$$

So, the deconvolution of an DOFS signal can be achieved by iteratively solving (17) and (18). The prior information is implicitly included in the denoising process. That is, the constraint on deconvolution can be achieved by an accurate denoising prior.

# E. Data-Driven Denoising Prior

We have used the denoising convolutional neural networks (CNN) to the Raman-OTDR (ROTDR) and Brillouin Optical

![](images/5891827c004623df5e9cd27f02450a05c9f54e2789541fb99a0ec026d022db32.jpg)  
Fig. 3. Neural Network structure diagram of the 1DDCNN.

![](images/98ca30edb26dc078ac27b97b795195369b2232954ecee0b4d149a05449f067db.jpg)  
Fig. 4. PSNR of the inputs and outputs of ten 1DDCNNs.

Time Domain Analyzer (BOTDA) systems [22], [23]. The CNNs outperform the conventional denoising methods because it can obtain more accurate priors through training. So, we employed the one-dimensional denoising CNN (1DDCNN) we proposed as the denoiser for (18) [22]. The structure of the 1DDCNN is shown in Fig. 3. It consists of one-dimensional Conv layers, BN layers, and ReLU layers. The input of the 1DDCNN is a noisy OTDR signal, and the output is the corresponding noise signal. Using noise signals as training targets converges more easily than using noise-free signals because white noise is Gaussian distribution. The size of the convolution kernel is 3. The channel number of the first and last Conv layers is 1, while the channel number of the rest Conv layers is set to 64 to extract more features. The network consists of 20 Conv layers. So, the receptive field of 1DDCNN is 41.

A similar OTDR simulation model is used to generate the training data [22]. The difference is that the synthetic data does not take into account the convolution process, so it can satisfy arbitrary spatial resolutions. To accelerate the convergence, the noise level in (18) should be gradually reduced. We set the initial value of the regularization parameter $\mu$ to be 4, and it is quadrupled for each iteration. The total iteration time is ten. Therefore, we should train ten different 1DDCNNs to handle ten noise levels. For each noise level, we generate 10000 pairs of training curves, of which 8000 pairs are used as the training set and the remaining 2000 pairs as the validation set. Each synthesized curve contains 10000 sampling points. The 1DDCNNs are trained for 1000 epochs with a batch size of 128 and a learning rate of 0.0003. It takes about 10 hours to complete the training process for one 1DDCNN. Fig. 4 shows the average Peak SNR (PSNR) of validation data processed by

![](images/c2c2c7389881a5478e16b878cfef9c040ea31556bcfbe18ba7003f673c899783.jpg)  
Fig. 5. Denoised result of a synthetic OTDR trace with noise level of 1/128.

different 1DDCNNs. Significant SNR improvements are obtained using the 1DDCNNs. When the SNR of the input signal is greater than 25 dB, the noise suppression effect becomes weaker, which may be due to the limited calculation accuracy of the computer.

Fig. 5 demonstrates a synthetic OTDR trace and its denoised result. The fiber length is $1 0 \mathrm { k m }$ with a transmission attenuation of $0 . 2 \ : \mathrm { d B / k m }$ and a refractive index of 1.5. The sampling rate is $1 0 0 \mathrm { M S a / s }$ , and the noise level is 1/128. There is a −3 dB loss at $4 ~ \mathrm { k m }$ of the fiber and a 3 dB reflection at $6 ~ \mathrm { k m }$ . The noise is significantly reduced after processing using 1DDCNN. In addition, there is no distortion in the denoised signal around the loss and reflection points, indicating that the denoising process does not degrade the spatial resolution. Therefore, we can use these 1DDCNNs as effective denoising prior for HQS.

# F. Iterative Process and Results of HQS

We use a synthetic OTDR trace with the same parameters to demonstrate the iterative process of HQS. The difference is that the convolution process of the pump pulse is considered. The pulse duration is 100 ns, corresponding to 10 sampling points. Fig. 6 demonstrates the intermediate results of ten iterations when the regularization parameter $\lambda$ is set to 1. Fig. 6(a) shows the deconvolution result of (17). The denoised results are shown in Fig. 6(b). The signal noise becomes significantly larger after deconvolution using (17). And the noise is suppressed after the 1DDCNNs processing. During the iteration, the PSNR of $x$ and $b$ increase and eventually converge to a stable value, as shown in Fig. 7. By iterative computation, both deconvolution and fidelity are achieved.

Fig. 8 shows the result and details after ten iterations. Compared with the real fiber state, the detected data has a significant difference at the loss and reflection places due to pulse convolution. The falling edge at the loss point becomes 10 sampling points from 1 sampling point. And the signal at the reflection point is smoothed out, resulting in a smaller reflection intensity. After being processed using HQS, the deconvolved data effectively recovered the details of the data, achieving a deconvolution ratio of 10. In addition, the obtained result has no obvious artifacts, proving the validity of the data-driven denoising prior.

![](images/f4d2cb6a406a4b468deb030f944493d7432144a48cf9a51da10be80c6dcd6b20.jpg)

![](images/fc8299661e636d0640a1e19f76aa71cf7708745fbc60d631f8848e58bc40125f.jpg)  
Fig. 6. Results of ten iterations when $\lambda$ is 1. (a) Results of $x _ { \mathrm { k } }$ ; (b) results of $b _ { \mathrm { k } }$ .

![](images/2f70723bd2bb5f3a738eee494b128a6879a2c6c727225757493ce630c913b4dc.jpg)  
Fig. 7. PSNR of $x _ { \mathrm { k } }$ and $b _ { \mathbf { k } }$ for ten iterations.

# G. Definition of Deconvolution Gain

Existing DOFS deconvolution studies focus on the deconvolution ratios. There is a lack of quantitative evaluation methods for the other effects of the deconvolution process on the signal. Generally, only qualitative evaluations are done, as we described above “no significant artifacts”. To better evaluate the deconvolution performance, here we propose an evaluation method called deconvolution gain (DG):

$$
D G = 1 0 \times \log_ {1 0} \left(\frac {r \times S N R ^ {\prime}}{S N R _ {0}}\right), \tag {19}
$$

where $r$ is the deconvolution ratio, SNR represents the SNR after deconvolution, $S N R _ { 0 }$ represents the SNR of the detected signal. DG considers both the deconvolution ratio and the overall

![](images/a45bfbb2ae0962ba524ad230817ac4954039ec9ccaf64c8fc78f25d6f45f8403.jpg)

![](images/57e68e7728434b25c7ba0e6f01e6409538305e4f6d099a98e10a8eb2b4ccb084.jpg)

![](images/24141e67c2d1d5600c0f56a35cdecbbae9da1c01bf17ac22b5cbc21d1423e64b.jpg)  
Fig. 8. Deconvoluted result using HQS when λ is 1.

quality of the signal. If the spatial resolution is improved by directly changing the pulse duration, $r$ and $S N R ^ { \prime }$ are inversely proportional, so its DG is 0 dB. However, the DG of the result in Fig. 8 is 14.7 dB, implying that the proposed deconvolution method provides better results compared to boosting the spatial resolution through hardware modification.

# III. RESULTS AND DISCUSSION

# A. Optimization of Regularization Parameter

The flexibility of the iterative deconvolution algorithms is not only that they can be applied to arbitrary convolution kernels, but also that they have manually settable regularization parameter λ that controls the weight of the data term and regularization term. However, this also brings up the parameter optimization issue. We use the HQS method to process the synthetic OTDR trace in Fig. 8 with different λ. Fig. 9(a) shows the results around the reflection point. As λ increases, the signal at the reflection point becomes stronger, and the deconvolution effect is more obvious. However, the impact of the regularization term becomes weaker as $\lambda$ increases, resulting in a noisier result, as shown in Fig. 9(b). Fig. 10 demonstrates the relative error at the reflection point and noise level of the deconvoluted results using HQS with different λ. The minimum relative error is obtained when $\lambda$ is around 0.7.

![](images/d71e5be4b6de338b69ac7a9094c834657c484555fd40f3f953147c3fa624487b.jpg)  
  
Sampling points

![](images/c850ef147db1c4e721d5db223e3d004af4adf4984f79c6dec0a3313a277d0b42.jpg)  
(b   
Fig. 9. Deconvoluted results using HQS with different λ.

![](images/eade8b755da8da80603ff7da4aace2f2c7f69c6a1cb93e609810bbe517f096fe.jpg)  
Fig. 10. Relative errors at the reflection point and noise levels of the deconvoluted results using HQS with different λ.

The relative error does not keep getting smaller with λ because the noise due to deconvolution also increases the relative error. Therefore, the regularization parameter needs to be set according to the demand for noise level and deconvolution ratios.

# B. Simulation Results

To compare the performance between the HQS, SSRNet, and TVD, the test is first performed by simulation. The same synthetic OTDR trace is processed by the HQS, SSRNet, and TVD, respectively. The SSRNet-100ns is trained using a synthetic data set whose pulse duration is set to 100 ns. The regularization parameter of HQS is set to 0.7. And the regularization parameter of TVD is optimized to 0.012 to achieve a ten deconvolution

![](images/9f2c4354fddc2a8e12a9b93f2840b87f4f939313d194650610ff210f1e1aa68a.jpg)  
(a)

![](images/7e9f4f186401812fce86100cb5eb3f30926ea2aaf4b46241903b0985f3ee387c.jpg)  
Sampling points

![](images/5aa7220f2ff609867898c020c7eaca40ff9afb6e9e19b2d71c775ab7cc157524.jpg)  
Sampling points   
(c）  
Sampling points   
Fig. 11. Simulation results processed by the HQS, SSRNet, and TVD when the pulse duration is 100 ns.

ratio. As shown in Fig. 11, TVD is effective in recovering signals at the loss and reflection locations, but it introduces more noise than HQS and SSRNet-100ns. The DG of the processed results is 16.1 dB, 16 dB, and 8 dB using HQS, SSRNet-100ns, and TVD, respectively. The HQS can provide DG comparable with that of SSRNet-100ns, which is much higher than that of TVD.

Due to the flexibility of the iterative algorithms, they can be used for data with different pulse durations by simply adjusting regularization parameters. However, for end-to-end machine learning methods, neural networks need to be retrained for different system parameters. To illustrate this, a similar synthetic OTDR trace with 200 ns pulse duration is used for testing. The SSRNet-200ns is trained using data set whose pulse duration is 200 ns. The regularization parameters of HQS and TVD are increased to 2 and 0.025 to handle the deconvolution ratio of 20. As shown in Fig. 12, the HQS, SSRNet-200ns, and TVD can effectively enhance the spatial resolution to recover the information of loss and reflection point. However, SSRNet-100ns is unable to restore the high spatial resolution result and even introduces obvious wrong signals.

# C. Experimental Results

To demonstrate the effect of the proposed method on actual data, we set up an OTDR system, as shown in Fig. 13. A broadband amplified spontaneous emission source is employed

![](images/8f0c9e901b752606b5094ff65a3cdb95031b19698e3f0110fed8742e2cebdfb9.jpg)

![](images/b790e10b1cdd39bd45aa48cd709d0abb7f1499400481359177fb0de1c570fc86.jpg)

![](images/3dd0837b60a40b6430e408a5867c9d38a5313fe4e4f5e23c4372eebfc2227101.jpg)  
Fig. 12. Simulation results processed by the HQS, SSRNet, and TVD when the pulse duration is 200 ns.

![](images/39cda9c0c1d66f8f29efc16ea790b0e02147a73c3b991bcafff62d3b245bfa24.jpg)  
Fig. 13. Experimental setup of OTDR system.

as the light source. The continuous light is modulated to pulsed light by an acousto-optic modulator (AOM), controlled by an arbitrary function generator (AFG) with an electric pulse signal of 100 ns duration. The pulsed light enters the fiber under test (FUT) through an optical circulator. The backscattered light passes through the optical circulator and is converted into an electrical signal by a $1 0 0 \mathrm { M H z }$ bandwidth avalanche photodetector (APD). The electrical signal is then acquired by an oscilloscope at a sampling rate of $1 0 0 \mathrm { M S a / s }$ and averaged 512 times. The FUT is about $1 . 8 \mathrm { k m }$ long, and there is a 50-m long fiber connected to its

![](images/3b444d2763e4c29419ce1bf2d287c3215f7ddb2cae8597b02a44860551604788.jpg)  
Fig. 14. Measured light pulse profile.

![](images/72701a10606f85261dcad0111bfc1705c1107f2b812a67f8b2f4a102a2e54dff.jpg)

![](images/c6cea1d003c55fb00793294d9ae3a166b5cf6812b6d2c5eb8fb3f3869bb5a70e.jpg)  
Fig. 15. Deconvoluted results of the experimental data.

end. A reflection is generated by adjusting the flange connecting these two fiber spools.

To implement deconvolution, we need to measure the pulsed optical waveform using the APD. As shown in Fig. 14, although we set the AFG output to be a pulse of 100 ns duration, the detected pulse profile is not the ideal shape due to the response of the devices in the system. Therefore, we should use this measured profile as the convolution kernel for calculation. A SSRNet-measured is trained with a synthetic data set using this measured light pulse profile as the convolution kernel.

The deconvoluted results using TVD, SSRNet-100ns, SSRNet-measured, and HQS are shown in Fig. 15. According to the Nyquist theorem, the reflection signal can be restored to at most two sampling points. This matches (3), where the spatial resolution is limited by the sampling rate when deconvolution resolves the pulse duration limitation. Compared with the other methods, SSRNet-100ns introduces more artifacts indicating that the effectiveness of the end-to-end machine learning approach requires high accuracy of the convolution kernel. The noise levels are calculated based on the fluctuations between $5 0 0 \mathrm { ~ m ~ }$ and $1 5 0 0 \mathrm { ~ m ~ }$ . Then we can obtain the DG of TVD, SSRNet-measured, and HQS as 7.9 dB, 15 dB, and 15.8 dB, respectively. The HQS can provide flexible and high-gain DOFS deconvolution

# IV. CONCLUSION

This article introduces a DOFS deconvolution method based on HQS and data-driven denoising prior. The denoising prior is obtained using the 1DDCNN through training. This method combines the flexibility of iterative methods with the high performance of machine learning methods. To quantify the performance of the deconvolution algorithms, we propose an approach that integrates the deconvolution ratio and the SNR, called DG. Compared with TVD and SSRNet, the HQS provides higher DG with good universality. Although we use the basic OTDR for demonstration, the HQS can be widely applied to other DOFS systems, such as Raman-OTDR, Brillouin-OTDR, and phase-OTDR with corresponding denoising neural networks.

# REFERENCES

[1] P. Lu et al., “Distributed optical fiber sensing: Review and perspective,” Appl. Phys. Rev., vol. 6, no. 4, pp. 041302–041336, 2019.   
[2] X. Bao and L. Chen, “Recent progress in distributed fiber optic sensors,” Sensors, vol. 12, pp. 8601–8639, 2012.   
[3] F. Wang, W. Zhan, X. Zhang, and Y. Lu, “Improvement of spatial resolution for BOTDR by iterative subdivision method,” J. Lightw. Technol., vol. 31, no. 23, pp. 3663–3667, Dec. 2013.   
[4] J. Chao, X. Wen, W. Zhu, L. Min, H. Lv, and S. Kai, “Subdivision of Brillouin gain spectrum to improve the spatial resolution of a BOTDA system,” Appl. Opt., vol. 58, no. 2, pp. 466–472, 2019.   
[5] D. Zhou, D. Ba, B. Wang, L. Qiu, W. Hasi, and Y. Dong, “Millimeter-level recognition capability of BOTDA based on a transient pump pulse and algorithm enhancement,” Opt. Lett., vol. 46, no. 14, pp. 3440–3443, 2021.   
[6] T. Sperber, A. Eyal, M. Tur, and L. Thévenaz, “High spatial resolution distributed sensing in optical fibers by Brillouin gain-profile tracing,” Opt. Exp., vol. 18, no. 8, pp. 8671–8679, 2010.   
[7] S. Gao et al., “Monitoring local temperature and longitudinal strain along a nonuniform ${ \mathrm { A s } } _ { 2 } { \mathrm { S e } } _ { 3 }$ -PMMA tapered fiber by Brillouin gain-profile tracing,” Opt. Exp., vol. 30, no. 16, pp. 29655–29664, 2022.   
[8] J. Li, X. Zhou, Y. Xu, L. Qiao, J. Zhang, and M. Zhang, “Slope-assisted Raman distributed optical fiber sensing,” Photon. Res., vol. 10, no. 1, pp. 205–213, 2022.   
[9] R. Bernini, A. Minardo, and L. Zeni, “Accuracy enhancement in Brillouin distributed fiber-optic temperature sensors using signal processing techniques,” IEEE Photon. Technol. Lett., vol. 16, no. 4, pp. 1143–1145, Apr. 2004.   
[10] J. P. Bazzo, D. R. Pipa, C. Martelli, E. V. da Silva, and J. C. C. da Silva, “Improving spatial resolution of Raman DTS using total variation deconvolution,” IEEE Sensors J., vol. 16, no. 11, pp. 4425–4430, Jun. 2016.   
[11] S. Wang, Z. Yang, S. Zaslawski, and L. Thévenaz, “Short spatial resolution retrieval from a long pulse Brillouin optical time-domain analysis trace,” Opt. Lett., vol. 45, no. 15, pp. 4152–4155, 2020.

[12] L. Shen, Z. Zhao, C. Zhao, H. Wu, C. Lu, and M. Tang, “Improving the spatial resolution of a BOTDA sensor using deconvolution algorithm,” J. Lightw. Technol., vol. 39, no. 7, pp. 2215–2222, Apr. 2021.   
[13] Y. Li, C. Zhao, H. Wu, and M. Tang, “Long-range and high spatial resolution Brillouin time domain sensor using oversampling coding and deconvolution algorithm,” IEEE Sensors J., vol. 22, no. 15, pp. 14883–14891, Aug. 2022.   
[14] H. Wu, N. Guo, D. Feng, G. Yin, and T. Zhu, “Enhancing spatial resolution of BOTDR sensors using image deconvolution,” Opt. Exp., vol. 30, no. 11, pp. 19652–19664, 2022.   
[15] W. Zhu et al., “Submetric spatial resolution ROTDR temperature sensor assisted by wiener deconvolution,” Sensors, vol. 22, pp. 9942–9952, 2022.   
[16] A. Datta, V. Raj, V. Sankar, S. Kalyani, and B. Srinivasan, “Measurement accuracy enhancement with multi-event detection using the deep learning approach in Raman distributed temperature sensors,” Opt. Exp., vol. 29, no. 17, pp. 26745–26764, 2021.   
[17] J. N. Caceres, K. Noda, G. Zhu, H. Lee, K. Nakamura, and Y. Mizuno, “Spatial resolution enhancement of Brillouin optical correlation-domain reflectometry using convolutional neural network: Proof of concept,” IEEE Access, vol. 9, pp. 124701–124710, 2021.   
[18] H. Wu, C. Zhao, and M. Tang, “Super spatial resolution Raman distributed temperature sensing via deep learning,” IEEE J. Sel. Topics Quantum, vol. 28, no. 4, Jul./Aug. 2022, Art. no. 5600108.   
[19] W. Dong, P. Wang, W. Yin, G. Shi, F. Wu, and X. Lu, “Denoising prior driven deep neural network for image restoration,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 41, no. 10, pp. 2305–2318, Oct. 2019.   
[20] K. Zhang, Y. Li, W. Zuo, L. Zhang, L. V. Gool, and R. Timofte, “Plugand-play image restoration with deep denoiser prior,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 44, no. 10, pp. 6360–6376, Oct. 2022.   
[21] S. H. Chan, R. Khoshabeh, K. B. Gibson, P. E. Gill, and T. Q. Nguyen, “An augmented Lagrangian method for total variation video restoration,” IEEE Trans. Image Process, vol. 20, no. 11, pp. 3097–3111, Nov. 2011.   
[22] Z. Zhang, H. Wu, C. Zhao, and M. Tang, “High-performance Raman distributed temperature sensing powered by deep learning,” J. Lightw. Technol., vol. 39, no. 2, pp. 654–659, Jan. 2021.   
[23] H. Wu et al., “Real-time denoising of Brillouin optical time domain analyzer with high data fidelity using convolutional neural networks,” J. Lightw. Technol., vol. 37, no. 11, pp. 2648–2653, Jun. 2019.

Hao Wu received the B.S., M.S., and Ph.D. degrees from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2013, 2016, and 2019, respectively. Since 2019, he has been a Postdoctor with HUST. His research interests include the application of special optical fiber and machine learning algorithm in optical fiber sensing.

Mingming Zhang received the B.S. degree in 2019 from the Huazhong University of Science and Technology, Wuhan, China, where he is currently working toward the Ph.D. degree with the School of Optics and Electronic Information.

Zhao Ge received the B.S. degree from Jianghan University, Wuhan, China, in 2019, and the M.D. degree in 2022 from the Huazhong University of Science and Technology, Wuhan, China, where he is currently working toward the Ph.D. degree with the School of Optical and Electronic Information.

Zhongyao Luo received the B.S. degree from in 2020 the Huazhong University of Science and Technology, Wuhan, China, where he is currently working toward the Ph.D. degree with the School of Optics and Electronic Information.

Can Zhao received the B.S. and Ph.D. degrees in optical engineering from the School of Optics and Electronic Information, Huazhong University of Science and Technology (HUST), Wuhan, China, in 2014 and 2019, respectively. Since 2019, he has been a Postdoctor with HUST. His research interests are scheme and algorithm optimization of distributed optical fiber sensing.

Ming Tang (Senior Member, IEEE) received the B.Eng. degree from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technological University, Singapore, in 2005. His Postdoctoral Research with the Network Technology Research Centre was focused on the optical fiber amplifier, high-power fiber lasers, nonlinear fiber optics, and all-fiber signal processing. In February 2009, he was with Tera-photonics Group led by Prof. Hiromasa Ito in RIKEN, Sendai, Japan, as a Research Scientist conducting research on terahertz-wave generation, detection, and application using nonlinear optical technologies. Since March 2011, he has been a Professor with the School of Optics and Electronic Information, Wuhan National Laboratory for Optoelectronics, HUST, Wuhan, China. He has authored or coauthored more than 100 technical papers in the international recognized journals and conferences. His research interests include optical fiber-based linear and nonlinear effects for communication and sensing applications. Since 2001, he has been a Member of the IEEE Photonics Society.