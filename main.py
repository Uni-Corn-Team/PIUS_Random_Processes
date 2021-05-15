import team2_1
import team1

if __name__ == "__main__":
    Xsin, Ysin = team1.generate_input_signal()
    team1.non_inertial_link(Xsin, Ysin).show()
    team1.link_with_net_lag(Xsin, Ysin).show()
    team1.aperiodic_link_1st_order(Xsin, Ysin).show()
    team1.black_box(Xsin, Ysin).show()
    team2_1.noises()
