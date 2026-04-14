# Optical Phase-Sensitive Reflectometry Based on Orthogonal Frequency-Division Multiplexed LFM Signal in Fractional Fourier Domain

Can Zhao, Li Wang, Hao Wu, and Ming Tang*

Linear frequency modulated (LFM) phase-sensitive optical time-domain reflectometry ( $\varphi$ -OTDR) relieves the trade-off between sensing range and spatial resolution; however, it is still limited by low sidelobe suppression ratio and signal fading. Fractional Fourier transform (FrFT) is applied to LFM $\varphi$ -OTDR for signal generation and compression. An LFM pulse is generated using the $p$ -order FrFT of a direct current signal and then compressed using FrFT with order $1 - p$ to achieve a high sidelobe suppression ratio. Orthogonal frequency-division multiplexing in the fractional Fourier domain is utilized to suppress signal fading. In experiments, fading-free distributed phase measurement is realized using a multiplexed LFM probe pulse generated using a 0.4-order FrFT. Dynamic sensing is demonstrated via single-frequency or sweep-frequency vibration, thereby validating high sensing performance. This work will not only open up a route for signal processing in LFM pulse based high-performance $\varphi$ -OTDR, but also has significant potential for applications in other sensing systems using LFM signals.

# 1. Introduction

Distributed acoustic sensing (DAS) based on phase-sensitive optical time-domain reflectometry ( $\varphi$ -OTDR) has attracted considerable attention in fields including perimeter monitoring,[1] seismic wave detection,[2] and pipeline surveillance,[3] owing to its capability for distributed vibration monitoring with high sensitivity over long distances. The vibration amplitude and phase cannot be recovered in intensity-demodulated $\varphi$ -OTDR. Phase demodulation techniques have been proposed to quantitatively reconstruct the vibration amplitude, e.g., heterodyne detection,[4] IQ demodulation.[5] Intensive research has been conducted to enhance the performance of DAS, including the sensing distance,[6-8] spatial resolution,[4,9] and frequency response.[10,11]

Specifically, the sensing range of DAS is restricted by the received average signal-to-noise ratio (SNR), which is directly

related to the energy of injected pump pulses. The SNR can be effectively improved by increasing the pulse power; however, this is limited by nonlinear effects such as modulation instability. Another method of improving the SNR is increasing the pulse duration; however, this degrades the spatial resolution. Distributed optical amplification can overcome these limitations using Raman amplification,[6] Brillouin amplification,[7] and a combination of both to compensate for the fiber loss. These methods successfully extend the sensing distance to over $100\mathrm{km}$ . However, they require a high-power pump source and introduce additional noise.

An optical pulse-compression method has been proposed to minimize the tradeoff between the sensing distance and spatial resolution. This method utilizes a

linear frequency modulated (LFM) pulse and matched filter. In this manner, meter or even submeter spatial resolution can be achieved if a long LFM optical pulse with a duration up to the microsecond level is sent into a sensing fiber.[12] However, a critical problem of this method is the crosstalk caused by the relatively low peak side-lobe ratio (PSLR). The PSLR is typically increased by applying a window function to the matched filter in demodulation.[13] However, this causes an SNR penalty owing to the mismatch of the filter. The replacement of the rectangular window of a transmitted optical pulse with a Gaussian window and Hanning window can effectively improve the PSLR to 26 and 46 dB, respectively.[14,15] However, this reduces the pulse power or spatial resolution. Nonlinear frequency modulation (NLFM) pulses inherently have a high PSLR of $\approx 42$ dB; however, their main lobe is wider than that of LFM pulses.[16]

The sensing performance of $\varphi$ -OTDR is obstructed by signal fading, including polarization and interference fading. The former is generally eliminated using orthogonal polarization detection. Interference fading stems from the destructive interference of backscattering light, leading to the measured Rayleigh backscattered (RBS) light intensity lower than the noise floor. The Rayleigh interference patterns show high dependence on the optical frequency of the probe light. Thus, interference fading can be mitigated using a multifrequency source based on its frequency dependence. The inner-pulse frequency division and rotated-vector-sum (RVS) methods are widely used for $\varphi$ -OTDR

![](images/8beabbef62c86a9ef33fae46a1e9fc2a7a8878eaedfe0d3eef3ea7df6908b717.jpg)

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/lpor.202200838

DOI: 10.1002/lpor.202200838

with an LFM pulse.[17] Multicarrier generation via an electrooptic amplitude modulator has been validated in the NLFM pulse technique.[16] However, the division or multiplexing operation of an LFM signal reduces the spectrum efficiency because only a small part of the entire bandwidth is considered for pulse compression. Thus, the full width at half maximum (FWHM) of the compressed pulse after the matched filter increases, and the spatial resolution decreases.

In this paper, we apply the fractional Fourier transform (FrFT) to LFM signal generation and pulse compression. The FrFT is a generalization of the conventional Fourier transform (FFT), and it introduces rotations in the time-frequency domain. The decomposition basis function of the FrFT is extended from a single-frequency sinusoidal signal to an LFM signal. Therefore, the FrFT can be regarded as a matched algorithm for LFM signals. It has been widely used in parameter estimation for LFM signals in the radar and communication fields.[18-20] We utilize the additivity of the FrFT order to generate an LFM pulse using the $p$ -order FrFT of a direct current (DC) signal (hereinafter referred to as the FrFT-DC signal), and then compress it using an FrFT with order $1 - p$ . In theory, these two-step FrFTs are equivalent to the direct FFT of a DC signal. Hence, a fully compressed LFM pulse with a high PSLR and narrow FWHM is expected. We eliminate interference fading from the system using the orthogonal frequency division multiplexing (OFDM) of the LFM signal in the fractional Fourier domain. In optical communications, OFDM allows for greater spectral efficiency, reduced inter-symbol interference and resilience to multi-path distortion. It should be noted that the main disadvantages of OFDM are its high peak to average power ratio (PAPR) and sensitivity to carrier frequency offset and drift. As a comparison, LFM signal has constant amplitude over its duration and strong doppler tolerance. The combination of OFDM and LFM signals will reduce the PAPR and enhance its robustness to frequency drift, which will be of considerable benefit to sensing systems. The generated FrFT-DC signal is multiplexed by introducing an integral multiple-base frequency shift in the fractional Fourier domain. The frequency shift is considerably smaller than the FrFT-DC signal bandwidth in the Fourier domain, thereby yielding a spectrum-overlapped multicarrier LFM signal with a significantly higher spectrum efficiency than the previous works.[15-17] As a proof-of-concept, experiments are carried out on a $10\mathrm{km}$ single-mode fiber. An LFM pulse with a duration of $\approx 1$ $\mu s$ is generated by an FrFT-DC signal with an order of 0.4. Crosstalk is significantly suppressed using an FrFT-DC pulse with a PSLR higher than $60~\mathrm{dB}$ . Moreover, interference fading is considerably reduced by applying an orthogonal frequency-division multiplexed FrFT-DC signal in the fractional Fourier domain. Finally, vibration is measured using a piezoelectric ceramic transducer (PZT) driven by a single-frequency or sweep-frequency source in a range of $1 - 5\mathrm{kHz}$ , thereby validating the high sensing performance with a strain resolution of $143\mathrm{pc}\sqrt{\mathrm{Hz}^{-1}}$ and spatial resolution of $1\mathrm{m}$ . To the best of our knowledge, this is the first time that signal generation and processing is carried out in the fractional Fourier domain for $\varphi$ -OTDR. The two-step FrFT generates a fully compressed LFM pulse with a high PSLR, and the OFDM of the LFM signals suppresses signal fading with the highest reported spectrum efficiency.

# 2. Results and Discussion

In the experiments, the sampling rate of the arbitrary waveform generator (AWG) is $1\mathrm{GSa}\mathrm{s}^{-1}$ and the number of sampling points is 1024. The generated FrFT-DC signal has a duration of $\approx 1~\mu \mathrm{s}$ . The FrFT order of the DC signal is 0.4. The FrFT-DC signal is complex, as shown in Figure 1, and its spectrum width is $\approx 280\mathrm{MHz}$ , as shown in Figure 1b. The signal is compressed by applying a 0.6-order FrFT. The intensity of the compressed result is presented in the form of logarithms to better illustrate the signal compression performance of the two-step FrFTs (see Section S1, Supporting Information for more details), as shown in Figure 1c. The compressed FrFT-DC signal exhibits an ultranarrow compressed peak and a PSLR above $80\mathrm{dB}$ , as shown in the inset of Figure 1c. Moreover, the maximum noise floor is lower than -60 dB. For comparison, the PSLR of the signal compressed by the matched filter is less than $20\mathrm{dB}$ , and its main lobe is broader, as shown in Figure 1d.

The orthogonal frequency-division multiplexed FrFT-DC signal is generated by shifting the signal by frequency offset $f_{\mathrm{N}}$ (see Section S2, Supporting Information). According to the system setup, $f_{\mathrm{N}} = N \csc(0.6 * \pi / 2) / T$ and $T = 1024$ ns. The generated orthogonal frequency-division multiplexed FrFT-DC signal with three tones is shown in Figure 2. As shown in Figure 2a, the multiplexed FrFT-DC signals are compressed to three tones in the fractional Fourier domain. Figure 2b shows the intensity of the compressed signals. A high PSLR close to 80 dB is maintained, but with a higher noise floor close to -50 dB. Therefore, OFDM has a negligible influence on the compression performance of the FrFT-DC signal.

Proof-of-concept experiments are conducted on a $10\mathrm{km}$ single-mode fiber to demonstrate the feasibility of the proposed method. First, we investigate the influence of the frequency shift of the FrFT-DC signal on interference fading suppression. Multiple subcarriers are generated to construct orthogonal frequency-division multiplexed FrFT-DC signals. The frequency shift of the subcarriers is set as $N\Delta f = N\csc (0.6*\pi /2) / T,N = \pm 1,\pm 2,\pm 3,\dots$ . Thus, the frequency offset between every two subcarriers is in a range of $\Delta f$ to $6\Delta f$

The injected optical FrFT-DC pulse with $\pm 3\Delta f$ subcarriers is measured and compressed using the FrFT, as shown in Figure 3. The FrFT-DC signal is highly compressed, and the PSLR is higher than $40~\mathrm{dB}$ . The degradation of the PSLR can be ascribed to the nonlinearity of the modulation and additional noise in the system. Then, the RBS is detected and processed in a segment-by-segment manner to obtain the intensity traces of different subcarriers. The Pearson product-moment correlation coefficient (PCC) is used to analyze the correlation between the intensities of different traces. A smaller PCC corresponds to a lower correlation, indicating higher complementation of different subcarriers for better interference fading suppression.

The correlation coefficients between each subcarrier calculated using 80 successive acquisitions of the RBS are plotted in Figure 3b. The subcarriers with frequency offset $\Delta f$ are correlated with a high correlation coefficient of up to 0.7. The correlation coefficient decreases as the frequency offset increases. When the frequency offset is larger than $3\Delta f$ , the correlation coefficient is close to 0.25, which implies that the intensity traces are highly

![](images/842da7d7bde82b78545ad30108d830913ecb2a9125c5b1b684a23ed9537bd547.jpg)

![](images/f6c815b1ae690d71c719daf362ac0c10961cfe1c8fb6e6bf10eab7ff703c4b6b.jpg)

![](images/4edd2ed1fb8722ffe0b6fd184ecf4cef249712bb22b188b5e9574ffba42a2751.jpg)

![](images/1171e66fe7ed430a99a352f9e45f108b24c1b089bbb9fc540d7a8a1a41dad65c.jpg)  
Figure 1. a) Real and imaginary part of FrFT-DC signal; b) spectrum of FrFT-DC signal; c) intensity of the compressed FrFT-DC signal obtained using 0.6-order FrFT; d) intensity of the compressed signal obtained using matched filter.

![](images/9f24b1e5ecf641560c185ae43e568297f67a5dd26c978f14c22255d0f10fe09f.jpg)

![](images/e5ab09c7afc5a626fed9f25730f32fec34e8e55908af5a1d8559defb6ddba7d3.jpg)  
Figure 2. a) Amplitude of compressed three-tone FrFT-DC signal; b) intensity of the compressed three tone FrFT-DC signal obtained using 0.6-order FrFT.

![](images/0bbad6f2e53c56b63e1b7f99319077b833604b1d0ee1c5e617137cc5cc7331c7.jpg)

![](images/76e848431dd134a55a401a3285f0fa0b69642db4c9d5afad3de148096a367435.jpg)  
Figure 3. a) Intensity of measured optical pulse after compression; b) PCCs between each subcarrier for 80 successive traces.

uncorrelated. Therefore, a frequency offset of more than $3\Delta f$ is preferred for better interference fading suppression. However, a larger frequency offset increases the width of the main lobe and decreases the spatial resolution after the RVS method is applied to all subcarriers. We set the frequency shift within $\pm 3\Delta f$ in the following experiments for balance. Actually, $6\Delta f$ spacing involves 7 multiplexed FrFT-DC signals. According to Equation (S5) (Supporting Information), the time-domain width of the main lobe for single compressed LFM signal is $\Delta t = \cos \alpha /Tk$ where $Tk$ denotes the full bandwidth of the LFM signal. According to Figure 1b, the full bandwidth of the FrFT-DC signal is in the range of $400 - 500\mathrm{MHz}$ . Thus, the time-domain width of the main lobe for multiplexed FrFT-DC signals is $\Delta t = 7\cos (0.6*\pi /2) / Tk\approx 10\mathrm{ns}$ , which corresponds to a spatial resolution of $\approx 1\mathrm{m}$ .

The intensity traces of the orthogonal polarization signals obtained using a single subcarrier before the RVS method are shown in Figure 4. Interference fading occurs at most locations along the fiber, and the intensity fluctuation is more than $40~\mathrm{dB}$ (see Figure 4a). Although the polarization-diversity receiver mitigates polarization fading and improves the SNR, there are still numerous fading points owing to destructive interference (see Figure 4c). Consequently, phase errors occur, leading to vibration demodulation failures. For comparison, the RVS method is used to synthesize all subcarriers. The synthesized intensity traces of both orthogonal polarizations are respectively shown in Figure 4b. The intensity fluctuation of the traces is significantly reduced. Then, polarization synthesis is performed, as shown in Figure 4d. Compared to the results shown in Figure 4a,c, the signal intensity is significantly improved by multiple subcarriers. The signal intensity obtained by the conventional matched filter method is also shown in Figure 4d. The synthesized intensity trace of both orthogonal polarizations processed by matched filter shows greater fluctuation compared to that by FrFT. Especially, the intensity of most points is quite close to the noise floor, leading to a high probability of phase extraction failure. This is due to a lack of uncorrelated sensing channels because the matched filter cannot recover the multiplexed subcarriers. In contrast, the

signal intensity is significantly improved by using FrFT. In particular, the intensity of the extreme fading points is enhanced, and the intensity fluctuation is $\approx 10$ dB. Thus, signal fading, including polarization fading and interference fading, is considerably reduced by the subcarrier multiplexing of the FrFT-DC signal.

Dynamic strain measurements are carried out to demonstrate the performance of the system for DAS. A PZT is placed in the middle of the sensing fiber. The length of the fiber wound on the PZT is $\approx 2\mathrm{m}$ . A sinusoidal wave with a peak-to-peak voltage of $1\mathrm{V}$ and a frequency of $1\mathrm{kHz}$ is generated by an AWG to drive the PZT. The period of the sensing probe is $100~\mu \mathrm{s}$ , and 80 trace periods are acquired owing to the limited memory of the oscilloscope. After the RVS method is applied to all subcarriers, the vibration phase is restored by differentiating the phase traces with a step of $1\mathrm{m}$ . The demodulated differential phases of different periods are shown in Figure 5. All phase demodulation errors are eliminated except the phase anomaly induced by the PZT in the middle of the sensing fiber (see Figure 5a). The standard deviation (SD) of the differential phases is calculated to determine the distribution of phase fluctuations. As shown in Figure 5b, the SD of the phase of the synthesis signal is small along the fiber, and there is a peak corresponding to the vibration. The slight overall increase in the SD of the fiber after the vibration point is due to a decrease in the SNR caused by the insertion loss ( $\approx 2\mathrm{dB}$ ) of the PZT. The inset in Figure 5b shows a magnified view of the SD around the vibration point. The mean value of the rising and falling edges of the peak is $\approx 1\mathrm{m}$ , which corresponds to a spatial resolution of $\approx 1\mathrm{m}$ .

Figure 6 presents the vibration measurement results. The vibration phase trace is shown in Figure 6a, and it demonstrates that the vibration amplitude can be accurately extracted. The corresponding power spectral density (PSD) is computed and illustrated in Figure 6b. The frequency is correctly recovered, and no harmonics are observed. The SNR of this vibration is $\approx 25$ dB. The noise level in the PSD is $\approx -58$ dB rad $^2$ Hz $^{-1}$ , i.e., $1.3 \times 10^{-3}$ rad $\sqrt{\mathrm{Hz}^{-1}}$ . The strain resolution is calculated as $143\mathrm{p}\epsilon \sqrt{\mathrm{Hz}^{-1}}$ .[17] In addition, vibration with a chirp frequency of $1 - 5\mathrm{kHz}$ is applied to the PZT. The measured time-domain vibration signal is shown in Figure 6c. The vibration chirp is clearly re

![](images/32b93fd7a443bf81269ca69f5abfa7cf94b0675162543de97eda94393f4a64e0.jpg)

![](images/8c8ec2eea4d5850a0ce873cac93270920f490cc20ff7d6c5be4811ff1fe0ffd8.jpg)

![](images/4608018d332cafec73bf45ea2ecbdd191dcce696ac392e5021359f01efd64195.jpg)

![](images/ec05949a9def3acd9e903a4225363e1993229771572e19fe3ab36d3fdedac65e.jpg)  
Figure 4. a) Intensity trace of orthogonal polarization using single subcarrier; b) intensity trace of orthogonal polarization using multiple subcarriers; c) synthesized intensity trace of orthogonal polarization using single subcarrier; d) synthesized intensity trace of orthogonal polarization by conventional matched filter (in blue) and by FrFT using multiple subcarriers (in purple).

![](images/3304ea3a22af57d20e5865e2f680c9b6d1f1d41d0cea24b60a3ec34d27048702.jpg)

![](images/238c95216e2f7a086a0a9ae13753ac5ffa7181c54e0c5e9da768ec3b53866ccb.jpg)  
Figure 5. a) Differential phase traces for different periods; b) phase SD distribution along the sensing fiber.

stored. There are distortions in high-frequency vibration because of the insufficient sampling rate. The time-frequency spectrum is calculated using the short-time FFT with a Hamming window, as shown in Figure 6d. The vibration frequency increases linearly with time. This verifies that all types of vibration can be restored, indicating that the proposed method is practical and feasible.

The linearity of the response to strain is also verified. The driving voltage is varied from $200\mathrm{mV}$ to $2\mathrm{V}$ , and the frequency is maintained at $1\mathrm{kHz}$ . The linearity of the strain response is shown in Figure 7. The measured result is in good agreement with the linear fitting curve. The linear coefficient $(R^2)$ is 0.998, which indicates a good linear strain response capability.

# 3. Conclusion

We propose a method for suppressing interference fading in pulse compression using $\varphi$ -OTDR. The FrFT is applied to LFM signal generation and pulse compression to achieve a high PSLR and narrow main lobe. Furthermore, interference fading is significantly reduced using OFDM FrFT-DC signals with the highest reported spectrum efficiency, which are highly overlapped in the Fourier domain but orthogonal in the fractional Fourier domain. Proof-of-concept experiments are performed on a fiber with a length of $\approx 10$ km. The dynamic sensing of frequencies up to $5\mathrm{kHz}$ with a strain resolution of $\approx 143~\mathrm{p}\epsilon \sqrt{\mathrm{Hz}^{-1}}$ and spatial

![](images/976feb43314ad87667353e1e8d2b3835a08fecbb1b5bda3101e89cd606cc02c7.jpg)

![](images/0c429bdc27ae62673c7b750f9fb49e16da685cc95460861a667add9103f1dfdc.jpg)

![](images/dcea24a8237735b3ca17ecae5618f98691954fe0d9c7c10070dc5e907164f745.jpg)

![](images/3c66ad4a99954b791adf99c6bc3dd26f4b7ae988d7ca8c2ab9ca652f81e01936.jpg)  
Figure 6. a) Demodulated vibration phase of $1\mathrm{kHz}$ PZT; b) PSD of the $1\mathrm{kHz}$ vibration; c) the demodulated phase signal of PZT with sweeping frequency vibration; d) time-frequency spectrum of the demodulated sweeping frequency vibration.

![](images/1dafcd880cd930769243a8710fdd717bde0f721fc81235d784356d74bc69bbc6.jpg)  
Figure 7. Demodulated phase versus PZT driving voltage.

resolution of $1\mathrm{m}$ is successfully verified. The bandwidth of the signal is limited by the AWG, and higher performance can be expected by improving the FrFT order. We believe this work will not only open up a route for LFM pulse based high-performance $\varphi$ -OTDR, but can also be applied to other sensing systems that use LFM signals.

# 4. Experimental Section

Experimental Setup: The experimental scheme for the sensing system is shown in Figure 8. The experimental setup is quite similar to the self-homodyne coherent (SHC) communication system, where the local oscil

lator is sent along with the modulated signal originating from the same laser in the transmitter. Compared with a traditional coherent system, it is free from frequency offset between the lasers in transmitter and receiver ends. Additionally, SHC detection can improve the system stability with reduced complexity. An ultranarrow-linewidth (less than $1\mathrm{kHz}$ ) fiber laser (NKT E15) that operates at 1550.12 nm is used as the laser source. The use of an ultranarrow-linewidth laser could reduce the influence of phase noise as much as possible. The laser outputs highly coherent continuous wave light, which is divided into two parts in a ratio of 50:50 by a polarization-maintaining couple. One path is directed into an integrated coherent receiver (ICR, Fujitsu FIM24706/301) as the local oscillator (LO).

The other part is sent to a single-polarization IQ modulator (Fujitsu, FTM7962EP) to generate a probe signal. An arbitrary waveform generator (AWG, Tektronix AWG7122B) is used to generate an FrFT-DC signal and drive the modulator. An optical pulse with a high extinction ratio is obtained by cascading a semiconductor optical amplifier (SOA, Inphenix IP-SAD11513), which works as an optical switch, to the IQ modulator to chop the FrFT-DC signal. The SOA is controlled by an arbitrary function generator (AFG, Tektronix AFG3252C), which is synchronized to the AWG using an external clock source. An erbium-doped fiber amplifier (EDFA, Amonics AEDFA-PA-35) is implemented to boost the optical power of the probe signal. The amplified spontaneous emission of the EDFA is filtered using a fiber Bragg grating with a passband of $\approx 0.8\mathrm{nm}$ . Amplified probe pulses are injected into a sensing fiber through an optical circulator. The Rayleigh backscattered signal (RBS) obtained from the sensing fiber enters the signal port of the ICR. After the signal passes through a polarization-diversity receiver and $90^{\circ}$ optical hybrid, the beat signals between the LO and RBS are converted into four photocurrent signals by balanced photodetectors in the ICR.

A four-channel oscilloscope (Teledyne LeCroy, WaveRunner9404) is utilized for data acquisition at the receiver. Offline digital signal processing is performed on personal computer. The received four-channel signal is recombined to a two-channel complex signal corresponding to X and Y polarizations. For every polarization channel, the raw signal is processed

![](images/6a623bff98b1b57d417c530fe35f30ac8790248af35f0759676fae88eae6f809.jpg)  
Figure 8. Experimental setup. AWG, arbitrary waveform generator; AFG, arbitrary function generator; SOA, semiconductor optical amplifier; EDFA, erbium-doped fiber amplifier; PZT, piezoelectric ceramic transducer; ICR, integrated coherent receiver; Osc., oscilloscope.

using the FrFT segment via segment sliding along the fiber. The size of the moving window is the same as the length of the FrFT-DC signal, and the sliding step is one sampling point. The peak of each segment in the fractional Fourier domain is used to form complex vector. Finally, the complex vectors are combined using the RVS method to suppress signal fading.

FrFT Algorithm: Discrete algorithms are essential for the generation and processing of digital FrFT-DC signals. Two discrete algorithms are mainly used for numerical calculations. One is the eigendecomposition of a discrete Fourier transform matrix. This algorithm is accurate but highly complex.[21] The other is the discrete algorithm proposed by Ozaktas, which is comparable to the FFT in terms of calculation complexity;[22] thus, this algorithm is adopted. The FrFT algorithm is carried to generate baseband signal. Then an AWG is used to generate an electrical FrFT-DC signal and drive the modulator. The baseband signal is transferred to optical frequency domain by IQ modulation. The baseband signal transmission reduces the demand of bandwidth for the transmitter and receiver.

# Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

# Acknowledgements

This research was supported in part by National Key R&D Program of China, Grant No. 2018YFB1801205 and by National Natural Science Foundation of China (NSFC), Grant Nos. 61931010 and 62205111.

# Conflict of Interest

The authors declare no conflict of interest.

# Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# Keywords

fractional Fourier transform, linear frequency modulation, OFDM, phase-sensitive reflectometry

Received: November 4, 2022

Revised: January 3, 2023

Published online: February 7, 2023

[1] Z. Li, J. Zhang, M. Wang, Y. Zhong, F. Peng, Opt. Express 2020, 28, 2925.   
[2] J. B. Ajo-Franklin, S. Dou, N. J. Lindsey, I. Monga, C. Tracy, M. Robertson, V. R. Rodriguez Tribaldos, C. Ulrich, B. Freifeld, T. Daley, X. Li, Sci. Rep. 2019, 9, 1328.   
[3] H. Wu, X. Liu, Y. Xiao, Y. Rao, J. Lightwave Technol. 2019, 37, 4991.   
[4] M. Soriano-Amat, H. F. Martins, V. Durán, L. Costa, S. Martin-Lopez, M. Gonzalez-Herraez, M. R. Fernández-Ruiz, Light: Sci. Appl. 2021, 10, 51.   
[5] Z. Wang, L. Zhang, S. Wang, N. Xue, F. Peng, M. Fan, W. Sun, X. Qian, J. Rao, Y. Rao, Opt. Express 2016, 24, 853.   
[6] H. F. Martins, S. Martin-Lopez, P. Corredera, M. L. Filograno, O. Frazao, M. Gonzalez-Herraez, J. Lightwave Technol. 2014, 32, 1510.   
[7] H. He, B. Luo, X. Zou, W. Pan, L. Yan, Opt. Express 2018, 26, 23714.   
[8] Z. N. Wang, J. J. Zeng, J. Li, M. Q. Fan, H. Wu, F. Peng, L. Zhang, Y. Zhou, Y. J. Rao, Opt. Lett. 2014, 39, 5866.   
[9] M. Sagues, E. Pineiro, E. Cerri, A. Minardo, A. Eyal, A. Loayssa, Opt. Express 2021, 29, 6021.   
[10] M. Wu, X. Fan, X. Zhang, L. Yan, Z. He, J. Lightwave Technol. 2020, 38, 4874.   
[11] Y. Wakisaka, D. Iida, Y. Koshikiya, N. Honda, J. Lightwave Technol. 2022, 40, 822.   
[12] W. Zou, S. Yang, X. Long, J. Chen, Opt. Express 2015, 23, 512.   
[13] M. A. Richards, Fundamentals of Radar Signal Processing, McGraw-Hill, New York, USA 2005.   
[14] J.J. Mompo, S. Martin-López, M. González-Herráez, A. Loayssa, Opt. Lett. 2018, 43, 1499.   
[15] D. Chen, Q. Liu, Z. He, J. Lightwave Technol. 2019, 37, 4462.   
[16] J. Zhang, H. Wu, H. Zheng, J. Huang, G. Yin, T. Zhu, F. Qiu, X. Huang, D. Qu, Y. Bai, J. Lightwave Technol. 2019, 37, 4748.   
[17] D. Chen, Q. Liu, Z. He, Opt. Express 2017, 25, 8315.   
[18] F. Wang, Y. Wang, J. Liu, Y. Wang, Opt. Express 2018, 26, 21403.   
[19] L. Deng, M. Cheng, X. Wang, H. Li, M. Tang, S. Fu, P. Shum, D. Liu, J. Lightwave Technol. 2014, 32, 2629.   
[20] H. Zhou, X. Li, M. Tang, Q. Wu, X. Chen, M. Luo, S. Fu, D. Liu, Opt. Express 2016, 24, 28256.   
[21] S.-C. Pei, W.-L. Hsue, IEEE Signal Process. Lett. 2006, 13, 329.   
[22] H. M. Ozaktas, O. Arikan, M. A. Kutay, G. Bozdagt, IEEE Trans. Acoust., Speech, Signal Process. 1996, 44, 2141.