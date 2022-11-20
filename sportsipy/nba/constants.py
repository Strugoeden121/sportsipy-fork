PARSING_SCHEME = {
    'name': 'a',
    'games_played': 'td[data-stat="g"]:first',
    'minutes_played': 'td[data-stat="mp"]:first',
    'field_goals': 'td[data-stat="fg"]:first',
    'field_goal_attempts': 'td[data-stat="fga"]:first',
    'field_goal_percentage': 'td[data-stat="fg_pct"]:first',
    'three_point_field_goals': 'td[data-stat="fg3"]:first',
    'three_point_field_goal_attempts': 'td[data-stat="fg3a"]:first',
    'three_point_field_goal_percentage': 'td[data-stat="fg3_pct"]:first',
    'two_point_field_goals': 'td[data-stat="fg2"]:first',
    'two_point_field_goal_attempts': 'td[data-stat="fg2a"]:first',
    'two_point_field_goal_percentage': 'td[data-stat="fg2_pct"]:first',
    'free_throws': 'td[data-stat="ft"]:first',
    'free_throw_attempts': 'td[data-stat="fta"]:first',
    'free_throw_percentage': 'td[data-stat="ft_pct"]:first',
    'offensive_rebounds': 'td[data-stat="orb"]:first',
    'defensive_rebounds': 'td[data-stat="drb"]:first',
    'total_rebounds': 'td[data-stat="trb"]:first',
    'assists': 'td[data-stat="ast"]:first',
    'steals': 'td[data-stat="stl"]:first',
    'blocks': 'td[data-stat="blk"]:first',
    'turnovers': 'td[data-stat="tov"]:first',
    'personal_fouls': 'td[data-stat="pf"]:first',
    'points': 'td[data-stat="pts"]:first',
    'opp_minutes_played': 'td[data-stat="mp"]:first',
    'opp_field_goals': 'td[data-stat="opp_fg"]:first',
    'opp_field_goal_attempts': 'td[data-stat="opp_fga"]:first',
    'opp_field_goal_percentage': 'td[data-stat="opp_fg_pct"]:first',
    'opp_three_point_field_goals': 'td[data-stat="opp_fg3"]:first',
    'opp_three_point_field_goal_attempts': 'td[data-stat="opp_fg3a"]:first',
    'opp_three_point_field_goal_percentage':
    'td[data-stat="opp_fg3_pct"]:first',
    'opp_two_point_field_goals': 'td[data-stat="opp_fg2"]:first',
    'opp_two_point_field_goal_attempts': 'td[data-stat="opp_fg2a"]:first',
    'opp_two_point_field_goal_percentage': 'td[data-stat="opp_fg2_pct"]:first',
    'opp_free_throws': 'td[data-stat="opp_ft"]:first',
    'opp_free_throw_attempts': 'td[data-stat="opp_fta"]:first',
    'opp_free_throw_percentage': 'td[data-stat="opp_ft_pct"]:first',
    'opp_offensive_rebounds': 'td[data-stat="opp_orb"]:first',
    'opp_defensive_rebounds': 'td[data-stat="opp_drb"]:first',
    'opp_total_rebounds': 'td[data-stat="opp_trb"]:first',
    'opp_assists': 'td[data-stat="opp_ast"]:first',
    'opp_steals': 'td[data-stat="opp_stl"]:first',
    'opp_blocks': 'td[data-stat="opp_blk"]:first',
    'opp_turnovers': 'td[data-stat="opp_tov"]:first',
    'opp_personal_fouls': 'td[data-stat="opp_pf"]:first',
    'opp_points': 'td[data-stat="opp_pts"]:first'
}

SCHEDULE_SCHEME = {
    'game': 'th[data-stat="g"]:first',
    'date': 'td[data-stat="date_game"]:first',
    'time': 'td[data-stat="game_start_time"]:first',
    'boxscore': 'td[data-stat="box_score_text"]:first',
    'location': 'td[data-stat="game_location"]:first',
    'opponent_abbr': 'td[data-stat="opp_id"]:first',
    'opponent_name': 'td[data-stat="opp_name"]:first',
    'result': 'td[data-stat="game_result"]:first',
    'points_scored': 'td[data-stat="pts"]:first',
    'points_allowed': 'td[data-stat="opp_pts"]:first',
    'wins': 'td[data-stat="wins"]:first',
    'losses': 'td[data-stat="losses"]:first',
    'streak': 'td[data-stat="game_streak"]:first'
}

BOXSCORE_SCHEME = {
    'date': 'div[class="scorebox_meta"]',
    'location': 'div[class="scorebox_meta"]',
    'away_name': 'div[class="scorebox"] div:nth-child(1) div strong a',
    'home_name': 'div[class="scorebox"] div:nth-child(2) div strong a',
    'winning_name': '',
    'winning_abbr': '',
    'losing_name': '',
    'losing_abbr': '',
    'summary': 'table#line_score',
    'pace': 'td[data-stat="pace"]:first',
    'away_record': 'div[class="scorebox"] div:nth-child(1) div:nth-child(3)',
    'away_minutes_played': 'tfoot td[data-stat="mp"]',
    'away_field_goals': 'tfoot td[data-stat="fg"]',
    'away_field_goal_attempts': 'tfoot td[data-stat="fga"]',
    'away_field_goal_percentage': 'tfoot td[data-stat="fg_pct"]',
    'away_two_point_field_goals': 'tfoot td[data-stat="fg2"]',
    'away_two_point_field_goal_attempts': 'tfoot td[data-stat="fg2a"]',
    'away_two_point_field_goal_percentage': 'tfoot td[data-stat="fg2_pct"]',
    'away_three_point_field_goals': 'tfoot td[data-stat="fg3"]',
    'away_three_point_field_goal_attempts': 'tfoot td[data-stat="fg3a"]',
    'away_three_point_field_goal_percentage': 'tfoot td[data-stat="fg3_pct"]',
    'away_free_throws': 'tfoot td[data-stat="ft"]',
    'away_free_throw_attempts': 'tfoot td[data-stat="fta"]',
    'away_free_throw_percentage': 'tfoot td[data-stat="ft_pct"]',
    'away_offensive_rebounds': 'tfoot td[data-stat="orb"]',
    'away_defensive_rebounds': 'tfoot td[data-stat="drb"]',
    'away_total_rebounds': 'tfoot td[data-stat="trb"]',
    'away_assists': 'tfoot td[data-stat="ast"]',
    'away_steals': 'tfoot td[data-stat="stl"]',
    'away_blocks': 'tfoot td[data-stat="blk"]',
    'away_turnovers': 'tfoot td[data-stat="tov"]',
    'away_personal_fouls': 'tfoot td[data-stat="pf"]',
    'away_points': 'tfoot td[data-stat="pts"]',
    'away_true_shooting_percentage': 'tfoot td[data-stat="ts_pct"]',
    'away_effective_field_goal_percentage': 'tfoot td[data-stat="efg_pct"]',
    'away_three_point_attempt_rate': 'tfoot td[data-stat="fg3a_per_fga_pct"]',
    'away_free_throw_attempt_rate': 'tfoot td[data-stat="fta_per_fga_pct"]',
    'away_offensive_rebound_percentage': 'tfoot td[data-stat="orb_pct"]',
    'away_defensive_rebound_percentage': 'tfoot td[data-stat="drb_pct"]',
    'away_total_rebound_percentage': 'tfoot td[data-stat="trb_pct"]',
    'away_assist_percentage': 'tfoot td[data-stat="ast_pct"]',
    'away_steal_percentage': 'tfoot td[data-stat="stl_pct"]',
    'away_block_percentage': 'tfoot td[data-stat="blk_pct"]',
    'away_turnover_percentage': 'tfoot td[data-stat="tov_pct"]',
    'away_offensive_rating': 'tfoot td[data-stat="off_rtg"]',
    'away_defensive_rating': 'tfoot td[data-stat="def_rtg"]',
    'home_record': 'div[class="scorebox"] div:nth-child(2) div:nth-child(3)',
    'home_minutes_played': 'tfoot td[data-stat="mp"]',
    'home_field_goals': 'tfoot td[data-stat="fg"]',
    'home_field_goal_attempts': 'tfoot td[data-stat="fga"]',
    'home_field_goal_percentage': 'tfoot td[data-stat="fg_pct"]',
    'home_two_point_field_goals': 'tfoot td[data-stat="fg2"]',
    'home_two_point_field_goal_attempts': 'tfoot td[data-stat="fg2a"]',
    'home_two_point_field_goal_percentage': 'tfoot td[data-stat="fg2_pct"]',
    'home_three_point_field_goals': 'tfoot td[data-stat="fg3"]',
    'home_three_point_field_goal_attempts': 'tfoot td[data-stat="fg3a"]',
    'home_three_point_field_goal_percentage': 'tfoot td[data-stat="fg3_pct"]',
    'home_free_throws': 'tfoot td[data-stat="ft"]',
    'home_free_throw_attempts': 'tfoot td[data-stat="fta"]',
    'home_free_throw_percentage': 'tfoot td[data-stat="ft_pct"]',
    'home_offensive_rebounds': 'tfoot td[data-stat="orb"]',
    'home_defensive_rebounds': 'tfoot td[data-stat="drb"]',
    'home_total_rebounds': 'tfoot td[data-stat="trb"]',
    'home_assists': 'tfoot td[data-stat="ast"]',
    'home_steals': 'tfoot td[data-stat="stl"]',
    'home_blocks': 'tfoot td[data-stat="blk"]',
    'home_turnovers': 'tfoot td[data-stat="tov"]',
    'home_personal_fouls': 'tfoot td[data-stat="pf"]',
    'home_points': 'div[class="score"]',
    'home_true_shooting_percentage': 'tfoot td[data-stat="ts_pct"]',
    'home_effective_field_goal_percentage': 'tfoot td[data-stat="efg_pct"]',
    'home_three_point_attempt_rate': 'tfoot td[data-stat="fg3a_per_fga_pct"]',
    'home_free_throw_attempt_rate': 'tfoot td[data-stat="fta_per_fga_pct"]',
    'home_offensive_rebound_percentage': 'tfoot td[data-stat="orb_pct"]',
    'home_defensive_rebound_percentage': 'tfoot td[data-stat="drb_pct"]',
    'home_total_rebound_percentage': 'tfoot td[data-stat="trb_pct"]',
    'home_assist_percentage': 'tfoot td[data-stat="ast_pct"]',
    'home_steal_percentage': 'tfoot td[data-stat="stl_pct"]',
    'home_block_percentage': 'tfoot td[data-stat="blk_pct"]',
    'home_turnover_percentage': 'tfoot td[data-stat="tov_pct"]',
    'home_offensive_rating': 'tfoot td[data-stat="off_rtg"]',
    'home_defensive_rating': 'tfoot td[data-stat="def_rtg"]'
}

BOXSCORE_ELEMENT_INDEX = {
    'date': 0,
    'location': 1,
    'home_record': -1,
    'home_minutes_played': 7,
    'home_field_goals': 7,
    'home_field_goal_attempts': 7,
    'home_field_goal_percentage': 7,
    'home_two_point_field_goals': 7,
    'home_two_point_field_goal_attempts': 7,
    'home_two_point_field_goal_percentage': 7,
    'home_three_point_field_goals': 7,
    'home_three_point_field_goal_attempts': 7,
    'home_three_point_field_goal_percentage': 7,
    'home_free_throws': 7,
    'home_free_throw_attempts': 7,
    'home_free_throw_percentage': 7,
    'home_offensive_rebounds': 7,
    'home_defensive_rebounds': 7,
    'home_total_rebounds': 7,
    'home_assists': 7,
    'home_steals': 7,
    'home_blocks': 7,
    'home_turnovers': 7,
    'home_personal_fouls': 7,
    'home_points': -1,
    'home_true_shooting_percentage': 7,
    'home_effective_field_goal_percentage': 7,
    'home_three_point_attempt_rate': 7,
    'home_free_throw_attempt_rate': 7,
    'home_offensive_rebound_percentage': 7,
    'home_defensive_rebound_percentage': 7,
    'home_total_rebound_percentage': 7,
    'home_assist_percentage': 7,
    'home_steal_percentage': 7,
    'home_block_percentage': 7,
    'home_turnover_percentage': 7,
    'home_offensive_rating': 7,
    'home_defensive_rating': 7
}

PLAYER_SCHEME = {
    'summary': '[data-template="Partials/Teams/Summary"]',
    'season': 'th[data-stat="season"]:first',
    'name': 'h1',
    'team_abbreviation': 'td[data-stat="team_id"]',
    'position': 'td[data-stat="pos"]',
    'height': 'span[itemprop="height"]',
    'weight': 'span[itemprop="weight"]',
    'birth_date': 'td[data-stat=""]',
    'nationality': 'td[data-stat=""]',
    'age': 'nobr',
    'games_played': 'td[data-stat="g"]',
    'games_started': 'td[data-stat="gs"]',
    'minutes_played': 'td[data-stat="mp"]',
    'field_goals': 'td[data-stat="fg"]',
    'field_goal_attempts': 'td[data-stat="fga"]',
    'field_goal_percentage': 'td[data-stat="fg_pct"]',
    'three_pointers': 'td[data-stat="fg3"]',
    'three_point_attempts': 'td[data-stat="fg3a"]',
    'three_point_percentage': 'td[data-stat="fg3_pct"]',
    'two_pointers': 'td[data-stat="fg2"]',
    'two_point_attempts': 'td[data-stat="fg2a"]',
    'two_point_percentage': 'td[data-stat="fg2_pct"]',
    'effective_field_goal_percentage': 'td[data-stat="efg_pct"]',
    'free_throws': 'td[data-stat="ft"]',
    'free_throw_attempts': 'td[data-stat="fta"]',
    'free_throw_percentage': 'td[data-stat="ft_pct"]',
    'offensive_rebounds': 'td[data-stat="orb"]',
    'defensive_rebounds': 'td[data-stat="drb"]',
    'total_rebounds': 'td[data-stat="trb"]',
    'assists': 'td[data-stat="ast"]',
    'steals': 'td[data-stat="stl"]',
    'blocks': 'td[data-stat="blk"]',
    'turnovers': 'td[data-stat="tov"]',
    'personal_fouls': 'td[data-stat="pf"]',
    'points': 'td[data-stat="pts"]',
    'player_efficiency_rating': 'td[data-stat="per"]',
    'true_shooting_percentage': 'td[data-stat="ts_pct"]',
    'three_point_attempt_rate': 'td[data-stat="fg3a_per_fga_pct"]',
    'free_throw_attempt_rate': 'td[data-stat="fta_per_fga_pct"]',
    'offensive_rebound_percentage': 'td[data-stat="orb_pct"]',
    'defensive_rebound_percentage': 'td[data-stat="drb_pct"]',
    'total_rebound_percentage': 'td[data-stat="trb_pct"]',
    'assist_percentage': 'td[data-stat="ast_pct"]',
    'steal_percentage': 'td[data-stat="stl_pct"]',
    'block_percentage': 'td[data-stat="blk_pct"]',
    'turnover_percentage': 'td[data-stat="tov_pct"]',
    'usage_percentage': 'td[data-stat="usg_pct"]',
    'offensive_win_shares': 'td[data-stat="ows"]',
    'defensive_win_shares': 'td[data-stat="dws"]',
    'win_shares': 'td[data-stat="ws"]',
    'win_shares_per_48_minutes': 'td[data-stat="ws_per_48"]',
    'offensive_box_plus_minus': 'td[data-stat="obpm"]',
    'defensive_box_plus_minus': 'td[data-stat="dbpm"]',
    'box_plus_minus': 'td[data-stat="bpm"]',
    'defensive_rating': 'td[data-stat="def_rtg"]',
    'offensive_rating': 'td[data-stat="off_rtg"]',
    'boxscore_box_plus_minus': 'td[data-stat="plus_minus"]',
    'value_over_replacement_player': 'td[data-stat="vorp"]',
    'shooting_distance': 'td[data-stat="avg_dist"]',
    'percentage_shots_two_pointers': 'td[data-stat="fg2a_pct_fga"]',
    'percentage_zero_to_three_footers': 'td[data-stat="pct_fga_00_03"]',
    'percentage_three_to_ten_footers': 'td[data-stat="pct_fga_03_10"]',
    'percentage_ten_to_sixteen_footers': 'td[data-stat="pct_fga_10_16"]',
    'percentage_sixteen_foot_plus_two_pointers':
    'td[data-stat="pct_fga_16_xx"]',
    'percentage_shots_three_pointers': 'td[data-stat="fg3a_pct_fga"]',
    'field_goal_perc_zero_to_three_feet': 'td[data-stat="fg_pct_00_03"]',
    'field_goal_perc_three_to_ten_feet': 'td[data-stat="fg_pct_03_10"]',
    'field_goal_perc_ten_to_sixteen_feet': 'td[data-stat="fg_pct_10_16"]',
    'field_goal_perc_sixteen_foot_plus_two_pointers':
    'td[data-stat="fg_pct_16_xx"]',
    'two_pointers_assisted_percentage': 'td[data-stat="fg2_pct_ast"]',
    'percentage_field_goals_as_dunks': 'td[data-stat="pct_fg2_dunk"]',
    'dunks': 'td[data-stat="fg2_dunk"]',
    'three_pointers_assisted_percentage': 'td[data-stat="fg3_pct_ast"]',
    'percentage_of_three_pointers_from_corner':
    'td[data-stat="pct_fg3a_corner"]',
    'three_point_shot_percentage_from_corner':
    'td[data-stat="fg3_pct_corner"]',
    'half_court_heaves': 'td[data-stat="fg3a_heave"]',
    'half_court_heaves_made': 'td[data-stat="fg3_heave"]',
    'point_guard_percentage': 'td[data-stat="pct_1"]',
    'shooting_guard_percentage': 'td[data-stat="pct_2"]',
    'small_forward_percentage': 'td[data-stat="pct_3"]',
    'power_forward_percentage': 'td[data-stat="pct_4"]',
    'center_percentage': 'td[data-stat="pct_5"]',
    'on_court_plus_minus': 'td[data-stat="plus_minus_on"]',
    'net_plus_minus': 'td[data-stat="plus_minus_net"]',
    'passing_turnovers': 'td[data-stat="tov_bad_pass"]',
    'lost_ball_turnovers': 'td[data-stat="tov_lost_ball"]',
    'other_turnovers': 'td[data-stat="tov_other"]',
    'shooting_fouls': 'td[data-stat="fouls_shooting"]',
    'blocking_fouls': 'td[data-stat="fouls_blocking"]',
    'offensive_fouls': 'td[data-stat="fouls_offensive"]',
    'take_fouls': 'td[data-stat="fouls_take"]',
    'points_generated_by_assists': 'td[data-stat="astd_pts"]',
    'shooting_fouls_drawn': 'td[data-stat="drawn_shooting"]',
    'and_ones': 'td[data-stat="and1s"]',
    'shots_blocked': 'td[data-stat="fga_blkd"]',
    'salary': 'td[data-stat="salary"]',
    'field_goals_per_poss': 'td[data-stat="fg_per_poss"]',
    'field_goal_attempts_per_poss': 'td[data-stat="fga_per_poss"]',
    'three_pointers_per_poss': 'td[data-stat="fg3_per_poss"]',
    'three_point_attempts_per_poss': 'td[data-stat="fg3a_per_poss"]',
    'two_pointers_per_poss': 'td[data-stat="fg2_per_poss"]',
    'two_point_attempts_per_poss': 'td[data-stat="fg2a_per_poss"]',
    'free_throws_per_poss': 'td[data-stat="ft_per_poss"]',
    'free_throw_attempts_per_poss': 'td[data-stat="fta_per_poss"]',
    'offensive_rebounds_per_poss': 'td[data-stat="orb_per_poss"]',
    'defensive_rebounds_per_poss': 'td[data-stat="drb_per_poss"]',
    'total_rebounds_per_poss': 'td[data-stat="trb_per_poss"]',
    'assists_per_poss': 'td[data-stat="ast_per_poss"]',
    'steals_per_poss': 'td[data-stat="stl_per_poss"]',
    'blocks_per_poss': 'td[data-stat="blk_per_poss"]',
    'turnovers_per_poss': 'td[data-stat="tov_per_poss"]',
    'personal_fouls_per_poss': 'td[data-stat="pf_per_poss"]',
    'points_per_poss': 'td[data-stat="pts_per_poss"]'
}

NATIONALITY = {
    'ao': 'Angola',
    'ag': 'Antigua and Barbuda',
    'ar': 'Argentina',
    'au': 'Australia',
    'at': 'Austria',
    'bs': 'Bahamas',
    'be': 'Belgium',
    'ba': 'Bosnia and Herzegovina',
    'br': 'Brazil',
    'bg': 'Bulgaria',
    'cm': 'Cameroon',
    'ca': 'Canada',
    'td': 'Chad',
    'co': 'Colombia',
    'cv': 'Cape Verde',
    'cn': 'China',
    'hr': 'Croatia',
    'cu': 'Cuba',
    'cz': 'Czech Republic',
    'cd': 'Democratic Replubic of Congo',
    'dk': 'Denmark',
    'dm': 'Dominica',
    'do': 'Dominican Replubic',
    'eg': 'Egypt',
    'ee': 'Estonia',
    'fi': 'Finland',
    'fr': 'France',
    'gf': 'French Guiana',
    'ga': 'Gabon',
    'ge': 'Georgia',
    'de': 'Germany',
    'gh': 'Ghana',
    'gr': 'Greece',
    'gp': 'Guadeloupe',
    'gn': 'Guinea',
    'gy': 'Guyana',
    'ht': 'Haiti',
    'hu': 'Hungary',
    'is': 'Iceland',
    'ie': 'Ireland',
    'ir': 'Islamic Replubic of Iran',
    'il': 'Israel',
    'it': 'Italy',
    'jm': 'Jamaica',
    'jp': 'Japan',
    'lv': 'Latvia',
    'lb': 'Lebanon',
    'lt': 'Lithuania',
    'lu': 'Luxembourg',
    'ml': 'Mali',
    'mq': 'Martinique',
    'mx': 'Mexico',
    'me': 'Montenegro',
    'ma': 'Morocco',
    'nl': 'Netherlands',
    'nz': 'New Zealand',
    'ng': 'Nigeria',
    'no': 'Norway',
    'pa': 'Panama',
    'pl': 'Poland',
    'pr': 'Puerto Rico',
    'ke': 'Kenya',
    'kr': 'Republic of Korea',
    'mk': 'Republic of Macedonia',
    'cg': 'Republic of Congo',
    'ro': 'Romania',
    'ru': 'Russian Federation',
    'lc': 'Saint Lucia',
    'vc': 'Saint Vincent and the Grenadines',
    'sd': 'Sudan',
    'sn': 'Senegal',
    'rs': 'Serbia',
    'sk': 'Slovakia',
    'si': 'Slovenia',
    'za': 'South Africa',
    'ss': 'South Sudan',
    'es': 'Spain',
    'se': 'Sweden',
    'ch': 'Switzerland',
    'tw': 'Taiwan',
    'tt': 'Trinidad and Tobago',
    'tn': 'Tunisia',
    'tr': 'Turkey',
    'us': 'United States of America',
    'vi': 'U.S. Virgin Islands',
    'ua': 'Ukraine',
    'gb': 'United Kingdom',
    'tz': 'United Republic of Tanzania',
    'uy': 'Uruguay',
    've': 'Venezuela'
}

SEASON_PAGE_URL = 'http://www.basketball-reference.com/leagues/NBA_%s.html'

SCHEDULE_URL = 'http://www.basketball-reference.com/teams/%s/%s_games.html'

BOXSCORE_URL = 'https://www.basketball-reference.com/boxscores/%s.html'

BOXSCORES_URL = ('https://www.basketball-reference.com/boxscores/'
                 '?month=%s&day=%s&year=%s')

PLAYER_URL = 'https://www.basketball-reference.com/players/%s/%s.html'

ROSTER_URL = 'https://www.basketball-reference.com/teams/%s/%s.html'
