import streamlit as st
import datetime


def main():
    
    st.title("週間日付表示", "rainbow")
    
    # 開始日を設定
    start_date = st.date_input("開始日を入力してください", datetime.date(2021, 1, 31))

    # 週の日付を取得
    week_dates = get_week_dates(start_date)

    # 結果を表示
    for date in week_dates:
        st.write(date)
    
    
def get_week_dates(start_date):
    # 月曜日から日曜日までの曜日を定義
    weekdays = ['月', '火', '水', '木', '金', '土', '日']
    
    # 開始日を設定
    date = start_date
    
    # 週の日付を格納するリストを初期化
    week_dates = []
    
    # 週の日付を取得
    for i in range(7):
        # 月が切り替わる場合は日付の前に月を表示
        if date.day == 1 and i > 0:
            week_dates.append(f'{date.month}/{date.day}')
        
        # 日付と曜日を追加
        week_dates.append(f'{date.day}({weekdays[date.weekday()]})')
        
        # 日付を1日進める
        date += datetime.timedelta(days=1)
    
    return week_dates



if __name__ == "__main__":
    main()