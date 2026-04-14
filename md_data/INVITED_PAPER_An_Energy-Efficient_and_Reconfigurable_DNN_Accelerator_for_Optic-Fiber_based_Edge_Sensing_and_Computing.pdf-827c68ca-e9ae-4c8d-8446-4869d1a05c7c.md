# INVITED PAPER: An Energy-Efficient and Reconfigurable DNN Accelerator for Optic-Fiber based Edge Sensing and Computing

Ziang Duan2, Ruohan Ma1, Zixuan Shen1, Zhao Ge1, Hao Wu1, Ming Tang13, Chao Wang13

1 School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan, China   
2 School of Integrated Circuits, Huazhong University of Science and Technology, Wuhan, China   
3 Wuhan National Laboratory for Optoelectronics, Wuhan, China

Abstract—The signals of distributed optic-fiber may represent information related to certain events which can be classified by Deep Neural Networks (DNN). However, energy-efficient and realtime classification with different DNNs for different edge applications is a great challenge. This paper proposes a reconfigurable hardware accelerator design for DNNs with different structures to classify the signals from various optic-fiber sensors efficiently in real time. By exploiting the arithmetic operation similarity, the proposed reconfigurable design reuses a PE array to implement different convolutional layers and network structures of DNNs, and also utilizes sparsity in DNNs to achieve high energy efficiency and low computation latency. In addition, a design space exploration method is proposed to reach an optimal balance between mitigating on-chip memory overhead and minimizing computation latency so as to effectively achieve low latency and power consumption. FPGA implementation shows that it can achieve a reconfigurable design with 26484 LUTs and 14366 FFs. It outperforms the CPU/GPU solution, i.e., 137 and 99 times in energy efficiency at $\mathbf { 1 8 0 ~ M H z }$ , respectively. A preliminary Python simulation results in a case study shows that the accuracy of Resnet-12 implemented by the proposed design is $9 8 . 9 4 \%$ on the optic-fiber vibration signal classification task.

Keywords—Optical Fiber, Deep Neural Network, Hardware Accelerator, Sparsity, Design Space Exploration

# I. INTRODUCTION

The distributed optic-fiber signals (e.g., temperature, stresschange signals and vibration) classification has been widely used in many application scenarios (e.g., perimeter security, gasoline pipeline monitoring, railway safety monitoring) [1], as depicted in Fig.1. For optical fiber monitoring, it is often necessary to deploy optical fiber sensors in a distributed fiber optic network over several kilometers to collect data. Transmitting all collected raw data to the cloud poses a significant pressure on cloud storage and computing resources. Therefore, utilizing edge computing platform for real-time data processing and uploading the classified key data to the cloud can reduce the storage and

![](images/92db96fbd3a8e7fd244525ca462a8b412690a7d7b8ce40bdda5c91654b60a62f.jpg)  
ReconfigurableDNNAccelerator   
Fig.1 The optic-fiber based event monitoring and classification system.

This work was partially supported by National Natural Science Foundation of China (61974053), National Natural Science Foundation of China (61931010) and National Key Research and Development Program of China (2018YFB1801002). Ziang Duan and Ruohan Ma equally contributed to this paper. #Corresponding email: chao_wang_me@hust.edu.cn.

computing burden on the cloud. To achieve real-time processing, the edge computing platform for fiber vibration event recognition and classification should process one frame of data in less than the sensor's sampling interval. Additionally, since the edge processor will be deployed outdoors with constrained power budget, it is necessary to reduce power consumption and improve battery life to facilitate edge deployment. In general, power consumption budget could be from a few watts to hundred micro watts. However, the existing optic-fiber vibration event recognition algorithms in the literature employ Deep Neural Networks (DNN) to achieve good classification performance but involve intensive computation and consume significant power. C. Xu et. al. present a simple Convolutional Neural Networks (CNN) with manually extracted features to classify time-domain signals in two stages at the cost of low generalization capability [2]. S. Li et. al. construct a one-stage shallow CNN network to classify spatiotemporal at the cost of accuracy loss [3]. Z. Ge et. al. present a one-stage DNN to achieve high classification accuracy [4].

As far as we have surveyed from the literature, the aforementioned optic-fiber signals classification algorithms are implemented on CPU and GPU, which pose a significant challenge in the edge sensing and computing tasks with high realtime and energy efficiency requirements The computing latency of CPU is lengthy due to the sequential processing nature that results in relatively low processing efficiency. Multi-core/manycore CPU or GPU can significantly improve the computing power by parallel processing but are at cost of high power consumption. Therefore, the CPU/GPU based edge devices with very high computational power consumption and high cost, making it impossible for widely deploying them to undertake event classification tasks in large-scale distributed fiber-optic network systems.

To address the challenges of real-time performance and low energy consumption in optic-fiber based edge sensing and computing tasks, this paper proposes an energy-efficient and reconfigurable DNN hardware accelerator design that can be implemented in FPGA/ASIC. The main features of proposed design are listed as below:

1. Reconfigurable design: The reconfigurable strategy is implemented to DNN hardware accelerator design for convolution operations by dividing convolution kernels from different layers in channel dimension that can be computed in same core circuits, reducing redundant computation units, thereby minimizing hardware overhead.   
2. Zero-skipping strategy: The zero-skipping strategy is integrated in an address generator to utilize the sparsity of DNN data flow by mitigating zero data multiplications and additions, reducing redundant delay, power consumption, thereby enhancing computation efficiency.   
3. Design space exploration: The design space exploration method is used to balance computation latency and on-chip memory trade-off. Different computation units are designed by modeling their characteristics to directly meet the timing demands by specific tasks. This design and analysis approach enables efficient hardware design for different distributed optic-fiber signal classification application scenarios.

The remainder of this paper is organized as follows: Section II presents the proposed reconfigurable DNN hardware accelerator design; Section III presents the FPGA

![](images/e8cdf7f71f77cd06ab6fbcf2749a2d110fc7f545bb9cb026d8138435dd2901ce.jpg)  
Fig.2 Convolutional layer 6D loop nest.

implementation results and comparisons. Section IV provides the conclusion of this work.

# II. RECONFIGURABLE DNN ACCELERATOR DESIGN

# A. Reconfigurability analysis of DNN algorithm

Fig.2 presents the computation flow of single inference operations in a CNN model. A single convolution operation can be decomposed as a loop operation across six dimensions: the length $( P )$ and height $( \varrho )$ of output feature map, the number of output channels $( N )$ , the length (W) and height $( H )$ of convolution kernel, and the number of input channels (C). During the inference process, convolution calculations involve iterating over a total of six dimensions. This can be implemented by reusing a piece of commonly-shared core hardware circuits. Moreover, there are many data computations within the process that can be processed in parallel, aligning well with the implementation of hardware circuits.

Fig. 3 illustrates the basic structure of a ResNet-12 model for the classification of distributed optical fiber vibration signals caused by hammer, air pick, and excavator[4][5], and the major network structure mainly consists of convolutional layers. Given the high similarity in the computation flow between these convolutional layers, a reconfigurable hardware circuit is designed by reconfiguring and reusing a convolution engine circuit module for different convolutional layer computation tasks. Parameter registers are used to the configuration of different convolution calculation. Therefore, only a single convolution engine is required to complete all convolution

![](images/08bb07ff098fc2a119c07f3a4f305fbafab4990607823c62282ab379dea643bc.jpg)  
Fig.3 The network architecture of ResNet-12 for distributed optic-fiber signal classification [4].

![](images/ab4f845bb68aec85199de3c74268487910758e93a303a82431e72c68e95fc26f.jpg)  
Fig.4 The proportion of zero-valued data in each convolutional layer before and after 16-bit quantization of the ResNet-12 model.

![](images/c9c05298205cc6bf9ae705f7f649f574f5b333dc9739ada52efc8219d104b623.jpg)

![](images/51d30caf9c0838acdca4f0c633f12b86b3b2d6d77bce65d7924251a8ab83b0e8.jpg)  
  
(b)   
Fig. 5. (a) The overall architecture of the proposed reconfigurable DNN accelerator, which consists of a sparse address generator in high-speed clock domain and a reconfigurable PE array in low-speed clock domain. (b) The case study of mapping method for different convolution layers, with the input channel of 64.

computation tasks. This design can significantly reduce hardware overhead and enhances energy efficiency.

# B. Sparsity analysis of DNN algorithm

The sparsity in the DNN data flow primarily originates from three sources. First, there are regular zero values introduced during the padding in the convolution computation. Second, there are non-regular zero values resulting from the ReLU activation function after convolution calculations. Third, there is an overall increase in sparsity due to data quantization, as illustrated in Fig. 4. Considering all these factors, the feature map data of the ResNet-12 model exhibits an average sparsity of around $50 \%$ . These zero values in the convolution computation process can lead to unnecessary Multiplication and Accumulation (MAC) operations, resulting in redundant computation latency and waste power consumption. By generating addresses for non-sparse data, skipping of zero data can be effectively implemented without impacting the data processing correctness. Consequently, the zero-skipping hardware design can help omit all the MAC operations related to zero data at affordably small control hardware overhead, thereby enhancing computation efficiency and reducing power consumption.

# C. Reconfigurable hardware architecture design

Fig.5 (a) illustrates the proposed architecture of DNN accelerator consisting of a reconfigurable Processing Element (PE) array and a sparse address generator, operating in two different clock domains, respectively. In the slow clock domain, the circuit modules include the global buffer and the PE Array. The global buffer is responsible for caching feature map data from the fast clock domain, while the PE Array is the reconfigurable convolutional engine core. The proposed reconfigurable DNN accelerator design aims at achieving computational efficiency across different convolutional layers by reusing the PE Array, resulting in lesser hardware cost and lower energy consumption. In the fast clock domain, there are two modules: the Input Feature map (IFmap) data transmission module and the feature map addressing module. Irregular-zero skipping module with address generator is responsible for determining whether the data is zero, and generating addresses after data zero skipping.

Fig. 5 (b) shows an example that how the design reconfigurability is achieved by reusing the PE array to perform convolutions of different input sizes. Specifically, channels of the input and Output Feature map (OFmap) are mapped on the row and column of the PE array, respectively, while width and height of the IFmap are handled by each PE in different cycles. Each individual PE unit comprises Block RAM (BRAM) for storing weight data, multiply-accumulate units for MAC operations, and a register for storing the partial sum. The partial sums generated by the PEs in the same column will ultimately be summed together through an adder tree to obtain the final convolution result. The global buffer is responsible for dispatching the non-zero data in IFmap and corresponding sparse weight address for the reconfigurable PE array. In the example of Fig.5 (b), there are 64 input channels and 64 output channels, and every 8 channels of IFmap data are sent into a same row of the PE Array. The channels of the convolution kernel are also divided into groups of 8. Additionally, the 8 groups of convolution kernels (corresponding to the output channels) are sent in batches to the respective columns, for MAC operations with the corresponding data from the 8 groups of IFmap channels in the PE array.

The sparse address generator in the fast clock domain leverages data sparsity of the IFmap to implement zero skipping.

The address generator preprocesses regular zero values from padding and directly skip the addresses associated with padded zeros. Subsequently, the non-padded data enters the irregularzero skipping module for the determination of irregular zero value introduced by ReLU. When the IFmap data equals 0, the weight address counter increments by one, and the IFmap data with a value of 0 is not written into the FIFO. When the feature map data is not equal to 0, the weight address still increments by one, but the non-zero feature map data will be written into the FIFO.

# D. Design space exploration method

Different optical-fiber sensing and computation application scenarios have varying demands for processing latency and onchip memory overhead. Therefore, it is essential to conduct Design Space Exploration (DSE), calculating the corresponding processing latency and memory overhead for different PE array configurations. This is crucial for achieving efficient hardware implementation of DNN accelerators at the edge.

The IFmap data has three dimensions: the number of channels (??), heigh $( H )$ , and width (?? ), as shown in Fig.2. Additionally, the number of output channels $( N )$ in the feature map is determined by the number of convolutional kernels. Repeatedly computation of a large number of convolutional kernels results in significant processing delays. During the data processing, in order to enhance computational parallelism, the feature map can be partitioned into $A$ segments along the channel dimension. To further enhance parallelism, the $N$ convolutional kernels can also be divided into $B$ partitions.

For the $i$ -th convolutional layer, the data volume $M _ { i }$ in BRAM, and the inference latency $T _ { i }$ can be depicted by:

$$
M _ {i} = C * H * W + N * C * K * K + 2 * D * A \tag {1}
$$

$$
T _ {i} = K ^ {2} * C * Q * P * \frac {N}{A * B} * R \tag {2}
$$

where $N , P$ and $Q$ are the three dimensions of the output feature map data, $D$ represents FIFO cache depth, $K$ represents the size of convolutional kernel, and $R$ represents the non-zero values proportion of the feature map. For a DNN with a total of $L$ layers, the required on-chip memory resources $M$ and total inference latency $T$ can be depicted by:

$$
M = \max  \left(M _ {1}, M _ {2}, \dots , M _ {i}, \dots , M _ {L}\right) \tag {3}
$$

$$
T = \sum_ {i = 1} ^ {L} T _ {i} \tag {4}
$$

![](images/62c8421548ecf6b74eeb39441968593fb565292acd4fc3ddff778fb76271fb54.jpg)  
Fig. 6. Design space exploration in memory size, inference latency for Resnet-12 [4] and corresponding PE array size in the worst case of zero rate $R = 1$ at 100 MHz.

Different configurations of PE array row and column lead to varying hardware resource requirements and computation latency. Utilizing the above equations, computation latency and storage capacity for a given application's DNN neural network under various PE array configurations can be roughly estimated. Following the DSE method, the numbers of rows and columns in the PE Array can be tailored to achieve an optimal hardware design for the specific application.

# III. EXPERIMENT RESULTS AND DISCUSSION

Fig.6. shows a DSE case study result of a 12- convolutional-layer Resnet-12 model for 3-class optic-fiber vibration signal classification task on time-space signal dataset， and the optic-fiber vibration time-space signals are caused by hammer, air pick, and excavator [4]. Note that Y-axis is in log scale due to the large distribution range of the data in the figure. The DSE result is achieved by configuring PE arrays with different sizes from (4, 4) to (64, 64) and measuring the corresponding BRAM memory size and signal processing time per inference. Signal processing in distributed optic-fiber systems must meet the real-time requirements, e.g., the latency should be less than 256 ms at $1 0 0 \mathrm { M H z }$ and $R = 1$ in this study. Under this constraint, a solution with the minimum memory size is selected. The optimal design choice is to use the PE array with dimension of (8, 8), resulting in on-chip memory size of $1 . 4 \mathrm { M b }$ and inference latency of 81 ms, respectively.

Table 1 compares the performance of the proposed reconfigurable DNN design with the CPU and GPU solutions for the Resnet-12 model in edge sensing and computing applications [4]. In terms of the average classification accuracy for optical fiber vibration signals caused by hammer, air pick, and excavator, the Resnet-12 implemented on the proposed reconfigurable design outperforms the Resnet-12 implemented on other two platforms. This is because 16-bit fixed-point quantization employed by the proposed design introduces random errors and thereby improving generalization capability of the DNN to a certain degree. Regarding inference latency, the achieved low latency is attributed to the hardware accelerator design based on the characteristics of the DNN data flow and the employment of the zero-skipping strategy with $R$ being around 0.5 in each layer. In terms of energy efficiency, the introduction of reconfigurability and zero-skipping strategies leads to a substantial reduction in energy consumption. The former efficiently reuses the PE array circuitry, while the latter significantly reduces unnecessary energy consumption. Furthermore, through the DSE method, the proposed design adopts the optimal latency-matching approach, avoiding redundant memory resources and hardware overhead, and therefore, further improve the energy efficiency. The overall energy efficiency improvement is 137 times and 99 times as compared to CPU and GPU, respectively.

Table. 1. Comparison among the proposed reconfigurable DNN accelerator, CPU and GPU solutions   

<table><tr><td></td><td>CPU</td><td>GPU</td><td>This work</td></tr><tr><td>Network</td><td>ResNet-12[4]</td><td>ResNet-12[4]</td><td>ResNet-12[4]</td></tr><tr><td>Dataset</td><td colspan="3">Time-space Signal Dataset</td></tr><tr><td>Task</td><td colspan="3">2-D Time-space Signal Classification</td></tr><tr><td>Platform</td><td>Apple M2 8-core CPU</td><td>Apple M2 10-core GPU</td><td>Xilinx FPGA xc7a200tfbg484-2</td></tr><tr><td>Clock Frequency</td><td>2424 MHz</td><td>1398 MHz</td><td>180 MHz (High-speed Clock Domain) 90 MHz (Low-speed Clock Domain)</td></tr><tr><td>Precision</td><td>64-bit Floating point</td><td>64-bit Floating point</td><td>16-bit Fixed point</td></tr><tr><td>LUT</td><td>N/A</td><td>N/A</td><td>26484</td></tr><tr><td>FF</td><td>N/A</td><td>N/A</td><td>14366</td></tr><tr><td>RAM(MB)</td><td>N/A</td><td>N/A</td><td>0.235</td></tr><tr><td>Latency (ms/inference)</td><td>144</td><td>139</td><td>43</td></tr><tr><td>Throughput (GOPS)</td><td>N/A</td><td>N/A</td><td>5.76</td></tr><tr><td>Accuracy</td><td>95.89%</td><td>95.89%</td><td>98.94%</td></tr><tr><td>Power(W)</td><td>20</td><td>15</td><td>0.503</td></tr><tr><td>Energy Efficiency (mJ/inference)</td><td>2880</td><td>2085</td><td>21</td></tr></table>

# IV. CONCLUSION

This paper presents an energy-efficient reconfigurable DNN hardware accelerator utilizing limited on-chip hardware resources for optic-fiber vibration signal classification. During the inference process, the FPGA implementation achieves energy efficiency improvements of 137 times and 99 times compared to the CPU/GPU solutions, respectively, while maintaining relatively consistent accuracy. The study results confirm the feasibility for the energy-efficient hardware implementation of edge sensing and computing in distributed optical fiber systems.

# REFERENCES

[1] J. Li et al., "Pattern recognition for distributed optical fiber vibration sensing: a review," in Sensors, 2021.   
[2] C. Xu et al., "Pattern recognition based on time-frequency analysis and convolutional neural networks for vibrational events in $\boldsymbol { \Phi }$ -OTDR," in Optical Engineering, 2018.   
[3] S. Li et al., "A surveillance system for urban buried pipeline subject to thirdparty threats based on fiber optic sensing and convolutional neural network," in Structural health monitoring, 2021   
[4] Z. Ge et al., "High-accuracy event classification of distributed optical fiber vibration sensing based on time–space analysis," in Sensors, 2022.   
[5] K. He et al., "Deep Residual Learning for Image Recognition," in CVPR, 2016.