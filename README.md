# A First Look at Model Supply Chain: From the Risk Perspective

## RQ1: Usage Analysis.
#### Distribution and Downloads of Models

|                | M_b      | M_d      | M_r      | M_i        | M        |
|----------------|---------|---------|---------|-----------|----------|
| **Size**       | 49,648  | 540,838 | 566,022 | 1,251,376 | 1,817,398 |
| **Downloads**  | 1.4e9   | 2.7e8   | 1.5e9   | 2.5e8     | 1.7e9     |

#### Distribution of Derived Models
| Model | Count      | Percentage |
|-----------|------------|------------|
| M_f| 427,475    | 79.0%      |
| M_q | 100,564    | 18.6%      |
| M_m | 12,799     | 2.4%       |
| M_d | 540,838    | 100%       |

#### Detailed Distribution of Model Tasks by Dependency Types

| **Relation** | **NLP**            | **CV**           | **Other**        | **Total** |
|--------------|--------------------|------------------|------------------|-----------|
| Fine-Tune    | **109,591** (57.8%) | 63,721 (33.6%)   | 16,139 (8.6%)    | 189,451   |
| Merge        | **11,092** (94.0%)  | 551 (4.7%)       | 160 (1.3%)       | 11,803    |
| Quantize     | **31,855** (93.3%)  | 687 (2.0%)       | 1,615 (4.7%)     | 34,157    |

#### Top-10 Models by In-Degree and Out-Degree
| **In-Degree** Model                                | Task             | deg_in(m) | **Out-Degree** Model                              | Task             | deg_out(m) |
|-----------------------------------------------------|------------------|--------------------------|----------------------------------------------------|------------------|---------------------------|
| Novaciano/BAHAMUTH-PURGED-3.2-1B                    | text-generation  | 65                       | Qwen/Qwen1.5-0.5B                                 | text-generation  | 32,497                    |
| Novaciano/BAHAMUTH-PURGED-3.2-1B-Q6_K-GGUF          | --               | 65                       | black-forest-labs/FLUX.1-dev                      | text-to-image    | 32,173                    |
| QuantFactory/Loki-v2.6-8b-1024k-GGUF               | --               | 57                       | Qwen/Qwen1.5-1.8B                                 | text-generation  | 30,580                    |
| PJMixers-Archive/LLaMa-3-CursedStock-v1.6-8B        | text-generation  | 52                       | google/gemma-2b                                   | text-generation  | 23,792                    |
| PJMixers-Archive/LLaMa-3-CursedStock-v2.0-8B        | text-generation  | 47                       | google/gemma-7b                                   | text-generation  | 9,569                     |
| QuantFactory/L3-Deluxe-Scrambled-Eggs-On-Toast      | text-generation  | 36                       | distilbert/distilbert-base-uncased                | fill-mask        | 9,205                     |
| Casual-Autopsy/L3-Deluxe-Scrambled-Eggs-On-Toast    | text-generation  | 36                       | stabilityai/stable-diffusion-xl-base-1.0          | text-to-image    | 8,266                     |
| PJMixers-Archive/LLaMa-3-CursedStock-v1.8-8B        | text-generation  | 34                       | Qwen/Qwen1.5-7B                                   | text-generation  | 6,450                     |
| SanXM1/Driftwood-12B                               | text-generation  | 25                       | google-bert/bert-base-uncased                     | fill-mask        | 5,483                     |
| mergekit-community/L3.1-Athena-l-8B                 | text-generation  | 25                       | aubmindlab/bert-base-arabertv02                   | fill-mask        | 3,997                     |

#### Distribution of Chain Length
<img src="fig/chain_length_distribution.png" alt="Distribution of Chain Length" width="1000" />





#### Proportion of Finetune-Dominant, Merge-Dominant, and Quantize-Dominant Chains

| Chain Type          | Count |
|----------------------|--------------------|
| Finetune-dominant    | xxx(45.4%)              |
| Merge-dominant       | xxx(48.5%)             |
| Quantize-dominant    | xxx (6.1%)              |
| **Total Chains**     | 1,008,871          |

####  Diversity of Operation within Model Chains
| Operation Diversity            | Count |
|---------------------------------|------------|
| Single operation type           | xxx(45.9%)      |
| Exactly two operation types     | xxx(26.1%)      |
| All three operation types       | xxx(28.0%)      |

#### Top-10 Chains with Their Operation Ratios

| **Root Model**                                         | **Length** | **FineTune**  | **Merge**   | **Quantize**   |
|---------------------------------------------------------|-----------:|---------:|---------:|---------:|
| CohereLabs/c4ai-command-r-v01                           | 40         | **100%** | 0%       | 0%       |
| vicgalle/Configurable-Llama-3-8B-v0.2                   | 28         | 18.52%   | **81.48%** | 0%     |
| recoilme/recoilme-gemma-2-9B-v0.2                       | 23         | 0%       | **100%** | 0%       |
| cgato/Nemo-12b-Humanize-KTO-Experimental-Latest         | 22         | 4.76%    | **95.24%** | 0%     |
| fblgit/una-cybertron-7b-v2-bf16                         | 21         | 30.00%   | **65.00%** | 5.00%  |
| ericjiliangli/t5-small-news-summarization               | 21         | **100%** | 0%       | 0%       |
| answerdotai/ModernBERT-Large-Instruct                   | 21         | **100%** | 0%       | 0%       |
| lukasdrg/clinical_longformer_same_tokens_180k           | 20         | **100%** | 0%       | 0%       |
| berkeley-nest/Starling-LM-7B-alpha                      | 19         | **55.56%** | 38.89% | 5.56%   |
| FelixChao/Sectumsempra-7B-DPO                           | 18         | **52.94%** | 41.18% | 5.88%   |


#### Distribution of Cluster Size
<img src="fig/chain_length_distribution.png" alt="Distribution of Cluster Size" width="1000" />

### RQ2: Evolution Analysis.
### RQ3: Quality Analysis.
### RQ4: Risk Analysis.