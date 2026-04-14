# Enhanced Raman Distributed Temperature Sensor Using a High Raman Gain Fiber

Guijiang Yang, Hao Wu , Zi Liang, Liang Wang , Senior Member, IEEE, Changjian $\mathsf { K e } ^ { \mathbb { \oplus } }$ , Member, IEEE, Zhenggang Lian , Qianqing Yu, Zuming Xia, Ming Tang, Senior Member, IEEE, and Deming Liu

Abstract-We have designed and fabricated a single-mode Raman gain fiber (RGF) and use it to experimentally demonstrate a Raman distributed temperature sensor (RDTS) for high-precision temperature measurement with low power consumption. We have performed simulation to analyze the impact of fluorine-doped inner cladding on the control of the acoustic field and suppression of stimulated Brillouin scattering (SBS), showing that the SBS threshold can be improved by 37dB at 6wt% fluorine-doping concentration. Taking advantage of high Raman gain, a maximum signal-tonoise ratio (SNR) improvement of 6dB has been realized by using RGF under the same pump power as by using singlemode fiber (SMF), and the temperature uncertainty at the fiber

end is enhanced from $\pmb { 0 . 9 } ^ { \circ } \pmb { \mathbb { C } }$ to $\pmb { 0 . 5 } ^ { \circ } \pmb { \mathbb { C } }$ . To achieve comparable sensing accuracy as that of SMF-based RDTS, our RGF-based RDTS only consumes half of the power, showing good energy efficiency. The magnitude of SNR and temperature uncertainty enhancement is limited by the relatively large fiber attenuation, but it can be further improved through optimization of the fiber design with high fluorine-doping concentration and graded index structure.

![](images/feaa948883c3bde826fed5780d115a5c7fa3a870e1564b747a0ea98874c0401a.jpg)  
RGF structure

![](images/79a11d567c16d6fa746d6d77962c1b7b90527dab5a8c5c6ea0bc14feca977532.jpg)  
Fabricated RGF

Index Terms-Fiber optics sensors, Raman scatering, distributed optical fiber sensors, Raman gain fiber.

# I. INTRODUCTION

R AMAN distributed temperature sensor (RDTS) basedon spontaneous Raman scattering (SpRS) and optical on spontaneous Raman scattring (SpRS） and optical time-domain reflectometry technology can obtain the temperature distribution along the entire fiber with high spatial and temperature resolution, so it has been widely used in lots of applications including oil and gas pipeline monitoring, high-power transmission cables monitoring, fire alarming and nuclear industry etc [1]–[7]. In RDTS system, a pulsed pump light is injected into the sensing fiber and interacts with the fiber medium molecules to generate Raman Stokes (S) light and anti-Stokes (AS) light through SpRS, and the temperature information can be demodulated from the ratio of the AS and S light intensities. However, the intensity of the SpRS is about

Manuscript received October 5, 2021; revised October 31, 2021; accepted October 31, 2021. Date of publication November 2, 2021; date of current version December 14, 2021. This work was supported in part by the National Natural Science Foundation of China under Grant 62005087 and in part by the Open Projects Foundation of Yangtze Optical Fibre and Cable Joint Stock Ltd., Company (YOFC) under Grant SKLD2006. The associate editor coordinating the review of this article and approving it for publication was Dr. Santosh Kumar. (Corresponding author: Liang Wang.)

Guijiang Yang, Hao Wu, Zi Liang, Liang Wang, Changjian Ke, Ming Tang, and Deming Liu are with the School of Optics and Electronic Information and the Wuhan National Laboratory for Optoelectronics (WNLO), Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: hustwl $@$ hust.edu.cn).

Zhenggang Lian, Qianqing Yu, and Zuming Xia are with Yangtze Optical Electronic Company Ltd., Wuhan 430205, China.

Digital Object Identifier 10.1109/JSEN.2021.3124906

60dB weaker than the peak power of the input pump pulse [8], and the signal is gradually depleted along the fiber due to the fiber attenuation. Thus, the signal-to-noise ratio (SNR) becomes low after some fiber transmission, limiting the temperature accuracy and sensing distance. Usually to evaluate the performance of a fiber temperature sensor, besides common parameters such as temperature accuracy and temperature sensing range, signal-to-noise ratio (SNR), sensing distance, spatial resolution, and measurement time are also very important in a distributed fiber temperature sensor. High SNR results in better sensing performance. One simple method to improve the SNR is using large pump power, which can enhance the backscattered Raman signals. But the maximum pump power is limited by the onset of fiber nonlinear effects dominated by the stimulated Raman scattering (SRS) [9]. Therefore, it is difficult to infinitely increase the input pump power for SNR improvement in the standard single mode fiber (SMF) based RDTS. Some advanced techniques such as optical pulse coding [10], [11], image denoising [12], difference sensitivetemperature compensation [13], optical amplification [14], Rayleigh noise suppression [15], [16], wavelet transform modulus maximum [17], partial window-based non-local means method [18], auto-correction method [19], deconvolution algorithm [20], [21] and dispersion compensation [22] have been proposed to improve the sensing performance. Recently deep learning for denoising has also been employed in SMF based RDTS system to improve the SNR [23]. Nevertheless, the above methods either bring additional complexity or increase

the system cost. By taking the advantage of high SRS threshold and large backscattering coefficient, multimode fiber (MMF) is commonly used as the sensing medium in RDTS system [24]. However, the intermodal dispersion of MMF leads to the deterioration of the spatial resolution, limiting the sensing distance of MMF based RDTS within 10km range. So MMF is mostly employed for short-distance temperature sensing. To avoid mode dispersion, few-mode fiber (FMF) operated in quasi-single mode is proposed [25], but exciting only the fundamental mode in FMF requires special and complicated coupling process, which is not convenient. Moreover, most of the commercial components for optical fiber systems are based on single-mode fiber operation, the use of FMF would waste many existing resources and the cost of using FMF often exceeds the sensors. On the other hand, most of the existing RDTS techniques reported until now, no matter what fibers are used, do not take the pump power consumption of the system into account. In view of energy crisis nowadays, energy-efficient solutions for RTDS are desirable, i.e. better sensing performance achieved with less power consumption.

In this paper, we design and fabricate a single-mode Raman Gain Fiber (RGF) to achieve enhanced RDTS which realizes high-precision measurement at lower power consumption. The RGF has a step-index depressed cladding structure with a germanium-doped silica core, a fluorine-doped silica inner cladding and a silica outer cladding. Optical and acoustic field coupling in the RGF is investigated through simulation, where high fluorine-doping concentration in the inner cladding is demonstrated to be effective to suppress the Brillouin scattering, which is detrimental to the RGF based RTDS. Under the same power consumption, the RTDS system using RGF achieves a maximum SNR improvement of 6dB when compared with using SMF. To offer comparable sensing accuracy, the RGF based RTDS system can reduce the power consumption by half. Since the RGF is operated in single mode, it uses the common single-mode fiber components without extra cost and complexity which exists in FMF, and it does not have the detrimental intermodal dispersion existing in MMF. Therefore, the RGF based RDTS is potential for longrange and cost-effective distributed temperature monitoring.

# II. RAMAN GAIN FIBER DESIGN AND FABRICATION

# A. RGF Design and Simulation

In the RDTS system, a pulsed pump light is injected into the fiber and is backscattered to generate AS light and S light through SpRS. The AS light is strongly dependent on the fiber temperature, while the S light is insensitive to the temperature. Usually the temperature information is extracted from the ratio of the AS and S light intensities to reduce measurement errors induced by light intensity fluctuations. The ratio is expressed as follows [23]:

$$
\begin{array}{l} A (z, T) = \frac {P _ {A S} (z , T)}{P _ {S} (z , T)} \\ = \frac {K _ {A S}}{K _ {S}} \cdot \left(\frac {v _ {A S}}{v _ {S}}\right) ^ {4} \cdot \exp \left(- \frac {h \Delta v}{k T}\right) \cdot e x p \left[ - \left(\alpha_ {A S} - \alpha_ {S}\right) z \right] \tag {1} \\ \end{array}
$$

where $P _ { A S } ( P _ { S } )$ , ${ \upsilon } _ { A S } ( \upsilon _ { S } )$ , $\alpha _ { A S } ( \alpha _ { S } )$ and $K _ { A S } ( K _ { S } )$ are the power, frequency, attenuation coefficient and scattering

![](images/348550ae5a973acdbee7b57ba41f64ab8128eb237f2f0e4d1ff748b77c052620.jpg)

![](images/bc47efe4a5f474abad86f5a09a28a0b6be26c53e2cf9343f029705043c224717.jpg)  
Fig. 1. (a) RGF structure and (b) refractive index profile. $\mathsf { n } _ { 1 }$ , n2, and n3 are refractive indices for the core, inner cladding and outer cladding, respectively; a and b are the corresponding size.

coefficient of AS light (S light). $\Delta v$ is the Raman frequency shift, $h$ is the Planck constant, and $k$ is the Boltzmann constant. The temperature $T$ is demodulated based on Eq. (1). The power of backscattered AS light generated at the fiber length $z$ can be expressed as [25]:

$$
P _ {A S} (z) = D F _ {A S} (T) g _ {A S} P _ {0} G (z) \exp \left[ - \left(\alpha_ {R} + \alpha_ {A S}\right) z \right] \tag {2}
$$

where $D$ is a constant factor and $F _ { A S }$ is the temperaturedependent factor, gAS is the Raman gain coefficient, $P _ { 0 }$ is the input pump power, $\alpha _ { R }$ is attenuation coefficient at pump light. $G ( z )$ is Raman gain within pulse length. We can see that the AS light power is proportional to the Raman gain $G ( z )$ given by

$$
G (z) = \exp \left[ \left(g _ {A S} P _ {p} (z) c \Delta t\right) / \left(2 n A _ {e f f}\right) \right] \tag {3}
$$

where $P _ { p } ( z )$ is the pump power at position z, c is the light velocity in vacuum, $\Delta t$ is the pulse width, $n$ is the refractive index in the fiber core, and $A _ { e f f }$ is the effective mode area. From Eq. (2) we can see that the AS light power is proportional to the Raman gain, and hence the SNR and temperature accuracy can be obviously enhanced if the Raman gain becomes larger, implying that under the same pump power below SRS threshold better sensing performance can be expected. In other words, less pump power is enough to obtain comparable sensing performance if high Raman gain is offered. In Eq. (3), $g _ { R } / A _ { e f f }$ depends on the characteristics of the optical fiber, thus by designing a fiber with larger $g _ { R } / A _ { e f f }$ one can increase the Raman gain to enhance the temperature sensing performance.

We design and fabricate such an RGF to achieve enhanced RDTS system with low power consumption and high sensing performance. The fiber structure and refractive index profile of RGF are shown in Fig. 1(a) and 1(b). We adopt a step-index depressed cladding structure with a fiber core, an inner cladding and an outer cladding. The silica core with a diameter of 2a is doped by using germanium to have high refractive index $\boldsymbol { \mathrm { n } } _ { 1 }$ , while the inner silica cladding with a thickness of b is doped by using fluorine to have low index n2. The outer pure silica cladding has an index of ${ \mathfrak { n } } _ { 3 }$ . In the core, high germanium- doping concentration is used to enhance the confinement of optical field and increase the numerical aperture to reduce $A _ { e f f }$ , so the Raman gain can be increased, but the fiber loss is also increased at the same time. Note that the increase in fiber loss due to germanium doping is relatively small compared to other materials for doping [26], and germanium-doped fiber whose fabrication technology is mature are better matched to standard single-mode fiber for

![](images/dc03369701bd7aef08bde1cf02c10b1c8c365a54267c3d074ce18d691151b538.jpg)

![](images/72ee2069655d437a8da709b77ea434c9fac3602436b2b32e2bf7b66931c85fe9.jpg)

![](images/f3580f1652c6314440681060c7d1c13934405e3d4426280cfaa71f63a9958c58.jpg)  
Fig. 2. (a) The effective mode area and acousto-optic coupling coefficient in the fiber core as a function of fluorine-doping concentration in the inner cladding; (b) & (c) acoustic velocity profile at 0.5wt% and 6wt% fluorinedoping concentration, respectively.

low-cost operation. A fluorine-doped inner cladding can help achieve small effective mode area at a relatively low germanium doping in the core, which is desirable to increase the Raman gain but make the fiber attenuation maintain at a low level. Meanwhile, we adopt a small core diameter of $4 \mu \mathrm { m }$ , which also reduces the effective mode area and increases the Raman gain while ensuring the single-mode condition at $1 5 5 0 \mathrm { n m }$ .

On the other hand, accompanying the increase of Raman gain, the Brillouin scattering will also get enhanced, which would deplete the pump energy and deteriorate the performance of RDTS. Hence it is desirable to optimize the fiber structure to suppress the Brillouin scattering. Researchers have shown that to increase the SBS threshold the key is to reduce the overlap between the optical wave and acoustic wave in the core region, and suggested that using a dopant with opposite effects on the optical index and acoustic index would be helpful for this [27]–[29]. Fluorine doping usually decreases the optical index but increases the acoustic index, so it is used in the inner cladding of the RGF, which should be optimized so as to guide the optical wave but anti-guide the acoustic wave in the core region, eliminating the interaction between them. Considering the requirement of high Raman gain, low fiber loss and single-mode operation, here we study the impact of fluorine-doping concentration of the inner cladding on the acousto-optic coupling coefficient by using COMSOL Multiphysics simulation. In the simulation, the fiber core/inner/outer diameters are $4 / 2 4 / 1 2 5 \mu \mathrm { m }$ , respectively. The germanium-doping concentration is $1 6 . 4 \mathrm { w t } \%$ , which is the same as our fabricated fiber. Fig. 2(a) shows both the effective mode area and acousto-optic coupling coefficient as a function of fluorine-doping concentration in the inner

cladding. The effective mode area in the fiber core gradually decreases as the fluorine-doping concentration increases since the confinement of optical field is enhanced at large relative core-cladding index difference, and accordingly the Raman gain would increase. So high fluorine doping can alleviate the germanium-doping concentration in the fiber core and hence reduce the fiber attenuation without compromise of the light confinement in the core. While the acousto-optic coupling coefficient suddenly drops to nearly zero when the fluorine-doping concentration is increased beyond $4 . 3 7 \mathrm { w t } \%$ , indicating that there is almost no interaction between optical wave and acoustic wave in the core region. This can be explained through the analysis of the acoustic velocity profile distribution. Fig. 2(b) and (c) give the simulated acoustic velocity profiles for $0 . 5 \mathrm { w t } \%$ and $6\mathrm { w t } \%$ fluorine-doping concentration, respectively. At low fluorine-doping concentration, the acoustic velocity in the core is smaller than that in the inner cladding; while at high fluorine-doping concentration it is opposite. This means at $6\mathrm { w t } \%$ fluorine-doping concentration the acoustic refractive index in the core is lower than that in the inner cladding, such that the fiber core could not support the guided acoustic modes, and the interaction between the optical wave and acoustic wave is minimized. Thus, the acoustooptic coupling coefficient decreases to zero, leading to the suppression of the Brillouin scattering.

We also perform simulation to study the optical and acoustic field distribution inside the fiber for the above two cases of fluorine-doping concentrations. Fig. 3(a1) and (a2) show the optical field and acoustic field intensity profiles in the cross section of the RGF when $0 . 5 \mathrm { w t } \%$ fluorine-doping concentration of inner cladding is used. We can see that only the fundamental optical mode $\left( \mathrm { L P _ { 0 1 } } \right)$ is guided in the core with an effective mode area of $1 6 . 2 \mu \mathrm { m } ^ { 2 }$ , which verifies the single-mode operation of the RGF. And the acoustic mode $\left( \mathrm { L } _ { 0 1 } \right)$ is also confined in the fiber core, which indicates that the optical and acoustic fields have some overlap within the core region. The mode distribution of the two fields shown in Fig. 3(a3) also proves their overlap in the core. The overlap of the two waves in the core region makes their interaction take place, leading to a large acousto-optic coupling coefficient $f _ { A }$ of 0.98. Large $f _ { A }$ implies the SBS suppression is not good enough. On the other hand, Fig. 3(b1) and (b2) plot the optical and acoustic field intensity profiles for high fluorine doping, where the doping level is $6\mathrm { w t } \%$ . Different from the result in Fig. 3(a2), the acoustic field is now guided in the inner cladding rather than in the core, due to lower acoustic refractive index in the core than in the inner cladding. This means that there is almost no overlap between the optical mode and acoustic mode in the core region, which is seen from the optical mode and acoustic mode distribution at the fiber cross section in Fig. 3(b3). It significantly reduces acoustooptic coupling efficiency. Thus, the acousto-optic coupling coefficient $f _ { A }$ at $6\mathrm { w t } \%$ fluorine-doping concentration is as low as $1 . 8 \times 1 0 ^ { - 4 }$ , which is over three orders smaller than that at $0 . 5 \mathrm { w t } \%$ fluorine-doping concentration. By comparing the two acousto-optic coupling coefficients, it can be seen that the acousto-optic coupling efficiency in the core region would be suppressed by 5444 times when the fluorine-doping

![](images/b695206d88915ed132447a349db1e1fc8321b7b8aeffe9ab08970506784c68f2.jpg)

![](images/1ad661297757389fb3e89ffd3b67b069489d0253430c764f3032f2383fed9f8d.jpg)

![](images/683fc4ab0e56fc433fbf3c465652922c27def726b114fad457eabae214045583.jpg)

![](images/33d08bf196c48e92309e039c7cc91de582c133b7ae6fd92cbe1cbbdd860a1892.jpg)

![](images/3e81169ddd163429ee6386ead89714ca83f7ba8278a75e008b763f815d0558e4.jpg)

![](images/4b1b872d87574e2359e110dbf7fd3dd20d954b05b5a725bf0416278891e55aa7.jpg)  
Fig. 3. (a1)-(a3) Optical field profile, acoustic field profile, and mode distribution at $0 . 5 \mathsf { w t \% }$ fluorine-doping concentration; (b1)-(b3) optical field profile, acoustic field profile, and mode distribution at 6wt% fluorinedoping concentration. $A _ { e f f }$ and $f _ { A }$ represent the effective mode area and acousto-optic coupling coefficient, respectively.

concentration increases from $0 . 5 \mathrm { w t } \%$ to $6\mathrm { w t } \%$ , which implies that the stimulated Brillouin scattering (SBS) threshold can be enhanced by 37dB in logarithm unit. This is desirable to eliminate the detrimental effect from SBS on the sensing performance of RGF based RDTS. Note that the optical mode $\mathrm { L P _ { 0 1 } }$ also excites other higher-order acoustic modes, but the acoustic mode $\mathrm { L _ { 0 1 } }$ is found to produce the main effect in the study.

# B. RGF Fabrication and Testing

According to the above analysis, the RGF is fabricated using the following process. The fiber preform is fabricated using the modified chemical vapor deposition (MCVD) method, where a fluorine-doped cladding was firstly deposited with 45 layers, and each of the layer has roughly $1 0 0 \mu \mathrm { m }$ in thickness. Secondly, the high germanium-doped core was deposited by precisely altering the basic parameters, i.e. dopant concentration, deposition layer thickness (core size), so as to enhance the nonlinear effect of fiber and improve the Raman gain coefficient. The deposited tube was finally collapsed into a rod preform via a hydrogen-oxygen burner. A $5 0 0 \mathrm { m m }$ preform in length is drawn into RGF, using a commercial fiber drawing tower. By controlling the drawing speed and temperature, the fiber diameter can be accurately controlled to ensure fiber consistency. Table I gives the measured fiber parameters

![](images/94d3880147490c130125fd5674fdbb1c62ef09774a0458e5e4ea493bd333a2d5.jpg)  
(a)

![](images/6314ff1c9d2cade905909fb8367520057a25b708e421cf99f9d9bda0938710de.jpg)  
(b)

![](images/0d1aa1f03f4adbd959fd69d785838e2a38aa9e0321079428ec51db937a893f12.jpg)  
(c)

![](images/e9b834e0e7394bc5e9fb1c173bb9ceddf98d4e635e92209fd7c08f0667bbeae7.jpg)  
(d)   
Fig. 4. (a) Optical field profile, (b) acoustic field profile, (c) mode distribution, and (d) acoustic velocity profile for our fabricated RGF with fluorine doping concentration of $0 . 6 4 \mathrm { w } \mathrm { t } \%$ .

TABLE I MEASURED PARAMETERS OF OUR RGF   

<table><tr><td>Parameter Name</td><td>Measurement result</td></tr><tr><td>Microscopic picture of RGF cross section</td><td></td></tr><tr><td>Core/Inner/Outer diameter</td><td>4/24/125 μm</td></tr><tr><td>Refractive index profile n1/n2/n3</td><td>1.4812/1.4542/1.4573</td></tr><tr><td>Effective mode area</td><td>18.62 μm²</td></tr><tr><td>Cut-off wavelength</td><td>1078.62 nm</td></tr><tr><td>Raman gain factor gR/Aeff</td><td>3.64 (W*km)¹</td></tr><tr><td>Transmission loss αR (@1550nm)</td><td>0.675 dB/km</td></tr><tr><td>SBS threshold (@1550nm, 1km)</td><td>15.2 dBm</td></tr><tr><td>SRS threshold (@1550nm, 1km)</td><td>37.7 dBm</td></tr></table>

of our RGF. The doping concentration of germanium and fluorine are $1 6 . 4 \mathrm { w t } \%$ and $0 . 6 4 \mathrm { w t } \%$ , respectively. The RGF has high numerical aperture of $0 . 2 8 \ \textcircled { a } 1 5 5 0 \mathrm { n m }$ , large relative core-cladding index difference of $1 . 8 \%$ and small effective mode area of $1 8 . 6 2 \mu \mathrm { m } ^ { 2 }$ . The small core diameter of $4 \mu \mathrm { m }$ makes $A _ { e f f }$ small while ensuring the single-mode condition at $1 5 5 0 \mathrm { n m }$ . The Raman gain factor is as high as 3.6 $4 ( \mathrm { W } { * } \mathrm { k m } ) ^ { - 1 }$ , which is more than four times larger than that of SMF (0.76 $( \mathbf { W * k m } ) ^ { - 1 }$ [25]). The fluorine-doping concentration of our RGF is not high due to the limitation of our fiber drawing technology. The SBS threshold for 1km and $2 . 9 \mathrm { k m }$ fiber length are measured to be $1 5 . 2 \mathrm { d B m }$ and 11dBm, respectively.

Based on COMSOL Multiphysics, Fig. 4 plots the optical field and acoustic field intensity profiles, mode distribution and acoustic velocity profile in the cross section of our fabricated RGF. The results are similar to those in Fig. 3(a1)-(a3), where the acoustic wave exists in the core region and interacts with the optical wave, making the SBS suppression not good enough. The SBS threshold of our RGF is measured to be 15.2dBm for 1km length. Higher fluorine-doping concen-

![](images/61c7c4503f5b5c11ab01dbe212e0f7a17cc114d7f8c3547537c0539aa519e642.jpg)  
Fig. 5. Experimental setup of the RDTS system. WDM, wavelength division multiplexing filter; APD, avalanche photodiode; DAQ, data acquisition; FUT, fiber under test.

tration can be achieved by optimizing the fluorine-doping process and hence improve the SBS threshold as indicated in Fig. 2 and 3. The transmission loss of $0 . 6 7 5 \mathrm { d B / k m }$ is relatively high due to the strong scattering from the highly germanium-doped core and MCVD induced central dip in the refractive index profile [26]. The transmission loss can be reduced by adopting graded-index structure and increasing the fluorine-doping concentration in the inner cladding to reduce the scattering at the core-cladding interface. Finer control and optimization of the fiber manufacturing process to eliminate the central dip in the refractive index profile is also effective to further reduce the fiber attenuation [26]. 1.645dB splicing loss with SMF is found due to the optical field mode mismatch between RGF and SMF, which can be minimized by optimizing the process of fusion taper splicing, such as using the fused biconical taper technology [30].

# III. RAMAN GAIN FIBER ENHANCED RDTS

# A. Experiment Setup

The experiment setup of RDTS is shown in Fig. 5. A pulse laser at $1 5 5 0 \mathrm { n m }$ with a pulse width of 30 ns is used as the laser source for RDTS. The backscattered Raman AS and S light from the fiber under test (FUT) are filtered and separated by using a wavelength division multiplexing (WDM) filter, which prevents the influence from other wavelengths such as Rayleigh scattered light and Brillouin scattered light. Raman AS and S light are then detected by two avalanche photodiodes (APDs), respectively. A data acquisition card (DAQ) at a sampling rate of $2 5 0 ~ \mathrm { M S a / s }$ is used to collect the data. Two FUTs are used for comparison, i.e. our RGF and standard single-mode fiber (SMF). The FUT is $2 . 9 \mathrm { k m }$ long with the last $5 0 \mathrm { m }$ section heated inside an oven. The signal is averaged by 60,000 times to improve the SNR.

# B. Experiment Result

At first, we make the input pump power at the same level for both RGF and SMF based RDTS systems. The peak power of the pump pulse is 30dBm, which is slightly below the SRS threshold of RGF. The oven temperature is set to be $7 0 \mathrm { { } ^ { \circ } C }$ . Fig. 6(a) shows the collected AS signal of RGF and SMF, respectively. Despite the fact that the AS signal of RGF decreases quickly due to higher transmission loss, it is always

![](images/e29c6d3ee7b4d72bb33a86c7829c48e324ca7c4228351f16c2161996dc6d1528.jpg)  
(a)

![](images/8c9316b72c40a8f8db9175a4a67bf9731ba86991428a03017fd706b6b4123bbb.jpg)  
(b)   
Fig. 6. (a) Backscattered AS signal and (b) SNR along the FUT under the same pump power below the SRS threshold of RGF.

stronger than that of SMF thanks to its high Raman gain. Hence the SNR using RGF is improved by 6dB at the fiber beginning and $2 . 7 \mathrm { d B }$ at the fiber end, respectively, as shown in Fig. 6(b).

Further improvement of the SNR can be achieved by optimizing the RGF design and fabrication to reduce its transmission loss. The corresponding measured temperature distributions are given in Fig. 7(a) and (b), where four oven temperatures are used for the demonstration, i.e. $4 0 ^ { \circ } \mathrm { C }$ , $5 0 ^ { \circ } \mathrm { C }$ , $6 0 ^ { \circ } \mathrm { C }$ and $7 0 ^ { \circ } \mathrm { C }$ . The insets show the temperature distribution near the FUT end, from which we can see that the measured temperature by using RGF has smaller fluctuations than that by using SMF since the RGF provides high SNR due to large Raman gain. Fig. 7(c) plots the temperature uncertainty calculated along the RGF and SMF, respectively, when the oven temperature is $7 0 \mathrm { { } ^ { \circ } C }$ . The dotted black lines are the fitted curves. The temperature uncertainty by using RGF is $0 . 5 ^ { \circ } \mathrm { C }$ at the FUT end compared to $0 . 9 ^ { \circ } \mathrm { C }$ of by using SMF, indicating 1.8 times accuracy enhancement under the same power consumption. The spatial resolution of the RGF and SMF based RDTS systems are compared in Fig. 8. The experimental spatial resolution is defined as the fiber length of the temperature transition region from $10 \%$ to $90 \%$ of the peak amplitude. Almost the same spatial resolution of 3m is observed by using RGF and SMF. Since our RGF is a single mode fiber, there is no deterioration in spatial resolution due to intermodal dispersion. Thus, it can definitely support longer sensing distance with better temperature accuracy after its transmission loss is further reduced by optimizing the fiber design and fabrication mentioned above.

We also compare the temperature measurement by using the RGF and SMF based RDTS at the input pump powers slightly below their respective SRS thresholds. The last $5 0 \mathrm { m }$ FUT is heated to $7 0 \mathrm { { } ^ { \circ } C }$ . Fig. 9(a) show the temperature distribution measured by using RGF and SMF, where the peak powers of the pump pulse for the RGF and SMF based RDTS are 30dBm and $3 3 \mathrm { d B m }$ , respectively. The temperature uncertainty is calculated along the FUT, as given in Fig. 9(b). It can be seen that the temperature uncertainty using RGF is slightly lower than that using SMF. At the end of FUT, temperature uncertainties of $0 . 5 0 ^ { \circ } \mathrm { C }$ and $0 . 5 2 ^ { \circ } \mathrm { C }$ are obtained for RGF and SMF, respectively. With almost half of the power consumption, the RGF based RDTS can achieve almost the same level of temperature accuracy as that of SMF based RDTS. Thus, the RGF-based RDTS system is definitely an energy-efficient choice for distributed temperature measurement. Note that

![](images/ac985dd8b3f479eae59dfe262bc1f839fc533ece339b25ac70db88659df227a7.jpg)  
(a)

![](images/223d4871785367e38381d938c3bd08da4f2610a454ea19fdd04511e17ac71c5d.jpg)  
(b)

![](images/347d26f997049bf6d6c7907b8eaab2d8076946ecb7ec372f27073b1677c81b54.jpg)  
(c)

![](images/d2684ce304b5defc9fe8a00bfd547504d0338fa808e9e13013f349eeb801d1eb.jpg)  
Fig. 7. (a) & (b) Measured temperature distribution by using RGF and SMF under the same input pump power; (c) temperature uncertainty calculated along the RGF and SMF.   
(a)

![](images/d54052eec7247b7997d38a898a4bb01540cb74aa44df3f681e249a981aaa1fbb.jpg)  
(b)   
Fig. 8. Spatial resolution of the (a) RGF and (b) SMF based RDTS systems.

compared with SMF the temperature uncertainty using RGF is slowly increasing along the fiber length, which is caused by the relatively large transmission loss. As mentioned above, the transmission loss can be reduced by adopting graded-index structure and decreasing the germanium doping level in the core while increasing the fluorine-doping level in the inner cladding.

In addition, we also concatenate a $2 . 9 \mathrm { k m \ R G F }$ to a $2 . 9 \mathrm { k m }$ SMF to form one FUT (SMF $^ +$ RGF link) and use the

![](images/545042e51f83c4a801b00fddfe2271bd78256c8cfcacb98fa4aa261f82141640.jpg)  
(a)

![](images/9656502a3eda1fdef21a87771b9a2e362fe6a4ee01ce82347671f451e511bf28.jpg)  
(b)

![](images/430052175f31adbc1b32a3914953ae47456bf9b46e89472bfbdaa4ad4422bba5.jpg)  
Fig. 9. (a) Measured temperature distribution by using RGF and SMF under the pump power levels slightly below their respective SRS thresholds; (b) temperature uncertainty calculated along the FUT.   
(a)

![](images/ec9d3c5a4b477946275fc4bfd93b915fa2c266131560038adfc5bcd58200aa4c.jpg)  
(b)   
Fig. 10. (a) Intensity and (b) SNR of AS light along SMF + RGF link and SMF link.

combined fiber link for temperature measurement. A separate 5.8km SMF (SMF link) is also tested for comparison. In the experiment, we make the intensity of the AS light the same at the beginning of each link. Fig.10 shows the intensity and SNR of AS light along the two links, respectively. As can be seen in Fig. 10(a), the AS light intensity is the same at the first 2.9km SMF section for both links, but it is greatly increased when entering the RGF section, and correspondingly the SNR is improved by 5.2dB. Thanks to the high Raman gain, the temperature uncertainty at the end of the $\mathbf { S M F } + \mathbf { R G F }$ link is enhanced to $0 . 6 ^ { \circ } \mathrm { C }$ , compared with $1 . 0 ^ { \circ } \mathrm { C }$ of the SMF link. Since RGF is a single-mode fiber, it can be easily concatenated to SMF to improve the final sensing accuracy of a DTS system if necessary.

# IV. CONCLUSION

In conclusion, we have designed and fabricated an RGF with high Raman gain factor and experimentally demonstrated

an enhanced RGF-based RDTS with low power consumption and high sensing precision. The RGF has a step-index depressed cladding structure, with a highly germanium-doped silica core. Through COMSOL Multiphysics, the interaction between optical field and acoustic field in the core region is simulated. The simulation results show that when the fluorinedoping concentration in the inner cladding is beyond $4 . 3 7 \mathrm { w t } \%$ , the acousto-optic coupling efficiency is greatly reduced, and the coupling coefficient at $6\mathrm { w t } \%$ fluorine-doping concentration is as low as $1 . 8 ~ \times ~ 1 0 ^ { - 4 }$ , improving the SBS threshold by 37dB, which is helpful in enhancing the performance of RDTS. Due to single mode operation, the RGF-based RDTS avoids intermodal dispersion and uses simple components. Under the same pump power, a maximum SNR improvement of 6dB has been achieved by using RGF when compared with using SMF. And the temperature uncertainty obtained at the end of RGF is 1.8 times better than that of SMF. For the same sensing accuracy, our RGF-based RDTS only requires half of the power consumption. Unlike other fiberbased temperature sensors such as fiber Bragg grating (FBG) sensors, Fabry-Perot interferometers (FPIs) and Mach-Zehnder interferometers (MZIs) [31]–[34] where only one point is sensed in most of the cases, our RGF based RDTS can realize distributed temperature sensing over a long distance with high temperature accuracy of $0 . 5 ^ { \circ } \mathrm { C }$ . Compared with non-fiber optical temperature sensors such as [35]–[39], the RGF based RDTS has the advantages of simple system structure with low cost and high stability in complicated monitoring situations, such as environment with strong electromagnetic interference and high corrosion. Through optimization of the RGF design and fabrication to reduce the transmission loss and suppress the SBS, the sensing distance can be further extended to tens of kilometers with enhanced temperature accuracy. We believe the RGF based RDTS can serve as an economical solution for high-performance temperature sensing in the future.

# REFERENCES

[1] T. Yamate, G. Fujisawa, and T. Ikegami, “Optical sensors for the exploration of oil and gas,” J. Lightw. Technol., vol. 35, no. 16, pp. 3538–3545, Aug. 15, 2017.   
[2] A. Datta, H. Mamidala, D. Venkitesh, and B. Srinivasan, “Referencefree real-time power line monitoring using distributed anti-Stokes Raman thermometry for smart power grids,” IEEE Sensors J., vol. 20, no. 13, pp. 7044–7052, Jul. 2020, doi: 10.1109/JSEN.2019.2961185.   
[3] J. Li et al., “Long-range Raman distributed fiber temperature sensor with early warning model for fire detection and prevention,” IEEE Sensors J., vol. 19, no. 10, pp. 3711–3717, May 2019.   
[4] A. Morana et al., “Performances of radiation-hardened single-ended Raman distributed temperature sensors using commercially available fibers,” IEEE Trans. Nucl. Sci., vol. 67, no. 1, pp. 305–311, Jan. 2020.   
[5] I. Toccafondo et al., “Raman distributed temperature sensing at CERN,” IEEE Photon. Technol. Lett., vol. 27, no. 20, pp. 2182–2185, Oct. 15, 2015, doi: 10.1109/LPT.2015.2456029.   
[6] A. Ukil, H. Braendle, and P. Krippner, “Distributed temperature sensing: Review of technology and applications,” IEEE Sensors J., vol. 12, no. 5, pp. 885–892, May 2012, doi: 10.1109/JSEN.2011.2162060.   
[7] A. Barrias, J. R. Casas, and S. Villalba, “A review of distributed optical fiber sensors for civil engineering applications,” Sensors, vol. 16, no. 5, p. 748, 2016.   
[8] M. A. Soto et al., “Raman-based distributed temperature sensor with 1 m spatial resolution over 26 km SMF using low-repetition-rate cyclic pulse coding,” Opt. Lett., vol. 36, no. 13, pp. 2557–2559, Jul. 2011.   
[9] M. Premaratne, “Analytical characterization of optical power and noise figure of forward pumped Raman amplifiers,” Opt. Exp., vol. 12, pp. 4235–4245 Sep. 2004.

[10] Y. S. Muanenda et al., “Advanced coding techniques for long-range Raman/BOTDA distributed strain and temperature measurements,” J. Lightw. Technol., vol. 34, no. 2, pp. 342–350, Jan. 15, 2016.   
[11] X. Sun et al., “Genetic-optimised aperiodic code for distributed optical fibre sensors,” Nature Commun., vol. 11, no. 1, pp. 1–11, 2020.   
[12] M. A. Soto, J. A. Ramírez, and L. Thévenaz, “Intensifying the response of distributed optical fibre sensors using 2D and 3D image restoration,” Nature Commun., vol. 7, no. 1, p. 10870, Apr. 2016.   
[13] J. Li et al., “High-accuracy distributed temperature measurement using difference sensitive-temperature compensation for Raman-based optical fiber sensing,” Opt. Exp., vol. 27, pp. 36183–36196 Dec. 2019.   
[14] X. Jia et al., “Experimental demonstration on 2.5-m spatial resolution and $1 ~ ^ { \circ } \mathrm { C }$ temperature uncertainty over long-distance BOTDA with combined Raman amplification and optical pulse coding,” IEEE Photon. Technol. Lett., vol. 23, no. 7, pp. 435–437, Apr. 1, 2011, doi: 10.1109/LPT.2011.2107551.   
[15] B. N. Sun et al., “Accuracy improvement of Raman distributed temperature sensors based on eliminating Rayleigh noise impact,” Opt. Commun., vol. 306, no. 306, pp. 117–120, Oct. 2013.   
[16] B. Yan et al., “Temperature accuracy and resolution improvement for a Raman distributed fiber-optics sensor by using the Rayleigh noise suppression method,” Appl. Opt., vol. 59, no. 1, pp. 22–27, Jan. 2020.   
[17] Z. Wang et al., “An improved denoising method in RDTS based on wavelet transform modulus maxima,” IEEE Sensors J., vol. 15, no. 2, pp. 1061–1067, Feb. 2015.   
[18] A. Malakzadeh, M. Didar, and M. Mansoursamaei, “SNR enhancement of a Raman distributed temperature sensor using partial window-based non local means method,” Opt. Quantum Electron., vol. 53, no. 3, pp. 1–14, Mar. 2021.   
[19] J. Li, B. Yan, M. Zhang, J. Zhang, L. Qiao, and T. Wang, “Autocorrection method for improving temperature stability in a longrange Raman fiber temperature sensor,” Appl. Opt., vol. 58, no. 1, pp. 37–42, 2019.   
[20] J. P. Bazzo, D. R. Pipa, C. Martelli, E. V. da Silva, and J. C. C. da Silva, “Improving spatial resolution of Raman DTS using total variation deconvolution,” IEEE Sensors J., vol. 16, no. 11, pp. 4425–4430, Jun. 2016, doi: 10.1109/JSEN.2016.2539279.   
[21] G. D. B. Vazquez, O. E. Martinez, and D. Kunik, “Distributed temperature sensing using cyclic pseudorandom sequences,” IEEE Sensors J., vol. 17, no. 6, pp. 1686–1691, Mar. 2017, doi: 10.1109/JSEN. 2016.2647206.   
[22] J. Li, Y. Xu, M. Zhang, J. Zhang, L. Qiao, and T. Wang, “Performance improvement in double-ended RDTS by suppressing the local external physics perturbation and intermodal dispersion,” Chin. Opt. Lett. vol. 17, no. 7, 2019, Art. no. 070602.   
[23] Z. Zhang, H. Wu, C. Zhao, and M. Tang, “High-performance Raman distributed temperature sensing powered by deep learning,” J. Lightw. Technol., vol. 39, no. 2, pp. 654–659, Jan. 15, 2021.   
[24] M. A. Farahani and T. Gogolla, “Spontaneous Raman scattering in optical fibers with modulated probe light for distributed temperature Raman remote sensing,” J. Lightw. Technol., vol. 17, no. 8, pp. 1379–1391, Aug. 1, 1999.   
[25] M. Wang et al., “Few-mode fiber based Raman distributed temperature sensing,” Opt. Exp., vol. 25, no. 5, pp. 4907–4916, 2017.   
[26] M. M. Bubnov et al., “On the origin of excess loss in highly ${ \mathrm { G e O } } _ { 2 }$ -doped single-mode MCVD fibers,” IEEE Photon. Technol. Lett., vol. 16, no. 8, pp. 1870–1872, Apr. 2004.   
[27] Y. Koyamada, S. Sato, S. Nakamura, H. Sotobayashi, and W. Chujo, “Simulating and designing Brillouin gain spectrum in single-mode fibers,” J. Lightw. Technol., vol. 22, no. 2, pp. 631–639, Mar. 30, 2004.   
[28] M. Li et al., “Fiber designs for reducing stimulated Brillouin scattering,” in Proc. Opt. Fiber Commun. Conf. Expo., 2006, pp. 1–4, Paper OTuA4.   
[29] W. Zou, Z. He, and K. Hotate, “Acoustic modal analysis and control in w-shaped triple-layer optical fibers with highly-germaniumdoped core and F-doped inner cladding,” Opt. Exp., vol. 16, no. 14, pp. 10006–10017, 2008.   
[30] S. Jiang, C. Liang, L. Ma, J. Xiong, W. Zhang, and Z. He, “Ultralow-loss broadband all-fiber mode selective couplers for MIMO-less MDM transmission,” J. Lightw. Technol., vol. 38, no. 8, pp. 2376–2382, Apr. 15, 2020.   
[31] Y. Bao, Y. Huang, M. Hoehler, and G. Chen, “Review of fiber optic sensors for structural fire engineering,” Sensors, vol. 19, no. 4, p. 877, Feb. 2019.   
[32] R.-J. Tong, Y. Zhao, H.-F. Hu, and J.-F. Qu, “Large measurement range and high sensitivity temperature sensor with FBG cascaded Mach–Zehnder interferometer,” Opt. Laser Technol., vol. 125, May 2020, Art. no. 106034.

[33] D. Yi, F. Liu, Y. Geng, X. Li, and X. Hong, “High-sensitivity and large-range fiber optic temperature sensor based on PDMS-coated Mach–Zehnder interferometer combined with FBG,” Opt. Exp., vol. 29, no. 12, pp. 18624–18633, 2021.   
[34] J. Li, Z. Li, J. Yang, Y. Zhang, and C. Ren, “Microfiber Fabry-Pérot interferometer used as a temperature sensor and an optical modulator,” Opt. Laser Technol., vol. 129, Sep. 2020, Art. no. 106296.   
[35] T. Huynh, “Fundamentals of thermal sensors,” in Thermal Sensors, C. M. Jha, Ed. New York, NY, USA: Springer, 2015.   
[36] L.-Y. Chiang, C.-T. Wang, T.-S. Lin, S. Pappert, and P. Yu, “Highly sensitive silicon photonic temperature sensor based on liquid crystal filled slot waveguide directional coupler,” Opt. Exp., vol. 28, pp. 29345–29356, Sep. 2020.   
[37] H. Zhao, A. Vomiero, and F. Rosei, “Tailoring the heterostructure of colloidal quantum dots for ratiometric optical nanothermometry,” Small, vol. 16, no. 28, Jul. 2020, Art. no. 2000804.   
[38] S. Liu et al., “High sensitive $\mathrm { L n } ^ { 3 + } / \mathrm { T m } ^ { 3 + } / \mathrm { Y b } ^ { 3 + }$ $( \mathrm { L n } ^ { 3 + } = \mathrm { H o } ^ { 3 + }$ , $\mathrm { E r } ^ { 3 + }$ ) tri-doped $\mathrm { B a } _ { 3 } \mathrm { Y } _ { 4 } \mathrm { O } _ { 9 }$ upconverting optical thermometric materials based on diverse thermal response from non-thermally coupled energy levels,” Ceram. Int., vol. 45, no. 1, pp. 1–10, Jan. 2019.   
[39] Y. Tong, W. Zhang, R. Wei, L. Chen, and H. Guo, $\mathbf { \ddot { \ s } N a _ { 2 } Y M g _ { 2 } ( V O _ { 4 } ) _ { 3 } } { \mathrm { . } } \mathbf { E r } ^ { 3 + }$ , ${ \mathrm { Y b } } ^ { 3 + }$ phosphors: Up-conversion and optical thermometry,” Ceram. Int., vol. 47, no. 2, pp. 2600–2606, Jan. 2021.

Liang Wang (Senior Member, IEEE) received the B.S. degree from the Huazhong University of Science and Technology, Wuhan, Hubei, China, in 2008, and the Ph.D. degree from The Chinese University of Hong Kong in 2013. He is currently a Professor at the School of Optics and Electronic Information and the Wuhan National Laboratory for Optoelectronics (WNLO), Huazhong University of Science and Technology. He has published over 100 papers in international journals and conferences, and served as an editor for several journals. His research area mainly focuses on distributed fiber sensors and devices.   
Changjian Ke (Member, IEEE) is currently a Professor at the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.   
Zhenggang Lian is currently the CTO at Yangtze Optical Electronic Company Ltd., Wuhan, China.   
Qianqing Yu is currently an Engineer at Yangtze Optical Electronic Company Ltd., Wuhan, China.   
Zuming Xia is currently an Engineer at Yangtze Optical Electronic Company Ltd., Wuhan, China.   
Ming Tang (Senior Member, IEEE) is currently a Professor at the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.   
Deming Liu is currently a Professor at the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.

Guijiang Yang is currently pursuing the Ph.D. degree with the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.

Hao Wu is currently a Postdoctoral Fellow at the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.

Zi Liang is pursuing the Ph.D. degree with the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.