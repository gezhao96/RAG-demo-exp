# Reconfigurable Microwave Photonic Filter Based on Space-Division Multiplexing Powered by Artificial Neural Networks

Liang Huo , Hao Wu, Can Zhao , and Ming Tang , Senior Member, IEEE

Abstract—Space-division multiplexing (SDM) techniques bring new approaches for various applications in microwave photonic signal processing. In this work, an all-fiber reconfigurable microwave photonic filter (MPF) is realized based on SDM techniques using multicore fiber (MCF) and multimode fiber (MMF). The multimode interference (MMI) generated from the proposed MCF-MMF-MCF structure can be manipulated in dimensions of space and wavelength simultaneously, thus configuring the power distribution in all the taps of the MPF. The trained artificial neural network can accurately predict the operating wavelength and spatial input core for a target power distribution. In a low-cost, light-weight, and compact way, SDM fibers combined with MMI allow for greater flexibility and diversity in the response of the reconfigurable MPF.

Index Terms—Space-division multiplexing, multicore fiber, multimode fiber, microwave photonic filter, artificial neural network.

# I. INTRODUCTION

N RECENT years, in addition to in-depth research in optical fiber communication, space-division multiplexing (SDM) techniques have been introduced into microwave photonic (MWP) signal processing, with advantages of compactness, operation flexibility, and versatility [1]. SDM fibers like multicore fibers (MCFs) and few-mode fibers (FMFs) have been exploited to implement true time delay lines (TTDLs) in different configurations, combined with specialty fiber design [2]–[5], tapering techniques [6], and fiber gratings [7], [8]. Based on these TTDL implementations, various MWP signal processing applications can be achieved, such as microwave photonic filtering [6]–[9], arbitrary waveform generation [10], optical beamforming [11], and optoelectronic oscillation [12]–[14]. Among

Manuscript received June 18, 2021; revised September 1, 2021 and November 7, 2021; accepted May 4, 2022. Date of publication May 11, 2022; date of current version May 23, 2022. This work was supported in part by the National Key R&D Program of China under Grant 2018YFB1801205, in part by the National Natural Science Foundation of China under Grants 61931010 and 61722108, in part by the Hubei Province Key Research and Development Program under Grant 2020BAA006, and in part by the Innovation Fund of WNLO. (Corresponding author: Ming Tang.)

The authors are with the Wuhan National Lab for Optoelectronics (WNLO) & National Engineering Laboratory for Next Generation Internet Access System, School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: huoliang@hust.edu.cn; wuhaoboom@hust.edu.cn; zhao_can@hust.edu.cn; tangming@mail.hust.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSTQE.2022.3173077.

Digital Object Identifier 10.1109/JSTQE.2022.3173077

them, for the application of microwave photonic filters (MPFs), the existing SDM-fiber-based TTDL implementations are only controllable for the time delay, and they have not explored the multi-dimensional control for the tap coefficients of the MPF.

Besides, multimode fibers (MMFs) have been widely used in optical fiber transmission, sensing, and imaging systems. As a scattering medium, a single MMF can generate speckle patterns based on multimode interference (MMI). Therefore, MMFs can be used to realize a speckle-based spectrometer [15]–[19]. In order to enhance the operation bandwidth while ensuring high resolution, a kind of MMF spectrometer integrated with MCFs has been proposed [20]. The approach of SDM can multiply the bandwidth of the MMF spectrometer without sacrificing the resolution. However, MMFs combined with SDM techniques have not been explored in MWP signal processing yet. As the MMI can be changed in both dimensions of space and wavelength, which enables different output power distributions under various input conditions, it can be used to control the tap coefficients for the MPF. Because of the complexity of the MMI, it is difficult to give an accurate analytical solution to know the exact power distribution of specific output positions of the MMF. With the development of artificial neural networks (ANNs), complicated classification and regressing problems can be easily solved in a short response time, which can be a powerful tool for the analysis of complex MMI [21] determined by conditions of space and wavelength. Therefore, ANNs can quickly establish nonlinear mapping relationships between output power distributions and input conditions.

In this work, we propose a novel all-fiber configuration for a reconfigurable microwave photonic filter (MPF) based on MCF and MMF powered by ANNs. The proposed finite impulse response (FIR) MPF can be reconfigurable in both dimensions of operation wavelength and spatial input cores of the MCF, as the MCF-MMF-MCF structure can adjust the tap coefficients due to MMI. The ANN is composed of one input layer, six hidden layers, and one output layer, which are used to model the nonlinear relationships between the output amplitude-frequency curves of the proposed MPF and the input wavelength as well as the input core. After the ANN is trained by $7 5 \%$ of the measured dataset, the parameters of operation wavelength and spatial input core can be predicted when a target amplitude-frequency curve of the MPF is input. The mean absolute error (MAE) of the predicted operation wavelength is $0 . 0 9 \ \mathrm { n m }$ , and the accuracy of the predicted spatial input core is $100 \%$ . For experimental

![](images/9af4b21ff5560d160d7665efb6ffbe85cad8f86cbfb17578062af6ced8dd76b4.jpg)  
Fig. 1. Experimental setup for the proposed MCF-MMF-based MPF. VNA: vector network analyzer; ASE: amplified spontaneous emission; WSS: wavelengthselective switch; MZM: Mach–Zehnder modulator; RF: radio frequency; EDFA: erbium-doped fiber amplifier; VOA: variable optical attenuator; PD: photodiode.

validation, we input simulated amplitude-frequency curves to the trained ANN, and the output predicted parameters generate real MPF responses which are measured in good agreement with the target hence proves the robustness of our methodology.

# II. MATERIALS AND METHODS

# A. Experimental Setup

The experimental setup for the proposed MCF-MMF-based MPF is shown in Fig. 1. An amplified spontaneous emission (ASE) source, whose spectrum covers the $\mathrm { C + L }$ band, is connected with a wavelength-selective switch (WSS). The center wavelength and the bandwidth of the operation light can be tuned by the WSS. The light is then externally modulated by radio frequency (RF) signals in a Mach–Zehnder modulator (MZM). An erbium-doped fiber amplifier (EDFA) and a variable optical attenuator (VOA) are used to control the input power of the light. Then a $1 \times 8$ optical switch is used to choose the input core of the MCF by use of the fan-in multiplexer. After the light passes through the MCF-MMF-MCF structure, the seven output cores of the fan-out demultiplexer are connected to optical fiber delay lines with an equal interval of 5 ns in sequence, and they are combined by an $8 \times 1$ optical combiner. Finally, a vector network analyzer (VNA) is used to analyze the amplitude-frequency response of the proposed MPF.

# B. MCF-MMF-MCF Structure

The schematic of the MCF-MMF-MCF structure is also shown in Fig. 1, and the cross-section views of the MCF and the

MMF used in the proposed MPF are shown as insets. The MCF is a homogeneous seven-core single-mode fiber with a cladding diameter of $1 5 0 \mu \mathrm { m }$ and a core pitch of $4 2 \mu \mathrm { m }$ [6]. All the cores of the MCF are trench-assisted, which can effectively reduce the inter-core crosstalk. The length of each piece of MCF is 2 m long. The insertion losses of the fan-in/fan-out pair for each core of the MCF are below 2.5 dB, and the inter-core crosstalk of different cores in the MCF along with fan-in/fan-out devices are below −45 dB. The 10-cm-long MMF has a cladding diameter of $1 2 5 \ \mu \mathrm { m }$ and a core diameter of $1 0 5 \ \mu \mathrm { m }$ . The numerical aperture of the step-index MMF is 0.22. When the operation wavelength is located in C band, the total number of propagating modes in the MMF is estimated to be over 1000. We spliced the MCFs at both ends of the 10-cm-long MMF to form the MCF-MMF-MCF structure. This all-fiber structure combines both dimensions of space and wavelength for the regulation of the output power distribution in a compact way. Different operation wavelengths and spatial input positions to the MMF can excite different modes to form different MMIs resulting in various power distributions at the MMF output. If seven cores of the output MCF are utilized for constructing seven parallel delay lines, a 7-tap FIR-MPF can be formed and its transfer function $H ( w )$ can be written as

$$
H (w) = \sum_ {k = 0} ^ {6} a _ {k} e ^ {- j w \Delta T _ {k}} \tag {1}
$$

where $a _ { k }$ and $\triangle T _ { k }$ are the coefficient and time delay of the k-th tap respectively. Therefore, the MCF-MMF-MCF structure can be used to adjust the tap coefficients of the MPF, making

![](images/437e2f5f7ec0fb678a5e9b216c2138c0d1cfb628457ab72b080369f5b5bf3304.jpg)  
Fig. 2. Transmission spectra of all the seven output cores from the MCF-MMF-MCF structure under conditions of different input cores.

it reconfigurable in terms of wavelength and space dimensions simultaneously. The transmission spectra of all the seven output cores from the MCF-MMF-MCF structure under conditions of different input cores are shown in Fig. 2. It can be seen that the output MMI spectrum from each core behaves irregularly in an operation wavelength range larger than the nanometer scale.

# C. Fully-Connected Neural Network

In order to make the power distribution controllable, we need to know the law of power distribution under conditions of different wavelengths and input cores. However, it is difficult to give an explicit analytical solution due to the complex MMI, which can be changed by many internal and external factors such as the physical conditions of the fibers and the splicing conditions. The MCF-MMF-MCF structure can be regarded as a black box, and ANNs can model the complex nonlinear relationships between the output amplitude-frequency curves of the proposed MPF and the input wavelength as well as the input core. Therefore, when a target filtering curve is input, the ANN can provide predictions on the operation wavelength and input core to reconfigure the

![](images/85cee2f5bb14b9f076e69d051c0f3c0b105eaa620746241454732df0c928d6d8.jpg)  
Fig. 3. Architecture of the FCNN.

TABLE I HYPERPARAMETERS OF THE FCNN   

<table><tr><td>Hyperparameter</td><td>Value</td></tr><tr><td>Number of hidden layers</td><td>6</td></tr><tr><td>Number of neurons in the input layer</td><td>4001</td></tr><tr><td>Number of neurons in the Mth hidden layer</td><td>213-M</td></tr><tr><td>Number of neurons in the output layer</td><td>2</td></tr><tr><td>Batch size</td><td>64</td></tr><tr><td>Learning rate</td><td>3×10-4</td></tr></table>

TABLE II PERFORMANCE OF THE FCNN   

<table><tr><td>Result</td><td>Training data</td><td>Testing data</td></tr><tr><td>MAE of operation wavelength (nm)</td><td>0.10</td><td>0.09</td></tr><tr><td>Accuracy of input core (%)</td><td>99.78</td><td>100</td></tr></table>

proposed MPF, making the actual response and the target one as consistent as possible.

As mentioned above, the amplitude-frequency response curve of the MPF contains the information of all the tap coefficients, which are determined by the MMI. The information from both local and global features of the curve is well-suited to be extracted by a fully-connected neural network (FCNN) [22] [25]. Therefore, we use an FCNN to implement the nonlinear mapping function. The architecture of the FCNN is shown in Fig. 3. The input layer contains 4001 neurons, which correspond to 4001 sample points of the amplitude-frequency curves, and the output layer has two neurons, representing the operation wavelength and the input core. The hyperparameters of the FCNN are shown in Table I. The proposed FCNN has six hidden layers, and the M-th $\mathbf M = 1$ , 2, 3, 4, 5, 6) hidden layer has $2 ^ { 1 3 - \mathrm { M } }$ neurons. The batch size is set to 64, and the learning rate is $3 \times 1 0 ^ { - 4 }$ . The rectified linear unit (ReLU) is used as the activation function to introduce the nonlinearity.

# III. RESULTS AND DISCUSSION

We change the operation wavelength from 1530 nm to 1565 nm (with an interval of $0 . 2 { \mathrm { n m } } { \mathrm { , } }$ ) for each input core and collect the data of amplitude-frequency curves from the VNA. The normalized amplitude-frequency curves of the proposed MPF

![](images/bdbc36e2f98a19200e6ec22209b9c06ccbcbff2346e68f39753f1e0707826033.jpg)

![](images/91d185645bae4e8dcf6d112ce6e34b2263d6af433dfa349391fa82431197b5f3.jpg)

![](images/14dfeb98c12754965416ad07f3b4954542e4258b02e0be51b0a0283ba1aa985c.jpg)

![](images/25c92e3981837c718b2f8432c80efffec2d84125f0728d7d5d3f867182e9def2.jpg)

![](images/ae7c60e00a4a2a9a1a36624d4c2da5057082548b08c6ca15c1c399b9fef50d04.jpg)

![](images/bb9af889b36cae519ceda6f18dd9d0a57b337211fcfdf8944fe06858d9672d75.jpg)

![](images/0e421cb19d509556d47eda5c0cd02b90a6cc080b223298d899dbd895e0ca91a7.jpg)

![](images/ad511005935636d28fe10a8c33e5bc61dc667d29f02cfeb518846d6a90d0da22.jpg)  
Fig. 4. Normalized amplitude-frequency curves of the proposed MPF under conditions of different input cores and operation wavelengths: (a) input core 1; (b) input core 2; (c) input core 3; (d) input core 4; (e) input core 5; (f) input core 6; (g) input core 7.

under conditions of different input cores and operation wavelengths are shown in Fig. 4. Here, we number the operation wavelength from channel 1 to channel 176, starting at $1 5 3 0 \mathrm { n m }$ and ending at 1565 nm. The interval of the operation wavelength is $5 \ \mathrm { n m }$ in Fig. 4. Therefore, there are eight curves in each subfigure, showing significant differences under the conditions of different operation wavelengths and input cores. $7 5 \%$ of the data in the whole dataset are chosen randomly for training, while the remaining $2 5 \%$ are used for testing. The MAE is used to evaluate the accuracy of operation wavelength. The FCNN is trained for 1000 epochs, and during each epoch, the Adam optimizer is employed to optimize the network parameters [26]. The overall training time is 671 s. The FCNN is implemented by Pytorch deep learning framework on a personal computer with an AMD Ryzen 1950X 16-core processor and an NVIDIA GeForce GTX 1080 GPU.

As shown in Table Ⅱ, the MAE of the operation wavelength is $0 . 1 0 \ \mathrm { n m }$ for the training data and $0 . 0 9 \ \mathrm { n m }$ for the testing data, and the accuracy of the input core is $9 9 . 7 8 \%$ for the training data and $100 \%$ for the testing data. The main reason for prediction errors on operation wavelength and input core is the similarity of the amplitude-frequency curves corresponding to adjacent wavelength channels or input cores, which can be

reduced by improving the diversity of the frequency-amplitude response curves. When the operation wavelength changes below the sub-nanometer scale, the MMI in each core does not change rapidly with the operation wavelength. Sometimes the interference intensity remains stable in a certain wavelength range, making the amplitude-frequency response curves in this wavelength range highly similar. In this case, there will be a small deviation in the prediction of wavelength as the output of the FCNN is continuous for the predicted operation wavelength. In addition, in order to operate the proposed MPF system in the incoherent regime, the bandwidth of the operation light is set to be 0.2 nm by the WSS. As a result, there will be a spectral overlap when the interval between two adjacent operation wavelengths is less than $0 . 2 \ \mathrm { n m }$ , which makes the MMIs corresponding to the adjacent operation wavelengths with a high degree of similarity as well as the amplitude-frequency curves. Therefore, an absolute error of less than $0 . 1 \mathrm { n m }$ in the predicted wavelength is acceptable in the current system.

Furthermore, to verify the robustness of the proposed FCNN, we also use simulation data to make predictions of operation wavelength and input core and compare their response results. Firstly, we randomly generated four sets of simulation data based on (1) and sent them to the proposed FCNN to make predictions

![](images/143261afacf56ee69a81046b274563a63155f8692009f8a929c78ca68d4f487f.jpg)

![](images/756f3731366871ffda5865ae2b8289f7ffb414d36c4044b71d9bc7b7107f50db.jpg)

![](images/1889426c55b7b0655c3c4b2f59d4771f19638a1f2ed21864c249e8cb96d0a875.jpg)

![](images/28aa79a24557f698430051b362ddc3e5cd9b29f091351c7877fde0006473a5be.jpg)  
Fig. 5. Normalized amplitude-frequency curves of simulation and measured results: (a) input core 1, channel 45; (b) input core 4, channel 147; (c) input core 2, channel 5; (d) input core 1, channel 113.

of corresponding operation wavelength and input core. Then four sets of predicted operation conditions were applied to the practical system respectively to obtain the measured amplitudefrequency curves. If the simulation and measured results are in good agreement, it will demonstrate a good robustness of the FCNN and indicate that the proposed method can generate the practical filtering curve that is most similar to the target one in the current MPF system. As shown in Fig. 5, due to different input cores and operation wavelengths, the tap coefficients are changed as well as the equivalent number of samples. When the coefficients of several certain taps are much smaller than those of other taps, these taps can be ignored, therefore the number of effective taps will decrease from 7 and form different filtering curves. In Fig. 5(a) and (c), only 3 samples are combined to form a 3-tap MPF with different tap coefficients which results in different mainlobe-to-sidelobe suppression ratios (MSSRs). And the number of taps for Fig. 5(b) and (d) is 4 and 7 respectively.

However, in the current MPF system, constrained by the accuracy and range of operation wavelength and the limited spatial input positions (seven in the current case) to the MMF, it cannot generate completely arbitrary filtering curves. Therefore, the simulation setup is as close as the real experimental one. The predicted values of the input core and operation wavelength are fed into the practical system hence generate corresponding filtering curves as close as the expected target. Nevertheless, there will be defects in the practical filtering curves, which are caused by the noise and nonlinearity introduced by the devices in the proposed system. As shown in Fig. 5, there are some distortions between the simulation and measured results, which can be explained by the following two reasons: firstly, due to the implementation penalty of practical systems, it may not match the target curve perfectly; secondly, the distortions generated in the high-frequency part of the filtering curve could be attributed to the high-frequency fading introduced by the VNA and the MZM in the proposed system.

The main limitation of the MMI-based method is the susceptibility to environmental perturbations which can change the power distribution at the output end of the MMF. In our experiment, in order to prevent physical vibrations, we stuck the MCF-MMF-MCF structure onto a metal plate which was fixed on the optical shockproof platform. Besides, in order to prevent large changes in temperature, we kept the room temperature at $2 6 ~ ^ { \circ } \mathrm { C }$ during the experiment. Then we tested the same input conditions for the proposed MPF system at a time interval of 1h, $2 4 \mathrm { ~ h ~ }$ , and $4 8 \ \mathrm { h } .$ , and recorded these three sets of amplitudefrequency curves. The average correlations of all the three sets of data are over 0.9945, indicating the stability of the proposed MPF under the current experimental conditions. In addition, to further reduce the effect of environmental perturbations, such as mechanical vibrations and temperature fluctuations, on the MMI generated from the MCF-MMF-MCF structure, we can use good fixtures and temperature drift correction techniques as mentioned in [27], [28] to ensure the stability of the proposed MPF.

Besides, in order to make frequency-amplitude response curves more diverse and thus obtain arbitrary filtering shapes, we can make improvements from the following three aspects: firstly, to make the time delay difference between taps adjustable, tunable time delay lines can be connected to the output cores of the fan-out demultiplexer; secondly, to increase the number of taps, which is corresponding to the number of output cores, MCFs containing more cores can be chosen to replace the seven-core fiber we used in the proposed system; thirdly, multiple operation wavelengths and multiple spatial input cores can be considered to expand the parameter space. Meanwhile, the FCNN can predict multiple operation wavelengths, multiple spatial input cores, and time delay differences after retraining.

For FIR-MPFs, the amplitude-frequency curves are periodic, and the period is determined by the time delay difference between adjacent taps. Therefore, FIR-MPFs can also process microwave signals at high frequencies due to the periodic characteristic of filtering curves theoretically. However, the RF frequency processing range will be limited by the bandwidthlimited devices in the system, such as the RF signal generator, the electro-optic modulator, and the photodiode (PD). In our

proposed MPF, the measurable filter responses are limited by the bandwidth of the VNA, which is 6 GHz. The maximum number of sampling points of the VNA is 4001. We just presented the results whose frequency range is up to 1 GHz because the free spectral range (FSR) is only around $2 0 0 ~ \mathrm { M H z }$ , when the tap number increases, it may be hard to distinguish the details of the filtering curves due to the low resolution of the VNA which is limited by the operation bandwidth of the VNA. To extend the RF frequency processing range, we can use the VNA with higher resolution and higher bandwidth, as well as the Mach–Zehnder modulator and the PD. Besides, the FSR is determined by the time delay difference $T$ between adjacent taps $( \mathrm { F S R } = 1 / T )$ ), which is fixed to be 5 ns in our proposed MPF system. $T$ is determined by the length of the optical fiber delay lines. In order to increase the FSR of the filtering curve, we can shorten optical fiber delay lines or use other types of delay lines which can provide shorter time delay such as optical waveguide delay lines [29] and fiber Bragg grating arrays [30].

The target application for the proposed MPF is to be compatible with SDM fiber-wireless communication networks, where SDM fibers are used not only for signal distribution but also signal processing. For instance, the proposed MPF can be used for filtering microwave photonic signals with limited bandwidth such as single-tone or multi-tone RF oscillation signals which can be used for radar detection. Our proposed MPF can provide greater flexibility and diversity in the response of the reconfigurable MPF by controlling the tap coefficients based on MMI.

# IV. CONCLUSION

In conclusion, we propose an all-fiber reconfigurable FIR-MPF based on MCF and MMF. The reconfigurability of MPF can be realized in dimensions of wavelength and space simultaneously. With the aid of FCNN, we can predict the operation wavelength and spatial input core when a target amplitude-frequency curve is input. The testing results show that the MAE of the predicted operation wavelength is $0 . 0 9 \ \mathrm { n m }$ , and the accuracy of the predicted input core is $100 \%$ . Besides, simulation curves are used as input data to check the robustness of the FCNN, which ultimately show good agreement between simulation and measured results. We believe this all-fiber configuration based on SDM powered by FCNN will enhance the flexibility and diversity of reconfigurable MPFs with low cost, light weight, and compactness.

# REFERENCES

[1] S. García, R. Guillem, M. Ureña, and I. Gasulla, “Space-division multiplexing fibers for radiofrequency signal processing,” in Proc. IEEE Photon. Soc. Summer Topicals Meeting Ser., Cabo San Lucas, Mexico, 2020, pp. 1–2.   
[2] S. García and I. Gasulla, “Design of heterogeneous multicore fibers as sampled true-time delay lines,” Opt. Lett., vol. 40, no. 4, pp. 621–624, Feb. 2015.   
[3] S. García, R. Guillem, and I. Gasulla, “Ring-core few-mode fiber for tunable true time delay line operation,” Opt. Exp., vol. 27, no. 22, pp. 31773–31782, Oct. 2019.   
[4] S. Shaheen, I. Gris-Sánchez, and I. Gasulla, “True-time delay line based on dispersion-flattened 19-core photonic crystal fiber,” J. Lightw. Technol., vol. 38, no. 22, pp. 6237–6246, Nov. 2020.

[5] E. Nazemosadat and I. Gasulla, “Dispersion-tailored few-mode fiber design for tunable microwave photonic signal processing,” Opt. Exp., vol. 28, no. 24, pp. 37015–37025, Nov. 2020.   
[6] L. Huo et al., “IIR microwave photonic filters based on homogeneous multicore fibers,” J. Lightw. Technol., vol. 36, no. 19, pp. 4298–4304, Oct. 2018.   
[7] S. García et al., “Sampled true time delay line operation by inscription of long period gratings in few-mode fibers,” Opt. Exp., vol. 27, no. 16, pp. 22787–22793, Aug. 2019.   
[8] I. Gasulla, D. Barrera, J. Hervás, and S. Sales, “Spatial division multiplexed microwave signal processing by selective grating inscription in homogeneous multicore fibers,” Sci. Rep., vol. 7, Jan. 2017, Art. no. 41727.   
[9] S. García, D. Barrera, J. Hervás, S. Sales, and I. Gasulla, “Microwave signal processing over multicore fiber,” Photonics, vol. 4, no. 4, Dec. 2017, Art. no. 49.   
[10] R. Guillem, S. García, J. Madrigal, D. Barrera, and I. Gasulla, “Few-mode fiber true time delay lines for distributed radiofrequency signal processing,” Opt. Exp., vol. 26, no. 20, pp. 25761–25768, Oct. 2018.   
[11] I. Gasulla and J. Capmany, “Microwave photonics applications of multicore fibers,” IEEE Photon. J., vol. 4, no. 3, pp. 877–888, Jun. 2012.   
[12] L. Huang et al., “Stable and compact dual-loop optoelectronic oscillator using self-polarization-stabilization technique and multicore fiber,” J. Lightw. Technol., vol. 36, no. 22, pp. 5196–5202, Nov. 2018.   
[13] S. García and I. Gasulla, “Experimental demonstration of multi-cavity optoelectronic oscillation over a multicore fiber,” Opt. Exp., vol. 25, no. 20, pp. 23663–23668, Oct. 2017.   
[14] S. García and I. Gasulla, “Multi-cavity optoelectronic oscillators using multicore fibers,” Opt. Exp., vol. 23, no. 3, pp. 2403–2415, Jan. 2015.   
[15] B. Redding and H. Cao, “Using a multimode fiber as a high-resolution, low-loss spectrometer,” Opt. Lett., vol. 37, no. 16, pp. 3384–3386, Aug. 2012.   
[16] B. Redding, S. M. Popo, and H. Cao, “All-fiber spectrometer based on speckle pattern reconstruction,” Opt. Exp., vol. 21, no. 5, pp. 6584–6600, Mar. 2013.   
[17] B. Redding, S. M. Popo, Y. Bromberg, M. A. Choma, and H. Cao, “Noise analysis of spectrometers based on speckle pattern reconstruction,” Appl. Opt., vol. 53, no. 3, pp. 410–417, Jan. 2014.   
[18] S. F. Liew, B. Redding, M. A. Choma, H. D. Tagare, and H. Cao, “Broadband multimode fiber spectrometer,” Opt. Lett., vol. 41, no. 9, pp. 2029–2032, May 2016.   
[19] H. Cao, “Perspective on speckle spectrometers,” J. Opt., vol. 19, May 2017, Art. no. 060402.   
[20] Z. Meng et al., “Multimode fiber spectrometer with scalable bandwidth using space-division multiplexing,” AIP Adv., vol. 9, no. 1, Jan. 2019, Art. no. 015004.   
[21] K. Wang et al., “Advances in optical fiber sensors based on multimode interference (MMI): A review,” IEEE Sens. J., vol. 21, no. 1, pp. 132–142, Jan. 2021.   
[22] K. Cho and H. Jang, “Comparison of different input modalities and network structures for deep learning-based seizure detection,” Sci. Rep., vol. 10, Jan. 2020, Art. no. 122.   
[23] C. Zhu et al., “Image reconstruction through a multimode fiber with a simple neural network architecture,” Sci. Rep., vol. 11, Jan. 2021, Art. no. 896.   
[24] D. Hunter and B. Wilamowski, “Parallel multi-layer neural network architecture with improved efficiency,” in Proc. 4th Int. Conf. Hum. Syst. Interact., 2011, pp. 299–304.   
[25] W. Li, “Analysis on the weight initialization problem in fully-connected multi-layer perceptron neural network,” in Proc. Int. Conf. Artif. Intell. Comput. Eng., 2020, pp. 150–153.   
[26] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in Proc. 3rd Int. Conf. Learn. Representations, 2015, pp. 1–5, [Online]. Available: http://arxiv.org/abs/1412.6980   
[27] N. H. Wan et al., “High-resolution optical spectroscopy using multimode interference in a compact tapered fibre,” Nature Commun., vol. 6, Jul. 2015, Art. no. 7762.   
[28] B. Redding, M. Alam, M. Seifert, and H. Cao, “High-resolution and broadband all-fiber spectrometers,” Optica, vol. 1, no. 3, pp. 175–180, Sep. 2014.   
[29] C. Lin et al., “Silicon nanomembrane based photonic crystal waveguide array for wavelength-tunable true-time-delay lines,” Appl. Phys. Lett., vol. 101, no. 5, Jul. 2012, Art. no. 051101.   
[30] X. Gao et al., “A high-resolution compact optical true-time delay beamformer using fiber Bragg grating and highly dispersive fiber,” Opt. Fiber Technol., vol. 20, no. 5, pp. 478–482, Oct. 2014.

Liang Huo received the B.S. degree in 2016 from the School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan, China, where he is currently working toward the Ph.D. degree since 2018. His research interests include microwave photonics, fiber-based devices, specialty optical fibers, and optical signal processing.

Hao Wu received the B.S., M.Eng., and Ph.D. degrees from the School of Optical and Electronic Information, Huazhong University of Science and Technology (HUST), Wuhan, China, in 2013, 2016, and 2019, respectively. Since 2019, he has been a Postdoctoral Researcher with HUST. His research interests include the application of specialty optical fibers and machine learning algorithm in distributed optical fiber sensing.

Can Zhao received the B.S. and Ph.D. degrees from the School of Optical and Electronic Information, Huazhong University of Science and Technology (HUST), Wuhan, China, in 2014 and 2019, respectively. Since 2019, he has been a Postdoctoral Researcher with HUST. His research interests include distributed optical fiber sensing and specialty optical fibers.

Ming Tang (Senior Member, IEEE) received the B.E. degree from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technological University, Singapore, in 2005. His Postdoctoral Research with Network Technology Research Centre was focused on optical fiber amplifiers, high-power fiber lasers, nonlinear fiber optics, and all-optical signal processing. In February 2009, he was with the Tera-photonics group led by Prof. Hiromasa Ito in RIKEN, Sendai, Japan, as a Research Scientist conducting research on terahertz-wave generation, detection, and application using nonlinear optical technologies. Since March 2011, he has been a Professor with the School of Optical and Electronic Information, Wuhan National Laboratory for Optoelectronics, HUST. His research interests include optical fiber based linear and nonlinear effects for communication and sensing applications. Since 2001, he has been a member of the IEEE Photonics Society.