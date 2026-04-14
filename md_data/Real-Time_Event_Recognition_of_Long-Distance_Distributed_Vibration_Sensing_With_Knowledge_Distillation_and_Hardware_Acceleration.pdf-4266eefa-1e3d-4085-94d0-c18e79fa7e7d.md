# Real-Time Event Recognition of Long-Distance Distributed Vibration Sensing With Knowledge Distillation and Hardware Acceleration

Zhongyao Luo , Hao $\mathrm { W u } ^ { \mathbb { \oplus } }$ , Zhao Ge, and Ming Tang , Senior Member, IEEE

Abstract—Fiber-optic sensing, especially distributed optical fiber vibration (DVS) sensing, is gaining importance in Internet of Things (IoT) applications, such as industrial safety monitoring and intrusion detection. Despite their wide application, existing post-processing methods that rely on deep learning models for event recognition in DVS systems face challenges with realtime processing of large sample data volumes, particularly in long-distance applications. To address this issue, we propose to use a four-layer convolutional neural network (CNN) as the student model with ResNet as the teacher model for knowledge distillation. Compared to the baseline CNN model, which achieves $8 3 . 4 1 \%$ accuracy on data from previously untrained environments, the distilled CNN improves accuracy significantly to $9 5 . 3 9 \%$ , demonstrating its superior generalizability and robustness. Additionally, we propose a novel hardware design based on field-programmable gate arrays to further accelerate model inference. This design replaces multiplication with binary shift operations and quantizes model weights, enabling high parallelism and low latency. Our implementation achieves an inference time of 0.083 ms for a spatial–temporal sample covering a $\mathbf { 1 2 . 5 \ m }$ fiber length and 0.256 s time frame. This performance enables real-time signal processing over approximately $3 8 . 5 5 \ \mathrm { k m }$ of fiber, about $2 . 1 4 \times$ the capability of an Nvidia GTX 4090 graphics processing unit. The proposed method greatly enhances the efficiency of vibration pattern recognition, promoting the use of DVS as a smart IoT system. The data and code are available at https://github.com/HUST-IOF/Efficient-DVS.

Index Terms—Convolutional neural network (CNN), distributed vibration sensing, fiber-optic Internet of Things (IoT), hardware acceleration, real-time system.

# I. INTRODUCTION

D ISTRIBUTED optical fiber vibration sensing (DVS)technology, based on phase-sensitive optical time-domain reflectometry (phi-OTDR), uses optical fibers as sensing elements to provide dense, continuous measurements of vibration and recognize various intrusion events. This technology has been applied as smart Internet of Things (IoT) systems

Received 14 January 2025; accepted 2 February 2025. Date of publication 5 February 2025; date of current version 23 May 2025. This work was supported in part by the National Key Research and Development Program of China under Grant 2021YFB2800902; in part by the National Natural Science Foundation of China under Grant 62225110; and in part by the Innovation Fund of WNLO. (Corresponding author: Hao Wu.)

The authors are with the Wuhan National Laboratory for Optoelectronics, Next Generation Internet Access National Engineering Laboratory, and the Hubei Optics Valley Laboratory, School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: zluo@hust.edu.cn; wuhaoboom@hust.edu.cn; d202280977@hust.edu.cn; tangming@mail.hust.edu.cn).

Digital Object Identifier 10.1109/JIOT.2025.3539339

![](images/ea3763855fc0b5c15c92a81e8ef04b00e2f427ff0a3709e11c2eced3189095eb.jpg)  
Fig. 1. Schematic of DVS system. NLL: narrow linewidth laser, SOA: semiconductor optical amplifier, AWG: arbitrary waveform generator, EDFA: erbium-doped fiber amplifier, FUT: fiber under test, APD: avalanche photodetector, and DAQ: data acquisition card.

in various areas in recent years, including industrial safety monitoring and intrusion detection. Recent applications of DVS technology include railway safety monitoring [1], [2], perimeter security [3], [4], pipeline monitoring [5], [6], and smart cities [7]. As shown in Fig. 1, the phi-OTDR system captures Rayleigh backscattering light across the fiber, with phase variations induced by external vibrations providing valuable event information.

Despite its capabilities, DVS technology faces several challenges in IoT applications. The primary challenge for the system is the generalizability. Long-distance fibers are utilized as massive sensors in the system, which inevitably operate under varying signal acquisition conditions due to differences in deployment and environmental factors [8]. For instance, sections of the fiber used for pipeline monitoring may experience vastly different conditions: some portion might be exposed to the elements, encountering noise from rain, while others may be buried underground, affected by geographical vibrations. These discrepancies make it challenging to ensure consistent performance across all fiber sections. The variability of signals, driven by diverse environmental conditions and intrusion types, leads to challenges in generalizability. This issue directly contributes to higher false alarm rate and miss alarm rate, ultimately limiting the reliability of DVS systems in real-world IoT applications.

Traditional methods often rely on hand-crafted algorithms for data preparation and feature extraction, followed by classic machine learning for recognition [9], [10], [11], [12], [13], [14]. These approaches can be time-consuming and complex, requiring extensive expertise in signal processing. To solve these problems, deep learning models (DLMs) have been introduced to the field. Initially,

DLMs are introduced for pattern recognition based on extracted features [10]. With the development of more sophisticated and computationally powerful DLMs, they are capable of automatically extracting important features from noisy data and simultaneously handling feature extraction and pattern recognition tasks. The introduction of complex DLMs brings about improved performance and reduces the design workload. Consequently, they have received more attention in recent years.

Another significant challenge in IoT applications of DVS technology is the large volume of captured data, which scales with the length of the monitored fiber. Long-distance fiber monitoring generates vast amount of data, posing computational and storage challenges. Furthermore, applications like pipeline monitoring and earthquake detection require real-time or near-real-time responses to minimize potential damages. In such cases, achieving low-latency performance often takes precedence over perfect accuracy. For instance, in pipeline monitoring, rapid detection of potential leaks can prevent large-scale environmental contamination. While this approach may result in some false alarms, the associated costs are still far lower than the potential damage caused by delayed detection. However, deploying high-capacity DLMs in these scenarios further increases computational demands. Due to limited computational resources in real-world IoT deployments, real-time event recognition is often feasible only for short-distance fibers [15].

To improve the computational efficiency of the DVS system, there are typically three solutions. The first is data selection or down-sampling, which involves using prior knowledge and data analysis to identify and retain valuable signal sections or sample points [2], [7]. While this reduces the input data volume, it can lead to false negatives due to its reliance on hand-crafted algorithms. The second solution is model compression, which seeks to lower computational complexity and resource demands. However, existing approaches often require models with at least millions of parameters to maintain performance and generalizability [7], leaving room for further optimization to develop smaller and more efficient models. The third solution is the use of high-performance hardware, such as graphics processing units (GPUs) and cloud computing. While this approach can significantly increase computational power, it is often expensive and demands high power consumption, as well as a reliable communication system to handle the large volume of sample data.

This article proposes enhancing the signal processing capabilities of DVS systems through the use of shallow convolutional neural network (CNN) coupled with knowledge distillation (KD) and hardware acceleration. We introduce a shallow CNN as a more efficient alternative to DLMs, reducing model complexity and computational resource requirements. We identify the generalizability limitation of low-capacity models and propose to use the KD technique as a solution. To further improve the data processing throughput, we design an efficient hardware acceleration scheme based on a field programmable gate array (FPGA). An analog-to-digital converter (ADC) is integrated with the FPGA to minimize latency during data transfer, as depicted in Fig. 1.

Compared to other hardware accelerators, general-purpose processors, such as GPUs and tensor processing units (TPUs), provide high computational throughput but are significantly less power-efficient, with typical power consumption reaching hundreds of watts for artificial intelligence (AI) workloads. In contrast, FPGAs consume considerably less power, ranging from several watts to a few dozen watts, while offering comparable performance for specific tasks. This makes them highly efficient and adaptive for edge devices [16], [17]. Although general-purpose ASICs, designed for more general AI tasks, can achieve high efficiency with energy consumption of only a few watts [16], FPGA provides more flexibility. It allows for further optimization and adaption toward the model and the task, supporting a broader range of AI tasks and dynamic requirements. While we currently use FPGA with its flexibility to implement our hardware design, we plan to transfer our design into ASIC to achieve greater efficiency and performance for deployment in real-world IoT applications.

The proposed hardware acceleration scheme leverages FPGA’s flexibility to optimize model performance by replacing computationally expensive multiplication operations with shift-add operations, which are significantly less resource-intensive. The shift-add architecture facilitates parallel processing and faster computation, constrained only by the FPGA’s logic resources rather than its limited digital signal processing (DSP) blocks [18]. Additionally, we introduce a shift-parameter quantization technique, wherein model weights are quantized into integers representing the number of binary shift operations. This method, combined with shallow CNNs, enables real-time processing of the substantial data volumes generated by DVS systems. Beyond computational efficiency, the proposed scheme is highly costefficient, reducing reliance on DSP resources and external memory components. Furthermore, the FPGA platform’s compatibility with standard communication protocols (e.g., USB, Ethernet, PCIe) ensures seamless integration with existing IoT infrastructure.

In a word, the contribution of this work can be listed as follows.

1) We propose a novel scheme for designing and implementing real-time DVS algorithms, validated with real-world datasets. The results show performance and generalizability comparable to DLMs, while achieving real-time recognition over long-distance fibers. This demonstrates the potential of our approach to enhance the real-time capabilities of DVS systems, thereby improving the practicability of DVS technology in smart IoT applications.   
2) We propose to use shallow CNN models, coupled with KD, to develop a lightweight model that offers high performance and generalizability. This approach effectively addresses the throughput limitation brought by the high computational complexity of existing algorithms.   
3) We design a novel hardware acceleration scheme for shallow CNNs, utilizing shift-add structures and shift parameter quantization to significantly improve efficiency.

![](images/d40124a0d69ca6c51f2b95b3859ed6734983dec44faa44a392a270b212b9f80c.jpg)  
Fig. 2. Schematic of KD process.

# II. METHOD

# A. Knowledge Distillation Based on Logits

It is generally believed that large models, that is, models with more complex and efficient structural design and huge number of parameters, tend to be able to extract higher-level features, so that it can achieve better results in various tasks. In other words, large models often have better generalizability, and can better handle signals with various noise. On the other hand, the model inference process can be considered as finishing the specified task based on the “knowledge” contained in model structure and its parameters. The idea of KD is to extract the knowledge from large models (teacher models), and transfer the knowledge to small models (student models), so that the performance and generalizability of the later one can be improved. In the KD method based on logits [19], the output prediction distribution of the model is considered to contain valuable knowledge. This distribution represents the probabilities of classifying the input sample into each class. The distribution can be obtained through introducing a temperature parameter $T$ to the softmax function at output layer. The function can be expressed as

$$
\operatorname {S o f t m a x} (\mathbf {x} / T) _ {i} = \frac {e ^ {x _ {i} / T}}{\sum_ {j} e ^ {x _ {j} / T}} \tag {1}
$$

where $\textbf { x } = ~ \left[ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \right]$ is the input vector, which is the output of the network in this case. The knowledge is then transferred by guiding the student model to imitate the behavior of the teacher model. The process is to minimizing a loss function that measures the difference between the outputs of the teacher network and the student network, and also the difference between the outputs of the student network and the correct results, as shown in Fig. 2. The loss function usually consists of a standard classification loss, like cross-entropy, and a distillation loss that measures the difference between the softened probabilities generated by the teacher and student

networks. Formally, the loss function $\mathcal { L }$ can be expressed as

$$
\begin{array}{l} \mathcal {L} = \alpha \cdot \operatorname {C E} (\mathbf {y} _ {s}, \mathbf {y} _ {\text {t r u e}}) \\ + (1 - \alpha) \cdot \operatorname {K L} (\operatorname {S o f t m a x} (\mathbf {y} _ {t} / T), \operatorname {S o f t m a x} (\mathbf {y} _ {s} / T)) \tag {2} \\ \end{array}
$$

where CE denotes the cross-entropy loss, KL represents the Kullback–Leibler divergence, ytrue is the true label, $\alpha$ represents weight between two kind of losses, $\mathbf { y } _ { t }$ and ${ \bf y } _ { s }$ denote the outputs of the teacher and student networks, respectively. Through this optimization process, KD enables the creation of compact yet powerful neural networks capable of retaining the performance of their larger counterparts.

# B. FPGA-Based Hardware Acceleration

1) Parallel Design: Implementing CNNs on FPGAs presents significant challenges, particularly in handling the storage of intermediate data and model parameters [20]. There are two common approaches are used to address these issues.

1) External Memory Expansion: This method expands storage capacity by combining on-chip storage with external memory, forming a cache system [18], [21], [22], [23]. The design aligns memory access patterns with cache bandwidth limitations, ensuring efficient data access. Models are partitioned into sequential tasks that fit on the computing units.   
2) Compressed On-Chip Model: Alternatively, model compression enables storing of all intermediate data and parameters entirely on-chip. This design typically uses a pipelined structure, where multiple parallel modules implement different layers of the CNN to maximize throughput [18], [20].

In this article, we adopt the compressed on-chip model approach to achieve higher inference speed and reduced memory overhead. Each layer of the model is implemented as a separate module, as illustrated in Fig. 3. By leveraging parallelism and pipelining, this design improves throughput and minimizes latency.

![](images/eb46c6729c12c7d471823f4d78f4fa35a834d536684d7fb51061eed043a464bf.jpg)  
Fig. 3. Schematic of pipelined structure.

![](images/0e080f55706daf971e463c2fb1464427b6f2b0d1c97df96c608c635f6de471e8.jpg)  
Fig. 4. Line buffer structure.

2) Activation Buffering: The activation buffer temporarily stores intermediate data during computation, as depicted in Fig. 3. To optimize memory usage and reduce latency, a column-wise line buffer mechanism is introduced. Instead of buffering the entire input feature map, this mechanism stores only $P$ rows of data (equal to the kernel height), significantly reducing storage requirements.

For convolution and pooling operations, the computation can be expressed as

$$
\begin{array}{l} O _ {\text {c o n v}} [ m, x, y ] = \sum_ {n = 0} ^ {N - 1} \sum_ {p = 0} ^ {P - 1} \sum_ {q = 0} ^ {Q - 1} I [ n, S * x + p, S * y + q ] \\ * K [ m, n, p, q ] + B [ m ] \\ \end{array}
$$

(3)

$$
O _ {\max } [ n, x, y ] = \max  \left\{I [ n, x: x + P, y: y + Q ] \right\} \tag {4}
$$

where

1) O: Output feature map.   
2) I: Input feature map.   
3) M, N: Number of output and input channels.   
4) P, Q: Kernel dimensions (height and width).   
5) S: Stride.   
6) K: Convolution kernel.   
7) B: Bias term.

Only the data within the convolution window is required during computation, so the buffer can store just $P$ rows. For spatial–temporal input, where row represent time points and columns represent spatial positions, this design can significantly reduce storage needs and latency.

Fig. 4 illustrates the line buffer mechanism. For each column, data shifts upward, with new data occupying the bottom row. Consequently, the first convolution or pooling operation requires storing only $( P - 1 - S ) * W + Q$ elements. This results in a delay of caching these data from the previous layer before the operation of the next layer can begin. This requirement is significantly smaller compared to buffering the complete $P * W$ elements of $P$ rows and much smaller than buffering the entire feature map. Once started, the operation proceeds seamlessly as a sliding window moves through the rows.

![](images/627aae1c31c716dcfc4f49bff26d6d6743b8668e6a87c2c0d55e137ccd6b0f31.jpg)  
Fig. 5. Shift-add and MAC structure.

3) Shift-Add Structure: CNNs rely heavily on multiplication-and-accumulation (MAC) operations, which are implemented using DSP slices on FPGAs. However, the limited number of DSP slices restricts the scalability and throughput of CNN designs. To address this bottleneck, we propose replacing MAC operations with shift-add operations, which eliminates the need for DSP blocks, as shown in Fig. 5. The shift-add techniques exploits the representation of digital values as sums of powers of 2

$$
I \cdot W = I \cdot \sum_ {k = 0} ^ {K} 2 ^ {s _ {k}} s _ {k} \in Z. \tag {5}
$$

This approach replaces multiplication with bit-shift and addition operations, achieving high throughput without sacrificing computational accuracy or efficiency.

4) Shift Parameter Quantization: After replacing MAC operations, convolution layer weights are converted into shift parameters, which indicate the number of bit-shift operations required for each computation. To optimize storage and computation, we employ a magnitude-based post-training pruning strategy to discard less significant parameters. Smaller weights, which have minimal impact on the output, are pruned without significantly degrading model performance [24]. The quantization process is outlined in Algorithm 1, ensuring efficient parameter representation by the following.

1) Converting parameters into binary operations.   
2) Retaining only the top N significant bits, its position indicates number of shift operations required.   
3) Discarding insignificant shifts to reduce computational complexity and memory demand.   
5) Encoding: The final step is encoding the quantized parameters to minimize storage requirements. We use an offset binary encoding scheme, which shifts the parameters toward zero to optimize binary representation [25]. The encoding process includes the following.   
1) Extracting and storing the sign information.   
2) Quantifying the absolute values with a bias to center the range.   
3) Rounding outliers to the nearest representable value within the range.   
This encoding scheme ensures compact storage while preserving computational integrity and efficiency.

# III. EXPERIMENT

The proposed scheme is evaluated using a real-world dataset captured by a DVS system, as illustrated in Fig. 1. The system captures a trace of Rayleigh backscattering light every 1 ms,

Algorithm 1 Shift Parameter Quantization   
1: Input  
2: Params matrix of parameters  
3: $N$ Number of parameters remained  
4: Output  
5: Shifts Quantized parameters  
6: Signs Sign of parameters  
7:  
8: Signs $\leftarrow$ SIGN(Params)  
9: [rows, cols] $\leftarrow$ SHAPE(Params)  
10: for $i = 1$ to rows - 1 do  
11: for $j = 1$ to cols - 1 do  
12: BitPositions $\leftarrow$ ZEROS(N)  
13: count $\leftarrow 0$ 14: $P_{binary} \leftarrow$ BINARY(AbsParams[i][j])  
15: for $i \gets 0$ to LEN( $P_{binary}$ ) - 1 do  
16: if count < N then  
17: if $P_{binary}[i] = 1$ then  
18: BitPositions[count] $\leftarrow i + 1$ 19: count $\leftarrow$ count + 1  
20: else  
21: BitPositions[count] $\leftarrow$ None  
22: end if  
23: end if  
24: end for  
25: Shifts[i][j][:] $\leftarrow$ BitPositions  
26: end for  
27: end for

with a spatial interval of $1 . 2 5 \mathrm { ~ m ~ }$ . The traces are then combined together to provide change of signal over a section of time. Specifically, 256 consecutive traces are aggregated to capture the signal variations over a time span of $2 5 6 ~ \mathrm { m s }$ . A $3 0 ~ \mathrm { k m }$ long fiber is utilized, with a section of $5 0 \textrm { m }$ buried under $0 . 5 \mathrm { ~ m ~ }$ of composite material composed of soil, sand, and stones in random ratios. The heterogeneous composition of the material has a significant impact on the vibration signal detected by the fiber, making it an effective means to explore the influence of environmental complexity. This $5 0 ~ \mathrm { m }$ fiber section is divided into four equal segments, each measuring $1 2 . 5 \mathrm { ~ m ~ }$ in length. Due to the $1 . 2 5 \mathrm { ~ m ~ }$ spatial sampling interval, each segment corresponds to 11 data points within the DVS trace. Consequently, our samples are represented as 2-D matrices of size $2 5 6 \times 1 1$ , capturing the vibration signals along a $1 2 . 5 \mathrm { ~ m ~ }$ fiber segment over a time span of 0.256 s. Since the segments are directly derived from the raw data, the number of frames scales linearly with the fiber length. In other words, as the fiber length increases, additional segments are simply appended, increasing the computational load in proportion to the fiber length. Based this fact, we can decide the upper limit of fiber length that our system can process in real time.

The dataset comprises two parts: collected from different locations at different time with varying material compositions and simulating the installation of the system in different environments for the same application. Specific details regarding the composition of the datasets are provided in Table I. Typical data are shown in Fig. 6.

![](images/91cd7778fac38e8f9676f4014c64cd499fe6b33b2262eaf562776b953d769d5a.jpg)

![](images/f5a94fa498b0beea82d4b60fc2e57bd90f0edffe767fda75a3caf91c9e3cceb1.jpg)

![](images/5a26a30c62384db9446309cbafd0f81818543302f29cfa8d927aefcc335fc0f1.jpg)  
  
Fig. 6. Visualization of typical data samples. (a) Air Pick. (b) Excavator. (c) Hammer.

# A. Performance Evaluation

1) Evaluation on Proprietary Dataset: To evaluate and demonstrate the effectiveness of the proposed scheme, we employ a fivefold cross-validation strategy on Dataset 1. This strategy involves dividing the dataset into five equally-sized subsets or folds. The division of folds remains consistent

TABLE I CLASS LABEL AND SAMPLE DISTRIBUTION OF THE PROPRIETARY DATASETS   

<table><tr><td>Class</td><td>Dataset 1</td><td>Dataset 2</td></tr><tr><td>Hammer</td><td>3332</td><td>268</td></tr><tr><td>Air Pick</td><td>3558</td><td>330</td></tr><tr><td>Excavator</td><td>3359</td><td>277</td></tr></table>

TABLE II PARAMETERS OF THE CNN MODEL   

<table><tr><td>Layers</td><td>Kernel Size</td><td>Stride</td><td>Padding</td><td>Output Channels</td></tr><tr><td>Conv 1</td><td>3*3</td><td>1</td><td>1</td><td>8</td></tr><tr><td>MaxPool 1</td><td>2*2</td><td>2</td><td>0</td><td>8</td></tr><tr><td>Conv 2</td><td>3*3</td><td>1</td><td>1</td><td>16</td></tr><tr><td>MaxPool 2</td><td>2*2</td><td>2</td><td>0</td><td>16</td></tr><tr><td>Conv 3</td><td>3*3</td><td>1</td><td>1</td><td>32</td></tr><tr><td>AvgPool 1</td><td>2*2</td><td>2</td><td>0</td><td>32</td></tr><tr><td>Conv 4</td><td>3*3</td><td>1</td><td>1</td><td>64</td></tr><tr><td>flatten</td><td>-</td><td>-</td><td>-</td><td>2048</td></tr><tr><td>FC 1</td><td>-</td><td>-</td><td>-</td><td>3</td></tr></table>

TABLE III EVALUATION RESULTS OF THE RESNET MODELS   

<table><tr><td>Model</td><td>Val/%</td><td>Test/%</td><td>FLOPs</td><td>Params</td></tr><tr><td>Resnet-18</td><td>99.58</td><td>95.47</td><td>98472960</td><td>2777283</td></tr><tr><td>Resnet-34</td><td>99.50</td><td>97.67</td><td>226235392</td><td>8164803</td></tr><tr><td>Resnet-101</td><td>98.34</td><td>85.87</td><td>857427968</td><td>27532227</td></tr><tr><td>Resnet-152</td><td>99.07</td><td>83.04</td><td>552325120</td><td>43175875</td></tr></table>

throughout the subsequent evaluations to ensure fair comparison of results. During each iteration of the cross-validation process, the model is trained on four folds while the remaining fold is held out for validation. This process is repeated five times, with each fold serving as the validation set once. The Dataset 2 is used as test set to verify the generalizability of the model. By averaging the performance of the five runs, we obtain the final validation and test result. Adam optimizer is used for training. Learning rate is set to 0.001, and it is halved when the training loss does not decrease within five epochs. The training setting is also kept consistent for the subsequent evaluations.

To evaluate and demonstrate the performance of the lightweight model, a 4-layer CNN with a structure outlined in Table II is utilized. The model consists of four layers and has a total of 30 771 parameters. In terms of computational cost, it requires 2 282 496 floating-point operations (FLOPs). Additionally, this 4-layer CNN model serves as the baseline for evaluating the improvements in both performance and generalizability achieved through KD.

The baseline model achieves an average validation accuracy of $9 9 . 6 9 \%$ , while the average test accuracy is $8 3 . 4 1 \%$ . The change in training loss and validation loss is depicted in Fig. 7, showing a consistent decrease to stable values for both metrics. This trend indicates that the model avoids over-fitting on the training set [26], [27].

The feature visualization of the best model on the test set is shown in Fig. 8(a). The drop in accuracy clearly demonstrates the limitation of generalizability of the baseline model.

To ensure a strong baseline for KD, we employed the ResNet model, which is widely used for this task in the relevant research [28], [29], [30], as the teacher model. We

![](images/266749a17e71d62a0bed3358d199c3e7cfc737897327bcf4d98efb9ecbc20521.jpg)  
Fig. 7. Change of training and validation loss of the baseline model.

TABLE IV EVALUATION RESULTS OF THE BASELINE MODEL AND DISTILLED MODEL ON THE PROPRIETARY DATASET   

<table><tr><td>Model</td><td>Val/%</td><td>Test/%</td></tr><tr><td>Baseline Model</td><td>99.69</td><td>83.41</td></tr><tr><td>Distilled Model</td><td>99.61</td><td>95.39</td></tr></table>

further evaluated ResNet models with varying structures and depths on the dataset, and the results are presented in Table III. Considering our goal of improving both the performance and generalizability of the student model through KD, we selected the ResNet-34 model as the teacher model. The KD process introduces two additional hyperparameters, namely $\alpha$ and $T$ To identify the optimal values of these hyperparameters, we conduct a grid search, iterating through $\alpha$ values from 0 to 1 with a step of 0.1, and $T$ values from 1 to 10 with a step of 1. This comprehensive search reveals the best combination as $\alpha = 0 . 1$ and $T = 5$ , providing the highest student model’s validation accuracy over Dataset 1.

Through KD, as shown in Table IV, the model achieves an average test accuracy of $9 5 . 3 9 \%$ , while maintaining an average validation accuracy of $9 9 . 6 1 \%$ . The feature visualization on the test set is shown in Fig. 8(b), to better demonstrate the impact of KD. It is clear that the model trained with KD exhibits a more distinct boundary between samples belonging to different categories, demonstrating an improvement generalizability compared with the baseline model. The comparison of the baseline model, teacher model, and student model is presented in Fig. 9. According to the figure, it is evident that the baseline model, which has fewer capacity and depth compared to the teacher model, exhibits limitations in terms of generalizability. The baseline model fails to extract high-level features that are less influenced by the training dataset, resulting in poor and unstable performance on the test dataset. It also shows that the KD technique enables a lightweight CNN model, with only 30 771 parameters and requiring 2282496 FLOPs, to achieve generalizability comparable to a larger model with 8164803 parameters and 226235392 FLOPs.

Table V further shows several typical methods of DVS applications, evaluated on the proprietary dataset. Classis models, such as support vector machine (SVM), perform

![](images/162512da7eedc3eb4475978d6e3ea4f820c44fe4fae2ebaa391a3d4943d2a9c3.jpg)

![](images/69ce42397e36bab4313ab5fae12248cd361b2416cf76af83ed00315ee6bf783c.jpg)  
Fig. 8. Feature visualization of the models. (a) Baseline model. (b) Distilled model.

![](images/29cbba2ff4996e12c31f3b68cd6f6c590b1a9c439090aad00cbb5060f17ee956.jpg)  
Fig. 9. Validation accuracy and test accuracy of the models.

poorly, demonstrating their limitation for modern DVS tasks. DLMs with various architectures generally outperform traditional methods, demonstrating improved performance and generalizability. However, the results also indicate that larger models, do not necessarily achieve higher generalizability in DVS tasks, emphasizing the critical role of model structure. While lightweight models like ShuffleNet offer reduced complexity and generalizability, their performance is limited compared with DLMs. Notably, our proposed lightweight model, enhanced with KD, achieves a high generalizability and performance with only 30K parameters, which is several orders of magnitude smaller than other models.

TABLE V PREVIOUS WORKS ON DVS ALGORITHMS AND OUR WORK   

<table><tr><td>Model</td><td>Parameter Number</td><td>Val. Acc. (%)</td><td>Test Acc. (%)</td><td>Pub. Year</td></tr><tr><td>EfficientNet</td><td>474M</td><td>98.63</td><td>80.69</td><td>-</td></tr><tr><td>ResNext-101</td><td>86M</td><td>98.00</td><td>90.06</td><td>2022 [1]</td></tr><tr><td>ResNet-152</td><td>43M</td><td>99.07</td><td>83.04</td><td>2023 [29]</td></tr><tr><td>ResNext-50</td><td>22M</td><td>99.27</td><td>68.80</td><td>2022 [1]</td></tr><tr><td>DenseNet-121</td><td>6M</td><td>97.61</td><td>83.66</td><td>2023 [32]</td></tr><tr><td>ShuffleNet</td><td>1.4M</td><td>96.34</td><td>84.91</td><td>2023 [32]</td></tr><tr><td>SVM</td><td>-</td><td>59.17</td><td>57.26</td><td>2019 [11]</td></tr><tr><td>CNN-4 (This work)</td><td>30K</td><td>99.61</td><td>95.39</td><td>-</td></tr></table>

TABLE VI CLASS LABEL AND SAMPLE DISTRIBUTION OF THE PUBLIC DATASET   

<table><tr><td>Class</td><td>Sample Number</td></tr><tr><td>Background</td><td>3094</td></tr><tr><td>Digging</td><td>2512</td></tr><tr><td>Knocking</td><td>2530</td></tr><tr><td>Watering</td><td>2298</td></tr><tr><td>Shaking</td><td>2728</td></tr><tr><td>Walking</td><td>2450</td></tr></table>

2) Evaluation on Public Dataset: To further validate the generalizability of the proposed scheme, we further evaluated its performance on a public dataset [32]. This dataset is collected at different times by different individuals, to better simulate real-world scenarios. Its distinct characteristics, including, variations in environment, signal properties, sampling system parameters, and types of vibration events captured, making it ideal for assessing model robustness. The public dataset comprises six classes events designed to simulate real-world scenarios. The detailed composition is shown in Table VI. For evaluation, we randomly split the dataset into training/validation and testing subsets, allocating $80 \%$ of the samples for cross-validation and $20 \%$ for testing. To align the dataset’s temporal characteristics with those of the previously used datasets, we have applied down-sampling by selecting one data point every 40 points. This process is equivalent to reducing the sampling rate of the DVS system, ensuring that the data still accurately and directly represents the signals. The original sample size of $1 0 0 0 0 \times 1 2$ is thereby transformed to $2 5 0 \times 1 2$ .

The baseline model demonstrates reduced accuracy on data sampled under different and unknown conditions, highlighting its limited generalizability. To address this, we still use ResNet-34 as a teacher model and apply KD, which provides an average validation accuracy of $9 9 . 5 1 \%$ and an average test accuracy of $9 8 . 3 1 \%$ . A grid search is conducted to optimize the hyperparameters for distillation, using validation set performance as the reference. With a temperature $T = 7$ and a distillation coefficient $\alpha = 0 . 3$ , we achieved a validation accuracy of $9 8 . 5 2 \%$ and a test accuracy of $9 7 . 9 2 \%$ . The performance comparison between the baseline model and the distilled model is summarized in Table VII. The distilled model demonstrates a significant improvement over the baseline model, achieving higher validation and test accuracies. The public dataset, with its diverse characteristics, provides a robust platform for evaluating model performance across varied conditions. The results obtained align with previous

TABLE VII EVALUATION RESULTS OF THE BASELINE MODEL AND DISTILLED MODEL ON THE PUBLIC DATASET   

<table><tr><td>Model</td><td>Val/%</td><td>Test/%</td></tr><tr><td>Baseline Model</td><td>93.51</td><td>93.48</td></tr><tr><td>Distilled Model</td><td>98.56</td><td>97.92</td></tr></table>

findings, reinforcing the notion that while lightweight models can effectively process DVS signal patterns under similar sampling conditions, their generalizability is limited. However, KD can significantly enhance this generalizability.

# B. Implementation Evaluation

We conduct a performance evaluation of the proposed quantization method on the resulting KD-improved models. The entire model is quantized together, meaning that all weights are quantized to the same number of shift parameters. During the quantization process, we iterate through different values of the number of shift parameters, ranging from 1 to 10. This enables us to assess and analyze the performance of the model across different degrees of quantization, thus allowing us to identify the optimal balance between compression level and performance degradation. The results of the quantization process are presented in Fig. 10(a), which shows the performance of the quantized models on the validation set. Based on the results, it can be determined that the optimal number of shift parameters to be used is three. This allows the compressed model to achieve the same performance as the original model. To validate the generalizability of the model, the quantization process is further assessed on the test dataset, as demonstrated in Fig. 10(b). The results clearly indicate that the compressed model performs comparably to the original model, without any noticeable degradation in generalizability. This choice of quantization configuration effectively preserves all the essential information of the model while achieving the desired performance on the test dataset.

The encoding process is then performed to optimize the onchip storage. It is carried out on a layer-wise basis, which means that the parameters of the same layer are encoded together using the same bias. To determine the optimal number of bits used for encoding, we conduct iterations ranging from 1 to 8. The results obtained from the validation dataset, as depicted in Fig. 11(a), indicate that employing a 3-bit encoding scheme achieves lossless compression. Furthermore, the encoding process is performed on the test dataset and visualized in Fig. 11(b). It is evident that the encoding procedure brings a certain degree of performance degradation in terms of the generalizability of the model. Nevertheless, despite this influence, it is worth noting that the impact remains stable and minimal. Such stability in performance degradation implies that the encoding process does not significantly influence the overall performance of the model.

It is clear that the proposed approach offers an effective solution for achieving compression, with only a minimal impact on the generalizability of the model, as shown by the aforementioned results. We can then calculate the compression rate using the following information: the model initially

![](images/12a40032e833cf4deb95c7f31eea73a6d62a73b530b8f331950b20558c26cd03.jpg)

![](images/ec7af370912b237918e207bcfa577c825e7d5c60b8d3c21b4ecb7c4cd22854b5.jpg)  
  
  
Fig. 10. Change in accuracy with number of shift parameters. (a) Accuracy change on the validation set. (b) Accuracy change on the test set.

TABLE VIII PERFORMANCE OF THE MODELS ON DIFFERENT HARDWARE   

<table><tr><td>Model</td><td>Inference time on CPU/ms</td><td>Inference time on GPU/ms</td><td>Inference time on FPGA/ms</td></tr><tr><td>ResNet-34</td><td>1.846</td><td>0.375</td><td>-</td></tr><tr><td>Quantized CNN</td><td>0.254</td><td>0.178</td><td>0.083</td></tr></table>

consists of 30 771 32-bit floating-point format parameters, and each weight is compressed into three 3-bit shift parameters. Consequently, the compression rate can be calculated: $3 ~ \times$ $3 / 3 2 \times 1 0 0 \% = 2 8 . 1 2 5 \%$ . Additionally, the proposed compression scheme has been adapted to the shift-add structure, further enhancing the overall system performance.

The optimized model is then implemented with proposed FPGA-based hardware acceleration scheme. To evaluate the proposed scheme, we use the state-of-the-art CPU and GPU as the baseline performance. Here, the utilized CPU is Intel i9-14900, GPU is Nvidia GTX 4090. The average inference time of them is shown in Table VIII. The FPGA chip utilized here is Xilinx ZCU15eg. For quick development and fast implementation, the design is built with Xilinx high level HLS. The final design achieved a latency of 25 112 cycles running at a frequency of $3 0 3 ~ \mathrm { M H z }$ . The inference time of the system can be calculated as $2 5 1 1 2 \times 1 / ( 3 0 3 \times 1 0 6 ) \approx 0 . 0 8 3 ~ \mathrm { m s }$ . The sample time for each data frame is 256 ms, allowing the system

![](images/a7fd2ddf19d4b925d5b4b06e8cedba0c572474dc0d5bc8ae0f9d91badc063e03.jpg)

![](images/a71bf95f4d2254719ef456b0079265437f29433311e91dcbc8619976d6c37bc9.jpg)  
  
(b)   
Fig. 11. Change in accuracy with number of bits used for encoding. (a) Accuracy change on the validation set. (b) Accuracy change on the test set.

to process 3 084 frames within this interval. This processing capacity is equivalent to handling the data generated when the system monitors a fiber with a length of $1 2 . 5 \times 3 0 8 4 =$ $3 8 5 5 0 \mathrm { m }$ . Therefore, the system can achieve real-time processing over a $3 8 \mathrm { - k m }$ fiber, which is longer than the $3 0 { \cdot } \mathrm { k m }$ fiber utilized for sampling the dataset. Based on bibliographical research, the achieved recognition time of 0.083 ms is the fastest reported so far in the field [2], [7]. Furthermore, in cases involving longer fibers, the system’s scalability can be enhanced through enhancing hardware performance, reducing sampling rate, and optimizing the network parameters. Better hardware enables the system to handle larger amounts of data with greater efficiency as demonstrated in the experiment. Additionally, optimizing the network parameters and reducing sampling rate helps lower the computational load, allowing for extended fiber lengths with the same system throughput. These strategies can help the system to scale efficiently, making it suitable for large-scale IoT applications.

The resource requirement of the design is shown in Table IX. Our design makes efficient use of on-chip resources like look-up tables (LUTs) and flip-flops (FFs), allowing for high parallelism without being limited by the amount of DSP resources available. This optimization enables our system to achieve a higher performance compared with the CPU and GPU solutions. Although the parallel design vastly increases

TABLE IX HARDWARE RESOURCE UTILIZED   

<table><tr><td>Resource</td><td>Utilization</td><td>Available</td></tr><tr><td>LUT</td><td>280828</td><td>341280</td></tr><tr><td>FF</td><td>257011</td><td>682560</td></tr><tr><td>DSP</td><td>0</td><td>3528</td></tr><tr><td>BRAM</td><td>11</td><td>744</td></tr><tr><td>URAM</td><td>0</td><td>112</td></tr></table>

the hardware resources and hardware components running at the same time, our design still maintain at a relatively low power consumption level. AMD power estimator (XPE) is used to analyze the power consumption of the design. It takes 6.4 W when running, with only $0 . 7 5 0 \mathrm { ~ W ~ }$ power requirement when static. By contrast, the total graphic power (TGP) of GPU used here is 450 W, which is the power needed for the GPU to fully operate.

# IV. CONCLUSION

This article addresses the throughput limitations of DVS systems, which hinder the implementation of real-time recognition over long-distance fibers, which is essential for deploying DVS technology in smart IoT applications. To overcome this challenge, we propose using shallow CNN models as a more resource-efficient alternative to DLMs. We identify the issue of limited generalizability in lightweight models and address it by applying KD techniques to enhance their performance. Additionally, we propose a novel hardware acceleration scheme based on FPGAs to accelerate model inference. Our approach achieves a significant reduction in inference time, which is 2.14 times faster than state-of-theart GPU implementations and 4.52 times faster than CPU implementations, making it the fastest recognition method reported in this field to date. With this system, we enable realtime recognition over fibers up to $3 8 ~ \mathrm { k m }$ long, advancing the capabilities of DVS technology and its practical application as smart IoT systems.

While KD has proven effective in improving the performance of lightweight models, its success is inherently dependent on the teacher model’s ability to capture complex patterns under diverse conditions. In situations with intense noise or novel types of disturbances, the teacher model’s representations may fail to accurately capture the vibration patterns, leading to suboptimal guidance for the student model.

Furthermore, while this study focuses on DVS for largearea vibration sensing, the proposed real-time DVS system has the potential to be adapted for other IoT applications. For example, it could be applied in smart home systems by installing fibers around the home for peripheral monitoring or in health monitoring by attaching fibers to the human body to measure vital signs, such as heartbeats. To further enhance its practicality, future work should explore optimizations in energy consumption, particularly for large-scale industrial applications. Energy-efficient solutions are not only essential for reducing operational costs but also critical for ensuring the scalability and sustainability of IoT systems in such deployments. Moreover, combining these advancements with hybrid machine learning models could improve the system’s ability to

handle complex patterns or rare events, such as earthquakes, further expanding its generalizability and applicability across diverse IoT applications.

# REFERENCES

[1] J. Yang et al., “Railway intrusion events classification and location based on deep learning in distributed vibration sensing,” Symmetry, vol. 14, p. 2552, Dec. 2022.   
[2] N. Yang, Y. Zhao, and J. Chen, “Real-time $\Phi$ -OTDR vibration event recognition based on image target detection,” Sensors, vol. 22, p. 1127, Feb. 2022.   
[3] C. Lyu, Z. Huo, X. Cheng, J. Jiang, A. Alimasi, and H. Liu, “Distributed optical fiber sensing intrusion pattern recognition based on GAF and CNN,” J. Lightw. Technol., vol. 38, no. 15, pp. 4174–4182, Aug. 1, 2020.   
[4] X. Huang, B. Wang, K. Liu, and T. Liu, “An event recognition scheme aiming to improve both accuracy and efficiency in optical fiber perimeter security system,” J. Lightw. Technol., vol. 38, no. 20, pp. 5783–5790, Oct. 15, 2020.   
[5] Y. Yang, Y. Li, T. Zhang, Y. Zhou, and H. Zhang, “Early safety warnings for long-distance pipelines: A distributed optical fiber sensor machine learning approach,” in Proc. AAAI Conf. Artif. Intell., 2021, pp. 14991–14999   
[6] C. Zhu, Y. Pu, K. Yang, Q. Yang, and C. L. P. Chen, “Distributed optical fiber intrusion detection by image encoding and SwinT in multi-interference environment of long-distance pipeline,” IEEE Trans. Instrum. Meas., vol. 72, pp. 1–12, May 2023.   
[7] H. Wu et al., “Smart fiber-optic distributed acoustic sensing (sDAS) with multitask learning for time-efficient ground listening applications,” IEEE Internet Things J., vol. 11, no. 5, pp. 8511–8525, Mar. 2024.   
[8] S. Zhang et al., “Adaptive decentralized ai scheme for signal recognition of distributed sensor systems,” Opto-Electron. Adv., vol. 7, no. 12, 2024, Art. no. 240119-1.   
[9] C. Xu, J. Guan, M. Bao, J. Lu, and W. Ye, “Pattern recognition based on enhanced multifeature parameters for vibration events in $\varphi$ -OTDR distributed optical fiber sensing system,” Microw. Opt. Technol. Lett., vol. 59, pp. 3134–3141, Dec. 2017.   
[10] H. Wu, Y. Qian, W. Zhang, and C. Tang, “Feature extraction and identification in distributed optical-fiber vibration sensing system for oil pipeline safety monitoring,” Photonic Sens., vol. 7, pp. 305–310, Dec. 2017.   
[11] H. Wu, X. Liu, Y. Xiao, and Y. Rao, “A dynamic time sequence recognition and knowledge mining method based on the hidden Markov models (HMMs) for pipeline safety monitoring with $\Phi$ -OTDR,” J. Lightw. Technol., vol. 37, no. 19, pp. 4991–5000, Oct. 1, 2019.   
[12] C. Cao, X. Fan, Q. Liu, and Z. He, “Practical pattern recognition system for distributed optical fiber intrusion monitoring system based on phasesensitive coherent OTDR,” in Proc. Asia Commun. Photonics Conf., 2015, Art. no. ASu2A.145.   
[13] X. Wang, Y. Liu, S. Liang, W. Zhang, and S. Lou, “Event identification based on random forest classifier for $\Phi$ -OTDR fiber-optic distributed disturbance sensor,” Infrared Phys. Technol., vol. 97, pp. 319–325, Mar. 2019.   
[14] H. Jia, S. Liang, S. Lou, and X. Sheng, “A $\$ 123$ -nearest neighbor algorithm-based near category support vector machine method for event identification of $\varphi$ -OTDR,” IEEE Sensors J., vol. 19, no. 10, pp. 3683–3689, May 2019.   
[15] W. Xu et al., “Real-time multi-class disturbance detection for $\phi$ -OTDR based on YOLO algorithm,” Sensors, vol. 22, no. 5, p. 1994, 2022.   
[16] K. Seshadri, B. Akin, J. Laudon, R. Narayanaswami, and A. Yazdanbakhsh, “An evaluation of edge TPU accelerators for convolutional neural networks,” in Proc. IEEE Int. Symp. Workload Charact. (IISWC), 2022, pp. 79–91.   
[17] M. Qasaimeh, K. Denolf, J. Lo, K. Vissers, J. Zambreno, and P. H. Jones, “Comparing energy efficiency of CPU, GPU and FPGA implementations for vision kernels,” in Proc. IEEE Int. Conf. Embed. Softw. Syst. (ICESS), 2019, pp. 1–8.   
[18] J. Meng, S. K. Venkataramanaiah, C. Zhou, P. Hansen, P. Whatmough, and J.-S. Seo, “FixyFPGA: Efficient FPGA accelerator for deep neural networks with high element-wise sparsity and without external memory access,” in Proc. 31st Int. Conf. Field-Programm. Logic Appl. (FPL), 2021, pp. 9–16.   
[19] G. Hinton, O. Vinyals, and J. Dean, “Distilling the knowledge in a neural network,” 2015, arXiv:1503.02531.

[20] H.-J. Kang, “AoCStream: All-on-chip CNN accelerator with streambased line-buffer architecture,” in Proc. ACM/SIGDA Int. Symp. Field Programm. Gate Arrays, 2022, pp. 1–7.   
[21] T. Aarrestad et al., “Fast convolutional neural networks on FPGAs with hls4ml,” Mach. Learn., Sci. Technol., vol. 2, no. 4, 2021, Art. no. 45015.   
[22] A. Anupreetham et al., “End-to-end FPGA-based object detection using pipelined CNN and non-maximum suppression,” in Proc. 31st Int. Conf. Field-Programm. Logic Appl. (FPL), 2021, pp. 76–82.   
[23] W. Pang, C. Wu, and S. Lu, “An energy-efficient implementation of group pruned CNNs on FPGA,” IEEE Access, vol. 8, pp. 217033–217044, 2020.   
[24] V. Sze, Y.-H. Chen, T.-J. Yang, and J. S. Emer, “Efficient processing of deep neural networks: A tutorial and survey,” Proc. IEEE, vol. 105, no. 12, pp. 2295–2329, Dec. 2017.   
[25] M. D. Todd, “2—Sensor data acquisition systems and architectures,” in Sensor Technologies for Civil Infrastructures (Woodhead Publishing Series in Electronic and Optical Materials), vol. 55, M. Wang, J. Lynch, and H. Sohn, Eds., Sawston, U.K.: Woodhead Publ., 2014, pp. 23–56.   
[26] S. Watanabe and H. Yamana, “Overfitting measurement of deep neural networks using no data,” in Proc. IEEE 8th Int. Conf. Data Sci. Adv. Anal. (DSAA), 2021, pp. 1–10.   
[27] M. M. Bejani and M. Ghatee, “A systematic review on overfitting control in shallow and deep neural networks,” Artif. Intell. Rev., vol. 54, pp. 6391–6438, Dec. 2021.   
[28] Z. Ge, H. Wu, C. Zhao, and M. Tang, “High-accuracy event classification of distributed optical fiber vibration sensing based on time–space analysis,” Sensors, vol. 22, no. 5, p. 2053, 2022.   
[29] X. Jin et al., “Pattern recognition of distributed optical fiber vibration sensors based on Resnet 152,” IEEE Sensors J., vol. 23, no. 17, pp. 19717–19725, Sep. 2023.   
[30] R. Yao, J. Li, J. Zhang, and Y. Wei, “Vibration event recognition using SST-based $\phi$ -OTDR system,” Sensors, vol. 23, p. 8773, Oct. 2023.   
[31] J. Y. Li, R. Yao, J. Zhang, X. Zhang, M. Ren, and T. Ma, “Pipeline threat event identification based on GAF of distributed fiber optic signals,” IEEE Sensors J., vol. 23, no. 21, pp. 26796–26803, Nov. 2023.   
[32] X. Cao, Y. Su, Z. Jin, and K. Yu, “An open dataset of $\phi$ -OTDR events with two classification models as baselines,” Results Opt., vol. 10, Feb. 2023, Art. no. 100372.

Zhongyao Luo received the B.Eng. degree in electronics and computer science from the University of Edinburgh, Edinburgh, U.K., in 2020. He is currently pursuing the Ph.D. degree with the School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan, China.

His current research interests include distributed optical fiber sensing and machine learning.

Hao Wu received the B.S., M.S., and Ph.D. degrees from Huazhong University of Science and Technology (HUST), Wuhan, China, in 2013, 2016, and 2019, respectively.

His postdoctoral research with HUST was focused on the machine earning algorithms for distributed optical fiber sensing. Since 2024, he has been a Research Associate with HUST. His current research interests are the integration of artificial intelligence and optical fiber.

Zhao Ge received the B.S. degree from Jianghan University, Wuhan, China, in 2019, and the M.D. degree from Huazhong University of Science and Technology, Wuhan, in 2022, where he is currently pursuing the Ph.D. degree with the School of Optical and Electronic Information.

Ming Tang (Senior Member, IEEE) received the B.Eng. degree from Huazhong University of Science and Technology (HUST), Wuhan, China, in 2001, and the Ph.D. degree from Nanyang Technological University, Singapore, in 2005.

His postdoctoral research with the Network Technology Research Center, Singapore, was focused on the optical fiber amplifier. In 2009, he was a Research Scientist with the Tera-Photonics Group, RIKEN, Saitama, Japan. Since 2011, he has been a Professor with HUST. His current research interests include optical fiber-based linear and nonlinear effects for communication and sensing applications.