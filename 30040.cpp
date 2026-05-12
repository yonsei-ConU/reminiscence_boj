#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>
#include <functional>

int Tst, Tc;
std::string subway[1000] = {"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Soyosan", "Dongducheon", "Bosan", "Dongducheon jungang",
                            "Jihaeng", "Deokjeong", "Deokgye", "Yangju", "Nogyang",
                            "Ganeung", "Uijeongbu", "Hoeryong", "Mangwolsa", "Dobongsan",
                            "Dobong", "Banghak", "Changdong", "Nokcheon", "Wolgye",
                            "Kwangwoon Univ.", "Seokgye", "Sinimun", "Hankuk Univ. of Foreign Studies",
                            "Hoegi", "Cheongnyangni (University of Seoul)", "Jegi-dong",
                            "Sinseol-dong", "Dongmyo", "Dongdaemun", "Jongno 5(o)ga",
                            "Jongno 3(sam)ga", "Jonggak", "City Hall", "Seoul Station",
                            "Namyeong", "Yongsan", "Noryangjin", "Daebang", "Singil",
                            "Yeongdeungpo", "Sindorim", "Guro", "Guil", "Gaebong",
                            "Oryu-dong", "Onsu(Sungkonghoe Univ.)", "Yeokgok", "Sosa",
                            "Bucheon", "Jung-dong", "Songnae", "Bugae", "Bupyeong",
                            "Baegun", "Dongam", "Ganseok", "Juan", "Dohwa", "Jemulpo",
                            "Dowon", "Dongincheon", "Incheon", "Gasan Digital Complex",
                            "Doksan", "Gumcheon-gu office", "Gwangmyeong", "Seoksu",
                            "Gwanak", "Anyang", "Myeonghak", "Geumjeong", "Gunpo",
                            "Dangjeong", "Uiwang", "Sungkyunkwan Univ.", "Hwaseo", "Suwon",
                            "Seryu", "Seodongtan", "Sema", "Osan College", "Osan",
                            "Jinwi", "Songtan", "Seojeong-ri", "Pyeongtaek Jije", "Pyeongtaek",
                            "Seonghwan", "Jiksan", "Dujeong", "Cheonan", "Bongmyeong",
                            "Ssangyong (Korea Nazarene Univ.)", "Asan", "Tangjeong", "Baebang",
                            "Onyang oncheon", "Sinchang (Soonchunhyang Univ.)", "", "", "",
                            "City Hall", "Euljiro 1(il)ga", "Euljiro 3(sam)ga", "Euljiro 4(sa)ga",
                            "Dongdaemun History & Culture Park (DDP)", "Sindang", "Sangwangsimni",
                            "Wangsimni (Seongdong-gu Office)", "Hanyang Univ.", "Ttukseom",
                            "Seongsu", "Konkuk Univ.", "Guui(Gwangjin-gu Office)",
                            "Gangbyeon(Dongseoul Bus Terminal)", "Jamsillaru", "Jamsil(Songpa-gu Office)",
                            "Jamsilsaenae", "Sports Complex", "Samseong (World Trade Center Seoul)",
                            "Seolleung", "Yeoksam", "Gangnam", "Seoul Nat'l Univ. of Education (Court & Prosecutor's Office)",
                            "Seocho", "Bangbae", "Sadang", "Nakseongdae (Ganggamchan)",
                            "Seoul Nat'l Univ. (Gwanak-gu Office)", "Bongcheon", "Sillim", "Sindaebang",
                            "Guro Digital Complex", "Daerim (Guro-gu Office)", "Sindorim", "Mullae",
                            "Yeongdeungpo-gu Office", "Dangsan", "Hapjeong", "Hongik Univ.",
                            "Sinchon", "Ewha Womans Univ.", "Ahyeon", "Chungjeongno (Kyonggi Univ.)",
                            "Yongdap", "Sindap", "Yongdu (Dongdaemun-gu Office)", "Sinseol-dong",
                            "Dorimcheon", "Yangcheon-gu Office", "Sinjeongnegeori", "Kkachisan", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Daehwa", "Juyeop", "Jeongbalsan", "Madu", "Baekseok",
                            "Daegok", "Hwajeong", "Wondang", "Wonheung", "Samsong",
                            "Jichuk", "Gupabal", "Yeonsinnae", "Bulgwang", "Nokbeon",
                            "Hongje", "Muakjae", "Dongnimmun", "Gyeongbokgung (Government Complex Seoul)",
                            "Anguk", "Jongno 3(sam)ga", "Euljiro 3(sam)ga", "Chungmuro",
                            "Dongguk Univ.", "Yaksu", "Geumho", "Oksu", "Apgujeong",
                            "Sinsa", "Jamwon", "Express Bus Terminal", "Seoul Nat'l Univ. of Education (Court & Prosecutor's Office)",
                            "Nambu Bus Terminal (Seoul Arts Center)", "Yangjae (Seocho-gu Office)", "Maebong",
                            "Dogok", "Daechi", "Hangnyeoul", "Daecheong", "Irwon", "Suseo",
                            "Garak Market", "National Police Hospital", "Ogeum", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Jinjeop", "Onam", "Byeollae Byeolgaram", "Danggogae", "Sanggye",
                            "Nowon", "Changdong", "Ssangmun", "Suyu (Gangbuk-gu Office)",
                            "Mia (Seoul Cyber Univ.)", "Miasageori", "Gireum", "Sungshin Women's Univ. (Donam)",
                            "Hansung Univ.(Samseongyo)", "Hyehwa", "Dongdaemun", "Dongdaemun History & Culture Park (DDP)",
                            "Chungmuro", "Myeong-dong", "Hoehyeon (Namdaemun Market)", "Seoul Station",
                            "Sookmyung Women's Univ.(Garwol)", "Samgakji", "Sinyongsan", "Ichon(National Museum of Korea)",
                            "Dongjak (Seoul National Cemetery)", "Chongshin Univ.(Isu)", "Sadang",
                            "Namtaeryeong", "Seonbawi", "Seoul Racecourse Park", "Seoul Grand Park",
                            "Gwacheon", "Government Complex Gwacheon", "Indeogwon", "Pyeongchon",
                            "Beomgye", "Geumjeong", "Sanbon", "Surisan", "Daeyami",
                            "Banwol", "Sangnoksu", "Hanyang Univ. at Ansan", "Jungang", "Gojan",
                            "Choji", "Ansan", "Singiloncheon", "Jeongwang", "Oido", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Banghwa", "Gaehwasan", "Gimpo Int'l Airport", "Songjeong", "Magok",
                            "Balsan", "Ujangsan", "Hwagok", "Kkachisan", "Sinjeong(Eunhaengjeong)",
                            "Mok-dong", "Omokgyo(Mok-dong Stadium)", "Yangpyeong", "Yeongdeungpo-gu Office",
                            "Yeongdeungpo Market", "Singil", "Yeouido", "Yeouinaru", "Mapo",
                            "Gongdeok", "Aeogae", "Chungjeongno (Kyonggi Univ.)", "Seodaemun",
                            "Gwanghwamun (Sejong Center for the Performing Arts)", "Jongno 3(sam)ga",
                            "Euljiro 4(sa)ga", "Dongdaemun History & Culture Park (DDP)", "Cheonggu",
                            "Singeumho", "Haengdang", "Wangsimni (Seongdong-gu Office)", "Majang",
                            "Dapsimni", "Janghanpyeong", "Gunja(Neung-dong)", "Achasan(Rear Entrance to Seoul Children's Grand Park)",
                            "Gwangnaru(Presbyterian. College & Theological Seminary)", "Cheonho (Pungnaptoseong)",
                            "Gangdong", "Gil-dong", "Gubeundari (Gangdong Community Center)", "Myeongil",
                            "Godeok", "Sangil-dong", "Gangil", "Misa", "Hanam Pungsan",
                            "Hanam City Hall (Deokpung & Sinjang)", "Hanam Geomdansan", "Dunchon-dong",
                            "Olympic Park (Korea National Sport Univ.)", "Bangi", "Ogeum", "Gaerong",
                            "Geoyeo", "Macheon", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Eungam", "Yeokchon", "Bulgwang", "Dokbawi", "Yeonsinnae",
                            "Gusan", "Saejeol(Sinsa)", "Jeungsan(Myongji Univ.)", "Digital Media City",
                            "World Cup Stadium(Seongsan)", "Mapo-gu Office", "Mangwon", "Hapjeong",
                            "Sangsu", "Gwangheungchang (Seogang)", "Daeheung (Sogang Univ.)", "Gongdeok",
                            "Hyochang Park", "Samgakji", "Noksapyeong (Yongsan-gu Office)", "Itaewon",
                            "Hangangjin", "Beotigogae", "Yaksu", "Cheonggu", "Sindang",
                            "Dongmyo", "Changsin", "Bomun", "Anam(Korea Univ. Hospital)",
                            "Korea Univ. (Jongam)" /* 개쪽팔리니까 이름 딴걸로 바꿔라;;*/,
                            "Wolgok (Dongduk Women's Univ.)", "Sangwolgok(KIST)", "Dolgoji", "Seokgye",
                            "Taereung", "Hwarangdae (Seoul Women's Univ.)", "Bonghwasan (Seoul Medical Center)",
                            "Sinnae", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Jangam", "Dobongsan", "Suraksan", "Madeul", "Nowon", "Junggye",
                            "Hagye", "Gongneung(Seoul National Univ. of Science & Technology)", "Taereung",
                            "Meokgol", "Junghwa", "Sangbong (Intercity Bus Terminal)", "Myeonmok",
                            "Sagajeong", "Yongmasan (Yongma Falls Park)", "Junggok", "Gunja(Neung-dong)",
                            "Children's Grand Park(Sejong Univ.)", "Konkuk Univ.", "Ttukseom Park",
                            "Cheongdam", "Gangnam-gu Office", "Hak-dong", "Nonhyeon", "Banpo",
                            "Express Bus Terminal", "Naebang", "Chongshin Univ.(Isu)", "Namseong",
                            "Soongsil Univ.(Salpijae)", "Sangdo", "Jangseungbaegi", "Sindaebang samgeori",
                            "Boramae", "Sinpung", "Daerim (Guro-gu Office)", "Namguro", "Gasan Digital Complex",
                            "Cheolsan", "Gwangmyeong sageori", "Cheonwang", "Onsu(Sungkonghoe Univ.)",
                            "Kkachiul", "Bucheon Stadium", "Chunui", "Sinjung-dong", "Bucheon City Hall",
                            "Sangdong", "Samsan Gymnasium", "Gulpocheon", "Bupyeong-gu Office",
                            "Sangok", "Seongnam (Geobuk Market)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Amsa", "Cheonho (Pungnaptoseong)", "Gangdong-gu Office", "Mongchontoseong(World Peace Gate)",
                            "Jamsil(Songpa-gu Office)", "Seokchon", "Songpa", "Garak Market",
                            "Munjeong", "Jangji", "Bokjeong", "Namwirye", "Sanseong",
                            "Namhansanseong (Seongnam Court & Prosecutor's Office)", "Dandaeogeori", "Sinheung",
                            "Sujin", "Moran", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "Gaehwa", "Gimpo Int'l Airport", "Airport Market", "Sinbanghwa",
                            "Magongnaru (Seoul Botanic Park)", "Yangcheon Hyanggyo", "Gayang", "Jeungmi",
                            "Deungchon", "Yeomchang", "Sinmokdong", "Seonyudo", "Dangsan",
                            "National Assembly", "Yeouido", "Saetgang", "Noryangjin", "Nodeul",
                            "Heukseok(Chung-Ang Univ.)", "Dongjak (Seoul National Cemetery)", "Gubanpo",
                            "Sinbanpo", "Express Bus Terminal", "Sapyeong", "Sinnonhyeon",
                            "Eonju", "Seonjeongneung", "Samseong Jungang", "Bongeunsa", "Sports Complex",
                            "Samjeon", "Seokchon Gobun", "Seokchon", "Songpanaru", "Hanseong Baekje",
                            "Olympic Park (Korea National Sport Univ.)", "Dunchon Oryun", "VHS Medical Center", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
};

inline void add_chain(int start, int end, std::vector<std::vector<std::pair<int, int>>> &g) {
    for (int i = start; i < end; i++) {
        g[i].emplace_back(i + 1, Tst);
        g[i + 1].emplace_back(i, Tst);
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::unordered_map<std::string, std::vector<int>> name_to_id;
    for (int i = 0; i < 1000; i++) {
        if (subway[i].empty()) continue;
        name_to_id[subway[i]].push_back(i);
    }
    int Q;
    std::cin >> Q;
    while (Q--) {
        std::cin >> Tst >> Tc;
        std::string A, B;
        std::string dummy;
        std::getline(std::cin, dummy);
        std::getline(std::cin, A);
        std::getline(std::cin, B);
        std::unordered_set<int> start;
        for (auto &v : name_to_id[A]) start.insert(v);
        std::vector<int> end = name_to_id[B];
        std::vector<std::vector<std::pair<int, int>>> g(1000);
        int K;
        std::cin >> K;
        std::getline(std::cin, dummy);
        bool processed[1000];
        for (auto &i : processed) i = false;
        while (K--) {
            std::string tmp;
            std::getline(std::cin, tmp);
            for (int v : name_to_id[tmp]) processed[v] = true;
        }
        // 1호선
        add_chain(100, 161, g);
        g[141].emplace_back(162, Tst);
        g[162].emplace_back(141, Tst);
        add_chain(162, 165, g);
        g[164].emplace_back(166, Tst);
        g[166].emplace_back(164, Tst);
        add_chain(166, 197, g);
        g[177].emplace_back(179, Tst);
        g[179].emplace_back(177, Tst);
        // 2호선
        add_chain(201, 243, g);
        g[201].emplace_back(243, Tst);
        g[243].emplace_back(201, Tst);
        add_chain(244, 247, g);
        g[211].emplace_back(244, Tst);
        g[244].emplace_back(211, Tst);
        add_chain(248, 251, g);
        g[234].emplace_back(248, Tst);
        g[248].emplace_back(234, Tst);
        // 3호선
        add_chain(309, 352, g);
        // 4호선
        add_chain(405, 456, g);
        // 5호선
        add_chain(510, 558, g);
        add_chain(559, 565, g);
        g[548].emplace_back(559, Tst);
        g[559].emplace_back(548, Tst);
        // 6호선
        for (int i = 610; i < 615; i++) g[i].emplace_back(i + 1, Tst);
        g[615].emplace_back(610, Tst);
        g[610].emplace_back(616, Tst);
        g[616].emplace_back(610, Tst);
        add_chain(616, 648, g);
        // 7호선
        add_chain(709, 761, g);
        // 8호선
        add_chain(810, 827, g);
        // 9호선
        add_chain(901, 938, g);
        // 환승역
        for (int i = 100; i <= 938; i++) {
            if (subway[i].empty() || processed[i] || name_to_id[subway[i]].size() == 1) continue;
            int x = name_to_id[subway[i]].size();
            auto &num = name_to_id[subway[i]];
            for (int j = 0; j < x; j++) {
                processed[num[j]] = true;
                for (int k = 0; k < j; k++) {
                    g[num[j]].emplace_back(num[k], Tc);
                    g[num[k]].emplace_back(num[j], Tc);
                }
            }
        }
        int dist[1000];
        for (auto &i : dist) i = 2147483647;
        int trace[1000] = {0};
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> q;
        for (int v : start) {
            dist[v] = 0;
            q.emplace(0, v);
        }
        while (!q.empty()) {
            auto [d, cur] = q.top(); q.pop();
            if (dist[cur] < d) continue;
            for (auto &[nextnum, nextdist] : g[cur]) {
                int t = d + nextdist;
                if (dist[nextnum] > t) {
                    dist[nextnum] = t;
                    trace[nextnum] = cur;
                    q.emplace(t, nextnum);
                }
            }
        }
        int min_val = 2147483647;
        int min_idx = 0;
        for (int v : end) {
            if (dist[v] < min_val) {
                min_val = dist[v];
                min_idx = v;
            }
        }
        if (min_val == 2147483647) {
            std::cout << "-1\n";
        } else {
            std::cout << min_val << '\n';
            int cur = min_idx;
            std::vector<int> path;
            while (start.find(cur) == start.end()) {
                path.push_back(cur);
                cur = trace[cur];
            }
            path.push_back(cur);

            std::vector<std::string> output;
            int station = 0;
            int last = 0;
            for (int i = (int)path.size() - 1; i >= 0; i--) {
                cur = path[i];
                // 환승 판정
                std::string tmp;
                if (!last || cur / 100 == last / 100) {
                    if (!(i && path[i] / 100 != path[i - 1] / 100)) {
                        tmp = "[";
                        tmp += '0' + (cur / 100);
                        tmp += "] ";
                        tmp += subway[cur];
                    }
                    station++;
                } else {
                    tmp = "<";
                    tmp += '0' + (last / 100);
                    tmp += " -> ";
                    tmp += '0' + (cur / 100);
                    tmp += "> ";
                    tmp += subway[cur];
                }
                if (!tmp.empty()) output.push_back(tmp);
                last = cur;
            }
            std::cout << station << '\n';
            for (auto &s : output) std::cout << s << '\n';
        }
    }
    return 0;
}
