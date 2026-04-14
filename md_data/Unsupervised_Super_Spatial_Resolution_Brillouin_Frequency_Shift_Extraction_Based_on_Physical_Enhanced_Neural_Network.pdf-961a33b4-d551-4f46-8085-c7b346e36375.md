# Unsupervised Super Spatial Resolution Brillouin Frequency Shift Extraction Based on Physical Enhanced Neural Network

Zhao Ge , Hao Wu , Zhiyong Zhao , Member, IEEE, Xuan Zou, Weilun Wei , and Ming Tang , Senior Member, IEEE

Abstract—Spatial resolution (SR), a core parameter of Brillouin optical time-domain analysis (BOTDA) sensors, determines the minimum fiber length over which physical perturbations can be accurately detected. However, the phonon lifetime in the fiber imposesan inherent limit on the SR, making sub-meter-level SR challenging to achieve. Conventional SR enhancement approaches, constrained by hardware limitations, often involve complex systems, or increased measurement times. Although deconvolution methods can mitigate hardware constraints, they suffer from distortion due to the nonlinear nature of the BOTDA response. Supervised deep learning approaches have recently emerged as an alternative, offering faster and more accurate post-processing through data-driven models. However, the need for extensive labeled data and the lack of physical priors lead to high computational costs and limited generalization. To overcome these challenges, we propose an unsupervised deep learning deconvolution framework, Physics-enhanced SR deep neural network (PSRN) guided by an approximate convolution model of the Brillouin gain spectrum (BGS). By embedding domain-specific physical knowledge directly into the architecture, PSRN enhances its interpretability and generalization across diverse BOTDA configurations. Besides, total variation regularization is introduced and proven to be effective in reducing artifacts. Simulated and experimental results demonstrate that PSRN can accurately retrieve sub-meter SR Brillouin frequency shift from any low-SR BGS input in a plug-and-play fashion, leveraging the interplay between neural network inference and embedded physical priors. This physics-neural network fusion establishes a generalizable paradigm for diverse fiber-optic sensing challenges.

Index Terms—Brillouin optical time-domain analysis, convolutional neural network, physics-based, spatial resolution, unsupervised learning.

Received 25 September 2025; revised 14 December 2025 and 21 January 2026; accepted 24 January 2026. Date of publication 28 January 2026; date of current version 16 April 2026. This work was supported in part by the National Natural Science Foundation of China under Grant 62225110 and Grant 61931010, in part by the Major Program (JD) of Hubei Province under Grant 2023BAA013, and in part by the Hubei Provincial Natural Science Foundation of China under Grant 2025AFB008. (Corresponding author: Hao Wu.)

The authors are with the Wuhan National Laboratory for Optoelectronics, Next Generation Internet Access National Engineering Laboratory, and Hubei Optics Valley Laboratory, School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan 430087, China (e-mail: gezhao@hust.edu.cn; wuhaoboom@hust.edu.cn; zhiyongzhao@hust.edu.cn; d202481278@hust.edu.cn; weiweilun@hust.edu.cn; tangming@mail.hust.edu.cn).

Both data and codes underlying the results presented in this paper are available in GitHub repository https://github.com/HUST-IOF/BOTDA_PSRN.

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JLT.2026.3658374.

Digital Object Identifier 10.1109/JLT.2026.3658374

# I. INTRODUCTION

B RILLOUIN optical time-domain analysis (BOTDA) hasemerged as a transformative technology in distributed emerged as a transformative technology in distributed fiber-optic sensing, distinguished by its unique capability to measure either strain or temperature variations along tens of kilometers of optical fiber. Unlike conventional point sensors, BOTDA exploits the inherent physical interaction between propagating light and acoustic phonons in optical fibers, a phenomenon known as stimulated Brillouin scattering (SBS). By analyzing the Brillouin frequency shift (BFS) induced by localized temperature or strain changes, BOTDA enables high-precision monitoring over extended distances [1], [2], [3]. This technology has become indispensable for health monitoring of critical infrastructure, including oil and gas pipelines, power cables, and civil engineering structures [4], [5], [6], [7]. However, conventional BOTDA systems face a fundamental limitation: the spatial resolution (SR) typically exceeds 1 m due to constraints imposed by the phonon lifetime $\mathrm { \sim 1 0 n s }$ ). This restriction hinders accurate detection of sub-meter-scale localized temperature/strain variations, thereby limiting its applicability in high-SR scenarios such as aerospace structural health monitoring or mine safety assessments.

To address SR limitations in BOTDA systems, the differential pulse-width pair (DPP) technique has been widely adopted [8], [9], [10], [11], [12]. In DPP-BOTDA, two Brillouin time-domain traces are independently acquired using long pump pulses with a slight width difference, and high-SR sensing signals are then extracted through trace subtraction. While this method offers advantages in implementation simplicity, it necessitates doubled measurement time and exhibits heightened susceptibility to polarization fading noise and system instability [13]. Alternative approaches leverage signal post-processing algorithms to enhance SR [13], [14], [15], [16]. For instance, by approximating Brillouin time-domain traces as a linear convolution between the pump pulse shape and the fiber’s impulse response, deconvolution algorithms have achieved an SR of $0 . 2 \mathrm { m }$ using 40 ns pump pulse [13]. However, because of the inertial features of the acoustic wave, BOTDA sensors cannot be rigorously regarded as a linear time-invariant system [13], [17]. The BGS envelope becomes dependent on the detuned frequency along the fiber, violating the linear convolution assumption. This nonlinearity leads to notable distortions in the recovered results [13], particularly in regions

![](images/95cf020907c941e343f5f2f918c7858e422a40c55e1660fa022a5d9cc4e238de.jpg)  
Fig. 1. Schematic illustration of the pipeline of PSRN.

with sharp and large BFS change. Although some sophisticated preprocessing methods have been proposed to eliminate this distortion, e.g., by using pulse differential preprocessing, it will however cause an increasement of measurement time [17], [18].

Recently, deep learning (DL) has emerged as a revolutionary paradigm for solving inverse problems in scientific sensing [19], [20], offering unique advantages in handling nonlinear mappings. A supervised learning-based SR enhancement method has been proposed [21], where models are trained on extensive simulated datasets to establish mapping relationships between BGS and their corresponding BFS. This approach has successfully demonstrated $0 . 5 \mathrm { ~ m ~ } \mathrm { S R }$ extraction from BGS measurements acquired with 40 ns pump pulses. However, training such models demands large-scale labeled datasets and computationally intensive procedures, rendering it time-consuming and energy-inefficient. Furthermore, the learned mapping functions are inherently pulse-width-specific, any change in pump pulse parameter and sweep frequency step necessitates model retraining, severely limiting practical adaptability.

In this paper, to overcome these limitations, we design and propose a novel SR improvement method based on unsupervised learning. We combine the convolutional model of BGS with a neural network, which we name physics-enhanced SR neural network (PSRN). PSRN does not require thousands of labeled data for training. Instead, it only needs a set of BGS input. Through self-supervised learning, the interaction between the neural network and the physical model optimizes the network’s weights and biases, gradually refining them and ultimately achieving sub-meter SR improvement. The incorporation of physics-based priors into the learning process not only improves model robustness under varying measurement conditions but also enhances interpretability. Moreover, PSRN incorporates total variation (TV) regularization as a key constraint to alleviate the multi-solution problem arising from unsupervised training. For experimental data with a 40 ns pulse width, the BFS retrieved by PSRN is highly consistent with that of a supervised trained neural network (STNN) method and significantly outperforms

the 45/40-ns DPP method. Crucially, simulation and experimental results confirm that PSRN can be directly applied to BGS obtained under different pulse widths and sweep steps without any retraining, demonstrating true plug-and-play capability across diverse BOTDA measurement scenarios. This level of flexibility far surpasses that of supervised learning methods.

# II. METHODS

Fig. 1 illustrates the architecture of the proposed unsupervised PSRN for BFS extraction. The method requires only a set of raw BGS signal $y$ obtained from a single measurement using yconventional BOTDA system. Notably, this approach dispenses with extensive labeled data and imposes no specific constraints on pulse width, frequency scanning step size, or BGS length. PSRN takes the low SR BGS measurement $y$ as its sole input. yThrough its manually designed structure, the network generates estimated parameters matrix $y _ { \mathrm { p r e } } \in \mathbb { R } ^ { 3 \times N }$ , which includes the predicted BFS $\nu _ { B }$ y, Brillouin linewidth $\Delta \nu _ { B }$ , and Brillouin gain coefficient $g _ { B }$ νB νBalong the fiber. Unlike supervised methods requiring true $\nu _ { B } / \Delta \nu _ { B } / g _ { B }$ (often experimentally inaccessible) to νB/ νB/gBoptimize weights and biases by minimizing errors between $y _ { \mathrm { p r e } }$ and labels, we compute the convolved BGS $\hat { y } = P ( y _ { \mathrm { p r e } } )$ y, where $P ( \cdot )$ y P ydenotes the convolution between the pump pulse and the Pfiber’s impulse response. The loss is defined as the discrepancy between the input BGS $y$ and the synthesized spectrum $\hat { y }$ , and is minimized via gradient descent. During this iterative optimization, the predicted parameters $y _ { \mathrm { p r e } }$ gradually converge to physically plausible values. Once the optimization reaches convergence, the BFS with high SR predicted by PSRN can be obtained. Moreover, the predicted parameters can be used to reconstruct the high SR BGS by the Lorentzian curve.

# A. Manually Designed Network Structure

The manually designed network $\mathrm { N e t } _ { \theta } ( \cdot )$ comprises three main θcomponents. The first component includes the input layer, a convolutional layer, and a maxpooling layer. The input layer

accepts two-dimensional BGS data of size $f _ { N } \times N$ , where $f _ { N }$ fN Nrepresents the number of swept frequencies of the BGS fN(determined by the sweep step), and $N$ denotes the number Nof BGS traces along the fiber length. The second component is a deep feature extraction module composed of 16 residual blocks, forming a total of 32 convolutional layers. Each residual block contains two $3 \times 3$ convolutional layers and a shortcut connection between the input and output, following the standard ResNet design [22]. Based on the number of convolutional kernels, the residual blocks are divided into four types with 64, 128, 256, and 512 kernels, respectively. Among the 16 residual blocks, these four types are distributed as 3, 4, 6, and 3 blocks, respectively. During the process of network iteration, the size of output feature maps gradually decreases in the frequency direction but remains unchanged in the fiber length direction. The third component is an upsampling layer, which is responsible for transforming the intermediate feature maps to the final output dimension. Ultimately, the network produces an output matrix of size $3 \times N$ , representing the predicted BFS $\nu _ { B }$ , Brillouin linewidth $\Delta \nu _ { B }$ , and Brillouin gain coefficient $g _ { B }$ νBalong the fiber.

# B. Physical Prior Knowledge

Regarding the physical prior knowledge $P ( \cdot )$ , the time-Pdomain signal measured by BOTDA equipment can be approximated as the convolution between the pulse shape and the system’s impulse response, where the SR is determined by the pump pulse width. The pulse shape itself is defined by the convolution of a short pulse and the Brillouin gain envelope. When a rectangular pump pulse with a width of $T _ { P }$ is used, the Brillouin gain $y _ { \mathrm { s h o r t } } ( z , t )$ generated at position $z$ TPin the fiber over y z, ta small uniform fiber segment of length $\Delta z$ zcan be expressed as the product of the temporal response of the Brillouin gain and the impulse response of the system [2], [23]:

$$
\begin{array}{l} y _ {\mathrm {s h o r t}} (z, t) = g (z) \frac {I _ {\mathrm {P}} ^ {0} A _ {\mathrm {S}} ^ {0}}{2 \Gamma_ {A} ^ {*}} \Delta z \left\{1 - \exp \left[ - \Gamma_ {A} ^ {*} \left(t - \frac {z + \Delta z}{V _ {g}}\right) \right] \right\} \\ \times \left[ u \left(t - \frac {z + \Delta z}{V _ {g}}\right) - u \left(t - T - \frac {z + \Delta z}{V _ {g}}\right) \right] \tag {1} \\ \end{array}
$$

$\begin{array} { r } { \Gamma _ { A } ( z ) = \frac { i \pi \left( v _ { B } ^ { 2 } ( z ) - v ^ { 2 } - i v \Delta v _ { B } \right) } { v } } \end{array}$ is the frequency detuning pa-A zrameter, where $\nu _ { B }$ vand $\nu$ are the BFS at position $z$ and the νB νsweep frequency, respectively, and $\Delta \nu _ { B }$ zis the intrinsic Brillouin linewidth. The constant $g ( z )$ νBis related to the electrostriction coefficient. The term $I _ { \mathrm { P } } ^ { 0 }$ g zrepresents the pump pulse intensity, while $A _ { \mathrm { S } } ^ { 0 }$ Iis the intensity of the continuous probe light, $V _ { g }$ is the Aspeed of light in the fiber, $u ( \cdot )$ Vgis the Heaviside unit step function, and $T$ uis the pump pulse width. The BGS at fiber position $z$ can T zbe solved by concatenating the Brillouin gain of many very short fiber units within the pump pulse width, which can be calculated by [2], [23]:

$$
y = P (z) = \sum_ {M = 0} ^ {l / \Delta z} y _ {\text {s h o r t}} \left(z - M \Delta z, \frac {z + M \Delta z}{V _ {g}}\right) \tag {2}
$$

where $l$ is the length of the pump pulse, $\Delta z$ is the length of a lshort fiber unit, and $P ( \cdot )$ zis the physical prior model.

PIt should be noted that (1)–(2) are derived under the assumption of an ideal rectangular pump pulse with negligible baseline leakage. This approximation is generally valid when the extinction ratio (ER) of the pulse-forming modulator is sufficiently high compared with the ratio between the sensing fiber length and the pump-pulse duration. Under such conditions, the contribution of residual background interaction outside the main pulse can be safely neglected. For very long fibers or BOTDA systems with limited ER, residual baseline leakage may accumulate along the fiber, leading to deviations from the idealized Brillouin interaction assumed in (1)–(2) and a gradual degradation of the model accuracy.

# C. Loss Function

To ensure the reliability of deconvolution results and mitigate the multisolution issues caused by ill-posed problems, we introduce two key losses: the deconvolution loss ${ \mathcal { L } } _ { \mathrm { d e c } }$ and the regularization loss $\mathcal { L } _ { \mathrm { r e g } }$ .

$$
\mathcal {L} = \mathcal {L} _ {\mathrm {d e c}} + \lambda \mathcal {L} _ {\mathrm {r e g}} \tag {3}
$$

Deconvolution Loss $\mathcal { L } _ { d e c }$ : During the forward process, the input BGS data $y$ is processed by the network to estimate the ycorresponding physical parameters $y _ { \mathrm { p r e } }$ . To ensure the estimated parameters $y _ { \mathrm { p r e } }$ yare consistent with the true values of $v _ { B }$ , $\Delta v _ { B }$ , and $g _ { B }$ y vB vB, the network must be optimized accordingly. Given gBthat the proposed high SR reconstruction framework is trained unsupervised and iteratively, we lack paired BGS data and corresponding reference parameters to guide network optimization. To align the estimated parameters $y _ { \mathrm { p r e } }$ with the observed BGS data $y$ , the physical prior model $P ( \cdot )$ is employed to map the y Pestimated parameters back to BGS data $\hat { y }$ . This reconstructed yBGS is then compared to the observed input $y$ , forming the deconvolution loss ${ \mathcal { L } } _ { \mathrm { d e c } }$ .

$$
\mathcal {L} _ {\mathrm {d e c}} = \| y - P (\operatorname {N e t} _ {\theta} (y)) \| _ {2} \tag {4}
$$

where $\| \cdot \| _ { 2 }$ represents the $L ^ { 2 }$ -norm. In contrast to supervised Ldeep learning deconvolution methods that typically focus on end-to-end mapping, the proposed method incorporates a physical constraint (the BGS convolution model) into the iteration process, effectively reducing potential inconsistencies between the estimated parameters and the observed BGS data.

Regularization loss $\mathcal { L } _ { r e g }$ : Due to the limited bandwidth of $y$ and the presence of noise, optimizing the network $\operatorname { N e t } _ { \theta } ( \cdot )$ ysolely by minimizing the reconstruction loss ${ \mathcal { L } } _ { \mathrm { r e c } }$ can lead to multiple solutions. These solutions may satisfy the physical equations, but do not correspond to the actual state of the fiber. To mitigate this ill-posed problem, we introduce the TV regularization loss $\mathcal { L } _ { \mathrm { r e g } }$ as an additional constraint during parameter estimation [24]. The original TV regularization method targeted image denoising under Gaussian noise [24], nevertheless it has evolved into a more general technique for inverse problems [25] while retaining its edge-preserving property [26].

$$
\mathcal {L} _ {\text {r e g}} = \left\| \nabla \left(\operatorname {N e t} _ {\theta} (y)\right) \right\| _ {1} \tag {5}
$$

where $\begin{array} { r } { \| \nabla \mathrm { N e t } _ { \theta } ( y ) \| _ { 1 } = \sum _ { z = 1 } ^ { N } | y _ { \mathrm { p r e } } ( z ) - y _ { \mathrm { p r e } } ( z - 1 ) | } \end{array}$ repreθ y z ysents the total variation of the solution $y _ { \mathrm { p r e } }$ y. The $\| \cdot \| _ { 1 }$ represents the $L ^ { 1 }$ -norm, and $N$ ydenotes the number of BGS traces along Lthe fiber length.

# III. RESULTS

PSRN was implemented using Python 3.8.19 and PyTorch 2.4.1. All experiments were conducted on a workstation equipped with an Intel(R) Xeon(R) Gold 6136 CPU, 256 GB of RAM, and an NVIDIA TITAN RTX GPU. The network was trained using the Adam optimizer with a learning rate of 10-4, which was used to update both the weights and biases during the optimization process. Notably, the weights and biases of the final layer are initialized to 0 and 0.1, respectively. This deliberate initialization strategy stabilizes the network’s output during the early iterations and mitigates large prediction deviations that may arise from random initialization. In this study, the input BGS length is flexible and can be adjusted as needed, with the maximum supported size primarily limited by the available GPU memory.

To ensure stable optimization behavior and reproducible reconstruction outcomes, the model is optimized for a fixed number of iterations for each measurement, while the loss value is recorded at every step. After the optimization completes, the predicted $y _ { \mathrm { p r e } }$ corresponding to the iteration that achieves the yminimum loss is selected as the final output. For simulated BGS, the maximum number of iterations is set to 2000 in this study. This is because the BFS, intrinsic Brillouin linewidth, and normalized gain are randomly varied over a relatively wide range in the simulations, resulting in a longer optimization process for the model to converge to the optimal solution. In contrast, for experimental measurements, empirical observations indicate that stable and near-optimal reconstructions can be reliably obtained within 1000 iterations.

# A. Simulation Results

A single BGS data of size $7 1 \times 9 8 0 0$ was generated through simulations, as shown in the Fig. 2(a). The simulation employed a 40 ns pump pulse, corresponding to a theoretical SR of $4 \textrm { m }$ . With a sampling rate of $1 \ \mathrm { G S a / s }$ , the simulated $1 \mathrm { - k m }$ fiber was divided into multiple segments with lengths randomly distributed between $0 . 5 \mathrm { m }$ and $5 \mathrm { m }$ . The shortest segment length, $0 . 5 \mathrm { m }$ , represents the minimum detectable scale of BFS variation and thus defines the ideal SR target for this study. Each fiber segment was assigned randomized physical parameters: BFS values ranging from 10.81 to 10.89 GHz, intrinsic Brillouin linewidth between 25 and 35 MHz, and normalized gain intensity between 0.8 and 1.0. The frequency sweep step was set to 2 MHz. It is important to note that the linewidth is the intrinsic Brillouin linewidth, and the simulated BGS linewidth is also related to the pump pulse width, which will be broader when narrow pump pulse is used [27]. To simulate measurement noise, Gaussian white noise with a variance of 0.005 was added to the normalized BGS data, yielding an approximate signal-to-noise ratio (SNR) of 23 dB. Fig. 2(b) shows a view of the 500–550 m region, where the dashed line represents the ground truth BFS. As highlighted

![](images/8c3e05cf14e8f5bf5a217ff5629e1fc558d30769f3d7b2e2964e5a99db818803.jpg)

![](images/4fd9b6ea31082a1de66c0f1349f5adb96852e11a36dfd353f8016a50a7564af5.jpg)  
Fig. 2. (a) Simulated 1 km BGS data using a 40 ns pump pulse; (b) enlarged view of BGS in 500-550 m, where the black line indicates the ground truth BFS.

by the red box, fiber segments shorter than 4 m show noticeable distortion in the BGS, demonstrating the limitations imposed by the system’s SR.

To evaluate the impact of the regularization loss, we conducted iterative reconstructions of the simulated 1 km BGS using PSRN with manually adjusted regularization weights $\lambda$ . Fig. 3(a) and (b) illustrate the evolution of the deconvolution loss ${ \mathcal { L } } _ { \mathrm { d e c } }$ and the structural similarity index (SSIM) between the reconstructed high-SR BGS and the ground truth BGS over iterations for different values of λ. As λ decreases, the deconvolution performance improves significantly, achieving the best results with a minimum ${ \mathcal { L } } _ { \mathrm { d e c } }$ of $3 . 2 6 \times 1 0 ^ { - 5 }$ and a maximum SSIM of 0.974 at $\lambda = 1 \times 1 0 ^ { - 7 }$ .. However, further reducing λ beyond this point does not lead to continued improvement. An excessively small λ weakens the effect of the regularization term $\mathcal { L } _ { \mathrm { r e g } }$ , rendering it ineffective. As shown in Fig. 4(a) and (b), a comparison of the BFS retrieval results with and without $\mathcal { L } _ { \mathrm { r e g } }$ indicates that the absence of TV regularization as an additional constraint leads to ambiguity in the solution. When the network $\operatorname { N e t } _ { \theta } ( \cdot )$ is trained solely by minimizing the deconvolution loss ${ \mathcal { L } } _ { \mathrm { d e c } }$ , it is prone to producing multiple plausible solutions, which is a typical manifestation of an ill-posed problem [28]. The BGS deconvolution process in the $5 0 0 { - } 5 5 0 \ \mathrm { m }$ region is visualized in Fig. 5. Specifically, Fig. 5(a) and (b) show the input BGS and the corresponding 0.5 m SR ground-truth BGS, respectively. Fig. 5(c)–(h) illustrate the evolution of the PSRN optimization at the 1st, 5th, 10th, 100th, and 2000th epoch. It should be noted that the spectra shown in Fig. 5(c)–(h) are synthesized by superimposing Lorentzian functions using the PSRN-predicted $y _ { \mathrm { p r e } }$ , which consists of the BFS, intrinsic Brillouin linewidth,

![](images/5cac2a375a6f32edf363624366fea0e7e3254f6e0df8c07c7bd399b1b81660eb.jpg)

![](images/e7dd86f712f8983338162549d701ef8d5d709fe4469db045c72d5838a4cf473a.jpg)  
Fig. 3. (a) Deconvolution loss and (b) SSIM evolution during iterative reconstruction of simulated 1 km BGS using PSRN under different regularization weights λ.

and normalized gain at each fiber position. This visualization is introduced to provide an intuitive representation of the convergence behavior of the three-parameter output. Due to the initialization of the final layer’s weights to zero with a bias of 0.1, the output at epoch 1 remains uniform. Through effective integration of physical prior knowledge, PSRN successfully guides the optimization trajectory toward an accurate high-SR reconstruction.

For high SR BFS extraction, Fig. 6 illustrates the optimization trajectory of the model’s output BFS during iterations process, where the estimated BFS gradually converges from its initial state to a physically plausible solution. It is evident that PSRN is capable of achieving high-SR reconstructions solely through constraints derived from physical priors, without relying on any labeled data. To evaluate the performance of PSRN, we conducted a direct comparison with a supervised learning approach. Specifically, we employed a STNN adapted from a previous study [21], which accepts fixed-size BGS input of $7 1 \times 5 4 0$ and output a $1 \times 5 4 0$ vector representing the ground truth BFS at $0 . 5 \mathrm { ~ m ~ } \mathrm { S R }$ . The STNN was trained on a synthetic dataset consisting of 10,000 simulated samples, requiring approximately 7.8 hours for data generation and an additional 7 hours for model training. The comparative results are shown in Fig. 7(a), with a detailed view of two consecutive $0 . 5 \mathrm { ~ m ~ }$

segments shown in Fig. 7(b). In these figures, the black line represents the ground truth BFS at $0 . 5 \mathrm { ~ m ~ } \mathrm { S R }$ , while the yellow line corresponds to the conventional LCF result. The blue and red dashed lines indicate the recovered results by PSRN and STNN, respectively. It is evident that PSRN accurately recovers the BFS, and the recovered result is in great agreement with the ground truth BFS, particularly at the sharp rising/falling edge. This level of rising/falling edge is unattainable for supervised learning methods, which struggle to accurately predict the position of sharp transitions [21]. To quantitatively evaluate performance, we computed the mean absolute error (MAE) relative to the ground truth BFS. PSRN achieved an MAE of only ${ 0 . 3 9 } \mathrm { M H z }$ , significantly outperforming the STNN, which yielded an MAE of 0.99 MHz. The MAEs of the PSRNpredicted linewidth and normalized gain are 0.31 MHz and 0.10, respectively.

In addition, PSRN exhibits strong adaptability to varying pump pulse widths. To validate its generalization capability, we generated simulated BGS using multiple pulse widths of 20, 30, 40, 50, and 60 ns. Fig. 8(a), (d), (g), and (j) show the raw BGS data with a 2 MHz step for pulse widths of 20, 30, 50, and 60 ns, respectively. The corresponding high-SR reconstructions obtained by PSRN are displayed in Fig. 8(b), (e), (h), and (k), and the retrieved BFS results are presented in Fig. 8(c), (f), (i), and (l). The BFS MAE comparison results for different pulse widths are summarized in Fig. 9(a). The previously proposed STNN model, which is trained only on data with a 40 ns pump pulse, exhibits limited generalization capability. When applied to pulse widths of 30 and 50 ns, STNN suffers from noticeable distortions, with the MAEs increasing to $1 . 3 5 ~ \mathrm { M H z }$ and 1.41 MHz, respectively. For the more extreme cases of 20 and 60 ns, severe distortions occur, and the MAEs rise sharply to $3 . 0 9 \mathrm { M H z }$ and $2 . 8 5 \mathrm { M H z }$ , respectively. In contrast, PSRN consistently delivers accurate 0.5 m SR enhancement across a wide range of pulse widths under identical noise conditions. Specifically, for pulse widths of 20, 30, 50, and 60 ns, PSRN achieves SSIM values of 0.990, 0.982, 0.974, and 0.961, with corresponding MAEs of 0.21, 0.30, 0.46, and $0 . 6 3 ~ \mathrm { M H z }$ , respectively. These results indicate that, under identical noise conditions, shorter pump pulses are inherently more favorable for achieving higher SR within the proposed PSRN framework. We further investigate the robustness of PSRN against noise, as shown in Fig. 9(b). The pump pulse width is fixed at 40 ns, while the SNR is varied. The results demonstrate that the proposed PSRN can effectively extract physically meaningful features from noisy BGS measurements and mitigate the adverse impact of noise on the inverse reconstruction process. Furthermore, the strong generalization of PSRN with respect to different frequency sweep steps is evaluated in Fig. 9(c), where sweep steps of 2, 4, and 8 MHz are considered. The results demonstrate that PSRN maintains stable performance across varying acquisition settings, confirming its strong invariance to both pulse width and frequency sweep step variations. These results collectively indicate that PSRN enables genuine plug-and-play deployment across diverse BOTDA systems without requiring parameterspecific retraining.

![](images/2c69d3776bde0842a18940b3af8808babbc60d1de28ba2910033214ad8336154.jpg)  
Fig. 4. (a) Comparison of BFS retrieval results with and without TV regularization. (b) Enlarged view of the green box region.

![](images/70863b5797be3bb088338cb7fe42cfff33b9fc5956c7d5350df836e4d38c3724.jpg)  
Fig. 5. Visualization of the BGS reconstruction process in 500-550 m region.

![](images/7773e1b94cd718f40540ba523ce2eafcb079e0f3c3fc27d2ec38ac96c5302674.jpg)  
Fig. 6. Optimization trajectory of BFS during PSRN iterations.

# B. Experimental Results

To further evaluate the performance of PSRN, a typical BOTDA sensor (Fig. 10) is employed for experimental validation. The continuous-wave laser output is split into probe and pump paths via a 50:50 optical coupler. In the upper branch, the probe light is frequency-swept from 10.81 GHz to $1 0 . 8 9 \ : \mathrm { G H z }$ in 2 MHz steps using an electro-optic modulator (EOM) driven by a radio frequency (RF) generator under carrier suppressed double-sideband modulation. The probe is then launched into a $4 . 9 \ \mathrm { k m }$ sensing fiber through an isolator. Three hotspots of 3.3 m, 1 m, and $0 . 5 \mathrm { ~ m ~ }$ lengths are located at the fiber end,

and these three hotspots are placed together in a thermostatic water bath and heated simultaneously to generate localized temperature-induced BFS changes. In the lower branch, the pump light is modulated by another EOM to generate high extinction ratio pump pulse with fast rising/falling time by using a programmable electrical pulse generator. The erbium-doped fiber amplifier (EDFA) is used to amplify the pump pulse light, and then the amplified pump pulse light passes through a polarization switch (PS) to reduce the polarization fading noise of the Brillouin gain. On the receiver side, a fiber Bragg grating (FBG) reflects the Brillouin Stokes sideband, which is detected by a photodetector (PD) and recorded via an oscilloscope. In the experiment, a 40 ns pump pulse is employed with a sampling rate of $1 \mathrm { { G S a / s } }$ , and 1000 averages are used; under these conditions, the BGS SNR at the end of the fiber is about 25.8 dB.

Unlike the simulation study where all Brillouin parameters are precisely known, experimental validation primarily focuses on the BFS. This is because reliable ground-truth values for the intrinsic Brillouin linewidth and the normalized gain are difficult to obtain in practical BOTDA measurements. Consequently, the experimental comparison emphasizes BFS, which is the most physically meaningful parameter in high-SR BOTDA sensing. The BGS signal from the hotspot region at the fiber

![](images/b9240a55e67b7b34dccaebedb6392cf4e69fd76d66cdec312106f555ebaa1220.jpg)

![](images/0ce97691a9e0f7986638b9c58bfe3233765c7a8d2b3ee0d44aebf04b97620007.jpg)  
Fig. 7. (a) Comparison of the BFS retrieval results obtained using the LCF, STNN, and PSRN. (b) Enlarged view of two adjacent 0.5 m segments.

![](images/d050cd004936c847eb2f09aeb181c15196a818ae89f5489bd22a306c9d0e8ccf.jpg)

![](images/db767a600755ac1d720ced87e66623a1a6a8d90c7fc9560ba330ba4bebb11c6f.jpg)

![](images/99fd7e2a187a626d7503b8fe1535f3c3194eafb60393d43b912574a15eaa6701.jpg)

![](images/2defa007a82514f361f1bb29ee6ca5fcc102a767a58c5d4da3f98e7f0cac0ca0.jpg)

![](images/402a12d2ccaca6403f77126087ae2f8a987e91278ed07dd27c19b85f36155a3e.jpg)

![](images/62f73505fd3dc461b9969ba73c2ef4c3a957991120d352d9b9cc82df0e8bab7b.jpg)

![](images/3a34c18993926b96b257c4d27b48a81f73a921ef7c99d5ec7b8df67c0519f0d7.jpg)

![](images/c9e1410cd9d73e4b494300a0828cbbbd1b81445270d7e6aaf080401958ec2190.jpg)

![](images/9f109f7f1532734daa70aa044a757ce83e498673d726893fcff3f778573d6a1e.jpg)

![](images/30a3e4fc29baad29d30d52ad360bd878a02ea014f9141e6fd4a91c020dfbdf68.jpg)

![](images/493b845e233681115c9ce53accf513692fafb60278215fdb772a162e896e041e.jpg)

![](images/5e44fa0381b42a74cae1af80cebc8bb50c7ccc45ac2dd972f2845bd5cc118f43.jpg)  
Fig. 8. High-SR BGS reconstruction and BFS retrieval results by PSRN on simulated data with varying pulse widths (20, 30, 50, and 60 ns) under a 2 MHz sweep step. (a), (d), (g), (j): Raw BGS inputs; (b), (e), (h), (k): High-SR BGS reconstruction results; (c), (f), (i), (l): High-SR BFS retrieval results.

end (Fig. 11(a)) was directly fed into PSRN, which successfully reconstructed a high-SR BGS (Fig. 11(b)). It is clearly seen that, owing to the limited SR, the 1 m and $0 . 5 \mathrm { m }$ hotspots in Fig. 11(a) are indistinguishable from the unheated sections. After processing with PSRN, however, all three hotspots are clearly resolved, as shown in Fig. 11(b). In order to compare the performances of the proposed PSRN and the existing techniques, we conducted

a direct comparison of multiple methods. As illustrated by the purple curve in Fig. 12(a), conventional LCF processing, with a theoretical SR of $4 \mathrm { m }$ , fails to resolve the hotspot accurately. The green solid line and the blue and red dashed lines represent the BFS retrieval results using the 45/40-ns DPP, STNN, and PSRN method, respectively. The average BFS retrieved by DPP and STNN (10.866 GHz) in 3.3 m-long hotspot was used as a

![](images/12ef75c160ae2dae3c9115a6559c8026e6bd3742cbddd2bc1a17a625506d87b1.jpg)

![](images/f7e6c87ec35d9f6268d31a50d49ca7e20f7815905c280ef0c2ea9f80a26cb36a.jpg)

![](images/f82f55785b54c011c54bece33c1be38ab9e1126d736ddb9d7e178dfaa32995be.jpg)  
Fig. 9. MAE comparisons under different pulse widths and sweep steps. (a) The MAEs of PSRN vs. STNN for different pulse widths; (b) the MAEs of PSRN vs. STNN for different SNR; (c) the MAEs of PSRN across various pulse widths and sweep steps.

reference for calibration, since conventional methods perform reliably at such scales. For the $0 . 5 \mathrm { ~ m ~ }$ hotspot (Fig. 12(b)), the absolute errors were $1 . 5 2 ~ \mathrm { M H z }$ for DPP, $0 . 3 4 ~ \mathrm { M H z }$ for STNN, and $0 . 3 7 \mathrm { M H z }$ for PSRN. These results demonstrate that PSRN can achieve sub-meter BFS retrieval accuracy directly on experimental data with a 40 ns pulse, without requiring labeled training data or supervised fine-tuning. The retrieved BFS results by PSRN is highly consistent with that of STNN and significantly outperforms the DPP method.

To validate the flexibility of the proposed method, experimental BGS signals with varying pulse widths were collected and directly fed into PSRN for iterative reconstruction, without any form of preprocessing. Fig. 13(a), (d), (g), and (j) show the raw experimental BGSs corresponding to 20 ns, 30 ns, 50 ns, and 60 ns pulse widths, respectively. The high-SR reconstructions produced by PSRN are shown in Fig. 13(b), (e), (h), and (k), while the retrieved BFS results are presented in Fig. 13(c), (f), (i), and (l). The results demonstrate that PSRN maintains strong generalization capability on real experimental data, consistently reconstructing high-SR BGSs across all tested pulse widths.

![](images/e5be1b75c70317345b5a4f81c5aaccf940ffb2de6d0907794fa9bd291d7235b4.jpg)  
Fig. 10. Experimental setup of the BOTDA system. RF: radio frequency, EOM: electro-optic modulator, PS: polarization switch, EDFA: erbium-doped fiber amplifier, FBG: fiber Bragg grating, PD: photodetector.

From the BFS retrieval results, it is evident that STNN fails to accurately predict high-SR BFS at 20 ns and 60 ns pulse widths, consistent with the trends observed in simulation. For the $0 . 5 \mathrm { m }$ hotspot, the absolute errors between the PSRN-retrieved BFS and the reference values are $1 . 8 6 \ : \mathrm { M H z }$ , 0.59 MHz, $0 . 3 0 \mathrm { M H z }$ , and $0 . 6 7 \mathrm { M H z }$ for pulse widths of 20 ns, 30 ns, 50 ns, and 60 ns, respectively. In contrast, STNN yields significantly higher errors of 5.01 MHz, 1.25 MHz, 1.03 MHz, and $8 . 6 9 \mathrm { M H z }$ , respectively, confirming PSRN’s superior adaptability and accuracy under varying measurement conditions.

In addition, PSRN is applicable to experimental data acquired with varying frequency sweep steps. Without any preprocessing, we directly applied iterative reconstruction to experimental BGS measurements containing a $0 . 5 \mathrm { ~ m ~ }$ hotspot under sweep steps of 2 MHz, 4 MHz, and 8 MHz. The results are shown in Fig. 14. PSRN successfully retrieved the BFS distributions corresponding to the $0 . 5 \mathrm { m }$ hotspot under all sweep conditions, demonstrating strong consistency and robustness. The absolute errors between the retrieved BFS and the calibrated reference values were 0.39 MHz, 0.32 MHz, and 0.31 MHz for 2 MHz, 4 MHz, and 8 MHz sweep steps, respectively.

To investigate how the SNR of the BGS affects the estimation accuracy of PSRN, we conducted additional experiments. a $9 . 8 ~ \mathrm { k m }$ sensing fiber was used, with a water bath was placed at the far end of the fiber with a $0 . 5 \mathrm { m }$ hotspot. The pump pulse width was 40 ns, and the rise/fall times were approximately 3 ns. To emulate different SNR conditions, we varied the number of averages (10, 50, 100, 500, 1000, 2000, 3000, and 4000), resulting in eight groups of raw BGS measurements with SNR levels of 11.2 dB, 14.7 dB, 15.9 dB, 18.7 dB, 20.8 dB, 21.3 dB, 22.2 dB, and 23.0 dB, respectively. Since the true BFS of the experimental data is not directly accessible, we used the averaged BFS retrieved by the 45/40 ns DPP and STNN methods from a 4 m hotspot placed in the same water bath as a reference. The absolute errors between this reference and the BFS predicted by each method were then calculated, and the comparison results are shown in Fig. 15. It can be observed that the PSRN consistently exhibits lower BFS estimation errors than the conventional 45/40 ns DPP method over the entire investigated SNR range. In particular, when the SNR exceeds approximately 15 dB, the

![](images/36b8b04d15d93d5bf5ce4648172f5c5499c0ffd1004b859fe76c921fe6e1660b.jpg)

![](images/0889841dc78be1ec02687a9f13014241d633aa1804536db5d462eb06278f6590.jpg)  
Fig. 11. (a) Raw BGS from the hotspot region. (b) High-SR BGS reconstructed by PSRN.

![](images/fc2190fcbcb04e3ddf2e63b2ea02444678f0a1ff784ea9d5de8b48df6b5415b4.jpg)

![](images/64a570e7611b2e91a4cd9f7f00a242836e409f34382bef9860c03b4df7cc1150.jpg)  
Fig. 12. (a) Comparison of the BFS retrieval results obtained using the LCF, 45/40-ns DPP, STNN, and PSRN methods. (b) Enlarged view of the $0 . 5 \mathrm { m }$ hotspot region.

![](images/b0ddf27386a9491c2be09377891aa1de011f808dc64df9626bb81881b57e0a6c.jpg)

![](images/32352c5cc6759d91dea00d3df64cea46242e353bb9ef2a76f51ad3b68606a9b7.jpg)

![](images/c993bb392276199745ff21c82c2c5ba955b1fbb197af17f0af1de2f2f458e10e.jpg)

![](images/9de44a71abb2ac173241986f1622ba7171fea84591526c0e404b44bd4673461f.jpg)

![](images/7eaa227056cbde2c816ff3e52704eb7ca361e3edc4080cb7c15b4aa8fd2c853b.jpg)

![](images/7a07b8fd3f124db9079ad17585aaa491b2f898260375a3072b00ab6d374b4ced.jpg)

![](images/44f04d252626230fda7be6ef3eb8023e91c96751799dedff62ccf1b53f9082dd.jpg)

![](images/8d60552699bd4cfe07521279739e6fdd0b370eb04c6d8b89e3d19fa55ba6329d.jpg)

![](images/adec75a7d256b51a47880c20dbce94e5c15663458197431bd31d8af6f65d03cd.jpg)

![](images/3f5bc5a9a511f5009188a291f5dca4acec0ff98e4151a2a5a3b9dc2e11abe385.jpg)

![](images/7e1c49c1f6835bbac7bf6e01ebdfeb2807cb6b4cfc3394d8975dabd7e375b6f6.jpg)

![](images/e101596b10d0b0731cc4d1127ae290a7ffa21253c9254d874b082572791be327.jpg)  
Fig. 13. High-SR BGS reconstruction and BFS retrieval results by PSRN on experimental data with varying pulse widths (20, 30, 50, and 60 ns) under a 2 MHz sweep step. (a), (d), (g), (j): Raw BGS inputs; (b), (e), (h), (k): High-SR BGS reconstruction results; (c), (f), (i), (l): High-SR BFS retrieval results.

![](images/8360534223331fe407e0c06cc4beaaaf17c2e262a2b253eeb1cdbb8ed9cba214.jpg)  
Fig. 14. Experimental BFS retrieval results under different frequency sweep steps using PSRN.

![](images/bc101ab301a6476e53f17f77af4261060f8ecc6e296dcb0497e2d4a6861ce398.jpg)  
Fig. 15. BFS estimation error versus BGS SNR for a 0.5 m hotspot (PSRN vs. STNN vs. 45/40 ns DPP).

BFS error of PSRN remains below $0 . 4 ~ \mathrm { M H z }$ , demonstrating a high level of robustness against measurement noise.

Since the typical processing time is a key factor for assessing the practical applicability of the proposed method,we calculated the processing time of PSRN. For the BGS size of 71 $\times ~ 5 4 0$ collected at the fiber end using a 40-ns pump pulse, the PSRN requires approximately 14 s per measurement on an NVIDIA RTX 4090 GPU and about 42 s per measurement on an NVIDIA TITAN RTX GPU. These times correspond to training the PSRN from a random initialization up to the fixed budget of 1000 iterations used in this work, and are shorter than the corresponding dataacquisition time, thus meeting practical application requirements. Moreover, the overall processing time can be further shortened when deployed on higher-performance hardware platforms. Using a more lightweight neural network can also reduce the processing time of PSRN. It should be emphasized that the proposed self-supervised strategy is designed as a customized solution for each individual measurement: the loss function is defined solely with respect to a single observed BGS, and the converged PSRN corresponds to the optimal solution for that specific sample. Therefore, a network optimized for one BGS cannot be directly reused as a universal model for subsequent BGS measurements. However,this does not mean that the previously converged PSRN is unusable. Under the same fiber and experimental conditions, it can serve as a strong initialization to accelerate the optimization for subsequent measurements.Our tests show that using the previously converged

PSRN as a pretrained model and performing self-supervised fine-tuning on the new measurement, the processing time can be significantly reduced from 14 s to 5 s.

# IV. CONCLUSION

This study proposes an unsupervised physics-guided deconvolution framework to overcome the inherent SR limitations of BOTDA sensors. The framework enables plug-and-play submeter SR BGS reconstruction and BFS retrieval without requiring labeled training data or hardware modifications. The physics-based constraints derived from prior knowledge eliminate the network’s dependence on paired low-high SR training data during the training process and enable the model to generalize effectively across different pulse widths and frequency sweep steps. Moreover, the incorporation of physical priors provides an interpretable structure to the learning process, offering better insight into how the reconstructed features relate to the underlying sensing mechanism and enhancing the model’s physical consistency. To further address the ill-posed problem of the deconvolution task and reduce solution ambiguity, a TV regularization term is introduced as an auxiliary constraint during parameter optimization, ensuring smoother and more physically plausible results. Both simulation and experimental results demonstrate that the proposed method significantly enhances the SR of BOTDA, successfully recovering detailed BGS features and continuous sub-meter variations in the BFS. Compared to conventional SR enhancement approaches, the proposed framework offers stronger nonlinear processing capability, higher prediction accuracy, better flexibility and generalization ability, and superior adaptability across various BOTDA configurations. This opens up a new paradigm for solving distributed fiber-optic sensing problems, where integrating the physical model of the sensing system into neural networks and extending its application can address traditional challenges such as data acquisition difficulties, poor generalization, high system complexity, low SR and SNR, etc.

# REFERENCES

[1] S. M. Maughan, H. H. Kee, and T. P. Newson, “Simultaneous distributed fibre temperature and strain sensor using microwave coherent detection of spontaneous Brillouin backscatter,” Meas. Sci. Technol., vol. 12, no. 7, pp. 834–842, 2001.   
[2] J.-C. Beugnot, M. Tur, S. F. Mafang, and L. Thévenaz, “Distributed brillouin sensing with sub-meter spatial resolution: Modeling and processing,” Opt. Exp., vol. 19, no. 8, pp. 7381–7397, 2011.   
[3] M. A. Soto, “Distributed brillouin sensing: Time-domain techniques,” in Handbook of Optical Fibers. Berlin, Germany: Springer, 2018, pp. 1–91.   
[4] H. Li, Y. Liu, J. Cao, and P. Shu, “Investigation of the BOTDA technology for structural condition monitoring of urban tunnel,” in Proc. IOP Conf. Ser.: Mater. Sci. Eng., 2019, vol. 603, no. 4, pp. 1–8.   
[5] D. Meng, F. Ansari, and X. Feng, “Detection and monitoring of surface micro-cracks by PPP-BOTDA,” Appl. Opt., vol. 54, no. 16, pp. 4972–4978, 2015.   
[6] R. Liu, S. Babanajad, T. Taylor, and F. Ansari, “Experimental study on structural defect detection by monitoring distributed dynamic strain,” Smart Mater. Struct., vol. 24, no. 11, 2015, Art. no. 115038.   
[7] Z. Zhou, X. Ma, Y. Liu, and H. Li, “A method for monitoring the uneven settlement of shield tunnels considering the flattening effect using distributed strain data measured from BOTDA sensors,” Struct. Health Monit., vol. 24, no. 1, pp. 351–371, 2025.

[8] S. Diakaridia et al., “Detecting cm-scale hot spot over 24-km-long singlemode fiber by using differential pulse pair BOTDA based on double-peak spectrum,” Opt. Exp., vol. 25, no. 15, pp. 17727–17736, 2017.   
[9] W. Li, X. Bao, Y. Li, and L. Chen, “Differential pulse-width pair BOTDA for high spatial resolution sensing,” Opt. Exp., vol. 16, no. 26, pp. 21616–21625, 2008.   
[10] A. Minardo, R. Bernini, and L. Zeni, “Numerical analysis of single pulse and differential pulse-width pair BOTDA systems in the high spatial resolution regime,” Opt. Exp., vol. 19, no. 20, pp. 19233–19244, 2011.   
[11] J. Urricelqui, M. Sagues, and A. Loayssa, “Phasorial differential pulsewidth pair technique for long-range Brillouin optical time-domain analysis sensors,” Opt. Exp., vol. 22, no. 14, pp. 17403–17408, 2014.   
[12] H. Wu, L. Wang, Z. Zhao, C. Shu, and C. Lu, “Support vector machine based differential pulse-width pair Brillouin optical time domain analyzer,” IEEE Photon. J., vol. 10, no. 4, Aug. 2018, Art. no. 6802911.   
[13] S. Wang, Z. Yang, S. Zaslawski, and L. Thévenaz, “Short spatial resolution retrieval from a long pulse Brillouin optical time-domain analysis trace,” Opt. Lett., vol. 45, no. 15, pp. 4152–4155, 2020.   
[14] R. Bernini, A. Minardo, and L. Zeni, “Accuracy enhancement in brillouin distributed fiber-optic temperature sensors using signal processing techniques,” IEEE Photon. Technol. Lett., vol. 16, no. 4, pp. 1143–1145, Apr. 2004.   
[15] F. Wang, W. Zhan, X. Zhang, and Y. Lu, “Improvement of spatial resolution for BOTDR by iterative subdivision method,” J. Lightw. Technol., vol. 31, no. 23, pp. 3663–3667, Dec. 2013.   
[16] J. Chao, X. Wen, W. Zhu, L. Min, H. Lv, and S. Kai, “Subdivision of Brillouin gain spectrum to improve the spatial resolution of a BOTDA system,” Appl. Opt., vol. 58, no. 2, pp. 466–472, 2019.   
[17] L. Shen, Z. Zhao, C. Zhao, H. Wu, C. Lu, and M. Tang, “Improving the spatial resolution of a BOTDA sensor using deconvolution algorithm,” J. Lightw. Technol., vol. 39, no. 7, pp. 2215–2222, Apr. 2021.   
[18] W. Wei, L. Shen, Z. Zhao, C. Zhao, and M. Tang, “Performance enhanced BOTDA sensor using differential golay coding and deconvolution algorithm,” in Proc. Opt. Fiber Commun. Conf. Exhib. (OFC), 2022, pp. 1–3.

[19] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol. 521, no. 7553, pp. 436–444, 2015.   
[20] A. Mathew, P. Amudha, and S. Sivakumari, “Deep learning techniques: An overview,” in Proc. Int. Conf. Adv. Mach. Learn. Technol. Appl., 2020, pp. 599–608.   
[21] Z. Ge, L. Shen, C. Zhao, H. Wu, Z. Zhao, and M. Tang, “Enabling variable high spatial resolution retrieval from a long pulse BOTDA sensor,” IEEE Internet Things J., vol. 10, no. 2, pp. 1813–1821, Jan. 2023.   
[22] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 770–778.   
[23] X. Sun et al., “Frequency shift estimation technique near the hotspot in BOTDA sensor,” Opt. Exp., vol. 27, no. 9, pp. 12899–12913, 2019.   
[24] L. I. Rudin, S. Osher, and E. Fatemi, “Nonlinear total variation based noise removal algorithms,” Physica D: Nonlinear Phenomena, vol. 60, no. 1–4, pp. 259–268, 1992.   
[25] T. Chan, S. Esedoglu, F. Park, and A. Yip, “Recent developments in total variation image restoration,” Math. Models Comput. Vis., vol. 17, no. 2, pp. 17–31, 2005.   
[26] D. Strong and T. Chan, “Edge-preserving and scale-dependent properties of total variation regularization,” Inverse Problems, vol. 19, no. 6, 2003, Art. no. S165.   
[27] M. Alem, M. A. Soto, M. Tur, and L. Thévenaz, “Analytical expression and experimental validation of the Brillouin gain spectral broadening at any sensing spatial resolution,” in Proc. 25th Opt. Fiber Sensors Conf., 2017, pp. 1–4.   
[28] Y. Zhao, Y. Li, S. Wang, and B. Yang, “Physical model and super-resolution theory-guided unsupervised deep learning deconvolution for seismic resolution enhancement,” IEEE Trans. Geosci. Remote Sens., vol. 63, 2025, Art. no. 5905813.