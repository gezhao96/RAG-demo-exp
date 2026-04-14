# Distributed Temperature and Curvature Sensing Based on Raman Scattering in Few-Mode Fiber

Zhuyixiao Liu, Hao Wu , Haoze Du, Zhongyao Luo, and Ming Tang , Senior Member, IEEE

Abstract-We propose and experimentally demonstrate a distributed temperature and curvature sensing method based on spontaneous Raman backscattered lights in a few-mode optical fiber. A loop structure is used to demodulate the distributed temperature information using the Raman anti-Stokes (AS) scattering lights. And the fiber curvature is estimated by the loss of Raman Stokes (S) light. This system can measure temperature and curvature at the same position of the fiber simultaneously. The experimental results show that the temperature uncertainty and spatial resolution can reach up to $0 . 2 4 \cdot ^ { \circ } C$ and $1 . 8 ~ \mathsf { m }$ on 6 km sensing fiber. Besides, the maximum measurement error is 0.11 cm within the curvature measurement range of 0.5–3 cm.

![](images/7ec286a545ecbd6ca6fa3e0904e6a18ef70a6ef94e1451412de047a37e058034.jpg)

Index Terms- Distributed curvature sensing, distributed temperature sensing, Raman scatering.

# I. INTRODUCTION

D ISTRIBUTED optical fiber sensing takes optical fiberas the medium for signal detection and transmission, which can provide a variety of physical parameters distributed along with the optical fiber [1], [2]. Due to the advantages of extensive laying, anti-electromagnetic interference, and quick response, it has been widely used in bridges and viaducts, oil and gas pipelines, smart power grids, and other industrial fields [3], [4], [5]. Furthermore, because of the unique physical characteristics of optical fiber such as softness, flexibility, etc., distributed optical fiber sensing has better prospects than traditional detectors in the fields of curvature measurement [6] and shaping measurement [7].

In recent years, there is an increasing demand for accurate measurement of temperature and curvature in the application of real-time monitoring of environmental changes and structural health. Currently, the main technologies

Manuscript received 29 September 2022; accepted 9 October 2022. Date of publication 18 October 2022; date of current version 30 November 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1801002, in part by the National Natural Science Foundation of China under Grant 61722108 and Grant 61931010, in part by the Hubei Province Key Research and Development Program under Grant 2020BAA006, in part by the Hubei Province Technology Innovation Program under Grant 2019AAA059, and in part by the Wuhan Science and Technology Achievement Transformation Program under Grant 2018010403011330. The associate editor coordinating the review of this article and approving it for publication was Dr. Qiang Wu. (Corresponding author: Hao Wu.) The authors are with the School of Optics and Electronic Information and the Wuhan National Laboratory for Optoelectronics (WNLO), Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: wuhaoboom $@$ hust.edu.cn). Digital Object Identifier 10.1109/JSEN.2022.3213871

used are fiber Bragg grating (FBG) [8], [9], [10], Raman distributed fiber sensing (RDFS) [11], and Brillouin sensing technology [13], [14], [15].

As a multipoint sensor, FBG has a high-resolution and high measurement accuracy, but limited when applied in longrange and multiple areas. Moreover, both existing grating manufacturing methods, whether laser direct writing and ultraviolet exposure, may have a negative effect on fiber strength and lifetime. RDFS system are mainly used in temperature sensing applications due to Raman signal’s high sensitivity to temperature changes, which is the basis of the RDFS system. Brillouin sensing uses Brillouin frequency shift (BFS) to extract temperature or strain information (bending and torsion cause strain to the optical fiber). However, the crossdisturbance of temperature and strain is unavoidable in these techniques, which limits the reliability and practicality of the system for curvature sensing.

To solve the above problem and realize the simultaneous distributed temperature and curvature measurement, some sensing schemes have been proposed. For example, we have demonstrated a hybrid Raman optical time-domain reflectometer (ROTDR) and Brillouin optical time-domain analysis (BOTDA) system that uses the BFS variation to extract the curvature information [16]. The system uses few-mode fiber (FMF) as the sensing fiber and can achieve a curvature radius measurement range of 0.9–2.7 cm. We also demonstrated a BOTDA system based on ring core fiber (RCF) that measures curvature by analyzing the BFS and Brillouin gain spectrum (BGS) variation [17]. Due to the advantages of bending loss resistance of RCF, the system can realize high-sensitivity measurement in the curvature radius range of $0 . 5 { - } 1 . 5 ~ \mathrm { c m }$

with extreme bending conditions. The multicore fiber based on space division multiplexing (SDM) technology is also used for curvature sensing [18]. The channels in multicore fiber can be independent and have different BFS variations for bending. This feature can improve the accuracy of measurement results. However, the SDM system has many hardware limitations. It needs special multicore optical fiber and corresponding high-performance multiplexing and demultiplexing devices. Besides, the above methods require many turns of the fiber around the cylinder to observe significant BFS variation, which is very inconvenient in practical applications. The complexity of the system can not be ignored as well.

In this article, we propose and experimentally demonstrate a novel distributed simultaneous temperature and curvature sensing approach based only on Raman signals in FMF. The system uses ROTDR technology to collect backscattered Raman Stokes (S) and anti-Stokes (AS) signals. The temperature information can be extracted from two directions AS signals based on loop structure, while the curvature information is extracted by the S signals. In addition, we use the one-dimensional denoising convolutional neural network (1D-DnCNN) to improve the measurement performance [19].

# II. PRINCIPLE

# A. Temperature Measurement Method

In the Raman distributed temperature sensing (RDTS) system, due to the existence of spontaneous Raman scattering, backscattered S light with a central wavelength of $1 6 6 3 \ \mathrm { n m }$ and AS light with a central wavelength of $1 4 5 0 ~ \mathrm { n m }$ will be generated when a $1 5 5 0 \ \mathrm { n m }$ pulsed light is injected into the sensing fiber. For the RDTS system, the AS light, which is more sensitive to temperature, is mainly used to measure the temperature information. Currently, there are two typical temperature demodulation schemes, including selfdemodulation [20], [21] and dual-demodulation [22], [23]. Self-demodulation using only AS light can achieve higher temperature measurement accuracy. The dual-demodulation uses the ratio of AS light and S light [22] or Rayleigh light [23]. The S light and Rayleigh light are used as reference signals to correct the fiber loss, so the dual-demodulation can effectively avoid the impact of external physical interference. However, after long-time exposure to external environment and aging, the fiber attenuation coefficients $\alpha _ { \mathrm { a s } }$ of AS light and $\alpha _ { s }$ of S light would have a different change, resulting in a severe distortion in the temperature demodulation results. In response to this problem, a single-AS light modulation method based on a loop structure was proposed [24]. In this structure, the sensing fiber is laid in a loop structure or directly adopts a twin-core cable, and the uplink and downlink directions backscattered AS signals are collected by the optical switch. A reference fiber is used for temperature comparison before the sensing fiber, as shown in Fig. 1. Keeping the reference fiber at the reference temperature when measuring can accurately calibrate the measurement result of the entire sensing optical fiber in real time. Besides, S light has a greater bending loss than AS light, so the uncertainty of temperature measurement using only AS light is lower. The scheme can also omit the precalibration process and reduce

![](images/f3137c66983e08168599eb97fe0a01d402367484a422b686705e11ec39270fbd.jpg)  
Fig. 1. Schematic of temperature demodulation based on the loop structure.

the measurement error. The specific demodulation process is as follows: typically, the uplink Raman AS light in the sensing fiber can be expressed as [25]

$$
\phi_ {\mathrm {a b}} = \phi_ {o} \frac {K _ {\mathrm {a s}} v _ {\mathrm {a s}} ^ {4}}{\exp \left(\frac {h \Delta v}{k T (z)}\right) - 1} \times \exp \left[ - \left(\alpha_ {o} + \alpha_ {\mathrm {a s}}\right) z \right] \tag {1}
$$

where $\phi _ { \mathrm { a b } }$ are the uplink direction backscattering intensity of AS, $K _ { \mathrm { a s } }$ and $\upsilon _ { \mathrm { a s } }$ are the scattering coefficient and optical frequencies of AS respectively, $h$ is the Planck constant, $\Delta v$ is the Raman frequency shift of the fiber, $k$ is the Boltzmann’s constant, $T$ is the fiber temperature, $\alpha _ { o }$ is the attenuation of pump and $z$ is the scattering position. Similarly, the downlink AS light $\phi _ { \mathrm { a f } }$ is obtained by switching the optical switch

$$
\phi_ {\mathrm {a f}} = \phi_ {o} \frac {K _ {\mathrm {a s}} v _ {\mathrm {a s}} ^ {4}}{\exp \left(\frac {h \Delta v}{k T (z)}\right) - 1} \times \exp \left[ - \left(a _ {o} + a _ {\mathrm {a s}}\right) (L - z) \right] \tag {2}
$$

where $L$ is the length of the optical fiber. Take the geometric mean of the intensity in two directions to obtain

$$
G = \sqrt {\phi_ {\mathrm {a f}} \phi_ {\mathrm {a b}}} = \phi_ {o} \frac {K _ {\mathrm {a s}} v _ {\mathrm {a s}} ^ {4}}{\exp \left(\frac {h \Delta v}{k T (z)}\right) - 1} \times \exp \left[ - \left(\alpha_ {o} + \alpha_ {\mathrm {a s}}\right) L \right]. \tag {3}
$$

Before the formal measurement, the system still retains the precalibration process to eliminate the defects of the fiber itself such as splice loss or bending loss caused by the necessary coiling in the actual application of the fiber. Therefore, the normalized fiber precalibration coefficients need to be measured without applying any additional bending to the fiber

$$
G _ {N} = \sqrt {\frac {\phi_ {\mathrm {a f}} ^ {\mathrm {c}} \phi_ {\mathrm {b f}} ^ {\mathrm {c}}}{\phi_ {\mathrm {r a f}} ^ {\mathrm {c}} \phi_ {\mathrm {r b f}} ^ {\mathrm {c}}}} \tag {4}
$$

where the $\phi _ { \mathrm { a f } } ^ { \mathrm { c } }$ and $\phi _ { \mathrm { b f } } ^ { \mathrm { c } }$ are the downlink and uplink scattering intensity of the sensing fiber respectively. The $\phi _ { \mathrm { r a f } } ^ { \mathrm { c } }$ and $\phi _ { \mathrm { r b f } } ^ { \mathrm { c } }$ are the downlink and uplink scattering intensity of the reference fiber respectively. To calibrate the measurement temperature of the sensing fiber and eliminate the constant term in (3), we measure the downlink and uplink backscattering intensity of the reference fiber to obtain $G _ { \mathrm { r } }$ . The reference temperature is recorded as $T _ { \mathrm { r } }$ . To simplify the formula, we use $K$ to present the constant $h \Delta v / k$ . Finally, the temperature at z can be demodulated by combining the above formula

$$
T (z) = \frac {K}{\ln \left[ \frac {\left(\exp \left(K / T _ {\mathrm {r}}\right) - 1\right) G _ {\mathrm {r}} G _ {N}}{G} + 1 \right]}. \tag {5}
$$

![](images/f77fbcf2440521c331ecbf4687aa92b69c97a47a337521c87277906d63cc7bb9.jpg)  
Fig. 2. Measured refractive index profile of the FMF.

# B. Curvature MeasurementMethod

To realize the simultaneous and discriminative measurement of curvature and temperature, we use ROTDR technology to detect the loss characteristics of Raman S light to obtain the curvature information. Compared with AS light, S light intensity is less affected by temperature. Besides, S light has a large wavelength than AS light and Rayleigh backscattering light, and is easier to leak when the fiber is bent. For the sensing fiber, the standard single-mode fiber (SSMF) is insensitive to bending. As for the multimode fiber (MMF), only a few high-order modes respond to bending and the variation of bending loss is not significant. To solve this problem, this article adopts the FMF as the sensing fiber. As a compromise of using SSMF and MMF, the excited higher order modes in the FMF by full injection are unstable and easy to leak, which means the bending loss is greater than SSMF, and therefore we can achieve a large curvature measurement range while temperature sensing. The measured refractive index profile and the microscope image of the used FMF are shown in Fig. 2. The core diameter is $1 6 . 3 5 ~ \mu \mathrm { m }$ and the cladding diameter is $1 2 5 \ \mu \mathrm { m }$ . The numerical aperture (NA) is 0.17. Two modes of $\mathrm { L P _ { 0 1 } }$ and $\mathrm { L P _ { 1 1 } }$ can be stably transmitted over long distances.

Fig. 3 shows the principle of curvature signal demodulation. The curvature of the sensing fiber changes the effective scattering area and the luminous flux in the fiber, which in turn introduces a large loss. Therefore, when the bending of the external structure acts on the sensing fiber, the fiber loss gradually becomes larger as the curvature decreases. The uplink S light $\phi _ { \mathrm { s } }$ in the sensing fiber can be expressed as [19]

$$
\phi_ {\mathrm {s}} = \phi_ {o} \frac {K _ {\mathrm {s}} v _ {\mathrm {s}} ^ {4}}{1 - \exp \left(- \frac {h \Delta v}{k T (z)}\right)} \exp \left[ - \left(\alpha_ {o} + \alpha_ {\mathrm {s}}\right) z \right]. \tag {6}
$$

Therefore, the S light intensity ratio of the sensing fiber and the reference fiber can be obtained

$$
\frac {\phi_ {\mathrm {s}}}{\phi_ {\mathrm {r s}}} = \frac {1 - \exp \left(- \frac {h \Delta v}{k T _ {\mathrm {r}}}\right)}{1 - \exp \left(- \frac {h \Delta v}{k T (z)}\right)} \exp \left[ - \left(a _ {o} + a _ {\mathrm {s}}\right) (z - z _ {\mathrm {r}}) \right] \tag {7}
$$

where $z _ { \mathrm { r } }$ and $T _ { \mathrm { r } }$ represents the position and temperature of the reference fiber respectively. In this article, we define the introduced bending loss as the modulation coefficient $B \left( z , R \right)$ . Therefore, in the process of measuring curvature, when bending with radius $R$ is introduced at position z, the S

![](images/167498f12341ebd87dfe3e8176eb0b54827bcd08ac945b20a3b2a5e88f290083.jpg)  
Fig. 3. Schematic of curvature demodulation based on fiber loss.

light intensity ratio of the sensing fiber and the reference fiber becomes

$$
\frac {\phi_ {\mathrm {s}}}{\phi_ {\mathrm {r s}}} = B (z, R) \times \exp \left[ \left(\alpha_ {o} + \alpha_ {\mathrm {s}}\right) \left(z _ {\mathrm {r}} - z\right) \right] \frac {1 - \exp \left(- \frac {h \Delta v}{k T _ {\mathrm {r}}}\right)}{1 - \exp \left(- \frac {h \Delta v}{k T (z)}\right)}. \tag {8}
$$

Compared with AS light, S light is not sensitive to changes in temperature. However, when the ambient temperature changes greatly, the effect of temperature on the S light intensity cannot be ignored, which can be explicitly observed in Fig. 3 and (8). To avoid the influence of temperature on the measurement of curvature, it is necessary to demodulate the temperature first to obtain the temperature $T \left( z \right)$ of the entire sensing fiber and bring it into (8). In the previous precalibration stage for temperature measurement, we demodulated the temperature $T ^ { \mathrm { c } } \left( z \right)$ of the entire sensing fiber based on (5). At the same time, we also measured the S light intensity of the sensing fiber and the reference fiber $\phi _ { \mathrm { s } } ^ { \mathrm { c } }$ and $\phi _ { \mathrm { r s } } ^ { \mathrm { c } }$ respectively. The S light intensity ratio of the sensing fiber and the reference fiber in the previous precalibration stage can be obtained

$$
\frac {\phi_ {\mathrm {s}} ^ {\mathrm {c}}}{\phi_ {\mathrm {r s}} ^ {\mathrm {c}}} = \exp \left[ \left(a _ {o} + a _ {\mathrm {s}}\right) \left(z _ {\mathrm {r}} - z\right) \right] \frac {1 - \exp \left(- \frac {h \Delta v}{k T _ {\mathrm {r}}}\right)}{1 - \exp \left(- \frac {h \Delta v}{k T ^ {\mathrm {c}} (z)}\right)}. \tag {9}
$$

Finally, the bending loss can be demodulated by (8) and (9) as

$$
B (z, R) = \frac {\phi_ {\mathrm {s}} \phi_ {\mathrm {r s}} ^ {\mathrm {c}}}{\phi_ {\mathrm {r s}} \phi_ {\mathrm {s}} ^ {\mathrm {c}}} \frac {1 - \exp \left(- \frac {h \Delta v}{k T (z)}\right)}{1 - \exp \left(- \frac {h \Delta v}{k T ^ {\mathrm {c}} (z)}\right)}. \tag {10}
$$

To further evaluate the relationship between measured loss and bending radius, we need to fit the measured results. In general, the bending loss in optical fiber can be expressed as [26]

$$
\operatorname {L o s s} = \frac {2 . 1 7 W ^ {2}}{\beta a ^ {2} (1 + W)} \cdot \frac {U ^ {2}}{V ^ {2}} \exp [ 2 W - \frac {2}{3} (\frac {W ^ {3}}{\beta^ {2} a ^ {2}}) \frac {R}{a} ] \tag {11}
$$

where $U$ and $W$ are normalized lateral propagation constants. $a$ is the half-width of the fiber core region. $V$ is normalized frequency. $\beta$ is longitudinal propagation constant. The above parameters are the constants related to the structural parameters of the optical fiber. $R$ is the bending radius. The formula

![](images/c3b35df55726da61fc19f7353a62084bf2edd81a5f20042391d58444ec098099.jpg)  
Fig. 4. Temperature and curvature measurement experiment setup.

can be simplified to

$$
\operatorname {L o s s} = A \times B ^ {R} \tag {12}
$$

where A and $B$ are the constants related to the structural parameters of the optical fiber.

# C. Experimental Setup

The measurement temperature and curvature experiment have been performed, and the experimental setup is shown in Fig. 4.

The laser source outputs an optical pulse with a pulsewidth of 10 ns and a central wavelength of $1 5 5 0 \ \mathrm { n m }$ . The output power of the pulses is $0 . 6 \mathrm { \ m W } .$ . The laser source adopts direct modulation, and then the optical pulse enters the fiber through an optical circulator. The optical switch is used to change the port of the sensing fiber to receive signal light in the opposite direction. The sensing fiber adopts the FMF manufactured by YOFC and the total length of the fiber is nearly $6 ~ \mathrm { k m }$ . In this experiment, a full injection is employed, that is, the injected light spot is large enough to excite all guided modes inside the FMF. We fuse two sections of MMFs to both end of the FMF, and used a multimode laser source to excite as many guided modes in the FMF as possible. The length of the two MMFs are both near $2 0 \mathrm { \ c m }$ , and the core diameter is $6 2 . 5 \ \mu \mathrm { { m } }$ and the cladding diameter is $1 2 5 \ \mu \mathrm { m }$ . This method not only improves the sensitivity of the FMF to bending, but also makes the FMF compatible with the multimode ROTDR hardware and reduces its impact on temperature measurement. The backscattered light passing through the optical circulator enters the wavelength division multiplexer (WDM), which is used to filter out AS light and S light. Two low-noise avalanche photodetectors (APDs) collect AS light and S light respectively and transmit the electrical signals to a $2 5 0 ~ \mathrm { M S a / s }$ data acquisition card (DAQ). Finally, the signal is averaged 60 000 times and transmitted to a computer for further demodulation.

# III. EXPERIMENTAL RESULTS

# A. Temperature Measurement

In the temperature measurement experiment, the fiber under test is divided into the heating part and the bending part. We place a $2 0 – \mathrm { m }$ long fiber in the temperature box at $4 . 7 \ \mathrm { k m }$ and set the temperature to $2 3 ~ ^ { \circ } \mathrm { C }$ , $4 0 ~ ^ { \circ } \mathrm { C }$ , $5 5 ~ ^ { \circ } \mathrm { C }$ , and $7 0 ~ ^ { \circ } \mathrm { C }$ . At the same time, the reference fiber temperature is maintained at $2 3 ~ ^ { \circ } \mathrm { C }$ as the reference. To verify that the system can effectively avoid the interference of bending, the bending area

![](images/e88c3c3449e70b8bdc84f7bd56642aefd5797cd242d113e5ba62f9008ee95afc.jpg)  
Fig. 5. Distribution of raw AS light intensity.

![](images/78e88e50006cb8717c34a382e2835a55421eb15d605ede82fab03a1f6b18b9ac.jpg)  
Fig. 6. Raw temperature demodulation results.

is set at $1 0 0 ~ \mathrm { m }$ behind the heating area. The fiber is bent one turn with a radius of $1 . 5 ~ \mathrm { c m }$ .

The AS light intensity in both directions measured at $4 0 ~ ^ { \circ } \mathrm { C }$ is shown in Fig. 5. Raw-1 represents the uplink direction AS light intensity. Raw-2 represents the downlink direction AS light intensity and the curve in the figure has been a flip transformation. Gm represents the geometric mean of Raw-1 and Raw-2. The inset in Fig. 5 shows the increase in AS light intensity induced by temperature changes. At the same time, the AS light intensity in the bending segment has a step change. It can be observed from the figure that the step change in curves Raw-1 and Raw-2 has been canceled through geometric mean as shown in the Gm curve, with only the increased part excited by the temperature changes remained. On this basis, the temperature curve demodulated based on (5) is shown in Fig. 6, and the temperature change of the heating segment is shown in detail in the inset. The curve changes obviously at different temperatures, but the low signal-to-noise ratio of the system causes the demodulated temperature curve to fluctuate greatly.

To further reduce the interference of noise and improve the temperature measurement performance, we adopt the 1D-DnCNN [19] for data denoising. The 1D-DnCNN is a convolutional denoising neural network trained with a large amount of RDTS data, which can reduce the noise of the RDTS system more effectively than the wavelet denoising method. The temperature measurement curve after denoising is shown in Fig. 7, where the demodulated temperature fluctuation is significantly reduced. To accurately evaluate the performance of the system, the absolute difference between two times at intervals under the same environmental conditions is calculated. We define the quadratic function fit curve of

![](images/21352e4f0c2ba3104dd1b9d5d369ec81b6b9b05b2e9d12d23373676344db11e5.jpg)  
Fig. 7. Temperature demodulation results after 1D-DnCNN denoising.

![](images/e348031ce6d325c04f98f1e74ecfa6f2f0c17dcd8c2c2b256fa0878514a6739d.jpg)

![](images/2f6168c08f3676282e0639dff301bcdb6ff2c050aa508f468efcc3b65c53c211.jpg)  
Fig. 8. (a) Temperature uncertainty with raw data. (b) Temperature uncertainty with 1D-DnCNN denoising.

this difference as the temperature uncertainty and use it to characterize the performance of the system, which is shown in Fig. 8. Lower temperature uncertainty means better system measurement performance. The temperature uncertainty curve using the raw data is shown in Fig. 8(a), the maximum temperature uncertainty is $0 . 6 3 \ ^ { \circ } \mathrm { C }$ . In the contrast, the temperature uncertainty curve after 1D-DnCNN denoising is shown in Fig. 8(b), and the maximum temperature uncertainty decreased significantly to $0 . 2 4 ~ ^ { \circ } \mathrm { C }$ .

In addition, the 10 ns pulsewidth light source is used in the experiment, and the theoretical spatial resolution is $1 \textrm { m }$ . But in practical applications, the spatial resolution would

![](images/534a8f3b76d00742a32dffb0f7b6f533728986365243e8912b2a3a32351d40cb.jpg)

![](images/dc9c98d102aa1150544160d9b4495ed8327aeab9030e837915b2fcca0570f0a0.jpg)  
Fig. 9. (a) Bending loss demodulation results. (b) Relationship between bending loss and radius of curvature.

degrade due to fiber dispersion and other factors. In this article, the actual spatial resolution is defined as the spatial distance corresponding to the intensity from $10 \%$ to $90 \%$ in the temperature step response. Therefore, the spatial resolution of the system after denoising is $1 . 8 \mathrm { ~ m ~ }$ , which is the same as before denoising, indicating that 1D-DnCNN does not further degrade the spatial resolution of the system.

# B. Curvature Measurement

In the curvature measurement experiment, the same experimental configuration as the previous one is maintained. The temperature of the heating area is kept at $5 5 ~ ^ { \circ } \mathrm { C }$ . Then we bend the fiber one turn with radius of 0.5, 1.0, 1.5, 2.0, 2.6, and $3 . 0 \ \mathrm { c m }$ , respectively. The fiber is wound on the surface of a selected cylinder to create a circle, which is closer to the real application situation. Besides, we try not to apply additional tension to the fiber during the winding process. The bending loss demodulated by (10) is shown in Fig. 9(a), and it is obvious that the fiber loss gradually increases as the radius of curvature decreases. The fitting results based on (12) are shown in Fig. 9(b).

The data were fit with the nonlinear least square method. It can be observed that in the measurement range of $0 . 5 { - } 3 ~ \mathrm { c m }$ , the fitting relationship between the measured bending loss and

![](images/7eb8a359fe8453f7723ac7994511df63322ba323584f44ec7ebfb1e859f5371b.jpg)  
Fig. 10. Distribution of raw AS light intensity in the hybrid measurement.

![](images/6dc5b7e67c681df587b3681b03970110a02460bc4019fdecd2598c556b65c5f7.jpg)

![](images/387d8c1fc8ff85dfcc8648eb483bad428e877601644bbf2faa44a7cc416766d3.jpg)  
Fig. 11. Hybrid measurement experiment demodulation results. (a) Temperature results. (b) Curvature results.

the radius of curvature is consistent with the theoretical formula while the curve remains monotonic. The determination coefficient of the fitting can reach up to 0.97155. Besides, we collected 100 data points near the change of bending loss and calculated their standard deviation as the loss measurement error, and its corresponding maximum measurement error in the fit curve is $0 . 1 1 ~ \mathrm { c m }$ . This shows that in practical application, the curvature radius of the object can be measured by the demodulated bending loss.

# C. Hybrid Measurement

To demonstrate that the system can achieve simultaneous measurement of temperature and curvature at the same position, the heating part maintains the temperature at $5 0 ~ ^ { \circ } \mathrm { C }$ and simultaneously applies a bending with a radius of $1 . 0 \ \mathrm { c m }$ for testing. AS light intensity is shown in Fig. 10.

The inset in Fig. 10 shows that the uplink and downlink AS light curves in the heating area do have a step change induced by bending. But the geometric mean of the two can well offset the effect of bending. The demodulated temperature

and curvature results are shown in Fig. 11. It is proven that the system can simultaneously measure the temperature and curvature at the same position. The demodulated temperature is consistent with the set value. The set radius of curvature is $1 . 0 \ \mathrm { c m }$ and the demodulated bending loss is 1.96 dB. The radius of curvature corresponding to this loss in the fit curve is $1 . 0 3 ~ \mathrm { c m }$ , and the error is only $3 \%$ .

# IV. CONCLUSION

In conclusion, we have proposed and demonstrated a longrange distributed optical fiber sensor system that can measure temperature and curvature, simultaneously. The proposed system uses the Raman loop structure to detect temperature, which can effectively avoid the influence of external perturbation on the measurement result. In our experiments, the temperature uncertainty and spatial resolution can reach up to $0 . 2 4 ~ ^ { \circ } \mathrm { C }$ and $1 . 8 \mathrm { ~ m ~ }$ over $6 ~ \mathrm { k m }$ fiber. The curvature is detected using the fiber loss characteristics based on ROTDR technology with a measurement error of $0 . 1 1 ~ \mathrm { c m }$ . The fiber loss and the radius of curvature maintain a good fit relationship in the measurement range from 0.5 to $3 \ \mathrm { c m }$ , and the coefficient of determination can reach up to 0.97155. In addition, the system performance can be further improved using optimized FMF. The method proposed in this article has the characteristics of low cost, simple structure, and convenient operation, and can promote the application of related technologies in practical situations.

# REFERENCES

[1] J. P. Dakin, D. J. Pratt, G. W. Bibby, and J. N. Ross, “Distributed optical fibre Raman temperature sensor using a semiconductor light source and detector,” Electron. Lett., vol. 21, no. 13, pp. 569–570, Jun. 1985.   
[2] X. Bao and L. Chen, “Recent progress in distributed fiber optic sensors,” Sensors, vol. 12, no. 7, pp. 39–8601, Jul. 2012.   
[3] A. Barrias, J. Casas, and S. Villalba, “A review of distributed optical fiber sensors for civil engineering applications,” Sensors, vol. 16, no. 5, p. 748, May 2016.   
[4] T. Yamate, G. Fujisawa, and T. Ikegami, “Optical sensors for the exploration of oil and gas,” J. Lightw. Technol., vol. 35, no. 16, pp. 3538–3545, Aug. 15, 2017.   
[5] A. Datta, H. Mamidala, D. Venkitesh, and B. Srinivasan, “Referencefree real-time power line monitoring using distributed anti-Stokes Raman thermometry for smart power grids,” IEEE Sensors J., vol. 20, no. 13, pp. 7044–7052, Jul. 2020.   
[6] P. Geng et al., “Two-dimensional bending vector sensing based on spatial cascaded orthogonal long period fiber,” Opt. Exp., vol. 20, no. 27, pp. 28557–28562, Dec. 2012.   
[7] Z. Zhao, M. A. Soto, M. Tang, and L. Thévenaz, “Distributed shape sensing using Brillouin scattering in multi-core fibers,” Opt. Exp., vol. 24, no. 22, pp. 25211–25223, Oct. 2016.   
[8] B. Huang and X. Shu, “Ultra-compact strain- and temperatureinsensitive torsion sensor based on a line-by-line inscribed phase-shifted FBG,” Opt. Exp., vol. 24, no. 16, pp. 17670–17679, Aug. 2016.   
[9] C. Markos et al., “High-Tg TOPAS microstructured polymer optical fiber for fiber Bragg grating strain sensing at 110 degrees,” Opt. Exp., vol. 21, no. 4, pp. 4758–4765, Feb. 2013.   
[10] T. Hu, Y. Zhao, and A.-N. Song, “Fiber optic SPR sensor for refractive index and temperature measurement based on MMF-FBG-MMF structure,” Sens. Actuators B, Chem., vol. 237, pp. 521–525, Dec. 2016.   
[11] G. Bolognini, J. Park, M. A. Soto, N. Park, and F. Di Pasquale, “Analysis of distributed temperature sensing based on Raman scattering using OTDR coding and discrete Raman amplification,” Meas. Sci. Technol., vol. 18, no. 10, pp. 3211–3218, Oct. 2007.   
[12] M. A. Farahani and T. Gogolla, “Spontaneous Raman scattering in optical fibers with modulated probe light for distributed temperature Raman remote sensing,” J. Lightw. Technol., vol. 17, no. 8, pp. 1379–1391, Aug. 1, 1999.

[13] X. Bao and L. Chen, “Recent progress in Brillouin scattering based fiber sensors,” Sensors, vol. 11, no. 4, pp. 4152–4187, Apr. 2011.   
[14] M. A. Soto, G. Bolognini, F. Di Pasquale, and L. Thévenaz, “Simplexcoded BOTDA fiber sensor with 1 m spatial resolution over a $5 0 ~ \mathrm { k m }$ range,” Opt. Lett., vol. 35, no. 2, pp. 259–261, Jan. 2010.   
[15] A. Minardo, R. Bernini, and L. Zeni, “Bend-induced Brillouin frequency shift variation in a single-mode fiber,” IEEE Photon. Technol. Lett., vol. 25, no. 23, pp. 2362–2364, Dec. 1, 2013.   
[16] H. Wu et al., “Few-mode optical fiber based simultaneously distributed curvature and temperature sensing,” Opt. Exp., vol. 25, no. 11, pp. 12722–12732, May 2017.   
[17] L. Shen et al., “Distributed curvature sensing based on a bending lossresistant ring-core fiber,” Photon. Res., vol. 8, no. 2, pp. 165–174, Feb. 2020.   
[18] Z. Zhao et al., “Spatial-division multiplexed Brillouin distributed sensing based on a heterogeneous multicore fiber,” Opt. Lett., vol. 42, no. 1, pp. 171–174, Jan. 2017.   
[19] Z. Zhang, H. Wu, C. Zhao, and M. Tang, “High-performance Raman distributed temperature sensing powered by deep learning,” J. Lightw. Technol., vol. 39, no. 2, pp. 654–659, Jan. 15, 2021.   
[20] D. Hwang, D.-J. Yoon, I.-B. Kwon, D.-C. Seo, and Y. Chung, “Novel auto-correction method in a fiber-optic distributed-temperature sensor using reflected anti-Stokes Raman scattering,” Opt. Exp., vol. 18, no. 10, pp. 9747–9754, May 2010.   
[21] B. N. Sun et al., “Accuracy improvement of Raman distributed temperature sensors based on eliminating Rayleigh noise impact,” Opt. Commun., vol. 306, pp. 117–120, Oct. 2013.   
[22] B. G. Gorshkov, G. B. Gorshkov, and M. A. Taranov, “Simultaneous temperature and strain sensing using distributed Raman optical timedomain reflectometry,” Laser Phys. Lett., vol. 14, no. 1, Jan. 2017, Art. no. 015103.   
[23] J. Park et al., “Raman-based distributed temperature sensor with simplex coding and link optimization,” IEEE Photon. Technol. Lett., vol. 18, no. 17, pp. 1879–1881, Sep. 2006.   
[24] M. A. Soto, A. Signorini, T. Nannipieri, S. Faralli, and G. Bolognini, “High-performance Raman-based distributed fiber-optic sensing under a loop scheme using anti-Stokes light only,” IEEE Photon. Technol. Lett., vol. 23, no. 9, pp. 534–536, May 1, 2011.   
[25] Z. Wang, X. Sun, Q. Xue, Y. Wang, Y. Qi, and X. Wang, “An optical fiber-folded distributed temperature sensor based on Raman backscattering,” Opt. Laser Technol., vol. 93, pp. 224–227, Aug. 2017.   
[26] D. Liu, Fiber Optics. Beijing, China: Science Press, 2016, pp. 86–88.

Zhuyixiao Liu is currently pursuing the Ph.D. degree with the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.

Hao Wu received the B.S., M.S., and Ph.D. degrees in optical engineering from the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, in 2013, 2016, and 2019, respectively.

He has been working as a Postdoctoral Researcher with the Huazhong University of Science and Technology since 2019. His research interests include the application of special optical fiber and machine learning algorithm in distributed optical fiber sensing.

Haoze Du is currently pursuing the Ph.D. degree with the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.

Zhongyao Luo is currently pursuing the Ph.D. degree with the School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, Hubei, China.

Ming Tang (Senior Member, IEEE) received the B.E. degree from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technological University, Singapore, in 2005. His Postdoctoral Research at the Network Technology Research Centre (NTRC) was focused on optical fiber amplifiers, high-power fiber lasers, nonlinear fiber optics, and all-optical signal processing.

In February 2009, he was a Research Scientist with the Tera-Photonics Group, RIKEN, Sendai, Japan, led by Prof. Hiromasa Ito, conducting research on terahertz-wave generation, detection, and application using nonlinear optical technologies. Since March 2011, he has been a Professor with the Wuhan National Laboratory for Optoelectronics (WNLO), School of Optical and Electronic Information, HUST. His current research interests include optical fiber-based linear and nonlinear effects for communication and sensing applications.

Dr. Tang has been a member of the IEEE Photonics Society since 2001.