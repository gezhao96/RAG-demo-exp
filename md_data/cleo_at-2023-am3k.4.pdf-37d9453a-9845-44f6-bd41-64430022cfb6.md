# Single-ended Distributed Vibration Sensing Using Forward Polarization Detection of CW Light Based on (1+8) Multicore Fiber

Haoze Du, Huan He, Can Zhao, Mingming Zhang, Hao Wu, and Ming Tang*

Wuhan National Lab for Optoelectronics (WNLO) & National Engineering Laboratory for Next Generation Internet Access System, School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, 430074

*corresponding author: tangming@mail.hust.edu.cn

Abstract: A single-ended distributed vibration sensing system based on 3km 1+8 MCF is proposed and experimentally demonstrated. The vibration is located by calculating the time delay between the two cores by cross-correlation algorithm. $©$ 2023 The Author(s)

# 1. Introduction

Distributed fiber optic vibration sensing has been widely used in structure health monitoring [1], communication network monitoring [2], and many other application scenarios.

Distributed optical vibration sensing systems can be divided into two categories, one part is based on interferometer and the other part is based on optical time-domain reflectometry (OTDR) technology [3]. Among them, polarization detection technique has the advantages of relatively high sensitivity and low cost, promising merging applications in the existing fiber networks. Recently, an integrated polarization sensing scheme in a self-homodyne coherent transmission system is proposed [5]. This scheme employs an adaptive polarization controller to monitor the polarization variations along the entire communication fiber link. However, this solution cannot locate the position where the vibration occurs. The distributed sensing system based on polarization detection mainly adopts polarization OTDR [4]. But OTDR detects backscattered signal, restricting the sensing distance.

In this paper, we build a single-ended loop configuration DVS system using $1 { + } 8$ MCF (1 polarization-maintaining central core and 8 single-mode side cores) with the ability to locate the vibration. The loop is formed by connecting the central polarization-maintaining (PM) fiber core and the single-mode (SM) side core. The effect of vibration on the state of polarization (SOP) is measured by using polarizers and photoelectric detectors. The bidirectional continuous-wave (CW) optical signals are respectively injected from the two fiber cores, and the vibration position is located by collecting the time delay of the vibration signals.

# 2. Principle

The schematic of the proposed method is illustrated in Fig.1 (a). When vibration is applied to the fiber under test, the SOP of the PM core is stable while that of the SM core is changed. Using this feature, the loop structure is constructed. The time difference of the power fluctuation caused by the variation of the single-mode core is measured by polarizers and photoelectric detectors. The cross-section of the 1+8 MCF is shown in Fig.1 (b). This fiber was designed and fabricated for self-homodyne coherent system [6], the central core of the $1 { + } 8 \ \mathrm { M C F }$ is the panda polarizationmaintaining core, and the structure of the side cores is G657B3. The cladding of the 1+8 MCF is $1 5 0 \mu \mathrm { m }$ , and the pitch of side cores is $3 1 \mu \mathrm { m }$ .

![](images/75db8fefa5ca95d3efb75f3e52274c53336708f4774e360cad69f91ef2ceda36.jpg)

![](images/a920ea63d05aa3d6501ce7d0bcab74290ff0ce2e13cc463a27434aa120d71c66.jpg)  
Fig. 1. (a) Schematic of the proposed method (b) Cross-section of 1+8 MCF.

The CW light injected in the single-mode core is defined as the forward light, and the light injected in the polarization-maintaining core is defined as the backward light. When a vibration occurs at position Z, forward light will transmit through the fiber with length (L-Z) while backward light will transmit through length Z, then both of the lights are received by two different photoelectric detectors. The time delay is represented as $\Delta \mathfrak { t }$ , then the vibration position Z can be calculated by:

$$
Z = L - \frac {c \Delta t}{2 n} \tag {1.1}
$$

# 3. Experimental Results

![](images/bf3391b3d712f3a375e9742273bc6d4f1214309d3a0c5a4294cf2e5a43550ea0.jpg)  
Fig. 2. (a) Single-ended distributed vibration sensing system based on $1 { + } 8$ MCF setup.

The proposed architecture using 1+8 MCF is illustrated in Fig. 2(a). A loop configuration consists of a central core and one side core. These two cores are connected at the end of $1 + 8$ MCF, and there is a polarizer between them to ensure that the light entering the PM core is linearly polarized. The transmission route of the forward light is indicated by the red line and the route of the backward light is indicated by the blue line. The length of the $1 { + } 8$ MCF measured by OTDR is $3 0 1 5 \mathrm { m }$ . The laser used in the experiment is a DFB laser working at wavelength of $1 5 4 9 . 3 2 5 \mathrm { n m }$ . The oscilloscope model is Tektronix MDO3104, of which the sampling rate is 100MHz and the total sampling window is 100ms. In the vibration test, the vibration position is set at the position $Z { = } 1 0 \mathrm { m }$ . The time-domain diagram of the twochannel optical signals is shown in Fig.3 (a) and Fig.3 (b). The correlation curve illustrated in Fig. 3(c) is obtained by cross-correlating the time-domain diagrams of the two signals. The inset in Fig. 3(c) presents the enlarged view around the correlation peaks. There are two correlation peaks in the inset, the second peak corresponds to a delay of $2 9 . 5 5 \mu \mathrm { s }$ . The vibration position $Z { = } 6 0 \mathrm { m }$ can be calculated according to equation (1.1), compared with the actual position, there is an error of $5 0 \mathrm { m }$ . The location accuracy is related with sampling rate, and the accuracy with 100MHz sampling rate is 1m. The first correlation peak around 0 may be caused by the PM core failing to maintain the polarization state due to excessive vibration.

![](images/6a3016fd88b1b20db50d74c80302d347446029349876a289799761028d605c9b.jpg)

![](images/06528865d13b905ed42c6833fea36114d79eb813acae68045549efc3a6dd6be4.jpg)

![](images/2ab316cf8e167fd6448e97c1abc48b334e57b41f887e4b37e1acd58e8bdddad4.jpg)  
Fig. 3. (a) (b) Time domain diagram forward light of and backward light; (c) Cross-correlation spectrum of the two sets of data, and the inset shows the enlarged view around the correlation peak.

In summary, we have experimentally demonstrated a single-ended distributed vibration sensing system using polarization detection based on 1+8 MCF. The results show that the SOPs of the central core and the side core have different sensitivities to vibration. This feature can be used to construct a single-ended loop structure to locate vibration in the actual environment. The 1+8 MCF has been proven suitable for the self-homodyne coherent system, and this verification paves the way to utilize this $1 + 8$ MCF practically for joint communication and sensing.

# 4. Acknowledgement

This work was supported by National Key R&D Program of China under Grant 2021YFB2800902, National Natural Science Foundation of China under Grant 62225110, and innovation Fund of WNLO.

# 5. References

[1] Adewuyi, A.P., et al, Struct. Health Monit., 8, 443–461 (2009).   
[2] X. Li, et al, J. Lightw.Technol., 30 (8),1113–1119, (2012).   
[3] X. Liu, et al, Sensors, 16 (8), Art. no. 1164, (2016).

[4] C. Wang, et al, in IEEE Photon. J. 8 (2), 1-14, (2016).   
[5] Y. Zeng, et al, Opt. Lett. 47, 4684-4687 (2022)   
[6] T. Gui, et al, in OFC 2022, paper Th4C.1.