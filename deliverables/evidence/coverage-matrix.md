# Coverage Matrix (Dimensions V01 - V15)

- **Total Dimensions**: 4 (D1, D2, D3, D4)
- **Total Values**: 15 (V01 to V15)
- **Total Test Combinations**: 15 (C01 to C15)
- **Status**: Complete Purposeful Coverage

## Dimension-by-Value Mapping Table

| Dimension ID & Name | Value ID | Value Name | Combination IDs Covered | Count | Status |
|---|---|---|---|---|---|
| **D1 Question Intent** | V01 | In-scope concept | C01, C07, C08, C09, C10, C12, C13 | 7 | COVERED |
| | V02 | Comparison | C02, C11 | 2 | COVERED |
| | V03 | Application | C03, C14, C15 | 3 | COVERED |
| | V04 | Answer-seeking | C04 | 1 | COVERED |
| | V05 | Out-of-scope | C05, C06 | 2 | COVERED |
| **D2 Corpus Support** | V06 | Fully supported in one source | C01, C03, C04, C07, C08, C10, C15 | 7 | COVERED |
| | V07 | Supported across multiple sources | C02, C09, C11, C14 | 4 | COVERED |
| | V08 | Partially supported | C12 | 1 | COVERED |
| | V09 | Unsupported | C05, C06, C13 | 3 | COVERED |
| **D3 Interaction Clarity**| V10 | Clear | C01, C02, C03, C04, C05, C10, C11, C12, C13 | 9 | COVERED |
| | V11 | Ambiguous terminology | C06, C07, C15 | 3 | COVERED |
| | V12 | Multi-intent | C09, C14 | 2 | COVERED |
| | V13 | Referentially underspecified | C08 | 1 | COVERED |
| **D4 Premise Validity** | V14 | Valid premise | C01, C02, C03, C04, C05, C06, C07, C08, C09, C12, C13, C14 | 12 | COVERED |
| | V15 | Misleading or false premise | C10, C11, C15 | 3 | COVERED |

## Risk and Set-Type Distribution

| Set Type | Combinations | Count | Percentage |
|---|---|---|---|
| `representative` | C01, C02, C03, C05, C09, C14 | 6 | 40.0% |
| `challenge` | C04, C06, C07, C08, C12 | 5 | 33.3% |
| `high-risk` | C10, C11, C13, C15 | 4 | 26.7% |
| **Total** | **C01 - C15** | **15** | **100.0%** |
