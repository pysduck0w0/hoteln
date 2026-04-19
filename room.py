# 模擬按鈕一：客人需求清掃
@router.post("/{room_id}/request-clean")
async def request_cleaning(room_id: int, db: Session = Depends(get_db)):
    # 更新資料庫該房間狀態為 'need_clean'
    ...

# 模擬按鈕二：房務完成回報
@router.post("/{room_id}/finish-clean")
async def finish_cleaning(room_id: int, db: Session = Depends(get_db)):
    # 更新資料庫該房間狀態為 'available'
    ...