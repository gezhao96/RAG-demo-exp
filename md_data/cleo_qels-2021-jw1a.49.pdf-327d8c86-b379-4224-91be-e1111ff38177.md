# Half-Wave-Plate based Adaptive Polarization Controller

Xuefeng Wang, Yifan Zeng, Ruolin Liao, Li Shen, Can Zhao, Hao Wu, and Ming Tang*

Wuhan National Lab for Optoelectronics (WNLO) & National Engineering Laboratory for Next Generation Internet Access System,

School of Optics and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, 430074

*corresponding author: tangming@mail.hust.edu.cn

Abstract: We experimentally demonstrated an endlessly adaptive polarization controller based on a rotatable half-wave-plate on the lithium niobate platform. It is recommended to eliminate the carrier fading in a self-coherent communication system. $©$ 2021 The Author(s)

# 1. Introduction

The self-coherent communication system is regarded as a competitive solution for short-reach optical interconnects which has attracted much attention recently [1]. Thanks to the remotely delivered local oscillator (LO) and the information-bearing signal originated by the same laser from the transmitter, the impact of laser phase noise can be minimized and the frequency offset is omitted. Thus, it is allowed to use an un-cooled laser with large linewidth and the DSP algorithms could be simplified [2].

However, carrier fading exists due to the varying state of polarization (SOP) of the LO caused by the randomly distributed birefringence along the single-mode fiber (SMF) and the impact of the unstable environment. To stabilize the SOP, usually, a specially designed adaptive polarization controller (APC) is needed.

Generally, an APC composed by phase shifters sandwiching couplers which are electrically driven by a polarization tracking algorithm can transfer any SOP to the TE state [3]. However, the reset operations are needed once the driving signals reach the boundaries. To avoid the reset, more cascaded phase shifters sandwiching couplers are needed. As a result, power consumption, space, and algorithmic complexity increase exponentially. In [4], it can be concluded that at least five stages of phase shifters cascaded couplers are needed to stabilize the SOP.

On the other hand, using cascaded rotatable waveplates to form an APC is also a common solution. An endlessly rotatable arbitrary waveplate can be realized by a lithium niobate (LN) driven by two orthogonal electric fields. So, an APC composed by two quarter-wave-plates (QWP) sandwiching one half-wave-plate (HWP) can be easily realized. To simplify the structure, [5] uses two-stage waveplates to lock the SOP at the TE state. The first waveplate acts as an endlessly rotatable waveplate with an adjustable phase range of - $\boldsymbol { \cdot } \pi$ to $\pi _ { \ast }$ , which transfers the varying SOP into the circular SOP, the second one as a QWP, which transfers the circular SOP into the linear SOP.

It is interesting to note that the carrier fading in the coherent communication system occurs only when the intensity of one of the orthogonal polarized LO signals reaches zero, thus the tracking goal could be simplified from TE linear SOP to the state of $I _ { x } = I _ { y }$ , where $I _ { x }$ and $I _ { y }$ are the intensities of the orthogonally polarized light.

In this paper, we proposed to use only one stage waveplate acting as a rotatable HWP to stabilize the SOP to the state of $I _ { x } = I _ { y }$ . The scheme is verified experimentally using a LN polarization controller (LN-PC).

# 2. Theoretical foundation

$$
G _ {1 / 2} = \left[ \begin{array}{l l} \cos (2 \alpha) & \sin (2 \alpha) \\ \sin (2 \alpha) & - \cos (2 \alpha) \end{array} \right] = \left[ \begin{array}{l l} 1 & 0 \\ 0 & - 1 \end{array} \right] \left[ \begin{array}{l l} \cos (2 \alpha) & \sin (2 \alpha) \\ - \sin (2 \alpha) & \cos (2 \alpha) \end{array} \right] \tag {1}
$$

![](images/4779e2a6a9e2b60c44e2c051c3b714fa8451c20472bf24716316d0aef5d3dd61.jpg)

![](images/d2cf860e30af2a45d7420c091d63fdfa6626e3f597f1e3782a68903e6d1b704e.jpg)

![](images/84783858bac285d587adababcd94d85916fc45dfa0647f3f97927cb11a3e9396.jpg)  
Fig. 1. The SOP rotation function of an HWP.

The Jones matrix of an HWP can be expressed as Eq. (1), where $\alpha$ is the principal axis orientation of the HWP about the $x$ -axis shown in Fig. 1(b). It can be divided into two parts. The second part is a rotation matrix. It rotates the xoy coordinate counterclockwise by $2 \alpha$ to the coordinate $\xi o \eta ^ { \prime }$ . Then, the first part reverses the direction of the $\eta ^ { \star }$ -axis to $\eta \mathrm { . }$ -axis. So, an $\alpha$ is always to be found for the HWP to transfer any arbitrary input SOP $\pmb { { E } } _ { i x y }$ into the state

of $I _ { \xi } = I _ { \eta }$ . Figuratively speaking, the angle between the long or short axis of the ellipse trajectory of the SOP and the $\xi .$ -axis should be $4 5 ^ { \circ }$ . The SOP tracking process is also presented on the Poincare sphere shown in Fig. 1(c). The second part of Eq. (1) rotates an arbitrary SOP $\mathrm { P _ { 0 } }$ to $\mathrm { P _ { 1 } }$ around the $\mathrm { S } _ { 3 }$ -axis with an angle of $4 a$ . Then, the first part rotates $\mathrm { P _ { 1 } }$ by $\pi$ rad around the $\mathrm { S } _ { \mathrm { l } }$ -axis to $\mathrm { P } _ { 2 }$ . $\mathrm { P } _ { 2 }$ locates on the target circle where $\mathbf { S } _ { 1 } = 0$ i.e. $I _ { \xi } = I _ { \eta }$ .

# 3. Experiment setup and results

To verify the polarization tracking capability of the HWP model, experiments are carried out. The setup is shown in Fig. 2(a). The CW polarized light is generated by a laser (Koheras BASIK MIKRO E15) with less than $1 0 0 \mathrm { k H z }$ linewidth and 13 dBm output power. Its SOP is scrambled by a polarization scrambler (FIBERPRO MOTORIZED POLARIZATION CONTROLLER PC 1300) shown in Fig. 3(a). A commercial LN-PC (PC-B4-00-PFA-PFA) driven by an in-house developed driving circuit (Fig. 2(b)) is adopted to function as a rotatable HWP to tracking the SOP. The output light from the LN-PC is separated by a PBS into two parts, half of which are detected to form the feedback signals, and the other half parts are coupled into a PBC. Then, the SOP is analyzed by a polarization analyzer (General Photonics PolaDetect POD-101D).

![](images/0e90b9e77cffae6921c1ac74eed07c051a6c3ab35529b0189ab2ffc185af3576.jpg)

![](images/445882b253359e8edc223a0011589ef08e1818c7caf7d01e4a2e9e10528a72dc.jpg)  
Fig. 2. (a) The setup of the testing system for the half-wave-plate (HWP) based adaptive polarization controller (APC). (b) The in-house developed driving circuit of the LN-PC. (PS: polarization scrambler. LN-PC: lithium niobate polarization controller. PBS/PBC: polarization beam splitter/coupler. OS: optical splitter. PA: polarization analyzer.)

The two-channel feedback signals are $I _ { x }$ and $I _ { y }$ . And the feedback error signal $C _ { e } = I _ { x } - I _ { y }$ is used at the input of the polarization tracking algorithm that runs on an ARM platform (STM32F407VETG). The principal axis orientation $\alpha$ of the HWP is adjusted by controlling the two driving voltages $V _ { 1 }$ and $V _ { 2 }$ (Fig. 3(b)) to minimize $C _ { e }$ to around 0. Then the SOP is stabilized to the target circle (Fig. 3(c)) where $I _ { x } = I _ { y }$ (Fig. 3(d)) without reset.

![](images/4a14b9eb86fde57a22f5e564a3d53c9de19108b6a0cf760b274fc67ae36aaa1d.jpg)

![](images/9ea34474adc571e8d477948418369300474023b044dc1f95994711c006bdb50d.jpg)

![](images/5bc2419eacf606d8b7874831e870a78522956608755f0f2af5dd07b08d5516d3.jpg)

![](images/6bde24caa87f7f40723871d19260a361d8ef8bf51e57d5a7d13f30db291efa11.jpg)  
Fig. 3. Experiment results. (a) The scrambled SOP. (b) The control signals. (c) The stabilized SOP. (d) The intensities of the orthogonal polarization components of the output light.

In conclusion, we experimentally demonstrate an HWP based APC that endlessly stabilizes any SOP from a SMF into the state of $I _ { x } = I _ { y }$ . It is recommended to eliminate the carrier fading in a self-coherent communication system. The HWP can also be implemented by planar waveguide on the basis of the silicon platform [6] and the thin-film LN platform [7] for integration with the silicon photonic coherence receiver.

# Acknowledgment

National Key R&D Program of China 2018YFB1801205; NSFC under Grants 61722108 and 61931010.

# References

[1] Cheng, C. Xie, Y. Chen, X. Chen, M. Tang, and S. Fu, “Comparison of Coherent and IMDD Transceivers for Intra Datacenter Optical Interconnects,” in Optical Fiber Communication Conference (OFC) 2019 (2019), pp. W1F.2.   
[2] T. Gui, X. Wang, M. Tang, Y. Yu, Y. Lu, and L. Li, “Real-Time Demonstration of $6 0 0 \mathrm { G b } / \mathbf { s }$ DP-64QAM SelfHomodyne Coherent Bi-Direction Transmission with Un-Cooled DFB Laser,” in Optical Fiber Communication Conference Postdeadline Papers 2020 (2020), pp. Th4C.3.   
[3] M. Ma, K. Murray, M. Ye, S. Lin, Y. Wang, Z. Lu, H. Yun, R. Hu, N. A. F. Jaeger, and L. Chrostowski, “Silicon Photonic Polarization Receiver with Automated Stabilization for Arbitrary Input Polarizations,” in Conference on Lasers and Electro-Optics (2016), pp. STu4G.8.   
[4] P. Oswald and C. K. Madsen, “Deterministic Analysis of Endless Tuning of Polarization Controllers,” J. Lightw. Technol. 24(7), 2932 (2006).   
[5] B. Koch, A. Hidayat, H. Zhang, V. Mirvoda, M. Lichtinger, D. Sandel, and R. Noe, “Optical Endless Polarization Stabilization at 9 krad/s With FPGA-Based Controller,” 20(12), 961-963 (2008).   
[6] C. K. Madsen, P. Oswald, M. Cappuzzo, E. Chen, L. Gomez, A. Griffin, A. Kasper, E. Laskowski, L. Stulz, and A. Wong-Foy, “Reset-free integrated polarization controller using phase shifters,” IEEE Journal of Selected Topics in Quantum Electronics 11(2), 431-438 (2005).   
[7] C. Wang, M. Zhang, X. Chen, M. Bertrand, A. Shams-Ansari, S. Chandrasekhar, P. Winzer, and M. Lončar, “Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages,” Nature 562(7725), 101-104 (2018).