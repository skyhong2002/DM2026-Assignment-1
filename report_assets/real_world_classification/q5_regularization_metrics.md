| setting | reg_type | reg_lambda | Accuracy | Precision | Recall | F1-score | loss_curve_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No Regularization | none | 0.0000 | 0.7200 | 0.7125 | 0.7500 | 0.7308 | report_assets/real_world_classification/q5_loss_no_regularization.png |
| L2 (lambda=0.01) | l2 | 0.0100 | 0.7200 | 0.7125 | 0.7500 | 0.7308 | report_assets/real_world_classification/q5_loss_l2_lambda_0.01.png |
| L2 (lambda=1) | l2 | 1.0000 | 0.7400 | 0.7342 | 0.7632 | 0.7484 | report_assets/real_world_classification/q5_loss_l2_lambda_1.png |
| L2 (lambda=100) | l2 | 100.0000 | 0.5067 | 0.5067 | 1.0000 | 0.6726 | report_assets/real_world_classification/q5_loss_l2_lambda_100.png |