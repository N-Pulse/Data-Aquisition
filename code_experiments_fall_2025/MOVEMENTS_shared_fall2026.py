"""
MOVEMENTS — fall 2026 (101 videos from videos_measures_720p).

For each input :
  code          : MOVEMENT code (identical whatever the baseline)
  file          : exact name of the video (.mov).
  label         : how it is displayed
  baseline_code : ORIENTATION of the hand (1 = up, 2 = side, 3 = down).
  start_state   : initial state of the hand ("open" or "closed").

Baseline complete (1-6) = baseline_code + 3 if start_state == "closed" ;
see baselines.baseline_of().

Name rule : "close_hand" in video name = start with closed hand ;
else = start with open hand. Movements that OPEN (open_*, openhand_*)
start with closed hand ; movements that CLOSE or GRASP (close_*, closetofist_*,
grasp*) start with open hand.
"""

MOVEMENTS_VERSION = "fall2026"

MOVEMENTS = {
    # --- orientation 1 (up), départ main ouverte ---
    '1_up_close_fourfingers_together_3sec': {'code': 1, 'file': '1_up_close_fourfingers_together_3sec.mov', 'label': 'Close four fingers together 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_index_3sec': {'code': 2, 'file': '1_up_close_index_3sec.mov', 'label': 'Close index 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_middle_3sec': {'code': 3, 'file': '1_up_close_middle_3sec.mov', 'label': 'Close middle 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_onlythumb_3sec': {'code': 4, 'file': '1_up_close_onlythumb_3sec.mov', 'label': 'Close only thumb 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_pinky_3sec': {'code': 5, 'file': '1_up_close_pinky_3sec.mov', 'label': 'Close pinky 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_ring_3sec': {'code': 6, 'file': '1_up_close_ring_3sec.mov', 'label': 'Close ring 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_thumb_3sec': {'code': 7, 'file': '1_up_close_thumb_3sec.mov', 'label': 'Close thumb 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_closetofist_allfingerstogether_fast_1sec': {'code': 10, 'file': '1_up_closetofist_allfingerstogether_fast_1sec.mov', 'label': 'Close to fist allfingerstogether fast 1 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_closetofist_allfingerstogether_3sec_maxforce': {'code': 11, 'file': '1_up_closetofist_allfingerstogether_3sec_maxforce.mov', 'label': 'Close to fist allfingerstogether max force 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_closetofist_allfingerstogether_3sec_normalforce': {'code': 12, 'file': '1_up_closetofist_allfingerstogether_3sec_normalforce.mov', 'label': 'Close to fist allfingerstogether normal force 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_closetofist_allfingerstogether_slow_3sec': {'code': 13, 'file': '1_up_closetofist_allfingerstogether_slow_3sec.mov', 'label': 'Close to fist allfingerstogether slow 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_grasp_donut_3sec': {'code': 15, 'file': '1_up_grasp_donut_3sec.mov', 'label': 'Grasp donut 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_wrist_dorsiflexion_maxforce_3sec': {'code': 28, 'file': '1_up_wrist_dorsiflexion_maxforce_3sec.mov', 'label': 'Wrist dorsiflexion max force 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_wrist_dorsiflexion_normalforce_3sec': {'code': 29, 'file': '1_up_wrist_dorsiflexion_normalforce_3sec.mov', 'label': 'Wrist dorsiflexion normal force 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_wrist_palmarflexion_maxforce_3sec': {'code': 30, 'file': '1_up_wrist_palmarflexion_maxforce_3sec.mov', 'label': 'Wrist palmarflexion max force 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_wrist_palmarflexion_normalforce_3sec': {'code': 31, 'file': '1_up_wrist_palmarflexion_normalforce_3sec.mov', 'label': 'Wrist palmarflexion normal force 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_close_onlythumb_palm_3sec': {'code': 32, 'file': '1_up_close_onlythumb_palm_3sec.mov', 'label': 'Close only thumb palm 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    '1_up_rotation_3sec': {'code': 37, 'file': '1_up_rotation_3sec.mov', 'label': 'Rotation 3 sec (up)', 'baseline_code': 1, 'start_state': 'open'},
    # --- orientation 1 (up), départ main fermée ---
    '1_up_open_fourfingers_together_3sec': {'code': 18, 'file': '1_up_open_fourfingers_together_3sec.mov', 'label': 'Open four fingers together 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_index_3sec': {'code': 19, 'file': '1_up_open_index_3sec.mov', 'label': 'Open index 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_middle_3sec': {'code': 20, 'file': '1_up_open_middle_3sec.mov', 'label': 'Open middle 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_onlythumb_3sec': {'code': 21, 'file': '1_up_open_onlythumb_3sec.mov', 'label': 'Open only thumb 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_pinky_3sec': {'code': 23, 'file': '1_up_open_pinky_3sec.mov', 'label': 'Open pinky 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_ring_3sec': {'code': 24, 'file': '1_up_open_ring_3sec.mov', 'label': 'Open ring 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_thumb_3sec': {'code': 25, 'file': '1_up_open_thumb_3sec.mov', 'label': 'Open thumb 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_openhand_fast_1sec': {'code': 26, 'file': '1_up_openhand_fast_1sec.mov', 'label': 'Open hand fast 1 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_openhand_slow_3sec': {'code': 27, 'file': '1_up_openhand_slow_3sec.mov', 'label': 'Open hand slow 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_wrist_close_hand_dorsiflexion_normalforce_3sec': {'code': 29, 'file': '1_up_wrist_close_hand_dorsiflexion_normalforce_3sec.mov', 'label': 'Wrist dorsiflexion normal force 3 sec, closed hand (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_wrist_close_hand_palmarflexion_normalforce_3sec': {'code': 31, 'file': '1_up_wrist_close_hand_palmarflexion_normalforce_3sec.mov', 'label': 'Wrist palmarflexion normal force 3 sec, closed hand (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_onlythumb_palm_3sec': {'code': 33, 'file': '1_up_open_onlythumb_palm_3sec.mov', 'label': 'Open only thumb palm 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_open_allfingers_together_3sec': {'code': 34, 'file': '1_up_open_allfingers_together_3sec.mov', 'label': 'Open all fingers together 3 sec (up)', 'baseline_code': 1, 'start_state': 'closed'},
    '1_up_close_hand_rotation_3sec': {'code': 37, 'file': '1_up_close_hand_rotation_3sec.mov', 'label': 'Rotation 3 sec, closed hand (up)', 'baseline_code': 1, 'start_state': 'closed'},
    # --- orientation 2 (side), départ main ouverte ---
    '2_side_close_fourfingers_together_3sec': {'code': 1, 'file': '2_side_close_fourfingers_together_3sec.mov', 'label': 'Close four fingers together 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_index_3sec': {'code': 2, 'file': '2_side_close_index_3sec.mov', 'label': 'Close index 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_middle_3sec': {'code': 3, 'file': '2_side_close_middle_3sec.mov', 'label': 'Close middle 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_onlythumb_3sec': {'code': 4, 'file': '2_side_close_onlythumb_3sec.mov', 'label': 'Close only thumb 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_pinky_3sec': {'code': 5, 'file': '2_side_close_pinky_3sec.mov', 'label': 'Close pinky 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_ring_3sec': {'code': 6, 'file': '2_side_close_ring_3sec.mov', 'label': 'Close ring 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_thumb_3sec': {'code': 7, 'file': '2_side_close_thumb_3sec.mov', 'label': 'Close thumb 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_closetofist_allfingerstogether_fast_1sec': {'code': 10, 'file': '2_side_closetofist_allfingerstogether_fast_1sec.mov', 'label': 'Close to fist allfingerstogether fast 1 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_closetofist_allfingerstogether_maxforce_3sec': {'code': 11, 'file': '2_side_closetofist_allfingerstogether_maxforce_3sec.mov', 'label': 'Close to fist allfingerstogether max force 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_closetofist_allfingerstogether_normalforce_3sec': {'code': 12, 'file': '2_side_closetofist_allfingerstogether_normalforce_3sec.mov', 'label': 'Close to fist allfingerstogether normal force 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_closetofist_allfingerstogether_slow_3sec': {'code': 13, 'file': '2_side_closetofist_allfingerstogether_slow_3sec.mov', 'label': 'Close to fist allfingerstogether slow 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_grasp_cup_3sec': {'code': 14, 'file': '2_side_grasp_cup_3sec.mov', 'label': 'Grasp cup 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_wrist_dorsiflexion_maxforce_3sec': {'code': 28, 'file': '2_side_wrist_dorsiflexion_maxforce_3sec.mov', 'label': 'Wrist dorsiflexion max force 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_wrist_dorsiflexion_normalforce_3sec': {'code': 29, 'file': '2_side_wrist_dorsiflexion_normalforce_3sec.mov', 'label': 'Wrist dorsiflexion normal force 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_wrist_palmarflexion_maxforce_3sec': {'code': 30, 'file': '2_side_wrist_palmarflexion_maxforce_3sec.mov', 'label': 'Wrist palmarflexion max force 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_wrist_palmarflexion_normalforce_3sec': {'code': 31, 'file': '2_side_wrist_palmarflexion_normalforce_3sec.mov', 'label': 'Wrist palmarflexion normal force 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_close_onlythumb_palm_3sec': {'code': 32, 'file': '2_side_close_onlythumb_palm_3sec.mov', 'label': 'Close only thumb palm 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_grasp_cup_4fingers_3sec': {'code': 35, 'file': '2_side_grasp_cup_4fingers_3sec.mov', 'label': 'Grasp cup 4fingers 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_rotation_up_3sec': {'code': 38, 'file': '2_side_rotation_up_3sec.mov', 'label': 'Rotation up 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    '2_side_rotation_down_3sec': {'code': 39, 'file': '2_side_rotation_down_3sec.mov', 'label': 'Rotation down 3 sec (side)', 'baseline_code': 2, 'start_state': 'open'},
    # --- orientation 2 (side), départ main fermée ---
    '2_side_open_fourfingers_together_3sec': {'code': 18, 'file': '2_side_open_fourfingers_together_3sec.mov', 'label': 'Open four fingers together 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_index_3sec': {'code': 19, 'file': '2_side_open_index_3sec.mov', 'label': 'Open index 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_middle_3sec': {'code': 20, 'file': '2_side_open_middle_3sec.mov', 'label': 'Open middle 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_onlythumb_3sec': {'code': 21, 'file': '2_side_open_onlythumb_3sec.mov', 'label': 'Open only thumb 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_pinky_3sec': {'code': 23, 'file': '2_side_open_pinky_3sec.mov', 'label': 'Open pinky 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_ring_3sec': {'code': 24, 'file': '2_side_open_ring_3sec.mov', 'label': 'Open ring 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_thumb_3sec': {'code': 25, 'file': '2_side_open_thumb_3sec.mov', 'label': 'Open thumb 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_openhand_fast_1sec': {'code': 26, 'file': '2_side_openhand_fast_1sec.mov', 'label': 'Open hand fast 1 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_openhand_slow_3sec': {'code': 27, 'file': '2_side_openhand_slow_3sec.mov', 'label': 'Open hand slow 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_wrist_close_hand_dorsiflexion_normalforce_3sec': {'code': 29, 'file': '2_side_wrist_close_hand_dorsiflexion_normalforce_3sec.mov', 'label': 'Wrist dorsiflexion normal force 3 sec, closed hand (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_wrist_close_hand_palmarflexion_normalforce_3sec': {'code': 31, 'file': '2_side_wrist_close_hand_palmarflexion_normalforce_3sec.mov', 'label': 'Wrist palmarflexion normal force 3 sec, closed hand (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_onlythumb_palm_3sec': {'code': 33, 'file': '2_side_open_onlythumb_palm_3sec.mov', 'label': 'Open only thumb palm 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_open_allfingers_together_3sec': {'code': 34, 'file': '2_side_open_allfingers_together_3sec.mov', 'label': 'Open all fingers together 3 sec (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_close_hand_rotation_up_3sec': {'code': 38, 'file': '2_side_close_hand_rotation_up_3sec.mov', 'label': 'Rotation up 3 sec, closed hand (side)', 'baseline_code': 2, 'start_state': 'closed'},
    '2_side_close_hand_rotation_down_3sec': {'code': 39, 'file': '2_side_close_hand_rotation_down_3sec.mov', 'label': 'Rotation down 3 sec, closed hand (side)', 'baseline_code': 2, 'start_state': 'closed'},
    # --- orientation 3 (down), départ main ouverte ---
    '3_down_close_fourfingers_together_3sec': {'code': 1, 'file': '3_down_close_fourfingers_together_3sec.mov', 'label': 'Close four fingers together 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_index_3sec': {'code': 2, 'file': '3_down_close_index_3sec.mov', 'label': 'Close index 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_middle_3sec': {'code': 3, 'file': '3_down_close_middle_3sec.mov', 'label': 'Close middle 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_onlythumb_3sec': {'code': 4, 'file': '3_down_close_onlythumb_3sec.mov', 'label': 'Close only thumb 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_pinky_3sec': {'code': 5, 'file': '3_down_close_pinky_3sec.mov', 'label': 'Close pinky 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_ring_3sec': {'code': 6, 'file': '3_down_close_ring_3sec.mov', 'label': 'Close ring 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_thumb_3sec': {'code': 7, 'file': '3_down_close_thumb_3sec.mov', 'label': 'Close thumb 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_closetofist_allfingerstogether_fast_1sec': {'code': 10, 'file': '3_down_closetofist_allfingerstogether_fast_1sec.mov', 'label': 'Close to fist allfingerstogether fast 1 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_closetofist_allfingerstogether_maxforce_3sec': {'code': 11, 'file': '3_down_closetofist_allfingerstogether_maxforce_3sec.mov', 'label': 'Close to fist allfingerstogether max force 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_closetofist_allfingerstogether_normalforce_3sec': {'code': 12, 'file': '3_down_closetofist_allfingerstogether_normalforce_3sec.mov', 'label': 'Close to fist allfingerstogether normal force 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_closetofist_allfingerstogether_slow_3sec': {'code': 13, 'file': '3_down_closetofist_allfingerstogether_slow_3sec.mov', 'label': 'Close to fist allfingerstogether slow 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_grasping_pinching_pen_2fingers_3sec': {'code': 16, 'file': '3_down_grasping_pinching_pen_2fingers_3sec.mov', 'label': 'Grasping pinching pen 2fingers 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_grasping_pinching_pen_allfingers_3sec': {'code': 17, 'file': '3_down_grasping_pinching_pen_allfingers_3sec.mov', 'label': 'Grasping pinching pen allfingers 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_wrist_dorsiflexion_maxforce_3sec': {'code': 28, 'file': '3_down_wrist_dorsiflexion_maxforce_3sec.mov', 'label': 'Wrist dorsiflexion max force 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_wrist_dorsiflexion_normalforce_3sec': {'code': 29, 'file': '3_down_wrist_dorsiflexion_normalforce_3sec.mov', 'label': 'Wrist dorsiflexion normal force 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_wrist_palmarflexion_maxforce_3sec': {'code': 30, 'file': '3_down_wrist_palmarflexion_maxforce_3sec.mov', 'label': 'Wrist palmarflexion max force 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_wrist_palmarflexion_normalforce_3sec': {'code': 31, 'file': '3_down_wrist_palmarflexion_normalforce_3sec.mov', 'label': 'Wrist palmarflexion normal force 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_close_onlythumb_palm_3sec': {'code': 32, 'file': '3_down_close_onlythumb_palm_3sec.mov', 'label': 'Close only thumb palm 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_grasping_pinching_pen_3fingers_3sec': {'code': 36, 'file': '3_down_grasping_pinching_pen_3fingers_3sec.mov', 'label': 'Grasping pinching pen 3fingers 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    '3_down_rotation_3sec': {'code': 37, 'file': '3_down_rotation_3sec.mov', 'label': 'Rotation 3 sec (down)', 'baseline_code': 3, 'start_state': 'open'},
    # --- orientation 3 (down), départ main fermée ---
    '3_down_open_fourfingers_together_3sec': {'code': 18, 'file': '3_down_open_fourfingers_together_3sec.mov', 'label': 'Open four fingers together 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_index_3sec': {'code': 19, 'file': '3_down_open_index_3sec.mov', 'label': 'Open index 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_middle_3sec': {'code': 20, 'file': '3_down_open_middle_3sec.mov', 'label': 'Open middle 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_onlythumb_3sec': {'code': 21, 'file': '3_down_open_onlythumb_3sec.mov', 'label': 'Open only thumb 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_pinky_3sec': {'code': 23, 'file': '3_down_open_pinky_3sec.mov', 'label': 'Open pinky 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_ring_3sec': {'code': 24, 'file': '3_down_open_ring_3sec.mov', 'label': 'Open ring 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_thumb_3sec': {'code': 25, 'file': '3_down_open_thumb_3sec.mov', 'label': 'Open thumb 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_openhand_fast_1sec': {'code': 26, 'file': '3_down_openhand_fast_1sec.mov', 'label': 'Open hand fast 1 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_openhand_slow_3sec': {'code': 27, 'file': '3_down_openhand_slow_3sec.mov', 'label': 'Open hand slow 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_wrist_close_hand_dorsiflexion_normalforce_3sec': {'code': 29, 'file': '3_down_wrist_close_hand_dorsiflexion_normalforce_3sec.mov', 'label': 'Wrist dorsiflexion normal force 3 sec, closed hand (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_wrist_close_hand_palmarflexion_normalforce_3sec': {'code': 31, 'file': '3_down_wrist_close_hand_palmarflexion_normalforce_3sec.mov', 'label': 'Wrist palmarflexion normal force 3 sec, closed hand (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_onlythumb_palm_3sec': {'code': 33, 'file': '3_down_open_onlythumb_palm_3sec.mov', 'label': 'Open only thumb palm 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_open_allfingers_together_3sec': {'code': 34, 'file': '3_down_open_allfingers_together_3sec.mov', 'label': 'Open all fingers together 3 sec (down)', 'baseline_code': 3, 'start_state': 'closed'},
    '3_down_close_hand_rotation_3sec': {'code': 37, 'file': '3_down_close_hand_rotation_3sec.mov', 'label': 'Rotation 3 sec, closed hand (down)', 'baseline_code': 3, 'start_state': 'closed'},
}

# Pour relire d'anciens enregistrements faits avec MOVEMENTS_shared_14112025.py,
# qui donnait un code différent au même geste selon l'orientation :
#   (orientation, ancien code) -> code canonique actuel
LEGACY_CODE_ALIASES = {
    (1, 8): 11,    # closetofist force max, orientation up (avant : 8)
    (1, 9): 12,    # closetofist force normale, orientation up (avant : 9)
    (1, 22): 23,   # open pinky, orientation up (avant : 22)
}