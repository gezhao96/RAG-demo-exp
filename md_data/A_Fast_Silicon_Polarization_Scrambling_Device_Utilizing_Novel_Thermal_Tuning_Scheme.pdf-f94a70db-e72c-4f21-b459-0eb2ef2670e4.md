# A Fast Silicon Polarization Scrambling Device Utilizing Novel Thermal Tuning Scheme

Weiqin Wang

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: 893614085@qq.com

Ziwen Zhou

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: zhouziwen@hust.edu.cn

Yifan Zeng

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: zengyifanhust@qq.com

Yining Sun

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: u202114836@hust.edu.cn

Hao Wu

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: 2019507013@hust.edu.cn

Siqi Yan*

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: *siqya@hust.edu.cn

Ming Tang

School of Optical and Electronic

Information and Wuhan National

Laboratory for Optoelectronics,

Optics Valley Laboratory

Huazhong University of Science and

Technology

Wuhan, China

e-mail: tangming@mail.hust.edu.cn

Abstract—The polarization management device plays a crucial role in high-speed optical communication systems. In this study, we focus on a polarization scrambling device that effectively perturbs polarization and is commonly employed to assess polarization-related parameters in high-speed optical communication systems. Through an innovative design of a new heater placement scheme, we have achieved a significant enhancement in the thermal adjustment response speed. Consequently, we present the development of a silicon-based rapid polarization scrambling device with a scrambling rate of 150 krads-1, which is the fastest among the silicon-based devices, to the best of our knowledge. The device offers the advantages of compact size, cost-effectiveness, compatibility with the CMOS process, and automatic regulation of the polarization scrambling speed.

Keywords—silicon photonics, polarization management, thermal tuning

# I. INTRODUCTION

State of polarization (SOP), as a unique feature vector of light, has always played an important role in the related application fields of light[1]. Effective and fast management of the SOP is crucial in many fields, such as biomedicine, quantum communication, optical communication, etc [2]. The adoption of polarization management devices has gained considerable traction in these fields[3].

Polarization management based on the electro-optic effect using the lithium niobate photonic platform offers ultra-high response speeds and nanosecond-level continuous electro-

optic control. However, these devices have limitations due to their large size and high half wave voltage and fabrication complexity[4]. As a result, their application in optical communication and optical sensing fields is significantly restricted.

The polarization management device, utilizing silicon photonics integration, provides several key advantages, including low cost, continuous regulation, and compatibility with CMOS technology[5][6]. Compared with the lithium niobate electro-optic polarization management device with a fast response time, but high power consumption, large size, and high cost, employing silicon-based planar optical waveguides for polarization management proves to be a more cost-effective and practical solution compared to other methods. However, the response time of the silicon device is commonly limited by the slow thermal-tuning process employing the metallic heaters on the top of the silicon waveguide.

In this work, we successfully developed a fast polarization scrambling device on the silicon photonics platform. This device allows for adjustable and rapid changes in the state of polarization (SOP), covering all possible SOPs. This capability enables us to test the performance of highspeed optical communication systems under rapid SOP changes. Thanks to the innovative integration of metal microheaters on the side of the waveguide, eliminating the need for a thick silicon layer in traditional thermal tuning schemes, the scrambling rate is experimentally demonstrated

to be $1 5 0 \mathrm { \ k r a d / s }$ , which is the fastest among the silicon polarization device, to the best of our knowledge.

# II. DESIGN OF POLARIZATION SCRAMBLING DEVICE

# A. Principle of Polarization Scrambling Device

The silicon-based polarization scrambling device mainly consists of two TPSs and a $2 \times 2$ MZI, as shown in Figure 1,

![](images/44d3dbed63e483240fec3557fcb698d33f1837a1694926356f1e1c0e85cfebe1.jpg)  
Fig.1. Structural demonstration of polarzition scrambling device.

the first TPS serves as a $0 ^ { \circ }$ placed wave plate, which regulates the optical polarization around the Poincaré sphere S1 axis of rotation, The second TPS and two adjacent 3-dB couplers form a MZI that rotates the optical polarization around the S3 axis. The two TPSs separately make the injection polarization along the two axis of rotation in the Poincaré sphere, if the injection polarization is on the large circle where the S2-S3 coordinate axis is, it can be achieved the conversion of the particular polarization to arbitrary polarization, thereby achieving the polarization scrambling function.

# B. Design of TPS

In our study, we have integrated metal microheaters on the sides of the Si waveguide, as shown in Fig. 2. Using COMSOL software, we conducted simulations to determine the size and location of the metal heater and compared its response time and light field loss by simulating light and thermal fields.

![](images/71c23da2867f4c19e5f13a725786c917a438c3527492b921ec675abf6b7d7768.jpg)  
Fig.2. Cross section diagram of TPS.

By placing the heater closer to the waveguide center, the response time of the device will decrease, but the loss of the light field will increase. On the other hand, moving the heater away from the waveguide center will result in lesser light field loss but a longer response time.

Based on our analysis, we identified that when the length of the TI heater is $0 . 4 7 5 ~ \mu \mathrm { m }$ , the thickness is $0 . 1 \ \mu \mathrm { m }$ , and the distance between the heater and the waveguide edge $( \mathrm { W _ { g a p } } )$ is set to $0 . 5 ~ \mu \mathrm { m }$ , we achieved a favorable balance between response time and light field loss. This method maximizes the phase modulation rate and ultimately enhances the performance of the polarization scrambling device.

# III. CHARACTERIZATION OF POLARIZATION SCRAMBLING DEVICE

# A. Testing of TPS

We evaluated the performance of TPS using the MZI structure and prepared a unique MZI test structure for this purpose, as shown in Figure 4.(a) The test structure introduced an additional geometry of $2 0 \mu \mathrm { m }$ in the upper arm of the MZI.

Through this test structure, we conducted dynamic response testing of the new type of metal heaters. By entering a single wavelength continuous light of $1 5 5 0 ~ \mathrm { n m }$ in port 1 of the test device, we then use a signal generator to load a steep square-wave signal of a fixed frequency on both ends of the electrode, the range of its amplitude is expanded as $( 0 , \mathrm { ~ V } _ { \pi } )$ , which enables the light intensity of the testing device output plot to change periodically.

We then used a high-speed photodetector to convert the light intensity change signal of plot 1' into an electrical signal, which was further output to an oscilloscope for real-time detection. By analyzing the light intensity change of plot 1', we determined the response time of the heater. As depicted in Figure 4(b), under the charge of a $5 0 \mathrm { k H z }$ square-wave signal, the heater's downward response time (from $90 \%$ to $1 0 \%$ ) is $3 . 5 ~ \mu \mathrm { s }$ , while the upward response time (from $10 \%$ to $90 \%$ ) is $2 \ \mu \mathrm { s }$ . These results exhibit a high consistency with the previous simulation findings.

![](images/b3cda0da1ee05da17b1f731c2bf33b751b12983ba6ff52a5c4f70a49bf3737f5.jpg)

![](images/2bd55e1c7abacae6683c9b450987d5e3f89571826c8c461726c3e687f15ac1d3.jpg)  
Fig.4. (a) Physical diagram of MZI testing device. (b) Normalized response time test.

# B. Testing of Polarization Scrambling Device

An essential performance indicator of the polarization scrambling device is the polarization scrambling rate, which represents the rate of change of the state of polarization (SOP) on the surface of the Poincaré sphere. To assess this parameter, we have established a dedicated test system, as illustrated in Figure 5(a).

In this test setup, a tunable laser emits light with a wavelength of $1 5 5 0 \mathrm { n m }$ , which is directed through a polarizer

and a polarization controller before entering our polarization scrambling device. To effectively cover the entire Poincaré sphere with the SOP generated by the scrambling device, we apply two triangular waves with different frequencies to φ1 and $\varphi 2$ TPS, respectively. The optical signal is then converted to an electrical signal through a polarization beam splitter (PBS) and a photodetector (PD), which is further accessed by an oscilloscope. By observing the intensity change rate of one polarization state, we can determine the corresponding scrambling rate

To validate the accuracy of the test results, we compare them with the scrambling rate calculated using the scrambling rate formula, which is as follows:

$$
\text {S c r a m b l i n g} = \sqrt {\left(\varphi_ {1 r a n g e} \times f _ {\varphi_ {1}}\right) ^ {2} + \left(\varphi_ {2 r a n g e} \times f _ {\varphi_ {2}}\right) ^ {2}} \tag {1}
$$

Where φ1range and $\varphi _ { 2 r a n g e }$ are the phase shifting ranges of the $\Phi 1$ and $\boldsymbol { \Phi } 2$ phase shifters, respectively $f _ { \varphi I }$ and $f _ { \varphi 2 }$ are the frequencies of the triangle wave signals applied to $\Phi 1$ and $\boldsymbol { \Phi } 2$ phase shifters, respectively. Here, we set $\varphi _ { I r a n g e } { = } 4 \pi$ and φ2range $= 2 \pi$ . $f _ { \varphi I }$ and $f _ { \varphi 2 }$ equals $5 0 ~ \mathrm { k H z }$ and $7 2 ~ \mathrm { k H z }$ respectively. Scrambling rate $= 1 5 0 \mathrm { k r a d s ^ { - 1 } }$ is calculated according to the test results, as demonstrated in Figure 5(b). This is consistent with the scrambling rate calculated through the formula.

![](images/b4dd1f64dd9698372a9d8a7dc603c889fec6d473c31dd7440dc057a7c3986e38.jpg)

Fig.5. (a) Polarization scrambling device testing system. (b)   
![](images/af5f63c829dca23ec69d3398a4d66faffcf0d2a3e8a47920a4347ebf5570a12e.jpg)  
Normalization test results of polarization scrambling device testing.

# CONCLUSION

We have designed a polarization scrambling device on silicon platform using a new type of thermal tuning structure. By optimizing the response time of thermal tuning, we have achieved a high-speed polarization scrambling, with a polarization scrambling speed of up to 150 krads, which is currently the fastest reported silicon polarization scrambling device.

Moving forward, our future research will focus on optimizing and iterating the heater's materials and positioning. Additionally, we aim to design more advanced polarization management devices on silicon-based platforms, such as devices capable of arbitrary polarization generation and automatic polarization control. These polarization management devices have broader applications in nextgeneration optical communication, biomedical, Light Detection and Ranging(LiDAR), and other fields. Our goal is to further enhance the optical signal polarization management system on the silicon photonics platform, contributing to the advancement of related applications.

# REFERENCES

[1] Lin Z, Lin Y, Li H, et al. High-performance polarization management devices based on thin-film lithium niobate[J]. Light: Science & Applications, 2022, 11(1): 93, doi: 10.1038/s41377-022-00779-8.   
[2] Snik F, Craven-Jones J, Escuti M, et al. An overview of polarimetric sensing techniques and technology with applications to different research fields[J]. Polarization: measurement, analysis, and remote sensing XI, 2014, 9099: 48-67, doi: 10.1117/12.2053245.   
[3] Wang X, Jia Y, Guo X, et al. Silicon photonics integrated dynamic polarization controller[J]. Chinese Optics Letters, 2022, 20(4): 041301, doi: col-20-4-041301.   
[4] Noé R, Koch B, Mirvoda V. LiNbO3-based endless optical polarization control[C]//2016 21st European Conference on Networks and Optical Communications (Noc). IEEE, 2016: 162-167, doi: 10.1109/NOC.2016.7507006.   
[5] Ma M, Shoman H, Tang K, et al. Automated control algorithms for silicon photonic polarization receiver[J]. Optics Express, 2020, 28(2): 1885-1896, doi: 10.1364/OE.380121.   
[6] Velha P, Sorianello V, Preite M V, et al. Wide-band polarization controller for Si photonic integrated circuits[J]. Optics Letters, 2016, 41(24): 5656-5659, doi: ol-41-24-5656.