# IDB30102_GroupAL_BlockchainSecurity

## Research Title
**Smart Contract Vulnerability Detection for Improved Detection Accuracy in Ethereum Blockchain**

## Group Number
Group AL

## Group Members
| Name | Student ID |
|------|------------|
| Ahmad Zaim Zharfan bin Mohd Zaidi | 52215225268 |
| Muhammad Aiman Syafiq bin Selamat | 52215226146 |

## Assigned Research Area
Blockchain Security (Group L)

## Research Problem
Current AI-based vulnerability detection approaches rely on single code representations, limiting detection accuracy and generalisability. Additionally, blockchain security research is fragmented, with solutions addressing individual threats in isolation.

## Research Aim
To develop and evaluate a prototype module for smart contract vulnerability detection that improves detection accuracy compared to single-representation approaches.

## Research Objectives
1. To identify common smart contract vulnerabilities and existing detection approaches.
2. To design a prototype module that integrates source code, opcode sequences, and control-flow graphs.
3. To evaluate the proposed prototype on Ethereum smart contract benchmark datasets.

## Proposed Solution
A multimodal deep learning prototype module that integrates source code, opcode sequences, and control-flow graphs through separate deep learning encoders, followed by a decision fusion mechanism.

## Research Methodology
- **Methodology:** Design Science Research (Peffers DSRM)
- **Development Model:** Prototyping

## Evaluation Plan
- **Baseline:** Single-representation models (source-only, opcode-only, CFG-only)
- **Dataset:** Ethereum smart contract benchmark datasets
- **Metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC, False Positive Rate

## Proposed Architecture
See `03_Architecture_and_Flowchart/` for the architecture diagram and flowchart.

## Technical Components
- **Programming Language:** Python
- **Libraries:** TensorFlow/PyTorch, Scikit-learn, NumPy, Pandas
- **Tools:** Git, GitHub, Jupyter Notebook

## Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/IDB30102_GroupAL_BlockchainSecurity.git
