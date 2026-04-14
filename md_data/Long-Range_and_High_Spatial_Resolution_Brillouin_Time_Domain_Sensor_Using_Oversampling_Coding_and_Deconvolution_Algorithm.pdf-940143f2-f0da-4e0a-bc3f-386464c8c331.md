# Long-Range and High Spatial Resolution Brillouin Time Domain Sensor Using Oversampling Coding and Deconvolution Algorithm

Yiqi Li, Can Zhao , Hao Wu , and Ming Tang, Senior Member, IEEE

Abstract-Brillouin optical time domain reflectometer is widely used due to the advantage of single-ended input, but facing the trade-off between sensing distance, spatial resolution, and measurement time in long range application. Harnessingthe co-propagatingRaman amplification,we introduce Golay code under oversampling conditions to enhance the performance of the sensor. The relationship between the coding gain and the oversampling rate is investigated to determine the optimal sampling rate. At the sampling rate of 250 MSa/s, long distance experiments are conducted over a 100 km sensing fiber with 64-bit return to zero Golay coding using 100 ns optical pulses, yielding a BFS uncertainty of about 1 MHz along the fiber and complete rising edge of 20 m. At the same time, the total variationregularization-based deconvolution algorithm is proposed to resolve the deterioration of spatial resolution due to direct decoding. The robustness of the algorithm over different signal-to-noise

ratio, temperature gradients, and sampling rates is investigated through simulations and experiments. Finally, the spatial resolution of the experimental results is improved to be higher than $\ 6 m$ , which is one third of the original result. These methods greatly facilitate optical pulse coding in long range and high-resolution sensing.

Index Terms- Optical fiber sensors, Brillouin scattering, pulse coding, deconvolution.

![](images/b74cf6c73bbf7829ad2861932a21f95b007fe95bac0660729104a9068e9ce842.jpg)

# I. INTRODUCTION

N DECADES of research and development, together with I the rapid development of optical communication [1], optical sensing techniques have seen prolonged booming in varies of fields, such as optical ranging [2], biosensing [3], [4] liquid sensing [5], and marine environment monitoring [6].

Manuscript received 18 May 2022; accepted 2 June 2022. Date of publication 17 June 2022; date of current version 1 August 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1801205, in part by the National Natural Science Foundation of China (NSFC) under Grant 61722108 and Grant 61931010, and in part by the Innovation Fund of Wuhan National Laboratory for Optoelectronics (WNLO). The associate editor coordinating the review of this article and approving it for publication was Prof. Santosh Kumar. (Corresponding author: Can Zhao.)

The authors are with the Wuhan National Laboratory for Optoelectronics (WNLO) and the National Engineering Laboratory for Next Generation Internet Access System, School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: 408210527@qq.com; zhao_can@mail.hust.edu.cn; wuhaoboom $@$ qq.com; tangming $@$ hust.edu.cn). Digital Object Identifier 10.1109/JSEN.2022.3182392

Among them, distributed optical fiber sensors, especially sensors based on Brillouin scattering have been attracting much attention [1]. For instance, the Brillouin optical time domain analysis (BOTDA) [7] and reflectometer (BOTDR) [8] have advantages of long sensing distance, strong robustness, and the linear relationship between the Brillouin frequency shift (BFS) with strain and temperature [9], [10]. BOTDR based on Spontaneous Brillouin Scattering (SpBS) is widely used owing to the single-ended measurement, simple implementation, and convenient application. Nowadays, BOTDR can realize fast [11] and submeter [12] sensing (but within short fiber length), promising feasibility in high accuracy and dynamic vibration monitoring [13]. Furthermore, long-range sensing is required in many practical fields [14], such as bridge and tunnel condition monitoring, long transportation pipeline monitoring, submarine detection, geological disaster warning [15], etc. However, the SpBS signal is weak and difficult to detect, limiting the sensing distance and measurement accuracy. Therefore, it is of importance to explore remarkable approaches to long-range BOTDR.

An important factor affecting the sensing distance is the signal-to-noise ratio (SNR). The most direct way to improve SNR is the cumulative average method, but it requires a longer measurement time. Increasing the pulse width also improves the SNR and reduces the measurement uncertainty but deteriorates the spatial resolution (SR). In order to alleviate the trade-off [16] between measurement speed and accuracy, pulse width and SR, many methods are proposed to enhance the performance of BOTDR.

To improve the sensing distance, a typical way is to introduce the distributed Raman amplification (DRA) [17], by which a record of $1 5 0 ~ \mathrm { k m }$ sensing distance has been realized [18]. However, the spatial resolution of the previously reported long-distance sensing is still compromised to be tens of meters. In addition to first-order DRA, high-order or hybrid Raman amplification methods also have been proposed [19], which increase the performance but also raise the system cost. Besides, cascading erbium doped fiber amplifiers (EDFA) is also an effective approach to extending the sensing range [20], but breaks the passive fiber link and increases the complexity. It is unsafe and unreliable to carry long electrical power for the optical repeaters at the middle of the fiber for many practical applications. Another method to increase sensing distance is pulse coding, which improves the SNR without the deterioration of SR [21]. A scheme of Simplex codes and Landau-Placzek ratio based on SpBS is presented to improve temperature resolution long-range sensing [22]. Golay pulse coding is also used to improve the frequency accuracy in ultra-high spatial resolution sensing scheme but within relatively short range [23]. Recently, random coding is introduced to enhance the SNR [24], and over $6 0 ~ \mathrm { k m }$ sensing is realized with a frequency accuracy of 3 MHz. In fact, optical pulse coding alone can hardly reach the long-distance regime (e.g., over $1 0 0 \mathrm { k m } ,$ , because of the nonlinearity power constraint.

Meanwhile, a typical trouble in pulse coding is the slow transient effect of EDFA, which leads to decoding distortion. Although there are some schemes to improve the sequence flatness, such as predistortion [25], pre-depletion [26], postprocessing [27], the pulse peak power is greatly reduced. In contrast, the DRA doesn’t have such serious problems. Therefore, it is a very effective solution to introduce pulse coding and DRA simultaneously into the long-range BOTDR system. On the other hand, due to the power limitation of stimulated Brillouin scattering (SBS) under optical amplification, the incident power of the code sequence is lower than that of traditional single pulse. The conceptual advantages of the coding technique can be hardly realized in practice of realworld applications. Therefore, it is very interesting to increase the actual gain of pulse coding. In our previous work [28], the relationship between the coding gain and the sampling rate for correlation-coded OTDR was studied. Since the oversampling improves the Golay coding gain in OTDR systems, this feature will be helpful to further enhance the performance of longrange BOTDR.

In this paper, we combine the first-order co-propagating Raman amplification and over-sampled Golay coding in BOTDR to achieve long sensing range and high SR.

To determine the optimal sampling rate, the theoretical relationship between SNR and oversampling rate is firstly verified. Thanks to the additional gain provided by high over-sampling rate, a $1 0 0 \mathrm { - k m }$ sensing range is realized with the frequency uncertainty below 1 MHz. It should be noted that the decoding result of oversampling coding is the convolution of an equivalent triangle pulse and the impulse response, thus deteriorating the spatial resolution [29]. To restore the high-resolution results, a total variation regularization-based deconvolution algorithm is proposed in the system. Experimental results show that the spatial resolution can be improved to better than $6 \textrm { m }$ by the algorithm at the sampling rate of $5 0 0 ~ \mathrm { M S a / s }$ , which is one third of the original result.

# II. PRINCIPLE

# A. Over Sampling Coding in BOTDR

Optical coding techniques for sensing applications are based on intensity modulated pulse sequences, such as Simplex or Golay code. The feasibility of optical coding in BOTDR has been readily validated in different works [30]. It provides improved SNR without sacrificing response resolution under ideal circumstances. Typically, the Golay code has perfect autocorrelation property. In other words, the sum of autocorrelations of Golay codes $A _ { n }$ and $B _ { n }$ is as follows:

$$
r _ {n} = A _ {n} \otimes A _ {n} + B _ {n} \otimes B _ {n} = 2 L \delta_ {n} \tag {1}
$$

where $\otimes$ represents correlation, $\delta _ { n }$ represents the delta function, and $L$ represents the number of sequence elements. The realization of Golay code with intensity pulses is usually enabled by constructing four unipolar sequences $( A _ { n i } , B _ { n i } , i =$ 1, 2) [31]. The received signal is considered as the convolution between the pulse sequences and the impulse response (corresponds to the measured Brillouin scattering intensity trace under an infinitely narrow single pulse, $h _ { n }$ ), then a series of responses can be obtained.

$$
\left\{ \begin{array}{l} S _ {A i n} = h _ {n} \otimes A _ {n i} \\ S _ {B i n} = h _ {n} \otimes B _ {n i} \end{array} , \quad i = 1, 2 \right. \tag {2}
$$

By correlating each of these responses with its corresponding original sequence launched into the fiber and summing up the results, the fiber impulse response is retrieved:

$$
\begin{array}{l} S _ {n} = \operatorname {c o r r} \left\langle \left[ S _ {A 1 n} - S _ {A 2 n} \right], A _ {n} \right\rangle + \operatorname {c o r r} \left\langle \left[ S _ {B 1 n} - S _ {B 2 n} \right], B _ {n} \right\rangle \\ = r _ {n} * h _ {n} + \eta_ {n} \tag {3} \\ \end{array}
$$

When the noise source $\eta _ { n }$ is considered as the additive white Gaussian noise (AWGN), the coding gain is $\sqrt { L } / 2$ [32].

In the long range BOTDR, the pulse width is generally in tens to hundreds of nanoseconds. It means that the bandwidth is relatively low, thus high sampling rate is applicable without greatly increasing the cost. Under the oversampling condition, the pulse width $T$ is $m$ times of the sampling interval, m being the oversampling rate. In this case, the sum of the autocorrelations is no longer a delta function, but a triangular function with full width at half maximum (FWHM) of $m$ :

$$
\begin{array}{l} r _ {n} = A _ {n} \otimes A _ {n} + B _ {n} \otimes B _ {n} = 2 L m q _ {n} \\ q _ {n} = \operatorname {t r i} \left(\frac {n}{m}\right) = \left\{ \begin{array}{l l} 1 - \left| \frac {n}{m} \right|, & \left| \frac {n}{m} \right| \leq 1 \\ 0, & \text {o t h e r w i s e} \end{array} \right. \tag {4} \\ \end{array}
$$

Since the code length is extended from $L$ to Lm, the coding gain changes from $\sqrt { L } / 2$ to $\sqrt { L m } / 2$ . This feature would benefit a lot for the practical trial of pulse coding in long-range BOTDR where nonlinear effects constraint the power of injected optical pulses. However, due to the limited bandwidth of receivers in long range BOTDR, when the sampling rate is high, the AWGN becomes band-limited noise within the sampling rate bandwidth. Thus, the coding gain is not simply related to the code length, but also dependent on the property of noise. In this way, the coding gain can be seen as the ratio of RMS of the noise, given by [29]:

$$
\text {c o d i n g} = \sqrt {\frac {\sigma^ {2}}{\sigma^ {2} + 2 \sum_ {k = 1} ^ {m - 1} q (k) R _ {N} (k)}} \cdot \frac {\sqrt {L m}}{2} \tag {5}
$$

We define:

$$
\xi = 2 \sum_ {k = 1} ^ {m - 1} q (k) R _ {N} (k) \tag {6}
$$

where $\sigma$ is the RMS of the noise of a single sequence, $R _ { N } ( k )$ is the autocorrelation function of the noise, respectively. It is obvious that the change of SNR depends on the sign of $\xi$ . When it is negative, the SNR increases, otherwise the SNR decreases. When the sampling rate is large, after mathematical simplification, the coding gain denoted by (5) is no longer related to $m$ , but tends to be constant. It implies that the oversampling rate should be carefully chosen according to the feature of the noise. Therefore, it is necessary to comprehensively experimentally investigate the optimal sampling rate to enhance the performance in a specific sensing system, as has been carried out in the following section.

# B. Spatial Resolution

As stated in (3), the incident pulse under the oversampling coding scheme is equivalent to a triangular pulse. Then the result after directly decoding is given by:

$$
\begin{array}{l} S _ {n} = \operatorname {c o r r} \left\langle \left[ S _ {A 1 n} - S _ {A 2 n} \right], A _ {n} \right\rangle + \operatorname {c o r r} \left\langle \left[ S _ {B 1 n} - S _ {B 2 n} \right], B _ {n} \right\rangle \\ = r _ {n} * h _ {n} \\ = 2 L m \left[ q _ {n} * h _ {n} \right] \tag {7} \\ \end{array}
$$

where $h _ { n }$ means the impulse response with pulse width $T / m$ , and $^ *$ means convolution calculation. In other words, the decoding result of oversampling coding is the convolution of the equivalent triangular pulse and the impulse response. Although the equivalent pulse has the same FWHM as the original rectangular pulse, the base width of the triangle is doubled. The SR after decoding will be wider after the above convolution. That is to say, the SR is determined by the equivalent pulse and will become worse.

As the result by direct decoding is the convolution between equivalent pulse and system response, it is possible to reconstruct the high-resolution response by deconvoluting the results [33], [34]. In our system, a deconvolution algorithm based on the total variation regularization is introduced to improve SR without changing the system parameters. As aforementioned, $h _ { n }$ is the high SR signal we need to recover. The direct

inversion of the noisy decoding result is an ill-posed problem. The noise term will be amplified, causing undesirable consequences. In order to avoid such ill-conditioned calculation, total variation (TV)-based deconvolution is used to stabilize the recovered signal by introducing a regularization term:

$$
\hat {h} = \arg \min  \mu \| q * h - y \| _ {2} ^ {2} + \| h \| _ {T V} \tag {8}
$$

where $\mu$ is the regularization parameter, and $\lVert \cdot \rVert _ { 2 }$ is the L2 norm. The first term on the right is the fidelity item, which represents the difference with the raw data. The second term is the regularization term, calculating the sum of variations between neighboring recovered data along the fiber. It is given by:

$$
\| h \| _ {T V} = \sum_ {i} | h _ {i + 1} - h _ {i} | \tag {9}
$$

The essence of TV-based deconvolution is to find a solution of $h$ to minimize (8). The parameter $\mu$ determines the performance of the algorithm to a great extent, since it controls the relative weights of the data compliance and regularization terms. When $\mu$ is very large, the regularization term is invalid and the highest SR is obtained, but the result is sensitive to noise. As $\mu$ decreases, the weight of the regularization term becomes larger, forcing the result to become smooth. However, lower $\mu$ may make the signal over-smoothing and filter out effective sensing information.

At present, several algorithms have been proposed for the numerical computation of similar problems. The TV estimate is computed by a majorization-minimization approach based on convexity arguments [35]. To simplify the calculation, the least square method [36] is used to minimize (8), the weighted sum of regularization objective function.

# III. SIMULATION

In order to verify the effect of the deconvolution algorithm, the following simulation is performed with a commercial numerical simulator MATLAB (R2020b). The sensing fiber has a length of $2 0 0 \mathrm { ~ m ~ }$ and a uniform distribution of BFS at $1 0 . 6 8 ~ \mathrm { G H z }$ , including a $4 0 \mathrm { ~ m ~ }$ section with the BFS changed to 10.72 GHz near the fiber end. The effective pulse width of the Golay coded BOTDR system is set to 100 ns, that is, the abovementioned equivalent pulse is a triangular pulse with FWHM of $1 0 ~ \mathrm { m }$ . The analysis frequency of the detection system is swept in the range from $1 0 . 6 \ : \mathrm { G H z }$ to $1 0 . 8 \ : \mathrm { G H z }$ with a step of 2 MHz.

First, to investigate the influence of SNR on the deconvolution algorithm, the AWGN with different intensity is introduced on the decoded data with sampling rate of $5 0 0 ~ \mathrm { M S a / s }$ . For comparison, the data with SNR of 25 dB are directly fitted by Lorentzian curve without deconvolution, as represented by the blue curve in Fig. 1(a). The complete rising edge at the BFS change area is about $2 0 \mathrm { ~ m ~ }$ , which will bring about deterioration of SR. In contrast, the processed results using TV-based deconvolution $\mathit { \Pi } _ { \mathcal { M } \ } = \ 0 . 0 9 )$ show a significantly improved sharp edge with a total width of about 6 m. From the inset in Fig. 1(a), we can see that the BFS fluctuation induced from deconvolution is less than $0 . 4 ~ \mathrm { M H z }$ even at low SNR of

![](images/643587480cd36835249b2657b9c745c81db4edf0d8025380539fad3276fad940.jpg)  
(a)

![](images/1344318b6e07a6a92d8da497e66d125988bb820db0201eaac17b4c758407ab45.jpg)  
(b)   
(c)

![](images/a2b6bb2cd65828760b58697377c887bbcbf23065c1f6f663e80e3937151c298a.jpg)  
Fig. 1. Simulation to verify the influence of different parameters on the deconvolution algorithm. (a) The deconvolution on the decoding results of different SNR (yellow, purple, and red). The blue curve is obtained by direct Lorentzian curve fitting of the data with SNR of 25 dB without deconvolution; (b) The effect of deconvolution algorithm under temperature gradient, zooming in the heating edge; (c) The deconvolution outcome under different sampling rate, zooming in the rising edge.

15 dB. It means that the proposed algorithm shows a favorable robustness over different SNR.

Since the most common application scenario of BOTDR is temperature sensing, it is necessary to verify the robustness of the deconvolution algorithm to temperature gradients in addition to SNR. The temperature of the heating segments is set to be $2 0 ~ ^ { \circ } \mathrm { C }$ , $4 0 ~ ^ { \circ } \mathrm { C }$ , $6 0 ~ ^ { \circ } \mathrm { C }$ , and $8 0 ~ ^ { \circ } \mathrm { C }$ higher than the room temperature. Deconvolution operation is performed with the same $\mu$ on the signal with a SNR of 20 dB and sampling rate of $5 0 0 ~ \mathrm { { \ M S a / s } }$ . The BFS of the processed results is obtained in Fig. 1(b). The BFS recovered by the deconvolution algorithm is restored to the theoretical value corresponding to the temperature, and no obvious sensing error is generated. At the same time, the rising edge is restored to about $6 { - } 7 \mathrm { ~ m ~ }$ at different temperatures. Notably, the recovered spatial resolution will be higher for greater temperature change. Therefore, the TV-based deconvolution can restore the accurate temperature while significantly improving the SR in temperature sensing.

To further study the effect of oversampling rate on the deconvolution algorithm, the deconvolution algorithm with the same $\mu$ is applied to the data with 20 dB SNR at different sampling rates of 100 MSa/s, 250 MSa/s, 500 MSa/s respectively. As shown in Fig. 1(c), the rising edge of the recovered signal under $5 0 0 ~ \mathrm { M S a / s }$ is about $6 \textrm { m }$ , and the BFS is restored to its theoretical value. However, with the decrease of sampling rate, the performance becomes worse obviously. Therefore, the higher the sampling rate of raw data, the better the recovery effect of SR.

# IV. EXPERIMENTS

The experimental setup of the BOTDR system using complementary coding and Raman amplification is shown in Fig. 2. The continuous-wave (CW) light from a narrow linewidth $( { \sim } 1 \ \mathrm { k H z } )$ laser (NKT, E15), operating at $1 5 5 0 ~ \mathrm { n m }$ with ${ \sim } 1 2$ dBm output power, is split into two branches through a 70/30 optical fiber coupler. In the upper branch, a high extinction-ratio $( > 4 0$ dB) semiconductor optical amplifier (SOA, INPHENIX, IPSAD1512) driven by an arbitrary function generator (AFG, Tektronix, AFG31252C) is used to generate intensity modulated pulses. Here we adopt 64-bit return to zero (RZ) Golay coded pulses of 100 ns width with $50 \%$ duty cycle, considering both the coding gain and effect of nonlinearity. Then its state of polarization is scrambled by a polarization scrambler (PS, General Photonics, PCD005) to reduce polarization fading during interference. The pump pulse is launched into the fiber under test (FUT) through an optical circulator. The $1 4 6 0 ~ \mathrm { n m }$ Raman pump is coupled into the FUT for the first-order Raman amplification through a $1 4 6 0 / 1 5 5 0 \mathrm { n m }$ wavelength division multiplexer (WDM). Here, the Raman pump is injected in the co-propagating direction with the Brillouin pump, and the output power of the Raman pump is about 28 dBm to lengthen the sensing range as far as possible.

In the lower branch, the local light is aligned by a polarization controller (PC) before entering the Mach-Zehnder modulator (MZM, Oclaro, F10). The MZM is driven by a radio-frequency (RF) signal from a microwave generator (R&S, SMB100A) to generate the frequency-shifted reference light. The frequency of the microwave is ${ \sim } 1 0 . 1$ GHz. Then

![](images/044958d80360ae43349c33bccfa0e3b47e1e7799924651f30e5af7a6ba8d3d1a.jpg)  
Fig. 2. Experimental setup used to measure BFS with pulse coding and Raman amplification. SOA: semiconductor optical amplifier; AFG: arbitrary function generator; PS: polarization scrambler; WDM: wavelength division multiplexer; PC: polarization controller; MZM: Mach-Zehnder modulator; RF: radio-frequency; PD: photodetector; BPF: bandpass filter.

it is combined with SpBS light through a 50/50 optical fiber coupler before a balanced photodetector (PD, Thorlabs, PDB480C-AC) with a bandwidth of $8 0 0 ~ \mathrm { M H z }$ . The electric signal is directed to a bandpass filter (BPF) with a center frequency of $6 0 0 ~ \mathrm { \ M H z }$ and a bandwidth of 30 MHz to obtain the signal near the Brillouin frequency shift. Finally, it is collected by an oscilloscope (Tektronix, MDO3104) after passing through an electric amplifier and a detector. By sweeping the frequency of the microwave from 10.01 GHz to 10.21 GHz with a step of 2 MHz, the Brillouin scattering spectrum along the fiber is achieved. The power signal corresponding to each sweeping frequency is averaged 2000 times to improve the SNR. After about 100 groups of frequency sweeping, the distributed Brillouin scattering power spectrum along the sensing fiber can be obtained. Then, pulse decoding algorithm is applied to recover the single pulse response and TV-based deconvolution is utilized to improve the spatial resolution.

# A. Optimal Sampling Rate

In order to confirm the quantitative relationship between the coding gain and the oversampling rate m in the practical BOTDR system and to obtain the optimal setting, the sampling rates are set to $1 0 \ \mathrm { M S a / s }$ , $5 0 ~ \mathrm { M S a / s }$ , 100 MSa/s, 250 MSa/s, $5 0 0 ~ \mathrm { M S a / s }$ , $1 2 5 0 ~ \mathrm { M S a / s }$ respectively. It should be noted that the oversampling rate is taken as the ratio of the sampling rate to the pulse width rather than the codeword width in RZ coding. That is, $m$ is 1, 5, 10, 25, 50, 125, respectively. The sensing fiber is a $5 0 \ \mathrm { k m } \ \mathrm { S M F }$ . To estimate the trend of SNR with respect to sampling rate according to (5), the background noise of the system is collected at the sampling rate of $5 \mathrm { G S a / s }$ . The product of the noise autocorrelation $R _ { N }$ and the triangular function $q$ in (4) is calculated, as shown in Fig. 3(a). It is clear that the noise is bandwidth limited. Next, the term $\xi$ of (6) is calculated as shown in Table I.

The $\xi$ is negative at the sampling rate of $5 0 ~ \mathrm { M S a / s }$ , making the SNR higher than the theoretical trend. However, $\xi$ becomes positive at higher sampling rates, resulting in a lower SNR deflected from the theoretical calculation.

TABLE I THE TERM ξ FOR DIFFERENT SAMPLING RATES   

<table><tr><td>sampling rate (MSa/s)</td><td>10</td><td>50</td><td>100</td><td>250</td><td>500</td><td>1250</td></tr><tr><td>m</td><td>1</td><td>5</td><td>10</td><td>25</td><td>50</td><td>125</td></tr><tr><td>ξ</td><td>0</td><td>-0.0714</td><td>0.5282</td><td>0.7016</td><td>0.7484</td><td>0.7458</td></tr></table>

Next, the SNR distribution along the fiber is calculated. The calculated SNR of the last $5 0 0 ~ \mathrm { ~ m ~ }$ fiber at different sampling rate is depicted in Fig. 3(b). Generally, higher sampling rate leads to greater SNR. But the increasement of SNR significantly slows down as sampling rate grows. To better illustrate the SNR varying with sampling rate increasing, the average SNR is calculated using the mean power of the last $5 0 0 \mathrm { ~ m ~ }$ fiber at the end as shown in Fig. 3(c). The horizontal coordinates are logarithmic. The blue curve is the theoretical value calculated from $\sqrt { L m } / 2$ . The experimental result is higher than the theoretical value at $5 0 ~ \mathrm { M S a / s }$ . It reaches its maximum at $2 5 0 ~ \mathrm { M S a / s }$ , but deviates down from the theory at higher sampling rates and presents a trend of saturation. It means that the noise should be regarded as bandwidth limited white noise at high sampling rates. These results are in good agreement with above analysis. The sampling rate larger than $2 5 0 ~ \mathrm { M S a / s }$ could be feasible to obtain higher SNR in long range BOTDR.

# B. Long-Range Sensing

In order to verify the long-range sensing capability, the FUT is replaced with a 100 km SMF. And the sampling rate is $2 5 0 \ \mathrm { \ M S a / s }$ . To improve the SNR, 2000 times of averaging is applied in the experiments. As a comparison, measurements are conducted in coded BOTDR with and without oversampling respectively. The recovered BGS under oversampling coding is shown in Fig. 4(a). The fluctuation caused by the flange plate appears at $5 0 ~ \mathrm { k m }$ . To quantitively investigate the performance of the system, the BFS uncertainty under each condition is calculated, as shown in Fig. 4(b).

It is clear that the BFS uncertainty at the both fiber ends is much greater without oversampling than that with oversampling, and is still larger than 2 MHz at the rest area. As a contrast, the results obtained by oversampling coding reduce the BFS uncertainty to about 1 MHz along the fiber. Thus, the extra SNR gain provided by oversampling facilitates the application of Golay coding in long range sensing.

# C. Deconvolution Processing

To verify the uniform amplification of pulse sequences and avoid decoding error, the transmitted pulses are measured at the far end of FUT. The sum of the correlation of the transmitted pulses and the code sequence is in triangle shape without side lopes, as shown in Fig. 5. The equivalent pulse is in a triangle shape with a total width of 200 ns and FWHM of 100 ns as expected.

![](images/7f43de5c48c3e46587dfdf1101429c49c385517be5a8a1d2230d5ecdc4c4c460.jpg)

![](images/f2304bdc55b1163fd26f4eb5cc994fecace0b8b8ea927dc9334301188816d63c.jpg)

![](images/5ea1d8702de34502f756e22705d999daae31e8306101737d0ba81e17792554de.jpg)  
Fig. 3. (a) The product of the noise autocorrelation and the triangular function. The noise autocorrelation is calculated from the measured noise, and the triangular function is described as in principle; (b) The SNR distribution of 500 meters at the fiber end after decoding at different sampling rates; (c) The average SNR of the last $5 0 0 \mathsf { m }$ fiber after decoding at different sampling rates.

![](images/0bfc686df1e4dc79a1761b77130988798a143c407f517d0a947cd25b2e532fda.jpg)

![](images/a67bc84928ebba1c560e35e6e172d31286b13dd89991b67242e12b2ecdac8538.jpg)  
Fig. 4. Experimental results of long-range sensing based on $1 0 0 ~ \mathsf { k m }$ fiber: (a) 3D plot of BGS under oversampling coding, showing the power change due to Raman amplification and flange plate at $5 0 \kappa \mathsf { m }$ ; (b) BFS uncertainty calculated from consecutive measurements respectively with or without oversampling.

![](images/3731726d1e257522e2cd2cab34988556821bea414ebc8bf144c37dea56249552.jpg)  
Fig. 5. The verification of equivalent pulse at the far end of FUT. The inset shows a triangle with FWHM of 10 m without sidelobes.

It has been proved that the decoded results are the convolution of the equivalent pulse with the impulse response.

And a deconvolution algorithm is proposed to recover the highresolution response, which is verified through simulations. To validate the feasibility of the TV-based deconvolution in practical application, a fiber section of about $3 0 \textrm { m }$ a t $5 0 ~ \mathrm { k m }$ is placed in a water bath, and the rest is maintained in a stable room temperature. The initial temperature of the water bath is $2 3 ~ ^ { \circ } \mathrm { C }$ , followed by a gradient heating of $3 6 ~ ^ { \circ } \mathrm { C }$ , $4 4 ~ ^ { \circ } \mathrm { C }$ , $5 2 ~ ^ { \circ } \mathrm { C }$ , $6 0 ~ ^ { \circ } \mathrm { C }$ , and $6 8 \ ^ { \circ } \mathrm { C }$ . A total of 6 sets of data are obtained at $2 5 0 ~ \mathrm { { \ M S a / s } }$ for higher SNR.

The BFS distribution obtained with and without deconvolution algorithm is shown in Fig. 6(a), with $\mu$ taken as 0.4. When searching the optimal $\mu$ , we target on recovering the high spatial resolution, meanwhile avoiding the degradation of signalto-noise ratio (SNR) after processing. Figure 6(b) is a zoom-in view at $2 1 { - } 2 2 ~ \mathrm { k m }$ (highlighted in a red box in Fig. 6(a)). All the results show highly consistency, and the algorithm processing does not bring obvious errors. A clearer sight of the heating part (blue box in Fig. 6(a)) is presented in Fig. 6(c). The total length of the rising edge of raw data is about $2 0 ~ \mathrm { m }$ , which is consistent with the theory. After the deconvolution, the BFS at different temperatures can be restored to the theoretical level,

![](images/4411bd7c08d3daf1f6284e1b2a92e4fe081e4539e249123e3df87d59e7fc7581.jpg)

![](images/2134a6a32eea8cfa5c7c084c47ef824c72b904f02792abe718669e6055ffe41d.jpg)

![](images/1ac02f646b681a2b6ba201d19a7ef9e98c14cb38e9b6069f7e9b0dd669779dd4.jpg)  
Fig. 6. (a) The measured BFS distribution of the fiber at different temperature; (b) The zoom-in view of the BFS near 21 km fiber; (c) Measured BFS distribution at the fiber end near the heating section.

![](images/9b30afb1bae0ae5d197a76e110c757a8a2a5b2cd8eb902764b1c6d571bd4ba3e.jpg)  
Fig. 7. The rising edge of the temperature change before and after the deconvolution algorithm. The total length of rising edge is marked.

and the rising edge is improved to be better than 7 m. Regarding higher temperature change (e.g., $6 8 ~ ^ { \circ } \mathrm { C } )$ ), the rising edge can be even narrower as about $6 \mathrm { m }$ . Therefore, the deconvolution algorithm is robust to different temperatures and different BFS level.

The influence of sampling rate on the SR recovery is further verified. To achieve a higher SNR, the signal is oversampled with the sampling rate at $2 5 0 ~ \mathrm { M S a / s }$ and $5 0 0 ~ \mathrm { M S a / s }$ , respectively. The temperature of the water bath is $6 0 ~ ^ { \circ } \mathrm { C }$ , which means a BFS change of about $3 7 ~ \mathrm { M H z }$ . The measured BFS from the raw data without deconvolution is shown in the blue curve in Fig. 7. Next, the data are processed by the deconvolution algorithm, whose parameter $\mu$ is taken as 0.4. The rising edge is improved to $7 \textrm { m }$ at the sampling rate of $2 5 0 ~ \mathrm { M S a / s }$ , while maintaining the BFS level without distortion. Moreover, with higher sampling rate of $5 0 0 ~ \mathrm { M S a / s }$ and the same value of $\mu$ , the rising edge becomes steeper to be $6 ~ \mathrm { ~ m ~ }$ . Generally, the spatial resolution of BOTDR is evaluated by the fiber length covering the BFS change from $10 \%$ to $90 \%$ of the transition area [27]. It means

the spatial resolution would be smaller than $6 \textrm { m }$ by such definition.

These results are in good accordance with the simulation. It is worth mentioning that the BFS uncertainty is increased by about $0 . 5 ~ \mathrm { M H z }$ after the deconvolution algorithm. But it is still very valuable to increase the spatial resolution substantially at this trivial cost. As a comparison, the lasted reports on long range BOTDR using co-propagating Raman amplification achieved $1 0 0 \mathrm { k m }$ sensing distance with a spatial resolution of $4 0 \textrm { m }$ and temperature uncertainty of $3 ~ ^ { \circ } \mathrm { C }$ a t the fiber end [37]. Compared with Raman amplification only, optical pulse coding also improves the performance at the both ends of the sensing fiber. Specifically, in our experiments, the oversampling optical pulse coding combined with Raman amplification avoids the pulse depletion effect in EDFA, thus providing enough SNR for long range sensing. Moreover, using total variation regularization-based deconvolution algorithm, the spatial resolution is significantly improved. All these advantages of the coding methods contribute to the long-range sensing of $1 0 0 ~ \mathrm { k m }$ , with spatial resolution of $6 \textrm { m }$ and BFS accuracy about 1 MHz. These results have sufficiently validated the advantages of our proposed scheme and algorithm.

It should be noted that the highest SNR is obtained at the sampling rate of $2 5 0 \ \mathrm { M S a / s }$ , which means the optimal sampling rate in long range BOTDR. For the end of higher spatial resolution, the sampling rate could be increased but at higher cost. There is a gap between the recovered results and the theoretical, because the performance of deconvolution algorithm depends on several factors including the SNR, sampling rate and its parameter. And more work should be carried out in algorithm optimization to narrow the gap. What is more, the bandwidth of the receiving system will constraint the attainable spatial resolution. The use of a BPF at the receiver end limit the bandwidth to $3 0 ~ \mathrm { M H z }$ , yielding a theoretical spatial resolution of about $3 \textrm { m }$ .

# V. CONCLUSION

The distributed Raman amplification and oversampled Golay coding are combined to enhance the performance of BOTDR in long range sensing. At the sampling rate

of $2 5 0 ~ \mathrm { M S a / s }$ , the distributed sensing over $1 0 0 ~ \mathrm { k m }$ fiber is successfully realized using 64-bit Golay coding with a 100 ns pulse width. Thanks to the extra SNR gain provided by oversampling, the BFS uncertainty along the fiber is about 1 MHz. Moreover, a total variation regularization-based deconvolution algorithm is proposed to recover the high-resolution results from the convolution between the equivalent triangle pulse and the system response. Experiments show that the rising edge of the transition length at the heating segment is restored from $2 0 \mathrm { ~ m ~ }$ to higher than $6 \textrm { m }$ without any hardware modification. This method promises a new approach for high performance long-range sensing system.

# REFERENCES

[1] S. Chaudhary, L. Wuttisittikulkij, J. Nebhen, A. Sharma, D. Z. Rodriguez, and S. Kumar, “Terabyte capacity-enabled $1 0 \times 4 0 0$ Gbps) Is-OWC system for long-haul communication by incorporating dual polarization quadrature phase shift key and mode division multiplexing scheme,” PLoS ONE, vol. 17, no. 3, Mar. 2022, Art. no. e0265044.   
[2] S. Chaudhary et al., “Coherent detection-based photonic radar for autonomous vehicles under diverse weather conditions,” PLoS ONE, vol. 16, no. 11, Nov. 2021, Art. no. e0259438.   
[3] Y. Wang et al., “Biocompatible and biodegradable polymer optical fiber for biomedical application: A review,” Biosensors, vol. 11, no. 12, p. 472, Nov. 2021.   
[4] B. Kaur, S. Kumar, and B. K. Kaushik, “Recent advancements in optical biosensors for cancer detection,” Biosensors Bioelectron., vol. 197, Feb. 2022, Art. no. 113805.   
[5] R. He, C. Teng, S. Kumar, C. Marques, and R. Min, “Polymer optical fiber liquid level sensor: A review,” IEEE Sensors J., vol. 22, no. 2, pp. 1081–1091, Jan. 2022.   
[6] R. Min, Z. Liu, L. Pereira, C. Yang, Q. Sui, and C. Marques, “Optical fiber sensing for marine environment and marine structural health monitoring: A review,” Opt. Laser Technol., vol. 140, Aug. 2021, Art. no. 107082.   
[7] A. Motil, A. Bergman, and M. Tur, “State of the art of Brillouin fiberoptic distributed sensing,” Opt. Laser Technol., vol. 78, pp. 81–103, Apr. 2016.   
[8] Q. Bai et al., “Recent advances in Brillouin optical time domain reflectometry,” Sensors, vol. 19, no. 8, p. 1862, Apr. 2019.   
[9] H. Ohno, H. Naruse, M. Kihara, and A. Shimada, “Industrial applications of the BOTDR optical fiber strain sensor,” Opt. Fiber Technol., vol. 7, no. 1, pp. 45–64, Jan. 2001.   
[10] M. Niklès, L. Thévenaz, and P. A. Robert, “Simple distributed fiber sensor based on Brillouin gain spectrum analysis,” Opt. Lett., vol. 21, no. 10, p. 758, May 1996.   
[11] X. Bao, M. DeMerchant, A. Brown, and T. Bremner, “Tensile and compressive strain measurement in the lab and field with the distributed Brillouin scattering sensor,” J. Lightw. Technol., vol. 19, no. 11, pp. 1698–1704, Nov. 1, 2001.   
[12] H. Wang, D. Ba, X. Mu, D. Zhou, and Y. Dong, “Ultrafast distributed Brillouin optical fiber sensing based on optical chirp chain,” IEEE J. Sel. Topics Quantum Electron., vol. 27, no. 6, pp. 1–15, Nov. 2021.   
[13] T. Horiguchi, Y. Masui, and M. Zan, “Analysis of phase-shift pulse Brillouin optical time-domain reflectometry,” Sensors, vol. 19, no. 7, p. 1497, Mar. 2019.   
[14] S. B. Gorajoobi, A. Masoudi, and G. Brambilla, “Long range Ramanamplified distributed acoustic sensor based on spontaneous Brillouin scattering for large strain sensing,” Sensors, vol. 22, no. 5, p. 2047, Mar. 2022.   
[15] H. F. Pei, J. Teng, J.-H. Yin, and R. Chen, “A review of previous studies on the applications of optical fiber sensors in geotechnical health monitoring,” Measurement, vol. 58, pp. 207–214, Dec. 2014.   
[16] C.-Y. Hong, Y.-F. Zhang, G. W. Li, M.-X. Zhang, and Z.-X. Liu, “Recent progress of using Brillouin distributed fiber optic sensors for geotechnical health monitoring,” Sens. Actuators A, Phys., vol. 258, pp. 131–145, May 2017.

[17] H. Naruse and M. Tateda, “Trade-off between the spatial and the frequency resolutions in measuring the power spectrum of the Brillouin backscattered light in an optical fiber,” Appl. Opt., vol. 38, no. 31, pp. 6516–6521, Nov. 1999.   
[18] F. Rodríguez-Barrios et al., “Distributed Brillouin fiber sensor assisted by first-order Raman amplification,” J. Lightw. Technol., vol. 28, no. 15, pp. 2162–2172, Aug. 1, 2010.   
[19] M. N. Alahbabi, Y. T. Cho, and T. P. Newson, “150-km-range distributed temperature sensor based on coherent detection of spontaneous Brillouin backscatter and in-line Raman amplification,” J. Opt. Soc. Amer. B, Opt. Phys., vol. 22, no. 6, pp. 1321–1324, 2005.   
[20] X.-H. Jia et al., “Hybrid distributed Raman amplification combining random fiber laser based 2nd-order and low-noise LD based 1st-order pumping,” Opt. Exp., vol. 21, no. 21, pp. 24611–24619, 2013.   
[21] P. Clement, R. Gabet, V. Lanticq, and Y. Jaouën, “Enhancement of sensing range of Brillouin optical time-domain reflectometry system up to $1 5 0 \mathrm { k m }$ with in-line bi-directional erbium-doped fibre amplifications,” Electron. Lett., vol. 57, no. 3, pp. 142–144, Jan. 2021.   
[22] Y. Li, J. Wang, and Z. Yang, “A method for improving BOTDR system performance,” in Proc. Symp. Photon. Optoelectron., Shanghai, China, May 2012, pp. 1–4.   
[23] M. A. Soto, G. Bolognini, and F. D. Pasquale, “Analysis of optical pulse coding in spontaneous Brillouin-based distributed temperature sensors,” Opt. Exp., vol. 16, no. 23, pp. 19097–19111, Nov. 2008.   
[24] M. S. D. Zan, M. H. H. Mokhtar, M. M. Elgaud, A. A. A. Bakar, N. Arsad, and M. A. Mahdi, “Pulse coding technique in differential cross-spectrum BOTDR for improving the Brillouin frequency accuracy and spatial resolution,” in Proc. IEEE 8th Int. Conf. Photon. (ICP), Kota Bharu, Malaysia, May 2020, pp. 11–12.   
[25] Q. Wang, Q. Bai, C. Liang, Y. Wang, Y. Liu, and B. Jin, “Random coding method for SNR enhancement of BOTDR,” Opt. Exp., vol. 30, no. 7, pp. 11604–11618, Mar. 2022.   
[26] J. B. Rosolem, F. R. Bassan, D. E. de Freitas, and F. C. Salgado, “Raman DTS based on OTDR improved by using gain-controlled EDFA and preshaped simplex code,” IEEE Sensors J., vol. 17, no. 11, pp. 3346–3353, Jun. 2017.   
[27] F. Wang, C. Zhu, C. Cao, and X. Zhang, “Enhancing the performance of BOTDR based on the combination of FFT technique and complementary coding,” Opt. Exp., vol. 25, no. 4, pp. 3504–3513, Feb. 2017.   
[28] X. Sun et al., “Boosting the performance of distributed optical fiber sensors based on adaptive decoder,” in Proc. 26th Int. Conf. Opt. Fiber Sensors, Lausanne, Switzerland, 2018, pp. 1–4.   
[29] R. Liao et al., “Harnessing oversampling in correlation-coded OTDR,” Opt. Exp., vol. 27, no. 2, pp. 1693–1705, Jan. 2019.   
[30] Z. Li, Z. Yang, L. Yan, M. A. Soto, and L. Thevenaz, “Hybrid Golay-coded Brillouin optical time-domain analysis based on differential pulses,” Opt. Lett., vol. 43, no. 19, pp. 4574–4577, Sep. 2018.   
[31] M. A. Soto, P. K. Sahu, G. Bolognini, and F. Di Pasquale, “Brillouinbased distributed temperature sensor employing pulse coding,” IEEE Sensors J., vol. 8, no. 3, pp. 225–226, Mar. 2008.   
[32] M. Nazarathy et al., “Real-time long range complementary correlation optical time domain reflectometer,” J. Lightw. Technol., vol. 7, no. 1, pp. 24–38, Jan. 1989.   
[33] J. P. Bazzo, D. R. Pipa, C. Martelli, E. V. da Silva, and J. C. C. da Silva, “Improving spatial resolution of Raman DTS using total variation deconvolution,” IEEE Sensors J., vol. 16, no. 11, pp. 4425–4430, Jun. 2016.   
[34] S. Wang, Z. Yang, S. Zaslawski, and L. Thévenaz, “Short spatial resolutions retrieval from a long pulse BOTDA trace,” in Proc. 7th Eur. Workshop Opt. Fibre Sensors, Limassol, Cyprus, Aug. 2019, Art. no. 111992.   
[35] J. M. Bioucas-Dias, M. A. T. Figueiredo, and J. P. Oliveira, “Total variation-based image deconvolution: A majorization-minimization approach,” in Proc. IEEE Int. Conf. Acoust. Speed Signal Process., Toulouse, France, May 2006, pp. 861–864.   
[36] Y. Mei, X. Xu, L. Luo, and K. Soga, “Reconstruction of distributed strain profile using a weighted spectrum decomposition algorithm for Brillouin scattering based fiber optic sensor,” J. Lightw. Technol., vol. 38, no. 22, pp. 6385–6392, Nov. 15, 2020.   
[37] M. Song, Q. Xia, K. Feng, Y. Lu, and C. Yin, “100 km Brillouin optical time-domain reflectometer based on unidirectionally pumped Raman amplification,” Opt. Quantum Electron., vol. 48, no. 1, p. 30, Jan. 2016.

Yiqi Li received the B.S. degree from the School of Optical and Electronic Information, Huazhong University of Science and Technology (HUST), Wuhan, China, in 2019, where she is currently pursuing the master’s degree. Her research interests is optical fiber sensors.

Hao Wu received the B.S., M.Eng., and Ph.D. degrees from the School of Optical and Electronic Information, Huazhong University of Science and Technology (HUST), Wuhan, China, in 2013, 2016, and 2019, respectively. He has been working as a Postdoctoral Researcher at HUST since 2019. His current research interests include the application of specialty optical fiber and machine learning algorithm in distributed optical fiber sensing.

Can Zhao received the B.S. and Ph.D. degrees from the School of Optical and Electronic Information, Huazhong University of Science and Technology (HUST), Wuhan, China, in 2014 and 2019, respectively. He has been working as a Postdoctoral Researcher at HUST since 2019. His current research interests include distributed optical fiber sensing and specialty optical fiber.

Ming Tang (Senior Member, IEEE) received the B.E. degree from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technological University, Singapore, in 2005. His postdoctoral research at the Network Technology Research Centre (NTRC) was focused on optical fiber amplifiers, highpower fiber lasers, nonlinear fiber optics, and all-optical signal processing. In February 2009, he was with the Tera-Photonics Group led by Prof. Hiromasa Ito at RIKEN, Sendai, Japan, as a Research Scientist conducting research on terahertz-wave generation, detection, and application using nonlinear optical technologies. Since March 2011, he has been a Professor with the Wuhan National Laboratory for Optoelectronics (WNLO), School of Optical and Electronic Information, HUST. His current research interests are concerned with optical fiber-based linear and nonlinear effects for communication and sensing applications. He has been a member of the IEEE Photonics Society since 2001.