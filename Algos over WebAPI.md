Algo type is specified in algo_strategy proto field of related messages,
its value shall be as Abbreviation from algos list below, value is case sensitive.

Algo parameters are specified as a named values collection extra_attributes repeated field.

It is possible to request ATDL definition via WebAPI proto, see InformationRequest.algo_strategy_definition_request;
that may be helpful for getting parameter types, their default values, allowable values and some basic validation rules
(for example some parameter values must be greater than 0).

It is suggested to re-request ATDL definitions periodically
because they may change over time. There is no ATDL versioning, in other words, only most recent version is usable at
at a time.

There is one peculiar thing about parameter names in ATDL and actual names expected by CQGGW: ALGO_ prefix
has to be added to every name. So, if parameter name in ATDL is CQG_end_time, its name in extra_attributes
shall be ALGO_CQG_end_time. Parameter names are case sensitive.

Below, all parameters are listed as 'Name, underlying type (what is expected as its string value'

* CQG Arrival Price
Abbreviation: CQG ARRIVALPRICE
Parameters:
ALGO_CQG_cost_model                char
ALGO_CQG_drift_override            double
ALGO_CQG_economic_model            char
ALGO_CQG_end_time                  UTCTimestamp in YYYYMMDD-HH:MM:SS format
ALGO_CQG_gamma_factor              double
ALGO_CQG_i_would_price             price (double value, multiple of instrument's tick size)
ALGO_CQG_impact_model              char
ALGO_CQG_join_threshold            double
ALGO_CQG_max_chase_ticks           int
ALGO_CQG_max_duration_in_minutes   int
ALGO_CQG_min_duration              double
ALGO_CQG_opposite_size_ratio       double
ALGO_CQG_opposite_size_raw         int
ALGO_CQG_payup_model               char
ALGO_CQG_percent_of_volume         double
ALGO_CQG_slippage_tolerance        double
ALGO_CQG_start_time                UTCTimestamp
ALGO_CQG_success_probability       double
ALGO_CQG_tick_offset               int
ALGO_CQG_vol_override              float

* CQG Iceberg Slicer
Abbreviation: CQG ICESLICER
Parameters:
ALGO_CQG_end_time                UTCTimestamp
ALGO_CQG_i_wont_ticks            int
ALGO_CQG_interval_in_seconds     int
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_max_duration_in_minutes int
ALGO_CQG_max_show_quantity       int
ALGO_CQG_num_slices              int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_payup_model             char
ALGO_CQG_start_time              UTCTimestamp
ALGO_CQG_success_probability     double

* CQG Offset Payup
Abbreviation: CQG OFFSETPAYUP
Parameters:
ALGO_CQG_join_threshold      double
ALGO_CQG_max_chase_ticks     int
ALGO_CQG_opposite_size_ratio double
ALGO_CQG_opposite_size_raw   int
ALGO_CQG_payup_model         char
ALGO_CQG_success_probability double
ALGO_CQG_tick_offset         int

* CQG Offset Tick
Abbreviation: CQG OFFSETTICK
Parameters:
ALGO_CQG_enable_imbalance      bool (Y|N)
ALGO_CQG_imbalance_ratio       double
ALGO_CQG_max_chase_ticks       int
ALGO_CQG_opposite_size_ratio   double
ALGO_CQG_opposite_size_raw     int
ALGO_CQG_tick_offset           int
ALGO_CQG_trade_toward_behavior char

* CQG Payup
Abbreviation: CQG PAYUP
Parameters:
ALGO_CQG_join_threshold      double
ALGO_CQG_max_chase_ticks     int
ALGO_CQG_opposite_size_ratio double
ALGO_CQG_opposite_size_raw   int
ALGO_CQG_payup_model         char
ALGO_CQG_success_probability double

* CQG Peg
Abbreviation: CQG PEG
Parameters:
ALGO_CQG_tick_offset int

* CQG Randomized Iceberg
Abbreviation: CQG RICEBERG
Parameters:
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_pause_between_orders_ms int
ALGO_CQG_payup_model             char
ALGO_CQG_rand_max                int
ALGO_CQG_rand_min                int
ALGO_CQG_show_quantity           int
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int
ALGO_CQG_use_mbo                 bool (Y|N)

* CQG Randomized TWAP
Abbreviation: CQG RTWAP
ALGO_CQG_end_time                UTCTimestamp
ALGO_CQG_i_would_price           price
ALGO_CQG_impact_model            char
ALGO_CQG_interval_in_seconds     int
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_max_duration_in_minutes int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_order_size_override     int
ALGO_CQG_payup_model             char
ALGO_CQG_rand_max                int
ALGO_CQG_rand_min                int
ALGO_CQG_start_time              UTCTimestamp
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int
ALGO_CQG_use_mbo                 bool (Y|N)

* CQG Stop-Limit Arrival Price
Abbreviation: CQG SLARRIVAL
Parameters:
ALGO_CQG_cost_model              char
ALGO_CQG_drift_override          double
ALGO_CQG_economic_model          char
ALGO_CQG_end_time                UTCTimestamp
ALGO_CQG_gamma_factor            double
ALGO_CQG_i_would_price           price
ALGO_CQG_impact_model            char
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_max_duration_in_minutes int
ALGO_CQG_min_duration            double
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_payup_model             char
ALGO_CQG_percent_of_volume       double
ALGO_CQG_price_type              char
ALGO_CQG_slippage_tolerance      double
ALGO_CQG_start_time              UTCTimestamp
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int
ALGO_CQG_vol_override            double

* CQG Stop-Limit Iceberg
Abbreviation: CQG SLICEBERG
Parameters:
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_pause_between_orders_ms int
ALGO_CQG_payup_model             char
ALGO_CQG_price_type              char
ALGO_CQG_rand_max                int
ALGO_CQG_rand_min                int
ALGO_CQG_show_quantity           int
ALGO_CQG_success_probability     double
ALGO_CQG_use_mbo                 bool (Y|N)

* CQG Stop-Limit Sniper
Abbreviation: CQG SLSNIPE
Parameters:
ALGO_CQG_i_wont_ticks            int
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_pause_between_orders_ms int
ALGO_CQG_payup_model             char
ALGO_CQG_price_type              char
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int

* CQG Sniper
Abbreviation: CQG SNIPE
Parameters:
ALGO_CQG_i_wont_ticks            int
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_pause_between_orders_ms int
ALGO_CQG_payup_model             char
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int

* CQG Tick
Abbreviation: CQG TICK
Parameters:
ALGO_CQG_enable_imbalance      bool (Y|N)
ALGO_CQG_imbalance_ratio       double
ALGO_CQG_max_chase_ticks       int
ALGO_CQG_opposite_size_ratio   double
ALGO_CQG_opposite_size_raw     int
ALGO_CQG_trade_toward_behavior char

* CQG TWAP
Abbreviation: CQG TWAP
Parameters:
ALGO_CQG_end_time                UTCTimestamp
ALGO_CQG_i_would_price           price
ALGO_CQG_impact_model            char
ALGO_CQG_interval_in_seconds     int
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_max_duration_in_minutes int
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_order_size_override     int
ALGO_CQG_payup_model             char
ALGO_CQG_start_time              UTCTimestamp
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int

* CQG VWAP
Abbreviation: CQDG VWAP
Parameters:
ALGO_CQG_bucket_interval_minutes int
ALGO_CQG_economic_model          char
ALGO_CQG_end_time                UTCTimestamp
ALGO_CQG_i_would_price           price
ALGO_CQG_impact_model            char
ALGO_CQG_join_threshold          double
ALGO_CQG_max_chase_ticks         int
ALGO_CQG_max_duration_in_minutes int
ALGO_CQG_max_uncertainty_width   double
ALGO_CQG_opposite_size_ratio     double
ALGO_CQG_opposite_size_raw       int
ALGO_CQG_payup_model             char
ALGO_CQG_percent_of_volume       double
ALGO_CQG_start_time              UTCTimestamp
ALGO_CQG_success_probability     double
ALGO_CQG_tick_offset             int
ALGO_CQG_time_horizon_days       int
ALGO_CQG_wake_interval_seconds   int