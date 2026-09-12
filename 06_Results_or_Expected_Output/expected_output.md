# Expected Output

## Target Metrics
- **Accuracy:** ≥ 90%
- **Precision:** ≥ 90%
- **Recall:** ≥ 90%
- **F1-Score:** ≥ 90%
- **ROC-AUC:** ≥ 0.90
- **False Positive Rate:** ≤ 5%

## Baseline Comparison
| Model | Expected Accuracy |
|-------|-------------------|
| Source-Only | ~85% |
| Opcode-Only | ~87% |
| CFG-Only | ~86% |
| **Proposed Multimodal** | **≥ 90%** |

## Output Format
The prototype will output:
- Vulnerability detected: Yes/No
- Vulnerability type (if detected)
- Confidence score
