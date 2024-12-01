import streamlit as st

# 데이터 로드
recommendations = {
    1: {
        "음악": [
            {"text": "I Don’t Think That I Like Her – Charlie Puth", "image": "https://i.namu.wiki/i/5mVWfl3irjLAb6EzTEhrnH2zr6OJ9pvcmttixMpK814_6oDZglL1M2OYWMIHQ8rIm6GwvS_VecO7tzG1lkO8PdEx-lTDX8m8DAT21wH6jmkPX-S5fPUpM-kkNlSwXh0cWMCOSfCI5CwUtwNx26cS5w.webp"},
            {"text": "Steal The Show – Lauv", "image": "https://i.namu.wiki/i/zGienHnRJSsaxprHqd0xSY4yK6h3OStXmKJHtEhf4rIIzVK_jyvC_rAR2PMuEZ14IqMzeHUlYGoQVt4azh8Bb8tzP2dVR7codXxL7ewJwZwEo3szckQlMx0w1qwCVY6FrTFP5DJyoMXrL976dE8Qrg.webp"},
        ],
        "책": [
            {"text": "내가 틀릴 수도 있습니다 – 비욘 나티코 린데블라드", "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjEyMThfMTY0%2FMDAxNjcxMzY2NDg5NTk0.HD24AZQazrkEJlglIS7D6cUrkfU9yXnobP-ArN3aCH4g.kLUq78fotArKsNK-ECyP4JFaYQVnnX-hT4Oh-9enPocg.PNG.ysc5258%2Fimage.png&type=sc960_832"},
            {"text": "우울할 때 곁에 두고 읽는 책 – 스칼릿 커티스", "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MjNfMTg2%2FMDAxNjI0NDQ1OTk1Nzkz.0XpMJ3m2jzsZxd699pdUBXs-I3MEdzK2nqk-QezE4pAg.xKwkkOjb7wOOfMXlOZpENiIMNAvPMpxVF0E8HNZ9yCUg.JPEG.hina1227%2Foutput_2257759763.jpg&type=sc960_832"},
        ],
        "영화": [
            {"text": "리틀 포레스트", "image": "https://i.namu.wiki/i/l5I0WHjMJ9CkiAbHQGCqzGjc8s_4bmFrLe4K08h37t3kMg5H7K_a4flHGDvNX-BaLxEz2Ktgn0FO25XFzjAByGMJkCf3jlB_jS2Av-BFzYJXhJok_SH2n51tkAnrQ9pqC4RevYBfqdrP8hXqBx_v8Q.webp"},
            {"text": "라라랜드", "image": "https://i.namu.wiki/i/uMrHdRt_tzrE_gOqUwRUlCiE2zt2wEjiACKQmI41stjSV5SgAmkPmAGne6cWUMOHTM-MC4XUGhaCvqLOrzc50iLq79LuBSmpG8fOj1qivXoBxXOJi75uybIrTJtaswyS2tNnjC4vZkZq3kua9At22g.webp"},
        ],
        "취미": ["어른을 위한 컬러링 북", "요가나 간단한 스트레칭"],
        "요리": ["김치찌개, 미역국", "오트밀이나 죽"],
    },
    # 다른 기분 점수(2, 3, 4, 5)도 동일한 형식으로 추가
    # 예를 들어 기분 점수 2:
    2: {
        "음악": [
            {"text": "밤편지 – 아이유", "image": "https://i.namu.wiki/i/gnLssDON91eYh0k8BzGfDem744xdoJmBc2dzUWaKM3ORXdm7A8d5nsn58GWTXzvuUAML2P6qK-oTwiCtyUW55NeSxt3K3VQEBudJFYQ7MgA3GdbanDhF6DJ-xBk_IMrWPKiCRYEcfIpaxGYzM827ew.webp"},
            {"text": "Love Yourself – Justin Bieber", "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20151225_59%2Fkawaihya_1451019854852RPmsv_PNG%2F%25C4%25B8%25C3%25B3.PNG&type=sc960_832"},
        ],
        "책": [
            {"text": "아몬드 – 손원평", "image": "https://i.namu.wiki/i/TAM4wikEtzomy0-5t4-taJsyYm5R6bgIJGYCg8IAwb9WoTWkpkxv1NtNsA74y4AA5kvQcFKPZ7w4NhVRb2oMpHTl2wet0CqQRt530pIeKNtchh67yPxb-ad2H5niS7ZXK_pYmwAgJ4T6d2N5MIZ7wA.webp"},
            {"text": "페퍼민트 – 백온유", "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEwMTFfMjUg%2FMDAxNjk2OTgwNDYwNDI4.-j5RVVqSkhNA21ksTviDqa7BKW79n_3xAI0-LBulqq4g.riXIDDT4hmk29fC4-YMwIBH1ZwwgrYqGhtV49-tMEl0g.JPEG.madelia_%2FXL.jpg&type=sc960_832"},
        ],
        "영화": [
            {"text": "곡성", "image": "https://i.namu.wiki/i/GfeJ6eo6xe73JZSLd15wD5yWq93z-zQvn3ZaHtIyJinRIWEks3_t9j9264sxSgW8kYMrPoToLSTqkFgqSzfn8mWlejrgGbM1OrrHueLzQsHPcac8u29TNZFQAk0qDhsSBq7BAri1mY8zFwQGf5BDLw.webp"},
            {"text": "브로커", "image": "https://i.namu.wiki/i/9bydRgWCw4pXU4Z7ws3JQuMER42BsahHhznQlQLGDes9rkSTYQ0hMHkSUDOnmo2tF3brj1nfiFY2JlwyoA4BN2Z6TgAyDUQ-a9g5N1XLkKH8Gi3op6ZXitdIdxTMCABtQKOAE2yJdGRL6av4jgM_MA.webp"},
        ],
        "취미": ["일기쓰기", "짧은 산책"],
        "요리": ["샌드위치", "핫초코"],
    },
    3: {
        "음악": [
            {"text": "비밀번호 486 – 윤하", "image": "https://i.namu.wiki/i/WS0GnDCv-AiIsyrV58zeZ-WKYSfy3PAPLoQcZHeIYamd3dXtki5BqlWESGkLz1DXE2babV-6Xz3BiEdRbZH3bdcgkt9wsR2xlZPJ2_DYbATiuj1wwLaYY3KBJP9aeUpmanO4o1EBw7wJDd3e5V-oKQ.webp"},
            {"text": "Stay – The Kid LAROI , Justin Bieber", "image": "https://i.namu.wiki/i/FZbfcHWYo2MBO1AYn3XUDY01Zx8v_XHJYQJaRv9WsXKC9AD_4zsH__twbyx64oGc6VPJV_cHGsp_DdLl9t-7z2Rno21Y38MDqaHThnoHNxRZ9dyqkonAiKpUnJS1NNdhMovhPwP2f6ctLnyThsfuWg.webp"},
        ],
        "책": [
            {"text": "무궁화 꽃이 피었습니다 – 김진평", "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MThfMjIz%2FMDAxNjg0Mzk0MTc4NjQz.gwEqdGc4pywjnTfWdaFnNjoHEkqyWnHJMqPqWcdL7EAg.iOx3o8sO1HD24xsSYc2ZFTgYU8LxEO0mhP2GBUt4Xoog.JPEG.sunysuni%2F1684393908250.jpg&type=sc960_832"},
            {"text": "호밀밭의 파수꾼 – 제롬 데이비드 샐린저", "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA2MjlfMTM4%2FMDAxNjg4MDI5MjA3NTgy.kK4h8AxPB4BJ0qoMFmrt4icaTDk8IAcqyT_MdGfrZxMg.bxb6vXYSl1Bh0B3R_H_OiphKUBblQLyI0U9-i8w9APMg.PNG.gudals8912%2Fimage.png&type=sc960_832"},
        ],
        "영화": [
            {"text": "코코", "image": "https://i.namu.wiki/i/mnfmJpZj-q_hzDSG5FxPyRqYQaP5XJ3sE8UX2kfcKcYiIm_6736yRAc5godGTpVSMs2zYdkplcyrX8KNpvilwjQ5XCprGA_pW-f1yQIgMkRbo_ys-Eh2gSdar7oO8RNZ8d87s0sSOCMuUcxScmsbtA.webp"},
            {"text": "기생충", "image": "https://i.namu.wiki/i/6LwxXWmcxijZoX1YPCnBt77l0pHjAFh3050XNDjywpba9Ks7JZnKO0URqVVPoQ5muEtJR7O_F-njEFeMvYiZx1mH6YTOrzvhicAktiuDUTKWPbAE9XoI-lySDLyZlUDw-021eikyomXxFNTKiR2q7g.webp"},
        ],
        "취미": ["DIY 공예", "간단한 요리 도전"],
        "요리": ["토마토소스 파스타", "팬케이크"],
    },
    4: {
        "음악": [
            {"text": "Dynamite – 방탄소년단", "image": "https://i.namu.wiki/i/XWxuoSMVbCS7hDu82JX9b13OfcwkMAD8XUgVFDIW7J-pJKMO3Aw561QY62synkXXXVtAm8Nc3iSVWGh9l45DmVvZDnUz5_29_ijqsopEVtlzcjVZkKPQjYLxq9qcgKi5lH7195e2k3ynZIC6MzSFUw.webp"},
            {"text": "Mood – 24KGoldn", "image": "https://i.namu.wiki/i/hTLlrfN70P2qm9-agaJe9A3PHXkFDWDtoDKMRyW2l73UR0K1lBFgdrZf3bWoOaM10BJRAabbsIjLtR9RdLdRzgLq9FDNVsXzmEYD5u2njJcbxQqjegAEBGJRQh8azLnDZ4xJlwBuuPOn3-uK-oWfZg.webp"},
        ],
        "책": [
            {"text": "불편한 편의점", "image": "https://i.namu.wiki/i/YQKovtCeUlhWGA7W54XYjOUmFu2wIUTMpdGWIdED5w-BgOq---Zf8rKnOSxwKueAXqkLSzVl3_uklUeqMtm8v-_cRaJa41LJ2oUq970a44ouEqFgu7gmCUFmihM5x3CWW1kq_4X42YB-vFQCsc43JQ.webp"},
            {"text": "오늘 밤, 세계에서 이 사랑이 사라진다 해도", "image": "https://i.namu.wiki/i/BwYzKcbOeZLiGjUZRfsbourdpginlmtR8LfDDDfmpudsLFK6p9t6_tSKJAM74DFbHV-sokG2md84UwPmJ5iOBA0HIiHk3nAlmNHY9simepJl4Pilc1GJogdYYd8ZCqNeZVJmrLsgZ_fvtca5oTQboQ.webp"},
        ],
        "영화": [
            {"text": "탑건 매버릭", "image": "https://i.namu.wiki/i/kgJgux2MRWBjelCp_WXC65ZBr-_jBFcfig6bVThX-b-sefr_-g9l06jtLaOLxWEFvU1f5cNGSBqiJ5QGXaeO_BSEtwpI4a__-RrKmFlrI69BbilAwK-Z619RcWzfC6g3apbkXgphoLiB5Z0eoXmWUA.webp"},
            {"text": "인사이드 아웃2", "image": "https://i.namu.wiki/i/1y0EYtsSSN9pHGr1N-d-Uen37WwFDxZbzggEAOWu0se8sX0uw4UYTR1QcqyUMrLHsQvH_-Lk_deF5RxxeMDXIhYTsPg5kejwVmg3n0OEtoSlYtClCzqeOwMTjtBJCAYa2ezHSo0IFxyJ7V9DNz2Ltg.webp"},
        ],
        "취미": ["춤 배우기", "친구들과의 보드게임"],
        "요리": ["푸딩", "간단한 브런치"],
    },
    5: {
        "음악": [
            {"text": "뱅뱅뱅 – 빅뱅", "image": "https://i.namu.wiki/i/ukdt8fq9D2anDttkGVdMZlmXmcoo9PRbTZW8Peb7lyg_kSOhzyOsXSLBE4CV8ljCwlzdw15rdkh7J03fOsVqal-IA1_r3wl6_9iMf3Fj10iirWNg1jgLzjvhIlxRzw4PbPpLDdjKT8ZSoYNJ6VfTag.webp"},
            {"text": "삐딱하게 – G-DRAGON", "image": "https://i.namu.wiki/i/24BkA1NYxbFPFiwkSbNv9b5vmABjIB61-0AI0nF6JrfJQyMJlZRMXvg2Ld_Vl8SewmEdIvs29E4MB6dli3SM3v94TVqB44fpOAg1jBoDSupdgALsgYZZG5JtIoXmEEx70m3SHbUz43COtcJeMKLkRQ.webp"},
        ],
        "책": [
            {"text": "불편한 편의점", "image": "https://i.namu.wiki/i/YQKovtCeUlhWGA7W54XYjOUmFu2wIUTMpdGWIdED5w-BgOq---Zf8rKnOSxwKueAXqkLSzVl3_uklUeqMtm8v-_cRaJa41LJ2oUq970a44ouEqFgu7gmCUFmihM5x3CWW1kq_4X42YB-vFQCsc43JQ.webp"},
            {"text": "오늘 밤, 세계에서 이 사랑이 사라진다 해도", "image": "https://i.namu.wiki/i/BwYzKcbOeZLiGjUZRfsbourdpginlmtR8LfDDDfmpudsLFK6p9t6_tSKJAM74DFbHV-sokG2md84UwPmJ5iOBA0HIiHk3nAlmNHY9simepJl4Pilc1GJogdYYd8ZCqNeZVJmrLsgZ_fvtca5oTQboQ.webp"},
        ],
        "영화": [
            {"text": "위대한 쇼맨", "image": "https://i.namu.wiki/i/7qk43MU5IX2hIZfz5CTNKIKG9J383fez2SZb13qdTSzHNXtp1fB1vn38PZ9b45g4TGw5qbR7d15ARXTOS5Do4vbcFBf0sHU5EHExdEo1ThULSI4hW4HHuyWKBx7oAWKLsimiUl9CVjw11Fc8gAAEIg.webp"},
            {"text": "범죄도시2", "image": "https://i.namu.wiki/i/_WtFZbdi66DFDm7UsI4FOP1oOE6w1k1b962pzCO08jBFDkpqEokvlumn_QC8cXmDgjuvOvccb4eEINc7dfD6relD1sZKkbcupD7_JYgT4zq3lB2Ih-ZSqOvI8FWBO_py6tX2raTjfnb6EPyOOlLiVw.webp"},
        ],
        "취미": ["여행하기", "야외 스포츠"],
        "요리": ["바비큐 요리", "디저트 (마카롱, 케이크)"],
    },
}

# 세션 상태 초기화
if "mood_set" not in st.session_state:
    st.session_state["mood_set"] = False
    st.session_state["mood"] = None

# 앱 UI
st.title("기분에 따른 추천 웹앱")
st.write("기분에 따라 음악, 책, 영화, 취미, 요리를 추천해 드립니다.")

# 기분 설정 상태 확인
if not st.session_state["mood_set"]:
    st.subheader("기분 설정하기")
    st.session_state["mood"] = st.slider("현재 기분을 설정하세요 (1: 우울, 5: 최고)", min_value=1, max_value=5, value=3)
    if st.button("기분 확정"):
        st.session_state["mood_set"] = True
else:
    # 추천 항목 표시
    st.subheader("추천 항목")
    mood = st.session_state["mood"]
    st.write(f"현재 기분 점수: {mood}")
    for category, items in recommendations[mood].items():
        if category in ["취미", "요리"]:
            with st.expander(f"{category} 추천 보기"):
                for item in items:
                    st.write(f"- {item}")
        else:  # 사진을 추가할 카테고리
            with st.expander(f"{category} 추천 보기"):
                for item in items:
                    st.write(f"- {item['text']}")
                    if item["image"] != "링크를 입력하세요":
                        st.image(item["image"], use_column_width=True, width = 40)

    # 기분 재설정 버튼
    if st.button("기분 재설정"):
        st.session_state["mood_set"] = False
        st.session_state["mood"] = None
